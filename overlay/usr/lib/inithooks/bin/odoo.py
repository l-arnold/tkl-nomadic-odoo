#!/usr/bin/python
"""Set Odoo openuser db password and ADMIN pw
Option:
    --pass=     unless provided, will ask interactively
    --adminpw=    unless provided, will ask interactively
"""

import re
import sys
import getopt

import crypt
import random
import hashlib

from dialog_wrapper import Dialog
from pgsqlconf import PostgreSQL

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'adminpw='])
    except getopt.GetoptError, e:
        usage(e)

    password = ""
    adminpw = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--adminpw':
            adminpw = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "Openuser Password",
            "Enter new password for the Odoo 'openuser' account.")

    if not adminpw:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        adminpw = d.get_adminpw(
            "Odoo Admin-password",
            "Enter password for the odoo 'admin' database manager.",
            "eg: admin")

    sitesalt = ""
    for line in file("/opt/openerp/odoo/openerp-server.conf", "r").readlines():
        m = re.match(r"db_password ='(.*)';", line.strip())
        if m:
            sitesalt = m.groups()[0]
    
    for line in file("/opt/openerp/odoo/openerp-server.conf", "r").readlines():
        m = re.match(r"db_passwordd ='(.*)';", line.strip())
        updateconf() {
            CONF=/opt/openerp/odoo/openerp-server.conf
    sed -i "s/#db_password = openuser / db_password = ${OPENERP_PASS}" $CONF

    salt = hashlib.sha1(str(random.random())).hexdigest()[:8]
    fullsalt = hashlib.md5(sitesalt + salt).hexdigest()[:16]

    alg = "$6$"
    hash = hashlib.sha1(salt + password).hexdigest()
    hash = crypt.crypt(hash, alg + fullsalt)
    hash = alg + hash[len(alg)+len(fullsalt):]

    p = PostgreSQL(database='mahara')
    p.execute('UPDATE usr SET salt=\'%s\' WHERE username=\'openerp\';' % salt)
    p.execute('UPDATE usr SET password=\'%s\' WHERE username=\'openerp\';' % hash)
    p.execute('UPDATE usr SET passwordchange=0 WHERE username=\'openerp\';')

for line in file("/opt/openerp/odoo/openerp-server.conf", "r").readlines():
        m = re.match(r"admin_passwd ='(.*)';", line.strip())
        updateconf() {
            CONF=/opt/openerp/odoo/openerp-server.conf

            sed -i "s/#admin_passwd = admin / admin password = ${ODOO_PASS}" $CONF  

if __name__ == "__main__":
    main()
