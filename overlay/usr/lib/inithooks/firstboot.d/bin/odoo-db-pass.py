/usr/lib/inithooks/firstboot.d/50admin-db-pass

#!/bin/bash -e
# set odoo db password

. /opt/openerp/odoo/openerp-server.conf

updateconf() {
    CONF=/opt/openerp/odoo/openerp-server.conf

    sed -i "admin_password = admin" / "admin password = ${ODOO_PASS]" $CONF
}
