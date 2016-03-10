Odoo - From ERP to CRM, eCommerce to CMS
========================================

`Odoo`_is an all-in-one business management suite of mobile-friendly web
apps that integrates everything you need to grow your business: CRM,
website content management, project management, human resources,
accounting, invoicing and more. Odoo apps integrate seamlessly to
provide a full-featured open source ERP, but can also be used
stand-alone.

This appliance includes all the standard features in `TurnKey Core`_:

- Odoo v8 installed from upstream GIT source (`GitHub`_)
- Includes all base modules from base install of Odoo
- SSL support out of the box.
- `Adminer`_ administration frontend for PostgreSQL (listening on
  port 12322 - uses SSL).
- Webmin modules for configuring Apache2, PHP and PostgreSQL.

For a roadmap on where this appliance is heading, visit the 
`upstream`_ branch of the Odoo TKL build code and the release
`roadmap`_ on Github

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH: username **root**
-  PostgreSQL, Adminer: username **postgres**
-  Odoo Master Account: **admin**

.. _Odoo: https://www.odoo.com/
.. _GitHub: https://github.com/odoo/odoo
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Adminer: http://www.adminer.org/
.. _upstream: https://github.com/DocCyblade/tkl-odoo
.. _roadmap: https://github.com/DocCyblade/tkl-odoo/milestones
