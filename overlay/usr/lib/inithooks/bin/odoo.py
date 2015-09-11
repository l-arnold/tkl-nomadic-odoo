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

from dialog_wrapper import Dialog
from executil import system

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

    config = "/etc/odoo/openerp-server.conf"
    system("sed -i \"s|admin_passwd =.*|admin_passwd = \"%s\"|\" %s" % (password, config))

if __name__ == "__main__":
    main()
