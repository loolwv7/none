== Aggr ? ==
for volumes - you can't have a flexible volume without an aggregate.  Flex Vols
    are logical, Aggregates are physical.  you layer one or more flex vols on
    top (in side) of an aggregate

== How to monitor NetApp storage systems using SNMP ==
https://kb.netapp.com/support/index?page=content&id=1011225&pmv=print&impressions=false

== NetApp best practice ==
As the best practice, NetApp now recommends to set Fractional Reserve and Snap Reserve for your volumes to 0%. Don’t forget about that, if you want to save more storage space:
{{{
    > vol options “targetvol” fractional_reserve 0
    > snap reserve “targetvol” 0

Disable snapshots if you don’t use them:

    > snap sched “targetvol” 0
}}}

== How to add Disk SHELF to exist NetApp ==

http://community.netapp.com/t5/FAS-and-V-Series-Storage-Systems-Discussions/DS2246-SAS-install-FAS2240-2-Config-check/td-p/55471

http://community.netapp.com/t5/FAS-and-V-Series-Storage-Systems-Discussions/DS2246-SAS-install-FAS2240-2-Config-check/m-p/55487#M3904

http://www.cosonok.com/2013/03/how-to-hot-add-ds4243-shelf-quick-guide.html

 How to add a new disk shelf to a Netapp filer ??

 Assumption:- Filer has already one disk shelf connected this is the new one
 which has to be added and cabled.


 Cables required:- Two SAS cables , Two ACP (CAT6 ETHERNET ) cables if any


1. Rack the shelf

2. Connect power cables & turn the shelf on (wait about 30 seconds)

3. On the front of the shelf, change the shelf id to something unique. (try
and keep it sequential with the shelf that's already there)  DO NOT USE "00"

4. Wait about 45 seconds and then restart the shelf and make sure the
new shelf ID came up.

5. SSH into both filers and do "options disk.auto_assign off"

6. Do a "storage show disk -p" on both controllers and copy the
contents into a txt file and save it. (run this command again and make
sure all your disks are still there)

7. Do a "options autosupport.doit "before shelf add"" on both
controllers since i'm scared your doing this via community forums.
("before shelf add" is in quotes on the command)

8. Now for the fun part, take a SAS cable and plug one end into the
TOP circle of the OLD shelf and plug it in the BOTTOM square of the
         NEW shelf

9. Now take another SAS cable and plug one end into the BOTTOM circle
of the OLD shelf and plug it into the TOP square of the new shelf

10. assign your disks and don't forget to turn back on disk auto assign
when you're done.

11. Run "storage show disk -p" and make sure all of your old disks are
there.

(shelves at the end of a stack are always reversed, this is a special
circumstance and you will not cable all shelves like this in the future.
http://nayabrasools.blogspot.com/2012/10/how-to-add-new-disk-shelf-to-netapp.html




== Data ONTAP Basic Command Please? ==

  This post contains the list of commands that will be most used
and will come handy when managing or monitoring or troubleshooting a Netapp
filer.

    sysconfig -a : shows hardware
    configuration with more verbose information
    sysconfig -d :
    shows information of the disk attached to the filer
    version : shows the
    netapp Ontap OS version.
    uptime : shows the
    filer uptime
    dns info : this
    shows the dns resolvers, the no of hits and misses and other info
    nis info : this
    shows the nis domain name, yp servers etc.
    rdfile : Like
    "cat" in Linux, used to read contents of text files/
    wrfile :
    Creates/Overwrites a file. Similar to "cat > filename" in Linux
    aggr status : Shows
    the aggregate status
    aggr status -r :
    Shows the raid configuration, reconstruction information of the disks in filer
    aggr show_space :
    Shows the disk usage of the aggreate, WAFL reserve, overheads etc.
    vol status : Shows
    the volume information
    vol status -s :
    Displays the spare disks on the filer
    vol status -f :
    Displays the failed disks on the filer
    vol status -r :
    Shows the raid configuration, reconstruction information of the disks
    df -h : Displays
    volume disk usage
    df -i : Shows the inode
    counts of all the volumes
    df -Ah : Shows
    "df" information of the aggregate
    license :
    Displays/add/removes license on a netapp filer
    maxfiles : Displays
    and adds more inodes to a volume
    aggr create :
    Creates aggregate
    vol create
    <volname> <aggrname> <size> : Creates volume in an aggregate
    vol offline
    <volname> : Offlines a volume
    vol online
    <volname> : Onlines a volume
    vol destroy
    <volname> : Destroys and removes an volume
    vol size
    <volname> [+|-]<size> : Resize a volume in netapp filer
    vol options : Displays/Changes
    volume options in a netapp filer
    qtree create
    <qtree-path> : Creates qtree
    qtree status :
    Displays the status of qtrees
    quota on : Enables
    quota on a netapp filer
    quota off :
    Disables quota
    quota resize :
    Resizes quota
    quota report :
    Reports the quota and usage
    snap list :
    Displays all snapshots on a volume
    snap create
    <volname> <snapname> : Create snapshot
    snap sched
    <volname> <schedule> : Schedule snapshot creation
    snap reserve
    <volname> <percentage> : Display/set snapshot reserve space in volume
    /etc/exports : File
    that manages the NFS exports
    rdfile /etc/exports
    : Read the NFS exports file
    wrfile /etc/exports
    : Write to NFS exports file
    exportfs -a :
    Exports all the filesystems listed in /etc/exports
    cifs setup : Setup
    cifs
    cifs shares : Create/displays
    cifs shares
    cifs access :
    Changes access of cifs shares
    lun create :
    Creates iscsi or fcp luns on a netapp filer
    lun map : Maps lun
    to an igroup
    lun show : Show all
    the luns on a filer
    igroup create :
    Creates netapp igroup
    lun stats : Show lun
    I/O statistics
    disk show : Shows
    all the disk on the filer
    disk zero spares :
    Zeros the spare disks
    disk_fw_update :
    Upgrades the disk firmware on all disks
    options :
    Display/Set options on netapp filer
    options nfs :
    Display/Set NFS options
    options timed :
    Display/Set NTP options on netapp.
    options autosupport
    : Display/Set autosupport options
    options cifs :
    Display/Set cifs options
    options tcp :
    Display/Set TCP options
    options net :
    Display/Set network options
    ndmpcopy
    <src-path> <dst-path> : Initiates ndmpcopy
    ndmpd status :
    Displays status of ndmpd
    ndmpd killall :
    Terminates all the ndmpd processes.
    ifconfig :
    Displays/Sets IP address on a network/vif interface
    vif create :
    Creates a VIF (bonding/trunking/teaming)
    vif status :
    Displays status of a vif
    netstat : Displays
    network statistics
    sysstat -us 1 : begins a 1
    second sample of the filer's current utilization (crtl - c to end)
    nfsstat : Shows nfs
    statistics
    nfsstat -l :
    Displays nfs stats per client
    nfs_hist : Displays
    nfs historgram
    statit : beings/ends a
    performance workload sampling [-b starts / -e ends]
    stats : Displays
    stats for every counter on netapp. Read stats man page for more info
    ifstat : Displays
    Network interface stats
    qtree stats :
    displays I/O stats of qtree
    environment : display
    environment status on shelves and chassis of the filer
    storage show
    <disk|shelf|adapter> : Shows storage component details
    snapmirror
    intialize : Initialize a snapmirror relation
    snapmirror update :
    Manually Update snapmirror relation
    snapmirror resync :
    Resyns a broken snapmirror
    snapmirror quiesce
    : Quiesces a snapmirror bond
    snapmirror break :
    Breakes a snapmirror relation
    snapmirror abort :
    Abort a running snapmirror
    snapmirror status :
    Shows snapmirror status
    lock status -h :
    Displays locks held by filer
    sm_mon : Manage the
    locks
    storage download
    shelf : Installs the shelf firmware
    software get :
    Download the Netapp OS software
    software install :
    Installs OS
    download : Updates
    the installed OS
    cf status :
    Displays cluster status
    cf takeover : Takes
    over the cluster partner
    cf giveback : Gives
    back control to the cluster partner
    reboot : Reboots a
    filer

Pocket guide for netapp commands

This post contains the list of commands that will be most used
and will come handy when managing or monitoring or troubleshooting a Netapp
filer.

    sysconfig -a : shows hardware
    configuration with more verbose information
    sysconfig -d :
    shows information of the disk attached to the filer
    version : shows the
    netapp Ontap OS version.
    uptime : shows the
    filer uptime
    dns info : this
    shows the dns resolvers, the no of hits and misses and other info
    nis info : this
    shows the nis domain name, yp servers etc.
    rdfile : Like
    "cat" in Linux, used to read contents of text files/
    wrfile :
    Creates/Overwrites a file. Similar to "cat > filename" in Linux
    aggr status : Shows
    the aggregate status
    aggr status -r :
    Shows the raid configuration, reconstruction information of the disks in filer
    aggr show_space :
    Shows the disk usage of the aggreate, WAFL reserve, overheads etc.
    vol status : Shows
    the volume information
    vol status -s :
    Displays the spare disks on the filer
    vol status -f :
    Displays the failed disks on the filer
    vol status -r :
    Shows the raid configuration, reconstruction information of the disks
    df -h : Displays
    volume disk usage
    df -i : Shows the inode
    counts of all the volumes
    df -Ah : Shows
    "df" information of the aggregate
    license :
    Displays/add/removes license on a netapp filer
    maxfiles : Displays
    and adds more inodes to a volume
    aggr create :
    Creates aggregate
    vol create
    <volname> <aggrname> <size> : Creates volume in an aggregate
    vol offline
    <volname> : Offlines a volume
    vol online
    <volname> : Onlines a volume
    vol destroy
    <volname> : Destroys and removes an volume
    vol size
    <volname> [+|-]<size> : Resize a volume in netapp filer
    vol options : Displays/Changes
    volume options in a netapp filer
    qtree create
    <qtree-path> : Creates qtree
    qtree status :
    Displays the status of qtrees
    quota on : Enables
    quota on a netapp filer
    quota off :
    Disables quota
    quota resize :
    Resizes quota
    quota report :
    Reports the quota and usage
    snap list :
    Displays all snapshots on a volume
    snap create
    <volname> <snapname> : Create snapshot
    snap sched
    <volname> <schedule> : Schedule snapshot creation
    snap reserve
    <volname> <percentage> : Display/set snapshot reserve space in volume
    /etc/exports : File
    that manages the NFS exports
    rdfile /etc/exports
    : Read the NFS exports file
    wrfile /etc/exports
    : Write to NFS exports file
    exportfs -a :
    Exports all the filesystems listed in /etc/exports
    cifs setup : Setup
    cifs
    cifs shares : Create/displays
    cifs shares
    cifs access :
    Changes access of cifs shares
    lun create :
    Creates iscsi or fcp luns on a netapp filer
    lun map : Maps lun
    to an igroup
    lun show : Show all
    the luns on a filer
    igroup create :
    Creates netapp igroup
    lun stats : Show lun
    I/O statistics
    disk show : Shows
    all the disk on the filer
    disk zero spares :
    Zeros the spare disks
    disk_fw_update :
    Upgrades the disk firmware on all disks
    options :
    Display/Set options on netapp filer
    options nfs :
    Display/Set NFS options
    options timed :
    Display/Set NTP options on netapp.
    options autosupport
    : Display/Set autosupport options
    options cifs :
    Display/Set cifs options
    options tcp :
    Display/Set TCP options
    options net :
    Display/Set network options
    ndmpcopy
    <src-path> <dst-path> : Initiates ndmpcopy
    ndmpd status :
    Displays status of ndmpd
    ndmpd killall :
    Terminates all the ndmpd processes.
    ifconfig :
    Displays/Sets IP address on a network/vif interface
    vif create :
    Creates a VIF (bonding/trunking/teaming)
    vif status :
    Displays status of a vif
    netstat : Displays
    network statistics
    sysstat -us 1 : begins a 1
    second sample of the filer's current utilization (crtl - c to end)
    nfsstat : Shows nfs
    statistics
    nfsstat -l :
    Displays nfs stats per client
    nfs_hist : Displays
    nfs historgram
    statit : beings/ends a
    performance workload sampling [-b starts / -e ends]
    stats : Displays
    stats for every counter on netapp. Read stats man page for more info
    ifstat : Displays
    Network interface stats
    qtree stats :
    displays I/O stats of qtree
    environment : display
    environment status on shelves and chassis of the filer
    storage show
    <disk|shelf|adapter> : Shows storage component details
    snapmirror
    intialize : Initialize a snapmirror relation
    snapmirror update :
    Manually Update snapmirror relation
    snapmirror resync :
    Resyns a broken snapmirror
    snapmirror quiesce
    : Quiesces a snapmirror bond
    snapmirror break :
    Breakes a snapmirror relation
    snapmirror abort :
    Abort a running snapmirror
    snapmirror status :
    Shows snapmirror status
    lock status -h :
    Displays locks held by filer
    sm_mon : Manage the
    locks
    storage download
    shelf : Installs the shelf firmware
    software get :
    Download the Netapp OS software
    software install :
    Installs OS
    download : Updates
    the installed OS
    cf status :
    Displays cluster status
    cf takeover : Takes
    over the cluster partner
    cf giveback : Gives
    back control to the cluster partner
    reboot : Reboots a
    filer


vperumal Former NetApp Employee
http://community.netapp.com/t5/Data-ONTAP-Discussions/Data-ONTAP-Basic-Command-Please/td-p/59641


== NetApp basic how to ==
LUN create & map
1, fcp wwpn-alias set alias_name WWPN
2,igroup create -i -t windows_2008 win-group0 alias_name,1,2,3
igroup create -f -t aix IBM_P720 IBM_P720a IBM_P720b
igroup create -f -t windows IMAGE 198.0.0.10
igroup add initialtor_group nodename/alias_name
3, N6060A> 
vol create IBM_P720 aggr0a 330G
vol create IMAGE aggr0a 2448G
vol create DATA aggr0a 900G

vol create chjbak aggr0b 900G

snap reserve IBM_P720 0

4, lun create -s SIZE -t OSTYPE lun_PATH  (lun show)
lun create -s 5G -t aix /vol/IBM_P720/CRS01
lun create -s 5G -t aix /vol/IBM_P720/CRS02
lun create -s 5G -t aix /vol/IBM_P720/CRS03
lun create -s 100G -t aix /vol/IBM_P720/DATA01
lun create -s 100G -t aix /vol/IBM_P720/DATA02
lun create -s 100G -t aix /vol/IBM_P720/DATA03

lun create -s 898G -t windows /vol/chjbak/chjbak01

lun create -s 2048G -t windows_2008 /vol/IMAGE/image01
lun create -s 400G -t windows_2008 /vol/IMAGE/image02

5, lun map lun_PATH initialtor_group/alias_name 
N6060A> fcp wwpn-alias show
WWPN                Alias
----                -----
10:00:00:90:fa:09:34:87     198.0.0.221
10:00:00:90:fa:09:37:de     198.0.0.222
10:00:00:90:fa:09:35:b6     198.0.0.223
10:00:00:00:c9:88:9b:4b     IBM_P720a
10:00:00:00:c9:7a:14:35     IBM_P720b
10:00:00:00:c9:e0:b0:12     198.0.0.10
21:00:00:1b:32:90:4e:63     198.0.0.152

lun map /vol/IBM_P720/CRS01 IBM_P720
lun map /vol/IBM_P720/CRS02 IBM_P720
lun map /vol/IBM_P720/CRS03 IBM_P720
lun map /vol/IBM_P720/DATA01 IBM_P720
lun map /vol/IBM_P720/DATA02 IBM_P720
lun map /vol/IBM_P720/DATA03 IBM_P720
lun map /vol/IMAGE/image01 198.0.0.10
lun map /vol/IMAGE/image02 198.0.0.10



# NOTES
########

    sysconfig -a : shows hardware

    aggr status 
    aggr status -r 
    aggr show_space 
    vol status -s 
    vol status -r 
    lun stats 




# TEST failover works
1, cf takeover

2, cf status
Filer X has taken over Filer Y.

3, cf status
Filer X is ready for giveback.
partner ifconfig -a
partner vfiler status

4, vol status
   aggr status
N6060B(takeover) partner
   vol status
   aggr status


cf giveback
cf giveback -f

== simulator download ==
http://mysupport.netapp.com/NOW/cgi-bin/simulator

== 7 mode VS cluster mode ==


最开始的Ｄata Ontap 借鉴了最早的开源UNIX之一的BSD Net/2许多代码，包括 TCP/IP
堆栈、启动代码、设备驱动等，后来的Data
Ontap也从其他的开源UNIX借鉴了大量的代码。至于命令行接口是NetApp仿Unix独立开发的,另外WAFL文件系统与RAID代码及磁盘子系统为NetApp自己开发的所以与UNIX的完全不同。

一开始DataOntap没有什么mode之分的，NetApp收购了Spinnaker之后基于freeBSD把DataOntap与Spinnaker的软件重新整合出另一个叫Data
Ontap GX的操作系统来，当Data
Ontap更新至8.0版本后，NetApp统一了二者的版本号,并把原生的DataOntap称为7 mode,
后来的Data Ontap GX则称为 cluster mode,简称为c mode。

由于新的DataOntap cluster mode功能一直不够完善，NetApp一直同时开发着7 mode
和cluster mode两个操作系统，不过随着NetApp大力推广和开发cluster
mode，相信很快就会停止开发7 mode只有cluste mode了。目前（Data Ontap
8.1.1）二者功能上的区别如下：

Cluster-Mode Only

−Clustered scaleout (24-NAS: 4-SAN)
（多节点集群，如果提供SAN则一个集群最多4个节点）

−Namespace （统一命名空间）

−Nondisruptive operations （节点间平滑迁移volume或LUN）

−Management as single system （统一管理整个集群）

−Scalable and integrated multi-tenancy （可扩展及多租户）

−NFS v4, v4.1 (pNFS); SMB 2.0, 2.1

−Onboard antivirus

 

 7-Mode Only

 −SnapLock®

 −SnapVault® and OSSV

 −Qtree and synchronous SnapMirror

 −MetroCluster™

 −vFiler®

 −FlexShare®

 −IPv6, HTTP, FTP, SFTP, TFTP

  

  Both 7-Mode and Cluster-Mode

  −Unified architecture

  −Storage efficiency features 和（重复数据删除与压缩）

  −Snapshot™ copies and asynchronous volume SnapMirror®

  −Intelligent caching with Flash Cache

== Oncommand ==
http://mysupport.netapp.com/NOW/cgi-bin/software/
http://community.netapp.com/t5/OnCommand-Storage-Management-Software-Discussions/Operations-Manager-CORE-free-license-available/td-p/61964

== How to determine the disk and shelf firmware version on a controller and
verify it is up to date ==

https://kb.netapp.com/index?page=content&id=1010762&actp=LIST_POPULAR
https://kb.netapp.com/support/index?page=content&id=1011673&actp=LIST_RECENT

== IOPS calc ==
The Shot Analysis of NetApp FAS8040 (2-node, C-Mode) SPC-1 Results | Storage
News:
    http://www.stornews.com/?p=390

== upgrade shelf disk firmware ==
http://mysupport.netapp.com/NOW/cgi-bin/shelffwdnld.cgi/download/tools/diskshelf/bin/all_shelf_fw#7dot

== Re: Understanding aggregate and lun ==
http://community.netapp.com/t5/FAS-and-V-Series-Storage-Systems-Discussions/Understanding-aggregate-and-lun/td-p/23326/page/3

== Netapp DS4243, DS4246 and DS2246 SAS storage shelf experiences a spurious ID change ==
Generally it requires either a power cycle of the shelf or a new ESH module. Either one requires a downtime.

Netapp DS4243, DS4246 and DS2246 SAS storage shelf experiences a spurious ID change (KB Alerts) - Kamazoy Knowledge Books - IT Support in Birmingham:


== NetApp Knowledgebase - How to power down and power up the controllers in a 7-Mode HA-Pair: ==
https://www.google.com.sb/url?sa=t&rct=j&q=&esrc=s&source=web&cd=4&cad=rja&uact=8&ved=0CDcQFjADahUKEwjy8JT7oKjHAhVF0h4KHcV9DcI&url=https%3A%2F%2Fkb.netapp.com%2Fsupport%2Findex%3Fpage%3Dcontent%26id%3D1010084&ei=frTNVfK5NsWke8X7tZAM&usg=AFQjCNGEZJTW7GV4GkAFcw3RDvL4o0BHKg&bvm=bv.99804247,d.cWw

== Flash Pool setting ==
aggr create aggr_hybrid -t raid_dp -T sas -n 18 -r 18
aggr option aggr_hybrid hybrid_enabled on
aggr add aggr_hybrid -T ssd

priority hybrid-cache set aggr_hybrid read-cache=random-read
priority hybrid-cache set aggr_hybrid write-cache=random-write
