1, emerge phpsyslogng

2, nginx with php

server {
        listen 88;
        server_name localhost;
        index index.html index.htm index.php;
        root /usr/share/webapps/phpsyslogng/2.9.8m-r1/htdocs;
        access_log /var/log/phpsyslogng_access.log;
        error_log /var/log/phpsyslogng_error.log;
location ~ \.php {
        fastcgi_pass    127.0.0.1:9000;
        fastcgi_param SCRIPT_FILENAME /usr/share/webapps/phpsyslogng/2.9.8m-r1/htdocs$fastcgi_script_name;
        fastcgi_param QUERY_STRING $query_string;
        include fastcgi_params;
        } 
}

3, 127.0.0.1:88

http://www.devthought.com/2009/06/09/fix-ereg-is-deprecated-errors-in-php-53/
 if (preg_match("/([0-9]+)K/",$upload_max_filesize,$tempregs)) $upload_max_filesize=$tempregs[1]*1024;
 if (preg_match("/([0-9]+)M/",$upload_max_filesize,$tempregs)) $upload_max_filesize=$tempregs[1]*1024*1024;

SQL=You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for
the right syntax to use near 'TYPE=MyISAM' at line 7:

sed 's/TYPE=/ENGINE=/g' 
:%s#TYPE=MyISAM#ENGINE=MyISAM#gc

