mkfs.btrfs -L Gentoo /dev/sdb2 
Detected a SSD, turning off metadata duplication.  Mkfs with -m dup if you want
to force metadata duplication.

WARNING! - Btrfs v3.14.2 IS EXPERIMENTAL
WARNING! - see http://btrfs.wiki.kernel.org before using

Performing full device TRIM (27.94GiB) ...
Turning ON incompat feature 'extref': increased hardlink limit per file to
65536
fs created label Gentoo on /dev/sdb2
    nodesize 16384 leafsize 16384 sectorsize 4096 size 27.94GiB
    Btrfs v3.14.2

== make.conf ==
# gcc -c -Q -march=native --help=target | grep march
-march=core-avx-i


== fingerprint ==
emerge -av sys-auth/fprintd
emerge -av sys-auth/thinkfinger


== wacom ==
http://ubuntuforums.org/showthread.php?t=2185231

emerge x11-drivers/xf86-input-wacom
{{{
#!/bin/bash

## Get the "Device name" or ID number
## for touch from 'xsetwacom list dev'

DEVICE="ID 056a:00e6 Wacom Co., Ltd" 
TOUCH_STATE=`xsetwacom get "$DEVICE" touch`
if [ "$TOUCH_STATE" == "on" ]
  then
    echo "Touch is ON, turning OFF."
    xsetwacom set "$DEVICE" touch off
  else
    echo "Touch is OFF, turning ON."
    xsetwacom set "$DEVICE" touch on
fi
}}}


== VGA ==
http://www.thinkwiki.org/wiki/Intel_HD_Graphics
=== Power Saving Kernel Options ===

The following boot options may help considerably with power:

 * i915.i915_enable_rc6=1 i915.semaphores=1 pcie_aspm=force

== Packages ==
{{{
 emerge -av xkill www-servers/uwsgi nmon lsof iotop atop tiptop at atop
 ddrescue dosfstools ncdu sys-block/open-iscsi sys-block/fio parted sys-apps/pv
 hwinfo ed sci-visualization/gnuplot sys-apps/ethtool rdesktop net-misc/iperf
 net-misc/bridge-utils net-misc/tightvnc net-misc/aria2 net-fs/cifs-utils
 net-fs/nfs-utils net-analyzer/pchar net-analyzer/nsat nmap net-snmp
 net-analyzer/nessus net-analyzer/lft net-ftp/lftp net-analyzer/hydra
 net-analyzer/knocker fping net-analyzer/dnstracer recordmydesktop
 net-analyzer/ettercap media-sound/vimpc media-sound/sox media-sound/moc
 media-fonts/wqy-unibit mutt msmtp  strace dev-util/perf dev-util/ltrace
 dev-util/android-tools  dev-python/ipython
 dev-python/django app-emulation/docker  dev-db/redis app-text/zathura
 dev-db/oracle-instantclient-sqlplus app-text/stardict  app-misc/lfm
 app-misc/vlock rlwrap app-misc/hatools app-misc/leave app-misc/grc
 elasticsearch app-misc/birthday app-misc/binclock app-misc/abook
 app-forensics/rkhunter app-forensics/chkrootkit app-emulation/docker-compose
 app-arch/unrar app-benchmarks/dbench app-benchmarks/httperf
 app-benchmarks/stress app-benchmarks/wrk app-arch/p7zip app-antivirus/clamav
 sys-process/glances app-admin/conky app-admin/sysstat
 media-fonts/font-bh-lucidatypewriter-100dpi games-misc/fortune-mod
 games-misc/fortune-mod-tao games-misc/fortune-mod-taow
 games-misc/fortune-mod-slackware games-misc/fortune-mod-powerpuff
 games-misc/fortune-mod-osfortune games-misc/fortune-mod-at-linux net-im/pidgin
 app-admin/whowatch app-office/wps-office net-mail/getmail 
 media-gfx/xv ncmpcpp mpd app-misc/sl  traceroute cowsay
 app-vim/c-support app-vim/calendar app-vim/dirdiff app-vim/nerdcommenter
 app-vim/nginx-syntax app-vim/notes app-vim/screen app-vim/vimpython
 app-cdr/cdrtool  dev-texlive/texlive-xetex  
}}}


= Troubleshooting =
== iwlwifi ==
https://forums.gentoo.org/viewtopic-t-1001638.html




https://mail.systec.com.cn/ews/exchange.asmx
