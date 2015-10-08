
= tinycore linux =

== build environment ==
tce-load -iw compiletc.tcz

== required packages ==
libgcrypt11_1.5.0.orig.tar.bz2
libgpg-error-1.13.tar.bz2

sudo ln -sv /usr/local/lib/libgcrypt.so.11.7.0 /lib/libgcrypt.so.11


== lukfs ==
tc@box:~$ sudo cryptsetup --verbose --hash sha512 --iter-time 5000 --use-random luksFormat /dev/sdb1 

WARNING!
========
This will overwrite data on /dev/sda1 irrevocably.

Are you sure? (Type uppercase yes): YES
Enter LUKS passphrase: 
Verify passphrase: 
Command successful.

tc@box:~$ sudo cryptsetup luksOpen /dev/sda1 test

sudo mkfs.ext4 -m 0 /dev/mapper/test


== automatic mount on boot ==
https://bipedu.wordpress.com/2014/02/15/tiny-core-linux-no-autologin/

sudo dd if=/dev/urandom of=/mnt/sda1/tce/boot/mykeyfile bs=1024 count=4
sudo chmod -v 0400 /mnt/sda1/tce/boot/mykeyfile
sudo cryptsetup luksAddKey /dev/sdb1 /mnt/sda1/tce/boot/mykeyfile

sudo cryptsetup luksOpen /dev/sdb1 test --key-file /opt/mykeyfile

== enable root login ==
sudo mv /root/.profile /opt/root_profile_bak


== LUKS ON LVM ==

sudo grub-install /dev/sdb --root-directory=/mnt/sdb1

tc@systec:~$ sudo pvcreate /dev/sda2 
  Physical volume "/dev/sda2" successfully created
tc@systec:~$ sudo pvs
  PV         VG   Fmt  Attr PSize PFree
  /dev/sda2       lvm2 a-   1.43g 1.43g
tc@systec:~$ sudo vgcreate -v vg_systec /dev/sda2
    Wiping cache of LVM-capable devices
    Wiping cache of LVM-capable devices
    Adding physical volume '/dev/sda2' to volume group 'vg_systec'
    Archiving volume group "vg_systec" metadata (seqno 0).
    Creating volume group backup "/usr/local/etc/lvm/backup/vg_systec" (seqno 1).
  Volume group "vg_systec" successfully created

sudo lvcreate -n apps -l 100%FREE vg_systec
sudo cryptsetup --verbose --hash sha512 --iter-time 5000 --use-random luksFormat /dev/mapper/vg_systec-apps
sudo cryptsetup -v luksAddKey /dev/mapper/vg_systec-apps /opt/mykeyfile
sudo cryptsetup -v luksOpen /dev/mapper/vg_systec-apps apps --key-file /opt/mykeyfile 
Key slot 1 unlocked.
Command successful.

mkfs.ext4 -m 0 /dev/mapper/apps
sudo mount /dev/mapper/apps /opt/apps/

== Resize crypted LV ==
lvextend -L820G /dev/vg00/extra
cryptsetup resize extra_crypt
mount -o remount,resize /extra/




==  How to disable autologin bootcode ==
# Add the following line to /opt/bootsync.sh
cat >> /opt/bootsync.sh <<"EOF"
echo "booting" > /etc/sysconfig/noautologin
"EOF"

# Added "noautologin" at the end of each that line that says "append initrd="
sudo vi /mnt/sda1/boot/grub/menu.lst
kernel /tce/boot/vmlinuz ro root=/dev/sda1 cryptdevice=/dev/sdb1:test cryptkey=/dev/sda1:ext4:/opt/mykeyfile tz=HKT+8 noautologin quiet



== persistence mysql ==

sudo mkdir -v /opt/apps/mysql
sudo cp -Lr /usr/local/mysql/data /opt/apps/mysql/
sudo cp -fv /etc/my.cnf /opt/apps/mysql/
sed -i 's/#innodb_log_file_size/innodb_log_file_size/g' /opt/apps/mysql/my.cnf
sudo rm -vf /opt/apps/mysql/data/ib*

cat >> /opt/bootlocal.sh<< "EOF"
sudo rm -fvr /usr/local/mysql/data
sudo rm -fv /etc/my.cnf
sudo ln -sv /opt/apps/mysql/data /usr/local/mysql/data
sudo ln -sv /opt/apps/mysql/my.cnf /etc/my.cnf
sudo /usr/local/mysql/bin/mysqld_safe &
"EOF"

== References ==
http://forum.tinycorelinux.net/index.php?topic=9767.0

https://wiki.archlinux.org/index.php/Resizing_LVM-on-LUKS

== TIPs ==
=== mysql not start ==
http://serverfault.com/questions/104014/innodb-error-log-file-ib-logfile0-is-of-different-size

150726 01:20:07 mysqld_safe Starting mysqld daemon with databases from /usr/local/mysql/data
150726  1:20:07 [ERROR] mysqld: File '/usr/local/mysql/data/aria_log_control' not found (Errcode: 13 "Permission denied")
150726  1:20:07 [ERROR] mysqld: Got error 'Can't open file' when trying to use aria control file '/usr/local/mysql/data/aria_log_control'
150726  1:20:07 [ERROR] Plugin 'Aria' init function returned error.
150726  1:20:07 [ERROR] Plugin 'Aria' registration as a STORAGE ENGINE failed.
150726  1:20:07 [Note] InnoDB: Using mutexes to ref count buffer pool pages
150726  1:20:07 [Note] InnoDB: The InnoDB memory heap is disabled
150726  1:20:07 [Note] InnoDB: Mutexes and rw_locks use GCC atomic builtins
150726  1:20:07 [Note] InnoDB: Memory barrier is not used
150726  1:20:07 [Note] InnoDB: Compressed tables use zlib 1.2.8
150726  1:20:07 [Note] InnoDB: Not using CPU crc32 instructions
150726  1:20:07 [Note] InnoDB: Initializing buffer pool, size = 128.0M
150726  1:20:07 [Note] InnoDB: Completed initialization of buffer pool
150726  1:20:07 [ERROR] InnoDB: ./ibdata1 can't be opened in read-write mode
150726  1:20:07 [ERROR] InnoDB: The system tablespace must be writable!
150726  1:20:07 [ERROR] Plugin 'InnoDB' init function returned error.
150726  1:20:07 [ERROR] Plugin 'InnoDB' registration as a STORAGE ENGINE failed.
150726  1:20:07 [Note] CONNECT: Version 1.03.0006 February 06, 2015
150726  1:20:07 [Note] Plugin 'FEEDBACK' is disabled.
150726  1:20:07 [ERROR] Can't open the mysql.plugin table. Please run mysql_upgrade to create it.
150726  1:20:07 [ERROR] Unknown/unsupported storage engine: InnoDB
150726  1:20:07 [ERROR] Aborting

150726  1:20:07 [Note] unregister_replicator OK
150726  1:20:07 [Note] /usr/local/mysql/bin/mysqld: Shutdown complete

150726 01:20:07 mysqld_safe mysqld from pid file /var/run/mysqld/mysqld.pid ended

== alias ==
# grep file .ashrc 
alias reboot='/etc/init.d/services/crond stop; filetool.sh -b; sudo reboot'
alias poweroff='/etc/init.d/services/crond stop; filetool.sh -b; sudo poweroff'
alias halt='/etc/init.d/services/crond stop; filetool.sh -b; sudo halt'

