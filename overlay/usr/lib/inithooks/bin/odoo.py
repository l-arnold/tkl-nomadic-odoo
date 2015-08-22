#!/usr/bin/python

"""Set Odoo  ADMIN pw
Option:
    --adminpw=    unless provided, will ask interactively
"""

import re
import sys
import getopt

import crypt
import random
import hashlib

from dialog_wrapper import Dialog

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'adminpw='])
    except getopt.GetoptError, e:
        usage(e)

    adminpw = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--adminpw':
            adminpw = val


    if not adminpw:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        adminpw = d.get_adminpw(
            "Odoo Admin-password",
            "Enter password for the odoo 'admin' database manager.",
            "eg: admin")


    for line in file("/opt/openerp/odoo/openerp-server.conf", "r").readlines():
        m = re.match(r"admin_passwd ='(.*)';", line.strip())
        updateconf() {
            CONF=/opt/openerp/odoo/openerp-server.conf
            sed -i "s/#admin_passwd =*|admin password = ${adminpw}" $CONF  

if __name__ == "__main__":
    main()
