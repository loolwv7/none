== Apache About ==
I. How to fix APACHE "Could not reliably determine the server's fully qualified domain name?"
Just set the "ServerName localhost" in httpd.conf


=== 为APACHE服务器启用HTTPS(ssl key)功能 ===
{{{
openssl genrsa -des3 -out server.key 1024
openssl req -new -x509 -days 365 -key server.key -out server.crt
}}}

== Sed & Awk About ==
=== sed: Remove All Except Digits (Numbers) From Input ===
{{{
echo 'This is a test. 123456789 and 2nd number is 34. 3M3i4x5' | sed 's/[^0-9]*//g'
}}}

=== Sed delete dos CR/LF line ===
{{{
sed 's/.$//' file > out 
sed 's/\x0D$//' file > out
}}}

=== To remove all whitespace (including tabs) from left to first word ===
{{{
echo "     This is a test" | sed -e 's/^[ \t]*//'
sed  '/\#/d;/^$/d' /etc/nginx/nginx.conf
}}}

=== sed replace spaces with single space ===
{{{
sed -e "s/ \+/ /g;/^$/d" < ml.txt  > mll.txt
sed 's/ \{1,\}/ /g' 
}}}
[[http://superuser.com/questions/241018/how-to-replace-multiple-spaces-by-one-tab]]

=== remove all unwanted blank space then SORT it ===
{{{
sed 's/ /\n/g' < list  | sort
}}}

=== add/replace within <<<&>>> ===
{{{
# & replaces whatever matches with the given REGEXP.
$ sed 's@^.*$@<<<&>>>@g' path.txt
<<</usr/kbos/bin:/usr/local/bin:/usr/jbin/:/usr/bin:/usr/sas/bin>>>
<<</usr/local/sbin:/sbin:/bin/:/usr/sbin:/usr/bin:/opt/omni/bin:>>>
<<</opt/omni/lbin:/opt/omni/sbin:/root/bin>>>
$ sed 's@/usr/bin@&/local@g' path.txt
/usr/local/sbin:/sbin:/bin/:/usr/sbin:/usr/bin/local:/opt/omni/bin:
/opt/omni/lbin:/opt/omni/sbin:/root/bin
}}}

== Find About ==
=== 把找到的文件复制到另一个地方 ===
{{{
find /mnt/sda7/software_linux/ -name "*.exe" | xargs -i cp {} /home/ftp/incoming/
find /mnt/sda7/software_linux/ -name "*.exe" -exec cp '{}' /home/ftp/ ';'
find cacti-xxxx -type d -exec mkdir -p utf/{} ';'
find cacti-xxxx -type f -exec iconv -f GB2312 -t UTF-8 {} -o utf/{} ';'
find /home/user1 -name '*.txt' | xargs cp -av --target-directory=/home/backup/ --parents 
}}}

=== Find out all the jpg images and archive it ===
{{{
find /var/log -name '*.log' | tar cv --files-from=- | bzip2 -9 > log.tar.bz2 
find / -name *.jpg -type f -print | xargs tar -cvzf images.tar.gz
}}}

=== create symbol link from DIR ===
{{{
find /mnt/data/media/* -maxdepth 0 -type d -exec ln -sv '{}' . \;
}}}

=== 把目录下的包含大写字母的文件列出来 ===
{{{
find /usr/share/ -type f | xargs ls -l | grep '[:upper:]' | less -r
find . -maxdepth 2 -size +100M -exec ls -lh "{}" \;
}}}

=== 把目录下所有iso文件找出来并计算总大小(GB) ===
{{{
find /srv/ /mnt/media/ -name "*.iso" | xargs ls -lk | echo `awk '{a+=$5}END {print a}'`/1024/1024 | bc
find /srv/ /mnt/media/ -name "*.iso" | xargs ls -lk | awk '{a+=$5}END {print "Total sum is", a/1024/1024"GB"}'
find /srv/ /mnt/media/ -name "*.iso" -printf "%s\n" 2>/dev/null | awk '{a+=$1}END { print "Total sum is", a/1024/1024/1024"GB\nTotal time is :"}'
}}}

=== Find files out then Copy files with sequence number ===
{{{
find . -name "*tgz" -type f -exec ls -Sr '{}' \; |awk '{system("cp -v "$0" "NR)}'
}}}

=== 查找20100401时更改过的文件 ===
{{{
cat >> 20100401.sh <<"EOF"
FILE=`find ./ -name "*.tex"`
ls -l --full-time $FILE 2>/dev/null
grep "2010-04-01"
EOF
}}}

== Niubility Tool Netcat ==
=== Transfer file(s) ===
 * Suppose you want to send files in /data from computer A with IP 192.168.2.111 to computer B(with any IP), It's as simple as this:
{{{
server: $ tar -cf - /data | nc -l -p 6666
client: $ nc 192.168.2.111 6666 | tar -xf -
}}}
 * A single file can be sent even easier.
{{{
server: $ cat file | nc -l -p 6666
client: $ nc 192.168.2.111 6666 > file
}}}
 * And you may copy and restore whole disk with nc:
{{{
server: $ cat /dev/sda | nc -l -p 6666
cliend: $ nc 192.168.2.111 6666 > /dev/sda
}}}

=== As Port Scanner ===
nc -vv -z 127.0.0.1 8079-8081

== history how to use ==
{{{
$ history | grep 'ipt'
2    iptables -L -n -v -t nat
$ !2     # will execute the iptables command
}}}

MarkS, yes I know a way to make history contain only uniques. Do the following:
{{{
export HISTIGNORE="&"
That will make history not to save duplicate consecutive entries!
}}}

== some keycodes err will resolve ==
 * Added new keycodes for sk2506 HP multimedia 23-key keyboard
{{{
setkeycodes e016 235
setkeycodes e01e 158
setkeycodes e012 146
setkeycodes e014 148
setkeycodes e015 149
setkeycodes e02d 173
setkeycodes e018 236
setkeycodes e026 238
setkeycodes e017 227
setkeycodes e01f 159
setkeycodes e025 239
setkeycodes e023 237
}}}
=== For my HASEE-F4200  ===
{{{
atkbd.c: Unknown key released (translated set 2, code 0xd8 on isa0060/serio0).
atkbd.c: Use 'setkeycodes e058 <keycode>' to make it known.
getkeycodes will show you codes!
}}}
then
{{{
setkeycodes e058 125
}}}

== Safe Copying ==
{{{
#!/bin/bash
if [ -f $2 ]
then
	echo "$2 is exists. Do you want to overwrite it? (y/n)"
	read yn
	if [ $yn = "N" || $yn = "n" ]
	then
		exit 0
	fi
fi
cp $1 $2
}}}

== SMB About ==
{{{
smbmount //192.168.2.51/D memory/ -o iocharset=cp936,user=xxxx,pass= --verbose
smbclient -U user -I 192.168.16.229 -L //smbshare/    # List the shares
mount -t smbfs -o username=winuser //smbserver/myshare /mnt/smbshare
mount -t cifs -o username=winuser,password=winpwd //192.168.16.229/myshare /mnt/share
}}}

* Note that a password which contains the delimiter character (i.e. a comma ´,´)
will fail to be parsed correctly on the command line. However,
           the same password defined in the PASSWD environment variable or via
           a credentials file (see below) or entered at the password prompt
           will be read correctly.
{{{
mount.cifs -v -o iocharset=utf8,credentials=/root/pw.txt //192.168.200.252/share /mnt/zip/
mount.cifs -o username=cml,iocharset=utf8 //192.168.200.252/share /mnt/zip
sudo mount -t cifs -o username=${USER},password=${PASSWORD},uid=<user>,gid=<group> //server-address/folder /mount/path/on/ubuntu
[[http://unix.stackexchange.com/questions/68079/mount-cifs-network-drive-write-permissions-and-chown]]
}}}


== ss AND netstat && route && ip ==
 * This program is obsolete.  Replacement for netstat is ss.  Replacement for netstat -r is ip route.  Replacement  for  netstat  -i  is  ip  -s  link.Replacement for netstat -g is ip maddr.
{{{
ss -r
ip -s
ip maddr
netstat -lptu
netstat -antup
}}}

=== Add route gateway ===
{{{
route add a.b.c.d dev wlan0
ifconfig eth0 128.100.75.111 broadcast 128.100.75.0 netmask 255.255.255.0
route add -net 128.100.75.0 netmask 255.255.255.0
route add default gw 10.7.84.1 dev wlan0
}}}


== hdparm ==
{{{
hdparm -a 256 -d 1 -r 0 -u 0 -m 2 -c 1 -A 1 -K 0 -P 0 -X 0 -W 0 -S 0 /dev/sda 
}}}
will enable DMA ,32bit support, Sector count for multiple sector I/O to 2

==  If your swapdisk is less than a 1GB, then ==
{{{
dd if=/dev/zero of=/directory/with/much/free/space/tempswap bs=1k count=1000000
chmod 600 tempswap
mke2fs tempswap
mkswap tempswap
swapon tempswap
}}}



== Writing the actual CD ==

=== List content of ISO file ===
isoinfo -f -R -i cflinux-1.0.iso


 * Assuming that you've got cdrecord installed and configured for your cd-writer
type:
{{{
cdrecord --scanbus
cdrecord -v speed=<desired writing speed> dev=<path to your writers generic scsi device> boot.iso
}}}


== Sort about ==
 * Generate a tags file in case-insensitive sorted order.
{{{
find src -type f -print0 | sort -z -f | xargs -0 etags --append
}}}

Shuffle a list of directories, but preserve the order of files
within each directory.  For instance, one could use this to
generate a music playlist in which albums are shuffled but the
songs of each album are played in order.
{{{
ls */*.mp3 | sort -t / -k 1,1R -k 2,2
sort -n -k 2 -t : facebook.txt
sort: ls -l | sort -nr +4
cut: cut -f1 -d':' < /etc/passwd	
}}}

== Shuf about ==
{{{
shuf <<EOF
x
xx
xxx
EOF
shuf -i 1-100
shuf -e clubs hearts diamonds spades
}}}

== Paste about ==

 * For example
{{{
     $ cat num2
     1
     2
     $ cat let3
     a
     b
     c
     $ paste num2 let3
     1       a
     2       b
             c
$ paste -d '%_' num2 let3 num2
          1%a_1
          2%b_2
          %c_
}}}

== Join about ==
 * For example:
{{{

     $ cat file1
     a a1
     c c1
     b b1
     $ cat file2
     a a2
     c c2
     b b2
     $ join file1 file2
     a a1 a2
     c c1 c2
     b b1 b2
}}}

25, Tar about.
*******************************************************
使用TAR作完整备份前,请先# telinit 1; then
tar czvf home.tar -V prg3_home_`date +%Y%m%d%H%M` /home

如果要备份到磁带,可加上M选项,以建立多份备份文件,避免因备份文件过大,无法放入单一磁带中:
tar cMvf /dev/st0 /home
如果不赶时间,可加上W选项,这样可一边备份一边检验备份文件的完整性,以确保该备份文件日后正常使用.
# cd /
# tar czvfW home.tar -V prg3_home_`date +%Y%m%d%H%M` /home

进行差异性备份:
tar czvf home.tar -g /var/log/home-1.snar /home
然后,TAR会参考home-1.snar内含的文件信息,建立LEVEL 1备份文件home-1.tar, 却只包含新增或改动的文件:
tar czvf home-1.tar -g /var/log/home-1.snar /home
还原备件文件, 先还原LEVEL 0, 再还原LEVEL 1 ...:
tar xvf home.tar -g /dev/null
tar xvf home-1.tar -g /dev/null
tar xvf home-N.tar -g /dev/null
可以写个脚本自动化.

cpio 备份到磁带, cpio的crc格式.
find /home -print | cpio -o -Hcrc > /dev/st0
cpio 从磁带取出
cpio -i -Hcrc < /dev/st0
使用CPIO备份到远程主机磁带:
find /home -print | cpio -o -Hcrc -O root@remotehost:/dev/st0

*******************************************************

# tar cf - subdir | gzip --best -c - > archive.tar.gz

For example, suppose you wish to implement
PGP encryption on top of compression, using `gpg' (*note gpg:
(gpg)Top.).  The following script does that:

     #! /bin/sh
     case $1 in
     -d) gpg --decrypt - | gzip -d -c;;
     '') gzip -c | gpg -s ;;
     *)  echo "Unknown option $1">&2; exit 1;;
     esac

   Suppose you name it `gpgz' and save it somewhere in your `PATH'.
Then the following command will create a compressed archive signed with
your private key:

     $ tar -cf foo.tar.gpgz -Igpgz .

Likewise, the command below will list its contents:

     $ tar -tf foo.tar.gpgz -Igpgz .
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
26, Tr about.

* Remove all zero bytes:

          tr -d '\0'

* Put all words on lines by themselves.  This converts all
non-alphanumeric characters to newlines, then squeezes each string
of repeated newlines into a single newline:

    tr -cs '[:alnum:]' '[\n*]'

* Convert each sequence of repeated newlines to a single newline:

    tr -s '\n'
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
27, Shred about.
`shred' overwrites devices or files, to help prevent even very
expensive hardware from recovering the data.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
28, Change mysqladmin password:
mysqladmin -u root password 'newpassword'
mysqladmin -u root -p'password' password 'newpassword'
# -----------------------------------------------------------------------------
MySQL:

  mysqldump --opt -u bugs -p bugs > bugs.sql 
PostgreSQL:

  pg_dump --no-privileges --no-owner -h localhost -U bugs > bugs.sql 

# -----------------------------------------------------------------------------
28, TC 流量控制实例
下载限制单个IP

tc qdisc add dev eth0 root handle 1: htb r2q 1
tc class add dev eth0 parent 1: classid 1:1 htb rate 30mbit ceil 60mbit
tc filter add dev eth0 parent 1: protocol ip prio 16 u32 match ip dst 192.168.1.2  flowid 1:1
就可以限制192.168.1.2的下载速度为30Mbit最高可以60Mbit

r2q,是指没有default的root，使整个网络的带宽没有限制

下载整段IP
tc qdisc add dev eth0 root handle 1: htb r2q 1
tc class add dev eth0 parent 1: classid 1:1 htb rate 50mbit ceil 1000mbit
tc filter add dev eth0 parent 1: protocol ip prio 16 u32 match ip dst 192.168.111.0/24 flowid 1:1

就可以限制192.168.111.0 到255 的带宽为3000k了，实际下载速度为200k左右。
这种情况下，这个网段所有机器共享这200k的带宽。

 
还可以加入一个sfq（随机公平队列）

tc qdisc add dev eth0 root handle 1: htb r2q 1
tc class add dev eth0 parent 1: classid 1:1 htb rate 3000kbit burst 10k
tc qdisc add dev eth0 parent 1:1 handle 10: sfq perturb 10
tc filter add dev eth0 parent 1: protocol ip prio 16 u32 match ip dst 192.168.111.168 flowid 1:1

sfq，他可以防止一个段内的一个ip占用整个带宽。
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
29, Mutt 
两个主要的邮箱格式分別是 mbox 和maildir 。其差別主要在于： mbox  是储存着所有邮件及其邮件头的一个文件；而 maildir 是一个目录树，每个邮件都是一个单独的文件，这往往能提升运行速度。 

http://donnlee.com/2010/01/22/do-you-love-mutt-use-offlineimap-fdm-and-rejoice/
http://jason.the-graham.com/2011/01/10/email_with_mutt_offlineimap_imapfilter_msmtp_archivemail/#sorting-mail-with-imapfilter

30, MP3
# http://stefaanlippens.net/audio_conversion_cheat_sheet
for i in *.mp3; do madplay -o `basename $i .mp3`.wav $i; done    
for i in *.mp3; do lame --decode $i `basename $i .mp3`.wav; done         

31, bc calculater
2^-4.7
echo "e(-4.7*l(2))" | bc -l

PI integer
time echo "scale=1000; a(1)*4" | bc -l

#  echo `date +%Y%m%d`
20090813
#  echo `date +%Y%m%d`-2
20090813-2
#  echo `date +%Y%m%d`-2 |bc
20090811 

32, Linux_fetion
qmake; make

33, dialog 
dialog --backtitle 测试程序 --title 第一步 --yesno 继续? 10 40
dialog --backtitle 设置程序 --title 注意 --msgbox GNU/LINUX 自由操作系统 10 50

34, stat file.
stat -c %s /var/log/etc-1.snar

35, dd about.
[all variants] Copy/Clone Partial Hard Drive:
http://ubuntuforums.org/showthread.php?t=1840320#post_11234165
copy partition:
# dd if=/dev/sda1 of=/dev/sdb1 bs=4096 conv=notrunc,noerror
( bs = block size, use stat -f /dev/sda1 get it 4096)
copy entire disk:
# dd if=/dev/sda of=/dev/sdb conv=notrunc,noerror
使用dd复制硬盘时, 目的硬盘不必做任何分区的规划, 直接就可以复制. 如果原硬盘的MBR扇区是可开机的, 新复制的硬盘亦可以开机了.
backup MBR
# dd if=/dev/sda of=/bak/sda-mbr.image bs=512 count=1
restore MBR
# dd if=/bak/sda-mbr.image of=/dev/sda bs=446 count=1
Task: Backup MBR and Extended Partitions Schema

Backup /dev/sda MBR, enter:
# dd if=/dev/sda of=/tmp/backup-sda.mbr bs=512 count=1
Next, backup entries of the extended partitions:
# sfdisk -d /dev/sda > /tmp/backup-sda.sfdisk
Copy /tmp/backup-sda.sfdisk and /tmp/backup-sda.mbr to USB pen or somewhere else safe over the network based nas server.
Task: Restore MBR and Extended Partitions Schema

To restore the MBR and the extended partitions copy backup files from backup media and enter:
# dd if=backup-sda.mbr of=/dev/sda
# sfdisk /dev/sda < backup-sda.sfdisk

# test write speed
dd if=/dev/zero of=testtttt bs=4k count=10000 conv=fdatasync
 10000+0 records in
 10000+0 records out
 40960000 bytes (41 MB) copied, 1.94146 s, 21.1 MB/s



BAKUP CDROM AS ISO FILE
dd if=/dev/cdrom of=/bak/mycd.iso bs=2048 conv=sync,notrunc
cat /dev/scd0 > RedHat-7.0-i386-powertools.iso 

A bizarre application of the conv=ebcdic option of dd is as a quick 'n easy, but not very secure text file encoder.

    cat $file | dd conv=swab,ebcdic > $file_encrypted
    # Encode (looks like gibberish).		    
    # Might as well switch bytes (swab), too, for a little extra obscurity.
    
    cat $file_encrypted | dd conv=swab,ascii > $file_plaintext
    # Decode.

36, set -o

37, readelf -h /usr/bin/ls 

38, cpio about.
1,backup:
# find /usr/share/ -name '*.png' | cpio -ocvB > /tmp/bak.cpio
# find /usr/share/ -name '*.png' | cpio -o > /dev/st0
2,restore:
# cpio -idvc < /tmp/bak.cpio
# cpio -i < /dev/st0

39, shutdown -n -r -F now

40, xbacklight -inc 98

41, Hiding the cookie jar

    # Obsolete Netscape browser.
    # Same principle applies to newer browsers.
    
    if [ -f ~/.netscape/cookies ]  # Remove, if exists.
    then
      rm -f ~/.netscape/cookies
    fi
    
    ln -s /dev/null ~/.netscape/cookies
    # All cookies now get sent to a black hole, rather than saved to disk.

42, # Correct methods of deleting filenames containing spaces.
    rm *\ *
    rm *" "*
    rm *' '*


43, backup server

tar -cvpzf /fswx.tgz --exclude=/proc --exclude=/lost+found --exclude=/fswx.tgz --exclude=/sys / 2>/root/fswx.log

rsync -avz --progress --exclude=/proc/* --exclude=/sys/* --exclude=/dev/* root@218.75.24.181::fswx /home/backup/fswx/

44, 急！！！/lib /ld-linux.so.2 丢了，　没有办法允许命令啊， 救命啊 ！ 新  [re: xyb]	 

那只是一个命令而已，复杂的操作还是受限制，我原来遇到这种情况，只要export LD_LIBRARY_PATH到一个有ld-so文件的目录即可，系统中不止是lib中有那个文件。 

45, dmidecode                          # Show DMI/SMBIOS: hw info from the BIOS

46, Use nohup to start a process which has to keep running when the shell is closed (immune to hangups).

# nohup ping -i 60 > ping.log &

47, SMB about.

mount -o iocharset=gb2312,codepage=936 /dev/sdb1 /mnt/zip/

48, # mkisofs -J -L -r -V TITLE -o imagefile.iso /path/to/dir

49, IP about
# route add -net 192.168.20.0 netmask 255.255.255.0 gw 192.168.16.254
# ip route add 192.168.20.0/24 via 192.168.16.254       # same as above with ip route
# route add -net 192.168.20.0 netmask 255.255.255.0 dev eth0
# route add default gw 192.168.51.254
# ip route add default via 192.168.51.254 dev eth0      # same as above with ip route
# route delete -net 192.168.20.0 netmask 255.255.255.0

# ifconfig eth0 192.168.50.254 netmask 255.255.255.0       # First IP
# ifconfig eth0 192.168.50.254/24       # First IP
# ifconfig eth0:0 192.168.51.254 netmask 255.255.255.0     # Second IP
# ip addr add 192.168.50.254/24 dev eth0                   # Equivalent ip commands
# ip addr add 192.168.51.254/24 dev eth0 label eth0:1

50,Change MAC address

Normally you have to bring the interface down before the change. Don't tell me why you want to change the MAC address...

# ifconfig eth0 down
# ifconfig eth0 hw ether 00:01:02:03:04:05      # Linux
# ifconfig fxp0 link 00:01:02:03:04:05          # FreeBSD
# ifconfig hme0 ether 00:01:02:03:04:05         # Solaris
# sudo ifconfig en0 ether 00:01:02:03:04:05     # Mac OS X Tiger
# sudo ifconfig en0 lladdr 00:01:02:03:04:05    # Mac OS X Leopard

51, tcpdump -n -i wlan0 net 10.7.84.0/24 >/home/wzsos.log
tcpdump port 80
# tcpdump -nl -i bge0 not port ssh and src \(192.168.16.121 or 192.168.16.54\)
# tcpdump -n -i eth1 net 192.168.16.121           # select to/from a single IP
# tcpdump -n -i eth1 net 192.168.16.0/24          # select traffic to/from a network
# tcpdump -l > dump && tail -f dump               # Buffered output
# tcpdump -i rl0 -w traffic.rl0                   # Write traffic headers in binary file
# tcpdump -i rl0 -s 0 -w traffic.rl0              # Write traffic + payload in binary file
# tcpdump -r traffic.rl0                          # Read from file (also for ethereal
# tcpdump port 80                                 # The two classic commands
# tcpdump host google.com
# tcpdump -i eth0 -X port \(110 or 143\)          # Check if pop or imap is secure
# tcpdump -n -i eth0 icmp                         # Only catch pings
# tcpdump -i eth0 -s 0 -A port 80 | grep GET      # -s 0 for full packet -A for ASCII

52, nmap about.
# nmap cb.vu               # scans all reserved TCP ports on the host
# nmap -sP 192.168.16.0/24 # Find out which IP are used and by which host on 0/24
# nmap -sS -sV -O cb.vu    # Do a stealth SYN scan with version and OS detection
PORT      STATE  SERVICE             VERSION
22/tcp    open   ssh                 OpenSSH 3.8.1p1 FreeBSD-20060930 (protocol 2.0)
25/tcp    open   smtp                Sendmail smtpd 8.13.6/8.13.6
80/tcp    open   http                Apache httpd 2.0.59 ((FreeBSD) DAV/2 PHP/4.

53, Traffic Control
Limit upload

DSL or cable modems have a long queue to improve the upload throughput. However filling the queue with a fast device (e.g. ethernet) will dramatically decrease the interactivity. It is therefore useful to limit the device upload rate to match the physical capacity of the modem, this should greatly improve the interactivity. Set to about 90% of the modem maximal (cable) speed.
Linux
For a 512 Kbit upload modem.

# tc qdisc add dev eth0 root tbf rate 480kbit latency 50ms burst 1540
# tc -s qdisc ls dev eth0                         # Status
# tc qdisc del dev eth0 root                      # Delete the queue
# tc qdisc change dev eth0 root tbf rate 220kbit latency 50ms burst 1540

54 partimage about.

./configure \
--prefix=/usr \
--build=$ARCH-slackware-linux \
--with-ssl


make || exit 1
make certificates
make prefix=$PKG/usr install
# start deamon
partimaged -n -L -d /tmp/

55, hwclock
save current time to hwclock.
# date "08091452"
# hwclock --systohc

56, rpm src rebuild
# rpmbuild --rebuild *.src.rpm
# cd /usr/src/redhat/RPMS/i386(X86)

57,  How to burn over the network?

Usally a file transfer with FTP is fast enough to feed a CD-recorder at quadruple (4x) speed even over a 10 Mbit ethernet. You can couple the ftp-client and cdrecord via a fifo. First create a fifo named cdimage:

    mkfifo cdimage
    ftp other.host.org
    get cdimg cdimage

Then treat cdimage like a regular file, i.e. issue the following command:

    cdrecord dev=0,1,0 speed=2 cdimage
cdrecord -v -eject speed=48 dev=0,0,0 $MYISO
cdrecord -v -dao speed=4 dev=/dev/dvd /path/to/Fedora-8-i386-DVD.iso


58, PERL批量替换
perl -pi -e 's|latin1|utf8|g' `find ./ -type f`

59, smbclient: Sending Messages To MS-Windows Workstations

The smbclient command can talk to an SMB/CIFS server. It can send a message to selected users or all users on MS-Windows systems:

smbclient -M WinXPPro <<EOF
Message 1
Message 2
...
..
EOF

OR

 
echo "${Message}" | smbclient -M salesguy2
 

60, Create a sooper simpel NAT firewall
# iptables -I FORWARD -i eth0 -o eth1 -m state --state ESTABLISHED,RELATED
-j ACCEPT
# iptables -I FORWARD -i eth1 -o eth0 -j ACCEPT
# iptables -t nat -I POSTROUTING -o eth0 -j MASQUERADE

61, import about.
import -geometry 1024x768 `date +%Y_%m_%d-%H%M%S`.png
cp /etc/sysctl.conf{,.`date +%Y%m%d-%H%M%S`} -v


grep -lri sshd /var/log
62, mplayer about
mplayer -cdrom-device /dev/cdrom cdda://

ffmpeg -f alsa -i default -f v4l2 -s 640x480 -i /dev/video0 output.mpg

ffmpeg -i /home/merlyn/張婧懿\ -\ 斑馬斑馬\ \(完整版\)\ -\ YouTube\
\[720p\].mp4 -vn -acodec copy  張婧懿\ -\ 斑馬斑馬.aac

cdda2wav -vall -cddb=1 -paranoia -B

echo 'wget -c www.example.com/files.iso' | at 09:00 
openvpn --mode server --server 192.168.1.0 255.255.255.0 --dev tun --dh dh1024.pem --ca ca.crt --cert  --key mycert.key --script-security 2

# about replace word
perl -pi -e 's/.../.../g'

# Sed print number
sed = updateAllConfigFiles.pl | sed 'N; s/^/     /; s/ *\(.\{6,\}\)\n/\1  /' | sed -n '190,195p'

# Get Serial Number Linux
dmidecode |grep -A8 "System Information" |grep "Serial Number" |sed 's/$/\r/'|sed 's/^[ \t]*//'

# delete begin 2 word 
sed s/^..// script.sh

# delete begin 11 characters with "-r" (mean extension features)
sed -r 's/.{11}$//' script.sh 
sed 's/^[0-9]*//' < script.sh
sed -r  's/^.{1}//' < list
sed 's/libgcc/&_eh/' = sed 's/libgcc/libgcc_eh/'

# converter utf8 file to gbk then display it.
more examples/demo.py | iconv -f utf8 -t gbk - | more

# awk about
http://ghostdog74.livejournal.com/37461.html

# Bash about
http://www.gnu.org/software/bash/manual/bashref.html
ubuntuforums.org/showthread.php?t=1007825

# Perl about
Here's an inspiration on how to quickly fix all scripts relying on short_open_tag being enabled:

find -name '*.php' | xargs perl -pi -e 's/<\?= ?(.*?) ?\?>/<?php echo($1); ?>/g'
find -name '*.php' | xargs perl -pi -e 's/<\?/<?php/g'
find -name '*.php' | xargs perl -pi -e 's/<\?phpphp/<?php/g'

# Bash Scientists
for number in (( number=1; number<=100; number++ )); do echo "number = $number"; done
  for number in {1..100}; do echo "number = $number"; done
    number=0; while [ $number -lt 100 ]; do echo "number = $number"; let number++; done
    number=100; until [ $number -lt 90 ]; do echo "number = $number"; ((number--)); done
# rsync about
    Synchronize files in a directory between 2 hosts using the program rsync. host1's /disk01 (source) is the remote host and /disk01 (destination) is a local directory. The destination is always made to look like the source even if files need to be deleted in the destination (--delete). The source's data is never touched. The source is always named first and the destination is always named second. Trailing / on the source as means copy the contents of this directory to the destination. Without the trailing / on the source you get the directory name copied with all it's files in it. Below uses ssh as the remote-shell program as the transport. It also turns on the lowest grade encryption to speed up the transfer.

rsync -av --delete --rsh="ssh -c arcfour -l root" host1.domain.lan:/disk01/ /disk01/

rsync --archive --delete --no-owner --exclude=*.sbopkg --verbose --timeout=30 slackbuilds.org\dotsslackbuilds/13.1/ /var/lib/sbopkg/SBo/13.1/

rsync (Network efficient file copier: Use the --dry-run option for testing)
  rsync -P rsync://rsync.server.com/path/to/file fileOnly get diffs. Do multiple times for troublesome downloads
    rsync --bwlimit=1000 fromfile tofileLocally copy with rate limit. It's like nice for I/O
      rsync -az -e ssh --delete ~/public_html/ remote.com:'~/public_html'public_htmlMirror web site (using compression and encryption)
	rsync -auz -e ssh remote:/dir/ . && rsync -auz -e ssh . remote:/dir/dirSynchronize current directory with remote one

# wget about
Use wget grab all of a certain type of file listed on a web page and put them in the current dir. The example will use jpeg's.

wget -r -l1 --no-parent -A "*.jpg" http://www.website.com/pictures/ 
wget --follow-ftp=on --input-file=ok_list --continue
tr -d ' \t\n\r\f' <inputFile >outputFile

# Kill program
pkill xbindkeys
kill  $(ps -A | grep xbindkeys | awk '{ print $1 }' | sed -n '1p')

# 計算自己在成都平均每天用了好多錢。
# echo "`awk '{a+=$2}END {print a}' fee_in_chengdu.tex`/65" | bc
awk '{ a+=$2 }END { print "sum is", a, " average is", a/NR }' < fee_in_chengdu.tex

echo 民生 | iconv -f gb2312 -t utf8 - | grep - * | iconv -f utf8 -t gb2312 -
# man about
man -t iptables | ps2pdf - > ascii.pdf

# Look about
look calc

# backup

find . -type f -name *ini | xargs egrep --color=always --with-filename '192.53.50.220|192.53.50.221' | uniq -c
useradd --groups adm,wheel,bin,root -g root --shell /bin/bash heyhey

# delete 7 days ago.
\ls 2*_*_*_db.tar.gz | awk -F_ -v d=`date +%Y%m%d -d '-7 days'` '$1$2$3<d{system("rm -f "$0)}'

# List process by memory useage.
ps aux |grep oracle |awk '{a+=$4}END {print a}'
ps -e -orss=,args= | sort -b -k1,1n | pr -TW$COLUMNS 

# Reiserfs data recovery
1. Create partition copy

        dd if=/dev/hda7 conv=noerror > /hda7.img

2. Set up device containing copy of partition (created in 1.)

        losetup /dev/loop/0 /hda7.img

3. Rebuild FS tree, performing a thorough partition scan and logging to /recovery.log file

        reiserfsck --rebuild-tree -S -l /recovery.log /dev/loop/0

(4. Check written log file)

        (less /recovery.log)

5. Create directory for mounting recovered partition

        mkdir /recovery

6. Mount recovered partition in directory created in 5.

        mount /dev/loop/0 /recovery

7. Access recovered partition's lost+found directory and look for files

        cd /recovery/lost+found

8. If not there (7.), then look for in original directory

        cd /recovery/

9. Remount /home partition

        mount /home

10. Copy recovered files from 7./8. to /home/

        cp /recovery// /home//

11. Unmount recovered partition

        umount /recovery

12. Detach recovered partition device

        losetup -d /dev/loop/0

sed -e 'N;s/.*/[&]/' << EOF
ok
ooo
> EOF
[ok
ooo]
top -b -n 2 -d 3 >>top.txt

#ssh proxy
ssh -qTfnN -D 7070 -p 8888 onlybird@ssh.onlybird.tk

# UPPER --> lower
convmv --notest -f UTF8 --lower -r ./

# Back up files in new-dir.
find . -depth -print0 | cpio --null -pvd new-dir
The example shows copying the files of the present directory, and
sub-directories to a new directory called new-dir.  Some new options are
the `-print0' available with GNU find, combined with the `--null'
option of cpio.  These two options act together to send file names
between find and cpio, even if special characters are embedded in the
file names.  Another is `-p', which tells cpio to pass the files it
finds to the directory `new-dir'.
*** done ***

# gnuplot
set term png enhanced font '/usr/share/fonts/TTF/LiberationSans-Regular.ttf' 12
Split movie:
mencoder -ovc copy -oac copy -ss 01:13:40 -endpos 00:3:11 -o test.mpeg input.mpeg
Split mpeg to picture.
ffmpeg -y -r 1000 -i "myfile.avi" -sameq "image.%06d.jpg"
ffmpeg -i some_video.flv -vcodec copy -acodec copy -ss 00:00:00 -t 00:02:24 cut_video.flv

# curl about
curl dict://dict.org/d:lier
curl -o /dev/null -w Connect: %{time_connect} TTFB: %{time_starttransfer} Total time: %{time_total} n http://www.google.com.sb/

time curl -s "http://www.google.com.sb/index.html?[1-1000]"
xset dpms force off
xrandr -o inverted

mysqldump -h host -u root -p --database --default-character-set=utf8 --hex-blob dbname >dbname_backup.sql
备份后的，可以直接source回去 

echo "OK?" | mutt -s "溫州移動日志" wzemc@163.com -a /mnt/media/incoming/RVTools_export_all_201276155054.xls

grub2-install --force --no-floppy --root-directory=/mnt/zip/ /dev/sdb
nc -vv -w 1 127.0.0.1 20-33


== Gentoo About ==
=== Snort: ''ERROR: Can't find pcap DAQ!'' ===
I solved it this way, the DAQ and snort compiled manually by adding the option
to configure snort path DAQ libraries and headers 
{{{
# Configure DAQ related options for inline operation. For more information, see
# README.daq
#
config daq: afpacket
config daq_dir: /usr/lib64/daq
config daq_mode: passive
}}}

Calculating dependencies \ * Digest verification failed:
 * /usr/portage/net-misc/dropbox/dropbox-1.4.23.ebuild
  * Reason: Filesize does not match recorded size
   * Got: 2312
    * Expected: 2309
    \cdots done!

brightmoon ~ # ebuild /usr/portage/net-misc/dropbox/dropbox-1.4.23.ebuild digest
>>> Creating Manifest for /usr/portage/net-misc/dropbox
brightmoon ~ # ebuild --force /usr/portage/net-misc/dropbox/dropbox-1.4.23.ebuild digest
>>> Downloading 'https://dl-web.dropbox.com/u/17/dropbox-lnx.x86-1.4.23.tar.gz'
--2013-01-11 18:21:57--  https://dl-web.dropbox.com/u/17/dropbox-lnx.x86-1.4.23.tar.gz
Resolving dl-web.dropbox.com\cdots 23.21.167.203, 23.21.195.122, 50.19.106.181, \cdots
Connecting to dl-web.dropbox.com|23.21.167.203|:443\cdots connected.
HTTP request sent, awaiting response\cdots 200 OK
Length: 18541708 (18M) [application/x-tar]

# about rename files
rename -v TEX tex *.TEX

There are several ways, but using rename will probably be the easiest.

Using one version of rename:

rename 's/^fgh/jkl/' fgh*

Using another version of rename (same as Judy2K's answer):

rename fgh jkl fgh*




## Minicom about
Minicom does not run from the host that you are trying to connect from the Sun box when you run as a non-root user.
Add yourself to the uucp and to the dialout group.

# usermod -a -G uucp,dialout [login]


## Check Badblocks.
From the terminal, type following command:

    $ sudo badblocks -v /dev/hda1 > bad-blocks

    The above command will generate the file bad-blocks in the current directory from where you are running this command.

    Now, you can pass this file to the fsck command to record these bad blocks

        $ sudo fsck -t ext3 -l bad-blocks /dev/hda1
            Pass 1: Checking inodes, blocks, and sizes
                Pass 2: Checking directory structure
                    Pass 3: Checking directory connectivity
                        Pass 4: Check reference counts.
                            Pass 5: Checking group summary information.

                                /dev/hda1: ***** FILE SYSTEM WAS MODIFIED *****

                                    /dev/hda1: 11/360 files, 63/1440 blocks
娌掗棞淇�,鎴戣嚜宸辨壘鍒扮瓟妗堜簡,瀵湪姝よ畵澶у鍒嗕韩涓€涓�.
        鎵€璎� block size & fragment size, 閫欐槸灞柤 file system
        鐨勪竴绋В姹烘柟妗�. 鑷�4.3 BSD, BSD 鐢ㄩ€欑ó鏂规硶渚嗚В姹烘獢妗� fragment
        鐨勫晱椤�
                鍏堝亣瑷�  a block size= 4K, a fragment size = 256Bytes.
        鍋囧浣犵従鍦ㄨ灏囦竴鍊� 1K 鐨勬柊妾旀瀵叆 file system, FS 鏈冩妸瀹冨瓨鍏� 4
        鍊媐ragment,鑰屼笉鏈冨瓨鍏� block,涓€浣嗛€欏€嬫獢妗堢辜绾岃 append 澧炲姞鍒� 4K
        鏅�, FS 鏈冨皣瀹冭綁瀛樺埌涓€鍊� block涓�, 鑰屽師渚嗙殑 16 鍊媐ragments 灏辨渻琚� clean
                                           ^^^^^^^^^^^^^^^^^^^^
                                       鍥犵偤鐣朵綘鐨勬獢妗堝ぇ鍒� 4K 鏅�,瀹冧綌鐢�
                                       浜� 16 (4K / 256 bytes) 鍊� fragments
                鍐嶈垑鍊嬩緥瀛�, 濡傛灉鐝惧湪鍙堝瓨浜嗕竴鍊嬫柊鐨� 4.1K 鐨勬獢妗�, FS 鏈冨垎閰�
        涓€鍊� block 鍙� 4鍊� fragment 绲� 閫欏€嬫獢妗�,
        鍥犵偤 1 block + 4 fragments = 4 K + 256 bytes * 4 = 4.1K

        鎵€浠�,鏈夋鍙煡,灏嶆柤涓€鍙� news server, bbs, 鎴栨槸鏈冩湁澶ч噺鐨勫皬妾旀瀛樺彇鏅�,
        鐐轰簡闄嶄綆 FS 鐨勭┖闁撹€楁悕鐜�,鎳夎┎鎺＄敤 -b 4096 -f 256,
        鑰屼笉瑕佹帯鐢ㄩ爯瑷€肩殑 -b 8192 -f 1024,鍥犵偤澶ч儴鍒嗙殑淇′欢閮戒笉瓒呴亷 512 bytes,
        鏈変簺鏇翠笉瓒呴亷 256 bytes, 浣嗘槸閫欐ǎ鍙兘鏈冮檷浣庡瓨鍙栫殑閫熷害.浣嗘垜鐩镐俊涓嶅毚閲�
        鏈夎垐瓒ｇ殑浜哄彲浠ヨ│瑭�.

# du about

du -hc | grep '^[0-9][0-9]M'
du --max-depth=1 -m | sort -n
du -h --max-depth=1 

# List processes by mem usage 
ps -e -orss=,args= | sort -b -k1,1n | pr -TW$COLUMNS
ps -eo pmem,pcpu,rss,vsize,args | sort -k 1 -r | more
find / -maxdepth 3 -size +100M -type f \( -iname "*.iso" -o -iname "*.tar" -o -iname "*.exe" \)

# SSH X11 Login

ssh -Y root@192.168.2.247


# If you're building software with autotools then you can do it with\ldots

CC=gcc-4.6.2 ./configure
make

# CISCO mib mem
"scale=2;`snmpwalk -v2c -c public localhost mem | grep memTotalFree | awk -F= '{ print $2 }' | tr -d -c 0-9`/`snmpwalk -v2c -c public localhost mem | grep memTotalReal | awk -F= '{ print $2 }' | sed 's/[^0-9]//g'`" | bc -l

# replace c++ comments to c comments
 find . -iname 鈥�*.h鈥� -exec sed -i 鈥榮#//\(.*\)#/*\1 */#鈥� {} \;

# Linux print how to 

lpstat -s
lp -d printer_name filename


# how to determine UDP port 

 nc -z -vv -u 10.20.160.211 161

# PXE About
http://blog.smartcore.net.au/smartos-ipxe-boot-with-pfsense/#2
http://thestorey.ca/wordpress/?p=26
http://wellsie.net/p/286/
http://readme.maven.pl/2007/01/13/pxe-remote-boot-for-your-homework-lab/

# install minimal gnome-desktop on Ubuntu Linux
sudo apt-get install lightdm gnome-terminal synaptic && sudo apt-get install --no-install-recommends gnome-session-fallback

## ubuntu live cd 
http://www.instalinux.com/cgi-bin/debian_image.cgi
http://mijyn.github.io/relinux/#download
http://www.remainsys.com/

# relinux how to 
sudo add-apt-repository ppa:relinux-dev/testing
sudo apt-get update


1. sudo vi /etc/apt/sources.list

Paste below two lines.

# Remainsys
deb http://www.remainsys.com/repository lucid/

2.Update recently added source list by executing

sudo apt-get update

3.Type

sudo apt-get install remainsys

You have successfully installed remainsys on your machine.



## Could not preserve times for system_backup.img: UTIME failed.


# OTRS how to 

http://linux4you2.blogspot.com/2012/04/how-to-install-open-ticket-request.html

# pFsense how to 
http://blog.sina.com.cn/s/blog_3eaf68c70100zegr.html
http://www.pczone.com.tw/vbb3/thread/29/129030/

# proftpd how to
http://blog.wu-boy.com/2008/04/freebsd-linux-ubuntu-proftpd-%e6%94%af%e6%8f%b4-utf-8-mysql-%e8%99%9b%e6%93%ac%e5%b8%b3%e8%99%9f-quota-%e9%99%90%e5%88%b6/

# rhel cluster how to
http://www.nxnt.org/2010/09/redhat-cluster-howto/

# tomcat about
# Restrict IP coming to Tomcat Service 
http://vicker313.wordpress.com/2010/11/05/restrict-ip-coming-to-tomcat-service/
http://tomcat-configure.blogspot.com/2009/01/tomcat-maxthreads-configuration.html


# CSV parsel 
 column -s, -t <  RVTools_export_all_2014716142140/RVTools_tabvHost.csv | less -#2 -N -S
 http://stackoverflow.com/questions/1875305/command-line-csv-viewer

# How to fix stale NFS mounts on linux without rebooting
http://joelinoff.com/blog/?p=356
 umount -lf /stale/fs

# NFS performance about
http://nfs.sourceforge.net/nfs-howto/ar01s05.html
 http://www.slashroot.in/how-do-linux-nfs-performance-tuning-and-optimization

 # Android
 adb shell mount -o remount rw /system 


 # ssh  debug1: Unspecified GSS failure. Minor code may provide more information
 GSSAPIAuthentication stops it from taking so long to authenticate
 Edit your /etc/ssh/sshd_config to set GSSAPIAuthentication no

 # snmp error log
 vi /etc/init.d/snmpd
 OPTIONS="-LS0-4d -Lf /dev/null -p /var/run/snmpd.pid -a"
 
 # Make special modules IN Linux
 brightmoon linux # make modules SUBDIRS=drivers/usb/serial/

 #  How to convert VirtualBox vdi to KVM qcow2
 qemu-img convert -f vdi -O qcow2 vm.vdi vm.qcow2

 # goagent import CA
 certutil -d sql:/home/merlyn/.pki/nssdb -A -t "C,," -n GoAgent -i /home/merlyn/goagent-goagent-3e867d2/local/CA.crt 
 certutil -d sql:/home/merlyn/.pki/nssdb -L

 #Pipe about
 www.serkey.com/tag/expdp-unix-pipe/
 danielwestermann.com/tag/oracle/page/2/
 stujordan.wordpress.com/2011/09/12/backing-up-esxi-images-using-ghettovcb-and-ftp/

 # tar Pipe
 http://blog.extracheese.org/2010/05/the-tar-pipe.html

 tar cf - . | ssh kumquat 'cd /work/bkup/jane && tar xvf -'

 tar cf - . | (cd /work/bkup/jane && tar xvf -)


# ulimit sysctl.conf

Increase max number of ulimit open file in Linux.

1- Step :  open the sysctl.conf  and add this line  fs.file-max = 65536

vi /etc/sysctl.conf   add end of line
fs.file-max = 65536

save and exit.

2. Step : vi /etc/security/limits.conf  and add below the mentioned

*          soft     nproc          65535
*          hard     nproc          65535
*          soft     nofile         65535
*          hard     nofile         65535
save and exit check max open file ulimit 


I am adding this to the mirror option. 
--exclude-glob distri/sites/.*/files/styles/
 
My plan is to exclude the styles directory fully. The problem is that it is 
insubfolders of 


distri/sites/foo/styles
distri/sites/foo1/styles
distri/sites/foo2/styles
distri/sites/foobar/styles
...

with the exclude option i posted above lftp will still download folders 
like: 
distri/sites/foobar/files/styles/square_thumbnail/public/rattan_ernte2.jpg

thankys for helping me.

I actually writing on a small script that mirrors an ftp to localhost:

lftp -e "
set ftp:list-options -a;
set ftp:charset ISO-8859-15;
set ssl:check-hostname no;
set net:timeout 60;
set net:max-retries 2;
set net:reconnect-interval-base 5;
open ftp://$user:$pass@$host;
lcd $local_dir;
cd $remote_dir;
mirror  --use-cache \
        --parallel=3 \
        --continue \
        --delete \
        --verbose=1 \   
        --exclude-glob screensnapr/ \
        --exclude-glob usage/ \
        --exclude-glob logs/ \
        --exclude-glob cgi-bin/ \
        --exclude-glob INCOMING/ \              
        --exclude-glob distri/sites/.*/files/styles/ \
        --exclude-glob amazon/
quit" | tee log.txt

# Persistent names for usb-serial devices
http://hintshop.ludvig.co.nz/show/persistent-names-usb-serial-devices/

=== USB boot ISO ===
http://www.pendrivelinux.com/install-grub2-on-usb-from-ubuntu-linux/

=== USB mount ===
{{{
mount -o defaults,rw,iocharset=iso8859-1 -v /dev/sdc1 /mnt/zip && cd /mnt/zip
mount -o defaults,rw,iocharset=cp936 -v /dev/sdc1 /mnt/zip && cd /mnt/zip
}}}
# Zabbix how to
https://www.digitalocean.com/community/tutorials/how-to-install-zabbix-on-ubuntu-configure-it-to-monitor-multiple-vps-servers

# SCO UNIX to VMware
http://bbs.chinaunix.net/forum.php?mod=viewthread&tid=255472
https://communities.vmware.com/thread/95323?start=0&tstart=0
https://communities.vmware.com/thread/295196

# Infomix Database
http://database.ittoolbox.com/groups/technical-functional/informix-l/how-to-backup-informix-db-1560639
http://stackoverflow.com/questions/51673/what-is-th-easiest-way-to-copy-a-database-from-one-informix-ids-11-server-to-ano
http://stackoverflow.com/questions/51673/what-is-th-easiest-way-to-copy-a-database-from-one-informix-ids-11-server-to-ano

# Arch Linux about
#pacman
https://flexion.org/posts/2013-05-spring-cleaning-arch-linux.html
https://www.digitalocean.com/community/tutorials/downloads-/-installation#getting-information

# Ansible How to
https://serversforhackers.com/getting-started-with-ansible/

# OpenERP how to
http://www.oscg.cn/openerp-manual-doc-03/

## extract audio from video file
sudo apt-get install -y libav-tools
avconv -i FILE_IN.mp4 -vn -c:a copy FILE_OUT.mp3


# extract EXE file in Linux 
unzip -a cp025109.exe

# How To Install and Configure EMC PowerPath on Linux
--------------------------------------------------------------------------------------------------------------
http://www.thegeekstuff.com/2010/10/powermt-command-examples/

[root@bakrac1 ~]# rpm -ivh --test EMCPower.LINUX-6.0.0.00.00-158.OL6.x86_64.rpm

[root@bakrac1 ~]# rpm -ivh EMCPower.LINUX-6.0.0.00.00-158.OL6.x86_64.rpm 
Preparing...                ########################################### [100%]
   1:EMCpower.LINUX         ########################################### [100%]
All trademarks used herein are the property of their respective owners.
NOTE:License registration is not required to manage the CLARiiON AX series array.
  
*** IMPORTANT *** 
Please check the following configurations before starting PowerPath:
   - Add _netdev to /etc/fstab mount options for PowerPath pseudo devices.
   - Ensure netfs service is started.
     netfs service is needed to mount devices with _netdev option.
   - Set LVM filter in /etc/lvm/lvm.conf according to PowerPath recommendation.
   - Blacklist all devices in /etc/multipath.conf and stop multipathd service.
   - Install PowerPath license(s) and ensure that policy is not set to BasicFailover.
   - If no license is available, ensure that only one HBA port is active in the host.
     PowerPath supports only single-HBA configuration when unlicensed.
Refer to PowerPath Installation and Administration Guide for details.


[root@bakrac1 ~]# emcpreg -install

===========   EMC PowerPath Registration ===========
Do you have a new registration key or keys to enter?[n] y
                  Enter the registration keys(s) for your product(s),
                  one per line, pressing Enter after each key.
                  After typing all keys, press Enter again.

Key (Enter if done): BQPI-OB4E-GFCA-Q7SW-MQ9B-Z76J
1 key(s) successfully added.
Key successfully installed.

Key (Enter if done): 
1 key(s) successfully registered.


[root@bakrac1 ~]# /etc/init.d/PowerPath start
Starting PowerPath: 
 done
[root@bakrac1 ~]# 
[root@bakrac1 ~]# powermt check_registration

Key BQPI-OB4E-GFCA-Q7SW-MQ9B-Z76J
  Product: PowerPath
  Capabilities: All 

powermt display options
powermt display hba_mode
powermt display paths
powermt display port_mode
powermt version
powermt check

# Save it
powermt save
cat /etc/powermt.custom


# Bonding how to RHEL6
https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Deployment_Guide/s2-networkscripts-interfaces-chan.html
--> ifcfg-bond0
DEVICE=bond0
IPADDR=192.168.200.11
NETMASK=255.255.255.0
GATEWAY=192.168.200.1
ONBOOT=yes
BOOTPROTO=none
USERCTL=no
NM_CONTROLLED=no
#BONDING_OPTS="miimon=100 mode=0 downdelay=200"
BONDING_OPTS="miimon=100 mode=1 primary=eth0 downdelay=0 primary_reselect=1"

--> ifcfg-eth0/eth1
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
MASTER=bond0
SLAVE=yes
USERCTL=no
NM_CONTROLLED=no
HWADDR=5c:f3:fc:da:ee:c4

# RHCS 
http://initrd.org/wiki/RHCS_Mechanics
https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Cluster_Administration/s2-admin-manage-ha-services-operations-cli-CA.html

# remount  read only root /
http://www.noah.org/wiki/Remount_root_partition
mount -n -o remount,defaults /dev/VolGroup00/LogVol00 /

# arch linux
[root@alarmpi ~]# systemctl mask gssproxy.service
Created symlink from /etc/systemd/system/gssproxy.service to /dev/null.
[root@alarmpi ~]# 

# Dropbear how to
mkdir /etc/dropbear

cd /etc/dropbear
dropbearkey -t rsa -f dropbear_rsa_host_key
dropbearkey -t dss -f dropbear_dss_host_key

# How to determine max memory supported?
dmidecode -t 16

## OSwatcher how to 
# running 120' collect for 48 hours.
./startOSWbb.sh 120 48 

export LC_ALL=en_US.UTF-8
java -d64 -jar oswbba.jar -i /media/incoming/zjsos/wzygj_c/2015-04-10_check/oswbb/archive/


# mpstat
mpstat -P ALL 2 10

# wicd failed to read stdin!
https://forums.gentoo.org/viewtopic-t-844975-view-next.html?sid=df197b34b4337a2cd73045d24e0fa418
# /usr/lib64/python2.7/site-packages/wicd/misc.py

    if return_obj:
        std_in = PIPE
    else:
        std_in = None
#        return f
OR:
    http://debiantjw.blogspot.com/2014/07/wicd-authentication-timed-out-solved.html
#        f = Popen(cmd, shell=False, stdout=PIPE, stdin=std_in, stderr=err,
        f = Popen(cmd, shell=False, stdout=PIPE, stdin=none, stderr=err,

# bootable 
http://linux-sunxi.org/Bootable_SD_card

== CSV to vCard ==
https://convertio.co/zh/xls-csv/
http://www.artistec.com/pages/CSV2vCard.html

== Citrix ICA launch ==
* sudo emerge -av net-misc/icaclient
# to open it with /opt/Citrix/ICAClient/wfica, and tell Firefox to remember
# that choice.

== SSH run comman ==
ssh server.com 'screen -d -m ~/myscript.sh'
ffmpeg -f v4l2 -s 640x480 -i /dev/video0 output.mpg

== Disable IPv6 ==
{{{
cat >> /etc/sysctl.conf <<"EOF"
net.ipv6.conf.all.disable_ipv6 = 1
EOF
}}}

== VLC fun ==
Open VLC media player and press Ctrl+N. Then type screen:// in URL and click
Play and see what happens!

== VirtualBox ==
=== graphic card support ===
The graphics card can't be utilized in a virtual machine like you're thinking.
There's very limited support with many caveats. Maybe in a few more years this
will improve. If you need hardware accelerated 3D graphics then dual boot with
Windows instead of using a virtual machine.

If you just want to make the virtual machine use a different resolution install
the VirtualBox guest additions in the Windows guest. They are available as an
option for the optical drive, it says something like "Install Guest Addons"
which will mount an image of the software in the guest so it can be installed.

== RPM about ==
=== Sort installed RPMs by size  ===
rpm -qa --queryformat '%{size} %{name}\n' | sort -rn | more

http://www.cyberciti.biz/howto/question/linux/linux-rpm-cheat-sheet.php

== tomcat ==
java.net.BindException: Cannot assign requested address
ifconfig lo up
cat /etc/hosts

== Quiet Console Login ==
touch .hushlogin

== Run script after login in ==
{{{
#! /bin/bash
# ~/.bash_profile

MAC=`ifconfig eth0 | sed -n '/HWaddr/p' | awk '{ print $5 }'`
CONFIRM_FILE="/opt/apps/.netconfig"

if [ $MAC  != '02:00:27:bb:f3:3e' ] && [[ ! -e "$CONFIRM_FILE" ]]
then
	/sbin/netconfig
else
	source ~/.bashrc
fi
}}}

== VPN how to ==
http://www.theusefulvpn.com/
http://www.adminsehow.com/2010/04/connect-to-pptp-vpn-from-linux-only-by-one-command/

== Moinmoin ==
https://labix.org/editmoin#head-0a5434b85feb1fb0cfc86c13d3ae6a7142076941
