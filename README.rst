Odoo Appliance - Turnkey Linux  
=======================
At RC2, available as ISO on https://sourceforge.net/projects/tklnomadicodoo/

(beta from L-Arnold based on CSVsol)

`Odoo`_ is a suite of web based open source business apps.


It's main apps include an `Open Source CRM`_, `Website Builder`_, `eCommerce`_, `Project Management`_, `Billing and Accounting`_, `Point of Sale`_, `Human Resources`_, Marketing, Manufacturing, Purchase Management, ...  Each application is standalone but you get a full featured `Open Source ERP`_ if you install several apps as they integrate to each others.

This appliance is based on `LAPP stack`_, including all the standard features in `TurnKey Core`_,
and on top of that:

- SSL support out of the box.

- WebShell SSH on   Port:12320
- Webmin On         Port:12321
- Adminer DBMgr on  Port: 12322
- WebConsole:   on  Port: 12325
  All management is linked from Webconsole as well as cursory documentation.

- PHP, Python and Perl support for Apache2 and PostgreSQL.
- `Adminer`_ administration frontend for PostgreSQL (listening on
  port 12322 - uses SSL).
  
- Webmin modules for configuring Apache2, PHP and PostgreSQL and system details.
- PostgreSQL listening on localhost (security)
- PostgreSQL password encryption enabled by default (security).
- The *postgres* user is trusted when connecting over local unix sockets
  (convenience).
- `Odoo`_ instaled branch: **master**.
- Odoo secured connection (http (port 80) auto redirects to https(port 443)).

- Odoo connection (listening on port 8069 -  Set up by default to open only to localhost).
  - You may want to Open this and can do so by going to /opt/openerp/odoo/openerp-server.conf
    removing 127.0.0.1 from "xmlrpc_interface = 127.0.0.1" and "netrpc_interface = 127.0.0.1"
    This will allow you to separate SSL Configuration from Odoo Configuration.

- Webmin module for configuring Samba.
- File server (`Samba`_) configurations:
   - Preconfigured wordgroup: WORKGROUP
   - Preconfigured netbios name: FILESERVER
   - Configured Samba and UNIX users/groups synchronization (CLI and
     Webmin).
   - Configured root as administrative samba user.
   - Configured shares:
      - Users home directory.
      - Public storage.
      - CD-ROM with automount and umount hooks (/media/cdrom).
- Default storage: */srv/storage*
- Accessing file server via samba on the command line::
    smbclient //1.0.0.61/storage -Uroot
    mount -t cifs //1.0.0.61/storage /mnt -o username=root,password=PASSWORD

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, Webshell, SSH, Samba: username **root**
-  PostgreSQL, phpPgAdmin: username **postgres**
-  Odoo: username **openerp**

Credentials *(passwords set by default)*
----------------------------------------

-  Odoo Master password: **admin**  (Change in Odoo Config file and Odoo DB Manager before any Data Base is created)
-  Odoo openuser password: **openuser**  ( Change in Postgresql inside Webmin then also Odoo Config File)
  
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
.. _Samba: http://www.samba.org/samba/what_is_samba.html

Built from initial Git-Clone made by Carlos' Tkl-Odoo at:
https://github.com/CLVsol/tkl-odoo

Tailored to work with TKLDEV 14 Jessie
Apache and other Configuration files to allow non Ported, Full SSL view of Odoo
SSL Updates will be required as in other Turnkeylinux Appliances
RC ISO's available under "Files" at  https://sourceforge.net/p/tklnomadicodoo/wiki/Home/

Details on Installation of CSR and TLD Certs to follow and can be found on www.turnkeylinux.org
