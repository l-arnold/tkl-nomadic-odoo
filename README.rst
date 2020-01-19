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

    - Odoo v11 installed from official Odoo Debian repo.
    - Includes all base modules from base install of Odoo.

    **Security note**: Updates to Odoo may require supervision so
    they **ARE NOT** configured to install automatically. See below for
    updating Odoo.

- SSL support out of the box.
- `Adminer`_ administration frontend for PostgreSQL (listening on
  port 12322 - uses SSL).
- Webmin modules for configuring Apache2, PHP and PostgreSQL.

For a roadmap on where this appliance is heading, visit the 
`upstream`_ branch of the Odoo TKL build code and the release
`roadmap`_ on Github

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
.. _Adminer: http://www.adminer.org/
.. _upstream: https://github.com/DocCyblade/tkl-odoo
.. _roadmap: https://github.com/DocCyblade/tkl-odoo/milestones
