Odoo - From ERP to CRM, eCommerce to CMS
========================================

`Odoo`_ is an all-in-one business management suite of mobile-friendly web
apps that integrates everything you need to grow your business: CRM,
website content management, project management, human resources,
accounting, invoicing and more. Odoo apps integrate seamlessly to
provide a full-featured open source ERP, but can also be used
stand-alone. Python programmers can develop their own app modules, or
choose from an array of free open source; or paid commerical ones.

This appliance includes all the standard features in `TurnKey Core`_:

- Odoo configurations:

    - Odoo v16 installed from debian backports apt repo.
    - Includes modules from base install of Odoo.

- **Security note**: As of 18.0, due to using the debian backports repo
  Updates to Odoo **ARE NOT** configured to install automatically.

- SSL support out of the box.
- `Adminer`_ administration frontend for PostgreSQL (listening on
  port 12322 - uses SSL).
- Webmin modules for configuring Apache2, PHP and PostgreSQL.

**Notice for special Odoo Localization**

In case you run a L10n Odoo Localization you will need other PIP Packages
and Libs installed on your system, please check your localization support on
OCA_.

Credentials *(passwords set at first boot)*
-------------------------------------------

**Note**: the Odoo password set at firstboot applies to both the Odoo
admin account (example app) AND the masterpassword  - however these can be
changed individually after firstboot.

-  Webmin, SSH: username **root**
-  PostgreSQL, Adminer: username **postgres**
-  Odoo Master Account: **admin**

.. _Odoo: https://www.odoo.com/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Adminer: https://www.adminer.org/
.. _OCA: https://github.com/OCA
