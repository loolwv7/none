#fortmart wiki
#language en

= Zabbix how to =
<<TableOfContents>>
== installation ==
Download and install postgresql in database server 

=== Configure postgresql ===
{{{
psql -U postgres

CREATE USER zabbix WITH PASSWORD 'zabbix';
CREATE DATABASE zabbix OWNER zabbix;
}}}

cd /usr/share/zabbix/database/postgresql
{{{
psql -U zabbix -d zabbix -f schema.sql
psql -U zabbix -d zabbix -f images.sql
psql -U zabbix -d zabbix -f data.sql
}}}

 * Setting up a local user account for zabbix in the database meant adding this line to /etc/postgresql-9.3/pg_hba.conf
{{{
local   zabbix      zabbix                            md5
}}}

=== emerge package ===
{{{
cat >> /etc/portage/package.use <<"EOF"
net-analyzer/zabbix server snmp ssh -mysql -oracle postgres frontend agent openipmi libxml2
EOF
emerge -av zabbix
}}}

=== Configure fpm-php ===
vi /etc/php/fpm-php5.5/php.ini
{{{
max_execution_time = 300
max_input_time = 300
post_max_size = 16M
}}}


=== Configure zabbix_server ===
{{{
# sed '/^#/d;/^$/d' /etc/zabbix/zabbix_server.conf
 LogFile=/var/log/zabbix/zabbix_server.log
 LogFileSize=128
 PidFile=/run/zabbix/zabbix_server.pid
 DBHost=
 DBName=zabbix
 DBUser=zabbix
 DBPassword=zabbix
  SNMPTrapperFile=/tmp/zabbix_traps.tmp
   StartSNMPTrapper=1
   AlertScriptsPath=/var/lib/zabbix/alertscripts
   ExternalScripts=/var/lib/zabbix/externalscripts
   CacheSize=128M
   HistoryCacheSize=128M
   TrendCacheSize=64M
   HistoryTextCacheSize=128M
   Timeout=30
}}}



=== Run on Nginx ===

/opt/nginx/conf/zabbix.conf
{{{
server {
        listen 8080;
        server_name localhost;
        index index.html index.htm index.php;
	root /usr/share/webapps/zabbix/2.2.5/htdocs;
        access_log off;
	error_log /tmp/xxxx.log;
location ~ \.php {
        fastcgi_pass    127.0.0.1:9000;
	fastcgi_param SCRIPT_FILENAME /usr/share/webapps/zabbix/2.2.5/htdocs$fastcgi_script_name;
	fastcgi_param QUERY_STRING $query_string;
	include fastcgi_params;
	} 
}
}}}

=== Start Servers ===
{{{
/etc/init.d/php-fpm start
/etc/init.d/zabbix-server start
/etc/init.d/nginx reload
}}}

http://127.0.0.1:8080
 * User: Admin
 * Password: zabbix

== Graph report ==
download zabbix-dynamic-pdf-report module
{{{
git clone https://github.com/spy86/Zabbix_
mkdir /usr/share/webapps/zabbix/2.2.5/htdocs/report
cp -r /tmp/Zabbix_/zabbix-dynamic-pdf-report/* /usr/share/webapps/zabbix/2.2.5/htdocs/report/
}}}

vi /usr/share/webapps/zabbix/2.2.5/htdocs/report/config.inc.php
{{{#!highlight python
<?php
//CONFIGURABLE
# zabbix server info(user must have API access)
$z_server       = 'http://127.0.0.1:8080/';
$z_user         = 'Admin';
$z_pass         = 'zabbix';
# Temporary directory for storing pdf data and graphs - must exist
$z_tmp_path     = '/tmp';
# Directory for storing PDF reports
$pdf_report_dir = './reports';
# Root URL to reports
$pdf_report_url = $z_server ."/report/reports";
# paper settings
$paper_format   = 'A4'; // formats supported: 4A0, 2A0, A0 -> A10, B0 -> B10,
C0 -> C10, RA0 -> RA4, SRA0 -> SRA4, LETTER, LEGAL, EXECUTIVE, FOLIO
$paper_orientation = 'portrait'; // formats supported: portrait / landscape
# time zone - see http://php.net/manual/en/timezones.php
$timezone       = 'Asia/Shanghai';
# Logo used in PDF - may be empty
# TODO: Specify image size!
$pdf_logo       = './images/zabbix.png';
$company_name   = 'Zabbix';

//DO NOT CHANGE BELOW THIS LINE
$z_tmp_cookies  = "/tmp/";
$z_url_index    = $z_server ."index.php";
$z_url_graph    = $z_server ."chart2.php";
$z_url_api      = $z_server ."api_jsonrpc.php";
$z_login_data   = "name=" .$z_user ."&password=" .$z_pass
."&autologin=1&enter=Sign+in";
?>
}}}

http://127.0.0.1:8080/report/


== Agentless Monitor ==
When the configuration of a Zabbix agent is not possible, but access via SSH or
Telnet is available, a Zabbix server can run any custom command and use its
return as a value collected. From this value it is possible, for example, to
generate graphs and alarms.
 * http://www.zabbix.com/agentless_monitoring.php



== TroubleShooting ==
=== Fix Chinese language support ===

copy an chinese font to ''$ZABBIX_ROOT''
{{{
cd /usr/share/webapps/zabbix/2.2.5/htdocs
cp -v /usr/share/fonts/TTF/uming.ttf fonts/
sed -i 's/DejaVuSans/uming/g' include/defines.inc.php 
}}}




http://www.linuxworms.in/2013/06/installing-zabbix-with-postgresql-in.html

http://wikibaseofknowledge.blogspot.com/2014/09/module-to-generate-pdf-reports-in-zabbix.html

https://www.zabbix.com/forum/showthread.php?t=24998&page=16

[[http://virtuallyhyper.com/2014/06/monitor-esxi-smart-attributes-with-zabbix-over-ssh/|Agentless Monitor]]
