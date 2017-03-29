1, AIX change timezone
# smit chtz
2, Set Asynchronous I/0 
# smit chgaio
maximum number of REQUESTS >= 8192
3, Set Operating System
# smit chgsys
maximum number of PROCESSES allowed per user ...
4, Set network
# smit mktcpip
5, Set swap
# smit chps
6, Mount cdrom
# mount -v cdrfs -p -r /dev/cd0 /cdrom
# cp /cdrom/ NAVIAGENT.lpp /usr/sys/inst.images
# smitty install
7, Show disk
# chgmgr -v
# lsdev -Cc disk 


8, How to determine if AIX uses a 32-bit kernel or 64-bit kernel ? 
An example of the getconf command is shown in the following:

# getconf KERNEL_BITMODE
64
# getconf HARDWARE_BITMODE
64
# getconf DISK_SIZE /dev/hdisk0
140013
The size is reported in MB, so the disk above is a 140 GB disk.






1.    Useful commands
Note  All AIX commands reference can be found under  
http //www.austin.ibm.com/doc_link/en_US/a_doc_lib/aixgen/wbinfnav/CmdsRefTop.htm
1.1    Memory
bootinfo –r    shows how much RAM does my machine has (as root)
lsattr –E –l sys0 –a realmem   shows how much RAM does my machine have (as non root)
rmss -c 512
rmss -r        sets the memory size to 512 MB
resets the memory size to the original one
1.2    Devices

lsattr  -El  en0    displays en0 driver params
lsattr  -El  ent0    displays ent0 HW params
lsattr -El rmt0    displays tape params
lscfg -vp -l rmt0    (all information about a tape drive)
lsattr  -El  sys0    displays system type, firmware, etc  driver params
lscfg –v    lists all system HW config (NVRAM)
lsdev –Csscsi    list all scsi devices
lsdev –Cspci    list all pci devices
lsparent –Ck scsi    list all scsi adapters
lsdevfc    list fiberchannel devices
cfgmgr    Configures devices
lsdev -Ccdisk     Shows all disks
lsdev -Cctape              Shows all tapes
cfgmgr -v -l device –v   Specifies verbose output. The cfgmgr command writes information about what it is doing to standard output.
cfgmgr -v -l device      Name Specifies the named device to configure along with its children.
If you only turned on a disk tower at e.g. scsi2 cfgmgr -v -l scsi2 will only configure this with detailed output.
lsdisp    To check which graphic adapter is installed.
lscfg -vp -l mga0     (all information about a adapter)
lscfg -vp -l hdisk0 | grep Machine    gives info about the disk manufacture type
lsslot -c pci    For 6F1 only !!!! Lists all slots ,voltage,boards,etc !!!!
bootlist -m normal cd0  rmt0 hdisk0   Changes the default bootlist
lsmcode -c    display the system firmware level and service processor
lsmcode -r -d scraid0    display the adapter microcode levels for a RAID adapter scraid0
lsmcode -A    display the microcode level for all supported devices
    
    
1.3    System info

/usr/bin/uname -m    Get machine ID
/usr/bin/uname -M    Get platform type
oslevel    Displays current AIX level
oslevel -r    Displays current AIX maintenance level
oslevel -g    List filesets at levels later than maintenance level !!!
lsps -a    Paging space settings.
lscfg -vp -l proc0  (1,2,3)   (all information about a processor[s])
lscfg -vp -l mem0 |pg    (all information about memory modules installed)
env ulimit    Environment setings - show user ulimit
bootinfo –s hdisk0     Displays disk size
lsattr -El sys0 -a systemid   Determines the system serial number
lscfg –vp|grep ROM|grep -v CD  Determines the system Firmware level
1.4    System issues

TERM=vt100      -If you execute a command/application and it responds with msg
‘ The type of your terminal is unknown to the system’,run those commands (In ‘ksh’)
set term=vt100   -Same (In tcsh’)
rcp -rp /dataVolumes/brisque1.1.0/jobs/flower.job sciroot@ripro3:/dataVolumes/ripro3.3.0/jobs/ -Copying a file from one Unix machine (Brisque) to another (Server) the assumption is that both machines know each other’s names (in hosts file)
dd if=/dev/fd0 of=/temp/diskimage bs=4096 -Duplicate a diskette copy from diskette to hard drive
dd if=/temp/diskimage of=/dev/fd0 bs=4096  -copy diskette image onto diskette
/usr/lpp/X11/bin/xset -display unix 0 s off  -Kill display timeout
lsfs -v jfs  -List of Filesystem items.
lsfs -q -v jfs         -you can see also the parameter of a filesystem and thus see if e.g. /backup was or is a big_filesystem_enabled one.
Important for the 2GB File limit.
lsuser –f root    Shows all user parameters (max .file size,etc)
sysdumpdev -L    Check last system dump status
sysdumpdev -l    Check system dump device settings
lslpp -f Upd_Timna_DTM.obj    List contents of the package
1.5    Networking

ksh
for ENT in ` lsdev –Cs pci|grep ent | awk '{ print $1 }'|cut –c 1,2,4 `;do
    mktcpip –S $ENT
done
exit      -Shows all interfaces IP config+mask+router+DNS !
host timna1    displays station default IP address – works ONLY in DNS environment
ifconfig en0    displays en0 driver params
netstat  -i    displays network interfaces setting
mktcpip -S en0    #host:addr:mask:_rawname:nameserv:domain:gateway:type:start
syslab18:192.9.100.1:255.255.255.0:en0:10.4.2.12:csil.creoscitex.com:10.4.30.1:N/A:no
GREAT TCPIP info in one command !!!
showmount –e    displays all exported volumes
showmount -a    show who's got my filesystemsses mounted over IP !
lssrc –g tcpip    displays all IP oriented processes status
entstat -drt ent0 |grep –i error    display any communication errors on etn0
entstat -r    Resets all the statistics back to their initial values.
arp -a    shows a local arp cache
cd /usr/local/es/;res    restarts appletalk
netstat  -ptcp    shows IP statistics
netstat  -pudp    shows UDP statistics
netstat  -c
         -s
         -m    client only;
server only
NFS mount
netstat -I en0 10    Trace en0 every 10 seconds
netstat -rn    Display routing info with IP address (10.4.27.182)
netstat -in    Shows the state of all configured interfaces
netstat -r    Display routing info with full hostnames (timna2.csil.creoscitex)
    nfsstat  –z      ;to    reset NFS stats without reboot
cat /etc/resolv.conf    Check DNS settings
stopsrc –g NFS     To stop NFS services on a client
startsrc –g NFS     To start NFS services on a client
traceroute 149.115.39.1    Trace all hobs (interconnections=routers) to the destination  IP
netpmon -o netpmon.out
trcstop    Traces all network processes activity into a logfile. Must be preceede by a trcstop command !
nslookup hostname    Shows the DNS server name and address
ping -R -c 1 bnc2    Ping with displaying the routing info
namerslv -s | grep domain | awk '{ print $2 }'    Displays a fully qualified domain name of a host
rup    Shows the status of a remote host on the local network
nmonnfs    Traces all NFS processes activity
mount hostname:/filesystem /mount-point    Mount an NFS filesystem
mknfsexp -d /directory     Creates an NFS export directory
mknfsmnt                            Creates an NFS mount directory
rmnfs                               Stops and un-configures NFS services
mknfs                               Configures and starts NFS services
exportfs -u (filesystem)            Un-exports a filesystem
exportfs                            Lists all exported filesystems
exportfs -a                        Exports all fs's in /etc/exports file
1.6    Disks

synclvodm -vP svg3    synchronizes ODM and the disk VG info.
redefinevg svg3    Redfined VG definition in ODM
lqueryvg -p hdisk0 –Avt  -reads logical volumes info from disk
bootinfo -s hdiskx    Shows Megabytes available even if no volume group is assigned.
lspv -p  hdiskx     (PP's used, location on disk, mount point)
lscfg -vp -l hdiskx      (all information about a disk/raid)
1.7    Filesystem

chfs -a size=+200000 /var    increases /var FS by 100MB
du -sk /john          shows directory used space in kb !!!!
mount all    mounts all FS
umount /dataVolumes/rtest9.1.0    unmounts a FS
fuser -k /dev/cd0    Releases a CD that will not unmount !
fuser -c /dataVolumes/rtest9.1.0  -Find out which process_id lock the FS
istat <filename>    Shows when the file was last created/modified/accessed !!!!
1.8    System monitoring

istat <filename>    Shows create/modify/access file info
alog -o -t boot | more    displays system boot log
w    Lists login users and their programs.
who    Identifies the users currently logged in
/usr/local/es/swho     Identifies the Ethershare users currently logged in
last  |more    shows last logins
last –20    Shows recent 20 lines
last root    Shows username ‘root’ login/logout record
last ftp     Shows all FTP session in the record
mount    shows all mounted filesystems (nfs+local)
ps -ef    show all running processes
ps -ef |grep Scitex     show all scitex running processes
du -ak /scitex|sort -n -r|head –10  -Display 10 biggest directories on the volume by size
find /scitex -xdev -size +2048 -ls|sort -rn +6|head –10  -to find 10 top files in the root (/) directory larger than 1 MB.”-xdev” helps searching ONLY in “/” !!!!!!!!!
history    Last commands run on the system by this user
alog -ot boot    Lists a log of all boot operations
grep TX /etc/environment    Verify daylight settings
1.9    Performance issues

nmon    a nice monitor - runs only on AIX5 and up
topas    a nice monitor - runs only on AIX 4.3.3 and up
monitor -top 10 -s 2    monitors system 10  top processes with 2 seconds
iostat 2    displays disks activity every 2 seconds refresh interval
iostat –a 2            AIX5 ONLY !!!!
displays disks and ADAPTER !!!! activity every 2 seconds refresh interval
vmstat 2    ;monitors virtual memory statistics every 2 seconds (see appendix A)
sar –P ALL 2 2    Show all CPU’s activity on an SMP machine
svmon –i 2    Monitors real and virtual memory
ps auxw | sort –r +3 |head –10  -Shows top 10 memory usage by process
ps auxw | sort –r +2 |head –10  -Shows top 10 CPU usage by process
ps –auw | grep defunct    Shows zombies processes (to kill – reboot or kill the parent)
filemon –O all –o filemon.out ; find / -name core ; trcstop    Traces FS,LV,disks,files activityof a “find” command into a logfile (filemon.out). Must be preceded by a trcstop command.
tprof –x find / -name core ; trcstop    Traces CPU activityof a “find” command Severall logfile are created. Must be preceded by a trcstop command.
tprof -ske -x "sleep 30"    -Trace CPU activity for next 30 seconds.Results in file sleep.tprof

lvmstat –ev svg1
lvmstat –v svg1 2    AIX5 ONLY !!!!
enable gathering the VG statistics
Display VG logical volumes statistics every 2 seconds
1.10    Remote issues (working over the modem)

pdelay tty0; pdisable tty0 >/dev/null ;penable tty0  
-Resets tty0
stty erase '^?'    Makes bakespace to work
/scitex/version/utils/modem/kermit -l /dev/ttyx –c atdt {phone #}     Use Unix to Dail-out  (for any reason) ttyx is the serial port the cable is connected
/scitex/version/utils/modem/kermit -s /u/d0/ripro_messages -i    Sends a file to a remote desktop in binary mode
/scitex/version/utils/modem/kermit –r
-Receives a file to from remote desktop
1.11    Browsing errlog with errpt

errpt -a  -s 0604090601  -e 0605090901    browse the errlog in  detail for all errors within a timeframe
errpt -a  -N SYSPROC |more
errpt -a  -N SYSPROC  > /tmp/err.log    Browse the errlog for the SYSPROC resource, can be into the file
errpt -j 5DFED6F1   -Browse the errlog by the identifier
errpt –A    -AIX5 ONLY !!!! Shows less detailes then errpt -a
errpt –D    -AIX5 ONLY !!!! eliminates double entries
1.12    Security issues

chmod -s Filename    Remove Sticky Bit to a file or directory

chmod +r+w+x+t Filename     Add Read+Write+Execute+Temp mode to a file or directory.
This is a ‘blanket’ change for all owner, user & group.
Numeric Access Modes  
0 (---) - no access
1 (--x) - execute permissions; search permissions for directories
2 (-w-) - write access
3 (-wx) - execute/search permission and write access
4 (r--) - read access
5 (r-x) - execute/search permission and read access
6 (rw-) - read and write access
7 (rwx) - execute/search permission and read and write access
mkpasswd -f    rebuild the /etc/passwd indexes in case of suspected corruption
1.13    Miscellaneous
ksh
find / -type f|xargs grep "10.4.27.181" 2> /dev/null
-Find all files containing my IP address
compress -c file > file.Z    Compresses the files while keeps the original
whereis  <command-ame>    Returms full path of program



== Useful HACMP commands ==
{{{
    clstat - show cluster state and substate; needs clinfo.
    cldump - SNMP-based tool to show cluster state.
    cldisp - similar to cldump, perl script to show cluster state.
    cltopinfo - list the local view of the cluster topology.
    clshowsrv -a - list the local view of the cluster subsystems.
    clfindres (-s) - locate the resource groups and display status.
    clRGinfo -v - locate the resource groups and display status.
    clcycle - rotate some of the log files.
    cl_ping - a cluster ping program with more arguments.
    clrsh - cluster rsh program that take cluster node names as argument.
    clgetactivenodes - which nodes are active?
    get_local_nodename - what is the name of the local node?
    clconfig - check the HACMP ODM.
    clRGmove - online/offline or move resource groups.
    cldare - sync/fix the cluster.
    cllsgrp - list the resource groups.
    clsnapshotinfo - create a large snapshot of the HACMP configuration.
    cllscf - list the network configuration of an HACMP cluster.
    clshowres - show the resource group configuration.
    cllsif - show network interface information.
    cllsres - show short resource group information.
    lssrc -ls clstrmgrES - list the cluster manager state.
    lssrc -ls topsvcs - show heartbeat information.
    cllsnode - list a node centric overview of the hacmp configuration.
}}}

http://www.aixhealthcheck.com/blog?topic=17

http://www.unixwerk.eu/aix/cluster-cmd.html


== Oracle install ==
export DISPLAY="localhost:0"




To see the details of installed file sets:
#lslpp -l
To list the installation history of all file set in bos.net packages:
#lslpp -ha bos.net.*
To list the files in the bos.rte package:
#lslpp -f bos.rte
To list the file set which contain /etc/hosts file:
#lslpp -w /etc/hosts
To list the pre requisites for bos.net.nfs.server file set:
#lslpp -p bos.net.nfs.server
To list the installable products on the device rmt0:
#installp -L -d /dev/rmt0.1
To install all filesets within bos.net and expands file system if it requires:
#installp -aX -d /dev/rmt0.1 bos.net
To remove bos.net:
#installp -u bos.net
To reject the applied software:
#installp -r
To commit the <package>:
#installp -c -f <package>
To cleanup an incomplete installation:
#installp -C
To check the <package>:
#lppchk -c <package> Verifies that the / (root), /usr and /usr/share parts of the system are valid with each other: #lppchk -v
To install the file set associated with fix IX9999 from rmt0:
#instfix -k IX9999 -d /dev/rmt0.1
To verify fix IY6969 installed:
#instfix -ik IY6969
How to display missing filesets from service pack:
#instfix -icqv | grep ':-:'
To verify if you have all packages installed for the current ML and why after upgrade you cannot see the newer version:

# instfix -i |grep ML
    All filesets for 6100-00_AIX_ML were found.
    All filesets for 6100-01_AIX_ML were found.
    All filesets for 6100-02_AIX_ML were found.
    All filesets for 6100-03_AIX_ML were found.
    All filesets for 6100-04_AIX_ML were found.
    All filesets for 6100-05_AIX_ML were found.
    All filesets for 6100-06_AIX_ML were found.
    All filesets for 6.1.0.0_AIX_ML were found.
    Not all filesets for 6100-07_AIX_ML were found.
	
# oslevel -s
6100-06-05-1115


== swap usage ==
svmon -Pt10 | perl -e 'while(<>){print if($.==2||$&&&!$s++);$.=0 if(/^-+$/)}'
#I need to see the following output:

    vmo -a

    vmstat 1 10

    lsps -a

    lsps -s

    svmon -G

