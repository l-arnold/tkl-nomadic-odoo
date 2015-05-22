<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

<html lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta http-equiv="Content-Style-Type" content="text/css">
        <meta http-equiv="Content-Script-Type" content="text/javascript">

        <title>TurnKeyOdoo</title>
        
        <link rel="stylesheet" href="css/ui.tabs.css" type="text/css" media="print, projection, screen">
        <link rel="stylesheet" href="css/base.css" type="text/css">

        <script src="js/jquery-1.2.6.js" type="text/javascript"></script>
        <script src="js/ui.core.js" type="text/javascript"></script>
        <script src="js/ui.tabs.js" type="text/javascript"></script>
        <script type="text/javascript">
            $(function() {
                $('#container-1 > ul').tabs({ fx: { opacity: 'toggle'} });
            });
        </script>
    </head>

<body>
    <h1>TurnKey Odoo</h1>
        
        <div id="container-1">
            <ul>
                <li><a href="#cp"><span>Control Panel</span></a></li>
                <li>SET HOSTNAME in WEBMIN to Make this Page Operate Correctly</li>
                <li>information will follow</li>
            </ul>

            <div id="cp">
                <div class="fragment-content">
                    <div>
                        <a href="https://<?php print
                        $_SERVER{'SERVER_NAME'}; ?>:12320"><img
                        src="images/shell.png"/>Web Shell</a>
                    </div>
                    <div>
                        <a href="https://<?php print
                        $_SERVER{'SERVER_NAME'}; ?>:12321"><img
                        src="images/webmin.png"/>Webmin</a>
                    </div>
                    <div>
                        <a href="https://<?php print
                        $_SERVER{'SERVER_NAME'}; ?>:12322"><img
                        src="images/phppgadmin.png"/>PHPPgAdmin</a>
                    </div>
                    <div>
                       <a href="https://<?php print
                       $_SERVER{'SERVER_NAME'}; ?>/web"><img
                        src="images/odoo.png"/>Odoo Main (https)</a>
                  </div>
                    <div>
                        <a href="http://<?php print
                        $_SERVER{'SERVER_NAME'}; ?>:8069"><img
                        src="images/odoo.png"/>Odoo Base http by default NOT Open - Test (http)</a>
                    </div>
                    <div></div>
                    <div></div>

                    <h2>Resources and references</h2>
                    <ul>
                        <li>
                          <a href="/phpinfo.php">Apache PHP information</a>
                          (to disable: rm /var/www/phpinfo.php)
                        </li>
                        <li>
                          <a href="/server-status">Apache server status</a>
                          (to disable: a2dismod status)
                        </li>
                        <li>
                          <a href="https://github.com/l-arnold/tkl-nomadic-odoo">TurnKey Odoo on GitHub</a>
                          (l-arnold/tkl-nomadic-odoo)
                        </li>
                        <li>
                          <a href="https://github.com/odoo">Odoo on GitHub</a>
                          (formerly OpenERP)
                        </li>
                    </ul>

              </div>
          </div>

</div>
</body>
</html>
