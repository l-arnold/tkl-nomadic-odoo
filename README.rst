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

    - Odoo v14 installed from 3rd party (official) Odoo apt repo.
    - Includes modules from base install of Odoo.

- **Security note**: Updates to Odoo may require supervision so they
  **ARE NOT** configured to install automatically. See below for
  updating Odoo.

- SSL support out of the box.
- `Adminer`_ administration frontend for PostgreSQL (listening on
  port 12322 - uses SSL).
- Webmin modules for configuring Apache2, PHP and PostgreSQL.


**Notice for special Odoo Localization**

In case tyou run a L10n Odoo Localization you will need other PIP Packages
and Libs installed on your system, please check your localization support on
OCA_.

Supervised Manual Odoo Update
-----------------------------

To upgrade to the latest version of Odoo from the command line::

    apt-get update
    apt-get install odoo

Credentials *(passwords set at first boot)*
-------------------------------------------

**Note**: the Odoo password set at firstboot applies to both the Odoo
admin account AND the masterpassword however these can be changed
individually after firstboot.

-  Webmin, SSH: username **root**
-  PostgreSQL, Adminer: username **postgres**
-  Odoo Master Account: **admin**

.. _Odoo: https://www.odoo.com/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Adminer: https://www.adminer.org/
.. _OCA: https://github.com/OCA
