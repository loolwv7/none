#!/bin/sh
# put other system startup commands here

# static ip
/opt/eth0.sh

# cron
/etc/init.d/services/crond start

# ssh daemon
/usr/local/etc/init.d/dropbear start &

# active crypt lv
sudo vgchange -a y
sudo cryptsetup -v luksOpen /dev/mapper/vg_systec-apps apps --key-file /opt/mykeyfile
sudo mount -t ext4 /dev/mapper/apps /opt/apps

# mysql 
sudo rm -fr /usr/local/mysql/data
sudo rm -f /etc/my.cnf
sudo ln -s /opt/apps/mysql/data /usr/local/mysql/data
sudo ln -s /opt/apps/mysql/my.cnf /etc/my.cnf
sudo /usr/local/mysql/bin/mysqld_safe &

# tomcat
export JAVA_HOME=/opt/apps/jdk1.7.0_80/
/opt/apache-tomcat-7.0.63/bin/startup.sh &
