#!/usr/bin/python

"""Set Odoo Admin Password
Option:
    --pass=    unless provided, will ask interactively
"""

import re
import sys
import getopt

import crypt
import random
import hashlib
import ConfigParser

from dialog_wrapper import Dialog
from executil import system
from pgsqlconf import PostgreSQL
from passlib.context import CryptContext

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val


    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Odoo Database Managment Screen Password",
            "Enter new database management screen password. This is used for Odoo database functions.")

    processed_password = CryptContext(['pbkdf2_sha512']).encrypt(password)

    p = PostgreSQL('odoo')
    p.execute("UPDATE res_users SET password='', password_crypt='{}' WHERE id=1".format(
        processed_password))

    config = ConfigParser.RawConfigParser()
    config_path = '/etc/odoo/odoo.conf'
    config.read(config_path)

    config.set('options', 'admin_passwd', processed_password)

    with open(config_path, 'w') as config_file:
        config.write(config_file)

if __name__ == "__main__":
    main()
