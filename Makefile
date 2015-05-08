COMMON_OVERLAYS = tkl-webcp samba-fileserver samba-sid-inithook
COMMON_CONF = tkl-webcp fileserver-storage samba-rootpass samba-webmin

CREDIT_ANCHORTEXT = Odoo Appliance

include $(FAB_PATH)/common/mk/turnkey/lapp.mk
include $(FAB_PATH)/common/mk/turnkey.mk
