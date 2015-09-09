Odoo Appliance - Turnkey Linux  
=======================
At beta v 01 (see release here and available as ISO on https://sourceforge.net/projects/tklnomadicodoo/  )

`Odoo`_ is a suite of web based open source business apps.  TKL-Nomadic-Odoo is a prebuilt install that integrates the current Odoo 8.0 Branch, and which has been preconfigured with Odoo Community Association Addon Modules - both OCA-Server Tools and the OCA - Magento Connector (Connector framework).

About Odoo.
It's main apps include an `Open Source CRM`_, `Website Builder`_, `eCommerce`_, `Project Management`_, `Billing and Accounting`_, `Point of Sale`_, `Human Resources`_, Marketing, Manufacturing, Purchase Management, ...  Each application is standalone but you get a full featured `Open Source ERP`_ if you install several apps as they integrate to each others.

This appliance is based on the Turnkeylinux (TKL) `LAPP stack`_, which integrates Linux, Apache Web, and PostgreSQL and includes all the standard features in `TurnKey Core`_, and on top of that:

- SSL support out of the box.

- WebShell SSH on   Port:12320
- Webmin On         Port:12321
- Adminer DBMgr on  Port: 12322
- Optional HTTPS: WebConsole:Port: 12324
- Optional HTTP WebConsole:  Port: 12325

  All management is linked from Webconsole as well as cursory documentation.

- PHP, Python and Perl support for Apache2 and PostgreSQL.
- `Adminer`_ administration frontend for PostgreSQL (listening on
  port 12322 - uses SSL).
  
- Webmin modules for configuring Apache2, PHP and PostgreSQL and system details.
- PostgreSQL listening on localhost (security)
- PostgreSQL password encryption enabled by default (security).
- The *postgres* user is trusted when connecting over local unix sockets
  (convenience).
- `Odoo`_ instaled branch: **8.0**.
- Odoo secured connection (http (port 80) auto redirects to https(port 443)).

- Odoo connection (listening on port 8069 -  Set up by default to open only to localhost).
  - You may want to Open this and can do so by going to /opt/openerp/odoo/openerp-server.conf
    removing 127.0.0.1 from "xmlrpc_interface = 127.0.0.1" and "netrpc_interface = 127.0.0.1"
    This will allow you to separate SSL Configuration from Odoo Configuration.


Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, Webshell, SSH: username **root**
-  PostgreSQL, phpPgAdmin: username **postgres**

Credentials *(passwords set by default)*
----------------------------------------

-  Odoo Master password: **admin**  (Change in Odoo Config file and Odoo DB Manager before any Data Base is created)
-  Odoo openuser password: **openuser**  (Firstboot resets - changes both openuser Postgresql user and Odoo config file)
  
.. _Odoo: https://www.odoo.com
.. _Open Source CRM: https://www.odoo.com/page/crm
.. _Website Builder: https://www.odoo.com/page/website-builder
.. _eCommerce: https://www.odoo.com/page/e-commerce
.. _Project Management: https://www.odoo.com/page/project-management
.. _Billing and Accounting: https://www.odoo.com/page/accounting
.. _Point of Sale: https://www.odoo.com/page/point-of-sale
.. _Human Resources: https://www.odoo.com/page/employees
.. _Open Source ERP: https://www.odoo.com
.. _LAPP stack: http://www.turnkeylinux.org/lapp
.. _PHPPgAdmin: http://phppgadmin.sourceforge.net/
.. _TurnKey Core: http://www.turnkeylinux.org/core

Built from initial Git-Clone made by Carlos' Tkl-Odoo at:
https://github.com/CLVsol/tkl-odoo

Tailored to work with TKLDEV 14 Jessie
Apache and other Configuration files to allow non Ported, Full SSL view of Odoo
SSL Updates will be required as in other Turnkeylinux Appliances
RC ISO's available under "Files" at  https://sourceforge.net/p/tklnomadicodoo/wiki/Home/

Details on Installation of CSR and TLD Certs to follow and can be found on www.turnkeylinux.org
