ORIG to L14

/usr/lib/inithooks/firstboot.d/50admin-db-pass

#!/bin/bash -e
# set odoo db password

. /opt/openerp/odoo/openerp-server.conf

updateconf() {
    CONF=/opt/openerp/odoo/openerp-server.conf

    sed -i "s/#admin_passwd = admin / admin password = ${ODOO_PASS}" $CONF
    sed -i "s/#db_password = openuser / db_password = ${OPENERP_PASS}" $CONF
}

