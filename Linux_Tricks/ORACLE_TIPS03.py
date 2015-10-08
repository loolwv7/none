rman可以备份的数据库:
target database  生产数据库
reconvery catalog database  目录数据库
auxiliary database 附注数据库

========================================================================
非catalog方式备份
全备份
0级增量备份
1级增量备份
[oracle@tlbb ~]$ sqlplus /nolog
SQL*Plus: Release 10.2.0.1.0 - Production on Thu Feb 5 17:38:01 2009
Copyright (c) 1982, 2005, Oracle.  All rights reserved.
SQL> conn /as sysdba
Connected.
SQL> archive log list
Database log mode              Archive Mode   //在归档状态下
Automatic archival             Enabled        //
Archive destination            USE_DB_RECOVERY_FILE_DEST
Oldest online log sequence     5
Next log sequence to archive   7
Current log sequence           7
SQL>
切换服务器归档模式
$sqlplus /nolog
SQL> conn /as /sysdba  (以dba的身分连接DB)
SQL> shutdown immediate;  (立即关闭数据库)
SQL> startup mount  (启动实例并加载数据库,但不打开)
SQL> alter database archivelog;  (更改数据库为归档模式)
SQL> alter database open; (打开数据库)
SQL> alter system archive log start;  (启用自动归档)
SQL> exit  (退出)

RMAN> connect target / (连接数据库)
connected to target database: TLBB (DBID=1486193478)
RMAN> backup database;  (全备份)
RMAN> backup  incremental level=0 database;  (0级增量备份)
RMAN> backup  incremental level=1 database;  (1级增量备份)
备份archivelog
backup database plus archivelog delete input;
备份表空间
backup tablespace user(用report schema;查看)
备份控制文件
backup current controlfile;
backup database include current controfile
================================================================================
备份集  backupset
镜像备份 image copies
copy datafile ... to ...
RMAN> copy datafile 4 to '/backup1/users.dbs';
RMAN> list copy;
单命令
backup database;
批命令备份
run {
allocate channel cha1 type disk;
backup
format "/backup1/full_%t"
tag full-backup
database;
release clannel cha1;
}
===================================================
备份计划:
星期天晚上 -level 0
星期一晚上 -level  2
星期二晚上 -level 2
星期三晚上 -level 1
星期四晚上 -level 2
星期五晚上 -level 2
星期六晚上 -level 2
bakl0
run {
allocate channel c1 type disk;
backup
incremental level 0
format "/backup1/inc0_%u_%T"
tag monday_inc0
database;
release channel c1;
}
bakl1
run {
allocate channel c1 type disk;
backup
incremental level 1
format "/backup1/inc1_%u_%T"
tag monday_inc1
database;
release channel c1;
}
bakl2
run {
allocate channel c1 type disk;
backup
incremental level 2
format "/backup1/inc2_%u_%T"
tag monday_inc2
database;
release channel c1;
}
命令:
rman target / msglog=/backup1/bakl0.log cmdfile=/backup/bakl0
crontab -e -u oracle
45 23 * * 0 rman target / msglog=/backup1/bakl0.log cmdfile=/backup/bakl0
45 23 * * 1 rman target / msglog=/backup1/bakl2.log cmdfile=/backup/bakl2
45 23 * * 2 rman target / msglog=/backup1/bakl2.log cmdfile=/backup/bakl2
45 23 * * 3 rman target / msglog=/backup1/bakl1.log cmdfile=/backup/bakl1
45 23 * * 4 rman target / msglog=/backup1/bakl2.log cmdfile=/backup/bakl2
45 23 * * 5 rman target / msglog=/backup1/bakl2.log cmdfile=/backup/bakl2
45 23 * * 6 rman target / msglog=/backup1/bakl2.log cmdfile=/backup/bakl2
分，时，天，月，星期
service crond restart

CONFIGURE CONTROLFILE AUTOBACKUP ON;
自动备份controlfile
delete backupset 11;
delete backupset 1;
删除备份
===================================================================
口令文件丢失(/dbs/orapwherming)
orapwd file=orapwherming password=pass123 entries=5

spfiel丢失(mv ../dbs/spfiletlbb.ora spfiletlbb.bak)
[oracle@tlbb dbs]$ rman target /
Recovery Manager: Release 10.2.0.1.0 - Production on Thu Feb 5 19:07:57 2009
Copyright (c) 1982, 2005, Oracle.  All rights reserved.
connected to target database: TLBB (DBID=1486193478)
RMAN> shutdown immediate;
using target database control file instead of recovery catalog
database closed
database dismounted
Oracle instance shut down
===============================================
RMAN> startup nomount;
RMAN> set dbid 1486193478;
RMAN> restore spfile from autobackup;
RMAN> restore spfile from '/backup1/ctlc-1486193478-20090205-09'; (如果自动不能找到，手工指定)
RMAN> shutdown immediate;
RMAN> startup;  (如果不行，先set dbid 1486193478;再startup)

controlfile丢失():
删除/u01/app/oracle/oradata/tlbb目录下*.ctl文件
sqlplus /nolog
conn /as sysdba
shutdown immediate;
shutdown abort;
exit
==================================================
RMAN> startup nomount;
RMAN> restore controlfile from autobackup;
      restore controlfile from '/backup1/ctlc-1486193478-20090205-09';
RMAN> alter database mount;
RMAN> recover database;
RMAN> alter database open resetlogs;

redolog file丢失:
删除/u01/app/oracle/oradata/tlbb目录下*.log文件
=================================================
sqlplus /nolog
conn /as sysdba
shutdown immediate;
startup mount;
recover database until cancel;
alter database open resetlogs;

datafile丢失：
删除/u01/app/oracle/oradata/tlbb目录下*.dbf文件
================================================
RMAN> report schema;看ID号:2
sql "alter database datafile 2 offline" ;
sql "alter database datafile 2 offline immediate" ;
restore datafile 2 ;
recover datafile 2 ;
sql "alter database datafile 2 online" ;
表空间丢失:
sql "alter tablespace users offline"
restore tablespace users
recover tablespace users
sql "alter database tablespace users online"
--------------------------------------------------------
非catelog方式完全恢复:
sqlplus /nolog
conn /as sysdba
shutdown abort;
rman target /
startup nomount;
restore controlfile from autobackup;
(restore controlfile from '/backup1/ctlc-1486193478-20090205-09';)
alter database mount;
restore database;
sqlplus /nolog
conn /as sysdba
create pfile from spfile;
cd /u01/app/oracle/product/10.2.0.1/dbs
vi inittlbb.ora
....
*._allow_resetlogs_corruption='TURE'
END
sqlplus /nolog
conn /as sysdba
shutdown immediate;
startup pfile=/u01/app/oracle/product/10.2.0.1/dbs/inittlbb.ora
shutdown immediate;
startup pfile=/u01/app/oracle/product/10.2.0.1/dbs/inittlbb.ora mount
alter database open resetlogs;
exit
recover databses;
alter database open restlogs;
基于时间:
基于SCN的恢复：
startup ount
restore database until scn 643309;
recover database until scn 643309;
alter database open resetlogs;
日志序列SEQUENCCE
report schema
list backup
crosscheck backup
delete

alter database open restlogs;做完这个之后，最好做个备份，要不然。redo log会出问题!
这是学习笔记，可能有点乱，错误之处请指正！ 
