CREDIT_ANCHORTEXT = Turnkey Odoo Appliance

BACKPORTS=y # install Odoo v16.x from backports
BACKPORTS_PINS=odoo-14 # try odoo-14 since odoo-16 package is gone

include $(FAB_PATH)/common/mk/turnkey/lapp.mk
include $(FAB_PATH)/common/mk/turnkey.mk
