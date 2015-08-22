#!/usr/bin/python

"""Set Odoo  ADMIN pw
Option:
    --ADMINPW=    unless provided, will ask interactively
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
                                       ['help', 'ADMINPW='])
    except getopt.GetoptError, e:
        usage(e)

    ADMINPW = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--ADMINPW':
            ADMINPW = val


    if not ADMINPW:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        adminpw = d.get_ADMINPW(
            "Odoo Admin-password",
            "Enter password for the Odoo 'admin' database manager.",
            "eg: admin")


if __name__ == "__main__":
    main()
