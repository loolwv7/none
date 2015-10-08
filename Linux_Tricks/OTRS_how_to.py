http://wiki.otterhub.org/index.php?title=Installation_on_Debian_6_with_Postgres
http://hirantha.wikidot.com/setting-up-nginx-for-otrs


1, emerge -av otrs yaml dev-perl/Crypt-SSLeay dev-perl/GD dev-perl/GDGraph dev-perl/Archive-Zip
dev-perl/Net-DNS

make error ``Could not set permissions''
http://bytesandbones.wordpress.com/2013/10/18/gentoo-otrs-emerge-error-chown-s-not-allowed/

2, $ pwd
/var/lib/otrs/bin
$ perl otrs.CheckModules.pl  | less
cpan DBD::Pg
cpan Net:SSL
cpan YAML:XS
cpan Encode:HanExtra
cpan GD::Text
cpan JSON::XS
cpan Mail::IMAPClient
cpan PDF::API2
cpan Template
cpan Net::LDAP
cpan Template
cpan Crypt::Eksblowfish::Bcrypt

perl -e shell -MCPAN
OR:
# install needed modules!


cd /opt/otrs/
cp Kernel/Config.pm.dist Kernel/Config.pm
cp Kernel/Config/GenericAgent.pm.dist Kernel/Config/GenericAgent.pm

perl -cw /opt/otrs/bin/cgi-bin/index.pl
perl -cw /opt/otrs/bin/cgi-bin/customer.pl
perl -cw /opt/otrs/bin/otrs.PostMaster.pl

$ perl -cw bin/cgi-bin/index.pl
bin/cgi-bin/index.pl syntax OK
$ pwd
/var/lib/otrs
$ perl -cw bin/cgi-bin/customer.pl
bin/cgi-bin/customer.pl syntax OK
$  perl -cw bin/otrs.PostMaster.pl
bin/otrs.PostMaster.pl syntax OK


3, connect with PostgreSQL OR http://127.0.0.1:802/otrs/installer.pl
postgres=# create user otrs password 'otrs' nosuperuser;
CREATE ROLE
postgres=# create database otrs owner otrs;
CREATE DATABASE

psql otrs < /opt/otrs/scripts/database/otrs-schema.postgresql.sql
psql otrs <  /opt/otrs/scripts/database/otrs-initial_insert.postgresql.sql 
psql otrs < /opt/otrs/scripts/database/otrs-schema-post.postgresql.sql


http://itsm-demo.otrs.com/otrs/public.pl?Action=PublicFAQZoom;ItemID=53


postgres=# \conninfo 
You are connected to database ``postgres'' as user ``postgres'' via socket in ``/run/postgresql'' at port ``5432''.
postgres=# \connect otrs
You are now connected to database ``otrs'' as user ``postgres''.

== troubleshooting ==
[Mon Aug 17 22:33:59 2015] otrs.CheckDB.pl: DBD::Pg::st execute failed: ERROR:
    permission denied for relation valid at /opt/otrs/Kernel/System/DB.pm line
    629.
    ERROR: OTRS-otrs.CheckDB.pl-10 Perl: 5.20.2 OS: linux Time: Mon Aug 17
    22:33:59 2015

otrs=# GRANT SELECT on valid TO PUBLIC;
GRANT
otrs=# 

# http://lists.otrs.org/pipermail/otrs/2011-March/035248.html
brightmoon otrs # bin/otrs.CheckDB.pl 
Trying to connect to database
DSN: DBI:Pg:dbname=otrs;
DatabaseUser: otrs

Connected.


### Allow access to the db

# vi /etc/postgresql-9.3/pg_hba.conf
# put the following at the top of the file

local   otrs    otrs    password
host    otrs    otrs    127.0.0.1/32    password

psql -U otrs -W -f scripts/database/otrs-schema.postgresql.sql otrs
psql -U otrs -W -f scripts/database/otrs-initial_insert.postgresql.sql otrs
psql -U otrs -W -f scripts/database/otrs-schema-post.postgresql.sql otrs

brightmoon ~ # sed '/^.*#/d;/^$/d' /opt/otrs/Kernel/Config.pm
package Kernel::Config;
use strict;
use warnings;
use utf8;
sub Load {
    my $Self = shift;
    $Self->{DatabaseHost} = '127.0.0.1';
    $Self->{Database} = 'otrs';
    $Self->{DatabaseUser} = 'otrs';
    $Self->{DatabasePw} = 'otrs';
    $Self->{DatabaseDSN} = "DBI:Pg:dbname=$Self->{Database};";
    $Self->{Home} = '/opt/otrs';
}
use base qw(Kernel::Config::Defaults);
1;



4 , nginx
# otrs.conf
server {
        listen 802;
        server_name localhost;
        index index.html index.htm index.php index.pl;
        root /opt/otrs/bin/fcgi-bin;
        error_log /tmp/xxxx.log;

location /otrs-web {
        gzip on;
        alias /opt/otrs/var/httpd/htdocs;
}

location ~ ^/otrs/(.*\.pl)(/.*)?$ {
        fastcgi_pass 127.0.0.1:8999;
        fastcgi_index index.pl;
        fastcgi_param SCRIPT_FILENAME /opt/otrs/bin/fcgi-bin/$1;
        fastcgi_param QUERY_STRING $query_string;
        fastcgi_param REQUEST_METHOD $request_method;
        fastcgi_param CONTENT_TYPE $content_type;
        fastcgi_param CONTENT_LENGTH $content_length;
        fastcgi_param GATEWAY_INTERFACE CGI/1.1;
        fastcgi_param SERVER_SOFTWARE nginx;
        fastcgi_param SCRIPT_NAME $fastcgi_script_name;
        fastcgi_param REQUEST_URI $request_uri;
        fastcgi_param DOCUMENT_URI $document_uri;
        fastcgi_param DOCUMENT_ROOT $document_root;
        fastcgi_param SERVER_PROTOCOL $server_protocol;
        fastcgi_param REMOTE_ADDR $remote_addr;
        fastcgi_param REMOTE_PORT $remote_port;
        fastcgi_param SERVER_ADDR $server_addr;
        fastcgi_param SERVER_PORT $server_port;
        fastcgi_param SERVER_NAME $server_name;
  }
}



5, OTRS installer !!
/etc/init.d/nginx start
/etc/init.d/perl-fcgi
cp /opt/otrs/var/cron/scheduler_watchdog.dist /opt/otrs/var/cron/scheduler_watchdog
/opt/otrs/bin/Cron.sh restart
You can use the OTRS Web Installer, after you installed the OTRS software, to set up and configure the OTRS database. The Web Installer is a web page you can visit in your browser. The URL for the web installer is http://localhost/otrs/installer.pl .







########################################################
troubleshooting

2015/02/13 13:09:46 [error] 8880#0: *27 open( "/opt/otrs/var/httpd/htdocs/skins/Agent/default/css-cache/CommonCSS_fb524e3e2db9c03a02c174085257e946.css" failed (13: Permission denied), client: 127.0.0.1, server: localhost, request: "GET /otrs-web/skins/Agent/default/css-cache/CommonCSS_fb524e3e2db9c03a02c174085257e946.css HTTP/1.1", host: "127.0.0.1:802", referrer: "http://127.0.0.1:802/otrs/installer.pl"
2015/02/13 13:09:46 [error] 8880#0: *27 open( "/opt/otrs/var/httpd/htdocs/skins/Agent/default/css-cache/ModuleCSS_615d0028817ad870646618b97f9602bd.css" failed (13: Permission denied), client: 127.0.0.1, server: localhost, request: "GET /otrs-web/skins/Agent/default/css-cache/ModuleCSS_615d0028817ad870646618b97f9602bd.css HTTP/1.1", host: "127.0.0.1:802", referrer: "http://127.0.0.1:802/otrs/installer.pl"
2015/02/13 13:09:46 [error] 8880#0: *27 open( "/opt/otrs/var/httpd/htdocs/js/js-cache/CommonJS_0866261f8a211c496fa6641c44afb9dc.js" failed (13: Permission denied), client: 127.0.0.1, server: localhost, request: "GET /otrs-web/js/js-cache/CommonJS_0866261f8a211c496fa6641c44afb9dc.js HTTP/1.1", host: "127.0.0.1:802", referrer: "http://127.0.0.1:802/otrs/installer.pl"
2015/02/13 13:09:46 [error] 8880#0: *27 open( "/opt/otrs/var/httpd/htdocs/js/js-cache/ModuleJS_8ec1dfd69749ce87e1362f1f7427a2d5.js" failed (13: Permission denied), client: 127.0.0.1, server: localhost, request: "GET /otrs-web/js/js-cache/ModuleJS_8ec1dfd69749ce87e1362f1f7427a2d5.js HTTP/1.1", host: "127.0.0.1:802", referrer: "http://127.0.0.1:802/otrs/installer.pl"
2015/02/13 13:09:46 [error] 8880#0: *27 open( "/opt/otrs/var/httpd/htdocs/js/js-cache/CommonJS_0866261f8a211c496fa6641c44afb9dc.js" failed (13: Permission denied), client: 127.0.0.1, server: localhost, request: "GET /otrs-web/js/js-cache/CommonJS_0866261f8a211c496fa6641c44afb9dc.js HTTP/1.1", host: "127.0.0.1:802", referrer: "http://127.0.0.1:802/otrs/installer.pl"
2015/02/13 13:09:46 [error] 8880#0: *27 open( "/opt/otrs/var/httpd/htdocs/js/js-cache/ModuleJS_8ec1dfd69749ce87e1362f1f7427a2d5.js" failed (13: Permission denied), client: 127.0.0.1, server: localhost, request: "GET /otrs-web/js/js-cache/ModuleJS_8ec1dfd69749ce87e1362f1f7427a2d5.js HTTP/1.1", host: "127.0.0.1:802", referrer: "http://127.0.0.1:802/otrs/installer.pl"


## permission issue
# chmod 755 *.js




开始页面:
http://127.0.0.1:802/otrs/index.pl
用户:
root@localhost
密码:
6ZsnKwsTFZlFDSLk 

=== Reset web login PASSWORD ===
./bin/otrs.SetPassword.pl root@localhost PASSWORD


20150817
Start page:
http://127.0.0.1:802/otrs/index.pl
User:
root@localhost
Password:
IkJ7KJEmgTXC9iJP

((enjoy))

Your OTRS Team
