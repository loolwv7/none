#! /bin/bash

#########################
# by: Merlyn
#        August 8, 2014
#########################

export DB=bitnami_redmine
export USERNAME=root
export PASSWORD=bitnami
export MYSQL=/opt/redmine-2.2.0-0/mysql/bin/mysql  
export MYSQLDUMP=/opt/redmine-2.2.0-0/mysql/bin/mysqldump  
export RSYNC=/usr/bin/rsync
export BACKUPFILE="$DB"_$(date +"%F_%H%M").sql.xz

# Umount&Mount remote share directory.
umount -v /mnt/mysql_backup
mount.cifs -v -o iocharset=cp936,username=merlyn,password=zjsos\@123\!\@\# //192.168.8.251/redmine_backup /mnt/mysql_backup

if [ $? -eq 0 ]; then

# Dump Database
echo "**Starting backup to local disk... "
$MYSQLDUMP -u$USERNAME -p$PASSWORD $DB | xz -6 > /mnt/tmp/$BACKUPFILE

# Upload XZ to 192.168.8.251
echo "**Starting RSYNC to remote share disk... "
$RSYNC -ap /mnt/tmp/ /mnt/mysql_backup 2>/dev/null
else
echo "**Starting just backup to local disk... "
$MYSQLDUMP -u$USERNAME -p$PASSWORD $DB | xz -6 > /mnt/tmp/$BACKUPFILE
fi

# Delete backup file older than 30 days
find /mnt/tmp -type f -mtime +30 -exec rm '{}' \;
