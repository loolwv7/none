#format wiki
#language zh-tw

= ORACLE DATABASE TIPS =
<<TableOfContents>>
== rlwrap ==

== Backup & Recovery ==
=== Show logs ===
SQL> SELECT * from v$log;

=== 10G AUTOTRACE ===
SQL> SET AUTOTRACE ON;
SQL> SELECT * from v$version where rownum <2;
SQL> SET AUTOTRACE TRACE EXPLAIN;
SQL> SELECT * from plan_table;

=== SCN (System Change Name) number ===
SQL> SELECT CURRENT_SCN from v$database;
SQL> SHOW PARAMETER CHECKPOINT_TO;

 * CheckPoint about. CHECKPOINT T1, CHECKPOINT T2.
{{{
|--------+--------+--------|
 	   T1		T2  When CRASH...
	       |---------->| REDO required
}}}
>> increace checkpoint
>> check how much Latch point exist.
SQL> SELECT name,gets,misses from v$latch where name='checkpint queue latch';
>> check Latch children points 
SQL> SELECT name,gets,misses from v$latch_children where name='checkpoint queue latch';

SQL> SELECT name,bytes from v$sgastat where upper(name) like '%CHECKPOINT%';
SQL> SELECT name,bytes from v$sgastat where name like 'object queue%';

SQL> SELECT sid,seq#,event from v$session_wait;
SQL> SELECT * v$log;

=== Fast-Start Fault Recovery ===
SQL> SELECT * FROM V$OPTION where Parameter='Fast-Start Fault Recovery';

=== Show dead case ===
{{{
SELECT distinct KTUXECFL,count(*) from x$ktuxe group by KTUXECFL;
SELECT ADDR,KTUXEUSN,KTUXESLT,KTUXESQN,KTUXESIZ from x$ktuxe where KTUXEUSN=10 and KTUXESLT=39;
DECLARE
}}}

=== TRACE oracle database OPEN processing ===
SQL> STARTUP MOUNT;
SQL> ALTER SESSION SET SQL_TRACE = TRUE;
SQL> ALTER DATABASE OPEN;

=== How to see the oldest flashback available? ===
 * Using the following query one can see the flashback data available.
{{{
SELECT to_char(sysdate,'YYYY-MM-DD HH24:MI') current_time, to_char(f.oldest_flashback_time, 'YYYY-MM-DD HH24:MI') OLDEST_FLASHBACK_TIME,
(sysdate – f.oldest_flashback_time)*24*60 HIST_MIN FROM v$database d, V$FLASHBACK_DATABASE_LOG f;

CURRENT_TIME OLDEST_FLASHBACK HIST_MIN
}}}

=== RMAN restore ===

 * 通过RMAN登陆到目标数据库。

connect to the 10.8.1.111 as sysdba and perform all the backup and recovery operations
rman target sys/oracle@instance_name connect catalog rman_db01/password@instance_name

 *. 把10.8.1.111注册到80的CATALOG上。

register database;

 *. 把其他的数据库用同样的方式注册到CATALOG上。

==== recover the oracle RMAN tablespace if it is dropped ====
http://www.iliachemodanov.ru/en/blog-en/21-databases/50-oracle-backup-and-restore-en
-----------------------------------------------------------------

Step 1:
Restore the control file that was taken before the tablespace was dropped
 
Step 2:

Restore and recover the db
{{{
RMAN> run
{
set UNTIL TIME "to_date('YYYY-MM-DD HH24:MI:SS')";
restore database;
restore archivelog;
}
RMAN> recover database until cancel using backup controlfile;
RMAN> alter database open resetlogs;
}}}

http://labite.wordpress.com/2012/08/31/tuning-linux-server-for-oracle-database/
==== Here is a restore example ====
{{{
RMAN> run {
 allocate channel dev1 type disk;
 restore (archivelog low logseq 78311 high logseq 78340 thread 1 all);
 release channel dev1;
}
}}}

==== Example RMAN restore ====

rman target sys/*** nocatalog 
run {
  allocate channel t1 type disk;
  # set until time 'Aug 07 2000 :51';
  restore tablespace users; 
  recover tablespace users; 
  release channel t1; 
}


RMAN> backup database format="/opt/data/fullbk.bak' tag='full';
SQL> SELECT count(*)from t;
RMAN> backup validate datafile 2(number show above);
SQL> SELECT * FROM v$database_block_corruption where file#=2;
RMAN> startup mount;
RMAN> blockrecover datafile 2 block 14 from backupset;
	Then done.

=== about expdp/impdp ===

Expdp@impdp用法

一、創建導出數據存放目錄

如：mkdir /u01/dump

二、創建directory邏輯目錄

CREATE OR REPLACE DIRECTORY DATA_DUMP_DIR AS '/u01/dump';

三、導出數據

1)按用戶導

expdp mctpsa/mctpsa@ipap schemas=mctpsa dumpfile=expdp.dmp DIRECTORY=DATA_DUMP_DIR;

2)並行進程parallel

expdp mctpsa/mctpsa@ipap directory=DATA_DUMP_DIR dumpfile=mctpsa3.dmp parallel=40 job_name=mctpsa3

3)按表名導

expdp mctpsa/mctpsa@ipap TABLES=sa_user,sa_dept dumpfile=expdp.dmp DIRECTORY=DATA_DUMP_DIR;

4)按查詢條件導

expdp mctpsa/mctpsa@ipap directory=DATA_DUMP_DIR dumpfile=expdp.dmp Tables=sa_user query='WHERE id=20';

5)按表空間導

expdp system/manager DIRECTORY=DATA_DUMP_DIR DUMPFILE=tablespace.dmp TABLESPACES=mctp,mctpsa;

6)導整個數據庫

expdp system/manager DIRECTORY=DATA_DUMP_DIR DUMPFILE=full.dmp FULL=y;


四、還原數據

1)導到指定用戶下

impdp mctpsa/mctpsa DIRECTORY=DATA_DUMP_DIR DUMPFILE=expdp.dmp SCHEMAS=mctpsa;

2)改變表的owner

impdp system/manager DIRECTORY=DATA_DUMP_DIR DUMPFILE=expdp.dmp TABLES=mctpsa.dept REMAP_SCHEMA=mctpsa:system;

3)導入表空間

impdp system/manager DIRECTORY=DATA_DUMP_DIR DUMPFILE=tablespace.dmp TABLESPACES=example;

4)導入數據庫

impdb system/manager DIRECTORY=DATA_DUMP_DIR DUMPFILE=full.dmp FULL=y;

5)追加數據

impdp system/manager DIRECTORY=dpdata1 DUMPFILE=expdp.dmp SCHEMAS=system TABLE_EXISTS_ACTION=append;


== Archive log about ==

=== Windows archivelog automatic clean how to. ===
{{{
CONFIGURE RETENTION POLICY TO RECOVERY WINDOW OF 3 DAYS;
CONFIGURE CONTROLFILE AUTOBACKUP ON;
}}}

=== List all archivelog backups for the past 24 hours ===
 RMAN> LIST BACKUP OF ARCHIVELOG FROM TIME 'sysdate-1';

=== 刪除大于4小時之前的所有歸檔文件，并加入計劃任務管理 ===
腳本如下
{{{
#! /bin/bash

#==================================================================

#set env

export ORACLE_HOME=/u01/app/oracle/product/10.2.0/db_1
export ORACLE_SID=racdb1
export PATH=.:${PATH}:$HOME/bin:$ORACLE_HOME/bin:$ORA_CRS_HOME/bin
#backup start

$ORACLE_HOME/bin/rman target /<<EOF
run {
        show all;
        allocate channel t1 type disk;
        allocate channel t2 type disk;
        crosscheck archivelog all;
        delete noprompt archivelog all completed before 'sysdate-4/24';
        sql 'alter system archive log current';
        backup as compressed backupset archivelog all format
        '/u01/app/oracle/backuparch/arch_%d_%T_%s_%p' delte all input;
        release channel t1;
        release channel t2;
        }
exit;
EOF
}}}
crontab -l
{{{
01 23 * * * /home/oracle/scripts/delete_archivelog.sh
}}}

=== Add archive log destination ===
{{{
alter system set log_archive_dest_1='location=+DATA/RACORA/ARCHIVELOG' SCOPE=SPFILE; 
ALTER SYSTEM SET log_archive_format='arch_%t_%s_%r.arc' SCOPE=spfile;
}}}


=== Enable Archive log mode in RAC envirenment ===
in any node
{{{
srvctl stop database -d racdb

sqlplus / as sysdba
 SQL> startup mount
 SQL> alter database archivelog
 SQL> shutdown immediate

srvctl start database -d racdb
}}}


== Thread about ==
SELECT thread#, instance, status FROM v$thread;
SELECT thread#, group#, status FROM v$log;

=== Adding threads ===
{{{
SQL> CONNECT SYS AS SYSBDA
SQL> STARTUP EXCLUSIVE
SQL> ALTER DATABASE ADD LOGFILE THREAD 2
SQL>     GROUP G4 ('FILE4.log') SIZE 500k,
SQL>     GROUP G5 ('FILE5.log') SIZE 500k,
SQL>     GROUP G6 ('FILE6.log') SIZE 500k;
SQL> ALTER DATABASE ENABLE PUBLIC THREAD 2;
}}}
== SID about ==
SID is System IDentifier

=== About instance mem and instruction ===
select COMPONENT,CURRENT_SIZE,MIN_SIZE,MAX_SIZE from v;
select name,value from v$pgastat where name in ('maximum PGA allocated','total PGA allocated');
select program from v$process order by program;
select platform_name from v$database;

=== Show exist group...and list ===
select group#,bytes,members from v$log;
select group#,member from v$logfile;

=== Show details of SGA pools ===
{{{ 
SET PAUSE ON
SET PAUSE 'Press Return to Continue'
SET PAGESIZE 60
COLUMN name  FORMAT A30
COLUMN value FORMAT A20
 
SELECT name,
value
FROM   v$parameter
WHERE  name like '%_pool%'
ORDER BY name
/
}}}

 * 当前SGA的总体情况
{{{
select * from v$sgainfo;
}}}
 * 当前SGA的详细信息
{{{
select * from v$sgastat
}}}

 * 空闲的Shared Pool大小：
{{{
select * from
v$sgastat
where pool = 'shared pool' and name = 'free memory'
}}}

 * SGA的变化记录
{{{
select * from v$sga_resize_ops
}}}

==== Library Cache的使用情况 ====
{{{
select * from v$librarycache;
}}}

==== Data Dictionary的使用情况 ====
{{{
select sum(gets), sum(getmisses), round(sum(getmisses) * 100 / sum(gets), 2 ) from v$rowcache;
}}}

=== 在EM没有开启的情况下，查询db_cache_size的优化建议 ===
{{{
select * from V$DB_CACHE_ADVICE;
}}}

=== Show parameter ===
SQL> SHOW PARAMETER db_cache_size;
SQL> SHOW PARAMETER spfile;
SQL> SHOW PARAMETER backgroud_dump;
SQL> SHOW PARAMETER dump_dest;
SQL> SHOW PARAMETER db_name;
SQL> SHOW PARAMETER instance_name;
SQL> SHOW PARAMETER PGA
SQL> SHOW PARAMETER SGA

=== Show instance ===
SQL> SHOW PARAMETER INSTANCE_NAME
SQL> SHOW PARAMETER SERVICE_NAME
SQL> SELECT INSTANCE_NAME from v$instance;
SQL> SELECT INSTANCE_NAME,STARTUP_TIME,VERSION from v$instance;

=== Show datafile ===
{{{
SELECT NAME from v$datafile;
SELECT NAME, FILE#, STATUS, FROM V$DATAFILE;
select tablespace_name, file_name ,AUTOEXTENSIBLE,MAXBYTES,INCREMENT_BY from dba_data_files order by 1,2;
}}}

=== How to check the maximum number of allowed connections to an Oracle database? ===
{{{
SELECT
  'Currently, ' 
  || (SELECT COUNT(*) FROM V$SESSION)
  || ' out of ' 
  || VP.VALUE 
  || ' connections are used.' AS USAGE_MESSAGE
FROM 
  V$PARAMETER VP
WHERE VP.NAME = 'sessions'
}}}


=== The number of sessions currently active ===
SELECT COUNT(*) FROM v$session


=== Change processes , sessions, transactions ! ===
processes=x
sessions=x*1.1+5
transactions=sessions*1.1
 
E.g.
processes=500
sessions=555
transactions=610
{{{ 
select name, value from v$parameter where name in ('sessions','processes','transactions');

alter system set processes=500 scope=both sid='*';
alter system set sessions=555 scope=both sid='*';
alter system set transactions=610 scope=both sid='*';
}}}


https://forums.oracle.com/forums/thread.jspa?threadID=898395

http://docs.oracle.com/cd/B19306_01/server.102/b14237/initparams191.htm

http://avdeo.com/2012/06/28/sessions-and-processes-parameters-oracle-11g/

http://webhelp.esri.com/arcgisserver/9.3/java/index.htm#geodatabases/oracle_1010194088.htm


=== Display active processes ===
sqlplus /nolog
{{{
SQL> connect sys/password@remoteip:1521/instance
SQL> connect sys/password as sysdba;
SQL> DESC V$PROCESS
}}}

=== Show recover_file ===
SQL> SELECT * from v$recover_file;
SQL> SELECT name from v$datafile where file#=3;

=== Show ADR information ===
SQL> SELECT * from v$diag_info;

=== ADR Command Interpreter (show alter recorder) ===
adrci> show alert
adrci> show incident;
adrci> show incident -mode DETAIL -p "incident_id=xxxx";

=== Test listener ===
{{{
tnsping SERVICE_NAME
lsnrctl start
lsnrctl status
}}}


=== How to find the NLS_LANG to set for a database? ===
{{{
SELECT value$ FROM sys.props$ WHERE name = 'NLS_CHARACTERSET' ;
SELECT * from NLS_SESSION_PARAMETERS;
}}}

{{{
select DECODE(parameter, 'NLS_CHARACTERSET', 'CHARACTER SET',
'NLS_LANGUAGE', 'LANGUAGE',
'NLS_TERRITORY', 'TERRITORY') name,
value from v$nls_parameters
WHERE parameter IN ( 'NLS_CHARACTERSET', 'NLS_LANGUAGE', 'NLS_TERRITORY')
}}}
http://www.oracle.com/technetwork/database/globalization/nls-lang-099431.html

=== Show user role ===
SQL> SELECT * FROM user_role_privs;

=== Check free/used space per tablespace ===

Example query to check free and used space per tablespace:
{{{
SELECT /* + RULE */  df.tablespace_name "Tablespace",
       df.bytes / (1024 * 1024) "Size (MB)",
       SUM(fs.bytes) / (1024 * 1024) "Free (MB)",
       Nvl(Round(SUM(fs.bytes) * 100 / df.bytes),1) "% Free",
       Round((df.bytes - SUM(fs.bytes)) * 100 / df.bytes) "% Used"
  FROM dba_free_space fs,
       (SELECT tablespace_name,SUM(bytes) bytes
          FROM dba_data_files
         GROUP BY tablespace_name) df
 WHERE fs.tablespace_name (+)  = df.tablespace_name
 GROUP BY df.tablespace_name,df.bytes
UNION ALL
SELECT /* + RULE */ df.tablespace_name tspace,
       fs.bytes / (1024 * 1024),
       SUM(df.bytes_free) / (1024 * 1024),
       Nvl(Round((SUM(fs.bytes) - df.bytes_used) * 100 / fs.bytes), 1),
       Round((SUM(fs.bytes) - df.bytes_free) * 100 / fs.bytes)
  FROM dba_temp_files fs,
       (SELECT tablespace_name,bytes_free,bytes_used
          FROM v$temp_space_header
         GROUP BY tablespace_name,bytes_free,bytes_used) df
 WHERE fs.tablespace_name (+)  = df.tablespace_name
 GROUP BY df.tablespace_name,fs.bytes,df.bytes_free,df.bytes_used
 ORDER BY 4 DESC;
}}}

== Troubshooting ==
== awr report ==
http://www.pafumi.net/AWR%20Reports.html#SGA_Target_Advisory
{{{
sqlplus / as sysdba
@?/rdbms/admin/awrrpt.sql
7days
begin to end
filename
}}}

=== 11g account expired ===
Disable Oracle's password expiry
http://www.odi.ch/weblog/posting.php?posting=520

=== Resolved ORA-12528 ===
 * TNS:listener: all appropriate instances are blocking new connections error

http://itbloggertips.com/2013/06/resolved-ora-12528-tnslistener-all-appropriate-instances-are-blocking-new-connections-error/

https://francispaulraj.wordpress.com/ora-12528-tnslistener-all-appropriate-instances-are-blocking-new-connections/

http://osamamustafa.blogspot.com/2012/02/ora-12528-tns-listener-all-appropriate.html

add (UR = A) in tnsnames.ora

=== add datafile to tablespace ===

alter tablespace OA add datafile '/oratest/OA02.dbf' size 10G;

http://linuxtechres.blogspot.com/2009/11/how-to-clean-up-disk-space-for-oracle.html

=== add space to database ===

SQL> ALTER TABLESPACE ts1 ADD DATAFILE '/path/to/file/name' SIZE 100M;

OR change it
SQL> ALTER DATABASE DATAFILE '/path/to/data/file/name' RESIZE 200M;


=== ORA-01157 & ORA-01110 ===
ORA-01157: cannot identify/lock data file 7 - see DBWR trace file
ORA-01110: data file 7: '/data/WZG_OA.dbf'

 * 既然出现报错的几个dbf文件已经不用，则解决办法相对简单，只要将对应的数据文件删除，并继续删除对应新增的表空间即可。操作过程如下：
 SQL> shutdown immediate;

 SQL> startup mount;
 SQL> select file#,name,status from v$datafile;
 SQL> alter database datafile '/tmp/test.dbf' offline drop;      //此处若不加drop会报错
 * 再次查看v$datafile表会发现对应的几个dbf文件状态由ONLINE变为RECOVER
 SQL> select * from v$tablespace;
 SQL> drop tablespace test including contents cascade constraints;

 删除完毕，再次执行startup成功。

==== RMAN use repair bad blocks ====
 * Sometimes Oracle takes forever to shutdown with the ``immediate'' option. As workaround to this problem, shutdown using these commands:
{{{
 alter system checkpoint;
 shutdown abort
 startup restrict
 shutdown immediate
}}}

 * Note that if your database is in ARCHIVELOG mode, one can still use archived log files to roll forward from an off-line backup. If you cannot take your database down for a cold (off-line) backup at a convenient time, switch your database into ARCHIVELOG mode and perform hot (on-line) backups. 

=== when the "dbstart" command haven't happen anything ===
check /etc/orata file, replace "N" with "Y"


=== tnsnames.ora ===
 I. tnsnames.ora Network Configuration File define the Remote login port and 
so on..

CONN SYSTEM/password@192.168.1.111:1521/oradb   ( port 1521 is ..)

=== sqlnet.ora ===
 I. sqlnet.ora File define OS authentication and Oracle authentication.

SQLNET.AUTHENTICATION_SERVICES=(False)  -> mean Oracle authentication
SQLNET.AUTHENTICATION_SERVICES=(All)    -> mean Linux OS authentication

=== Recovery Oracle orapw$ORACLE_SID file ===
loggin as Sys or System on the EM,the error i get is ``Your username and/or 
password are invalid.''

The value of Remote_login_passwordfile=Exclusive parameter should pfile/spfi
le.
Then just create a password file using ``orapwd'' utility and then try to lo
gged in. it will solve your problem.
=> $ orapwd file='$ORACLE_HOME/dbs/orapw$ORACLE_SID' password=pwd entries=10
 force=y

SELECT * FROM NLS_DATABASE_PARAM\begin{table}

=== Lost Oracle SYS and SYSTEM password? ===

$ sqlplus "/ as sysdba"
SQL> show user
SQL> passw system
SQL> passw sys

=== SPFILE 错误导致数据库无法启动(ORA-01565) ===
http://blog.csdn.net/robinson_0612/article/details/5774795

=== In order to see the database default tablespace issue ===

SQL> SELECT PROPERTY_VALUE FROM DATABASE_PROPERTIES WHERE property_name = 'DEFAULT_PERMANENT_TABLESPACE';

PROPERTY_VALUE
--------------------------------------------------------------------------------
USERS


=== Drop tablespace ===
http://psoug.org/snippet/TABLESPACE-Dropping-Tablespaces_851.htm

{{{
startup mount
alter database datafile '/path/to/filename' offline drop;
alter database open;
drop tablespace tbsp_name including contents cascade constraints;
}}}

== Upgrade&Installation how to ==
=== Patch download link ===
https://updates.oracle.com/Orion/PatchDetails/switch_to_simple?plat_lang=233P&patch_file=&file_id=&password_required=&password_required_readme=&merged_trans=&aru=12791168&patch_num=8202632&patch_num_id=1253975&default_release=80102050&default_plat_lang=233P&default_compatible_with=&patch_password=&orderby=&direction=&no_header=0&sortcolpressed=&tab_number=

=== Upgrade Oracle 10g Release 2 from 10.2.0.1 to 10.2.0.5 ===
# http://p-mayuranathan.blogspot.com/2012/07/patch-upgradation-from-10201-to-10205.html
=== uninstall Oracle database 10g ===
{{{
shutdown abort;
startup mount exclusive restrict;
drop database;
}}}

=== How to patch 10.2.0.4 from 10.2.0.1 in RHEL5 ===
http://www.oracleflash.com/29/Upgrade-Oracle-10g-Release-2-from-10201-to-10204.html
=== How to patch 10.2.0.1 to 10.2.0.4 in Oracle 10g RAC? ===
http://khalidali-oracledba.blogspot.com/2012/03/rac-upgradation-10201-to-10204.html

=== Delete an Instance from an Oracle RAC Database ===
http://www.oracle-base.com/articles/rac/delete-an-instance-from-an-oracle-rac-database.php

dbca -silent -deleteInstance -nodeList ol5-112-rac2 -gdbName RAC -instanceName RAC2 -sysDBAUserName sys -sysDBAPassword myPassword


=== query database size ===
{{{
select sum(bytes)/1024/1024/1024 from dba_segments;

select
( select sum(bytes)/1024/1024 data_size from dba_data_files ) +
( select nvl(sum(bytes),0)/1024/1024 temp_size from dba_temp_files ) +
( select sum(bytes)/1024/1024 redo_size from sys.v_$log ) +
( select sum(BLOCK_SIZE*FILE_SIZE_BLKS)/1024/1024 controlfile_size from v$controlfile) "Size in MB"
from
dual;
}}}




== ASM about ==
=== ASM Disk Volumes ===
{{{
column PATH format a15;
select path from v$asm_disk;
}}}

=== ASM Status ===
$ srvctl status asm
$ srvctl config asm -a

=== How to check free space in ASM ===
select name, state, total_mb, free_mb from v$asm_diskgroup;

SELECT name, type, ceil (total_mb/1024) TOTAL_GB , ceil (free_mb/1024) FREE_GB, required_mirror_free_mb,ceil ((usable_file_mb)/1024) FROM V$ASM_DISKGROUP;


=== Enable flashback database ===
{{{
SQL> select log_mode, flashback_on from v$database;
LOG_MODE     FLASHBACK_ON
------------ ------------------
ARCHIVELOG   NO

SQL> alter database flashback on;
Database altered.

SQL> select log_mode, flashback_on from v$database;
LOG_MODE     FLASHBACK_ON
------------ ------------------
ARCHIVELOG   YES
}}}

== emctl dbconsole about ==
http://blog.mclaughlinsoftware.com/oracle-architecture-configuration/changing-windows-hostname-and-oracle-enterprise-manager/
{{{
emca -deconfig dbcontrol db -repos drop
emca -config dbcontrol db -repos create
}}}



=== To disable FRA you can use ===
  ALTER SYSTEM SET DB_RECOVERY_FILE_DEST = '' scope=both;

=== ORA-00205 ===
 * error in identifying control file, check alert log for more info

http://www.oracledistilled.com/oracle-database/recover-from-a-corrupt-or-missing-control-file/


== Stream about ==
=== Advanced reciplication VS stream VS Goldgate ===
http://blog.devart.com/ten-ways-to-synchronize-oracle-table-data.html

 I. How to re-synchronize the streams replicated objects online 

http://eric-oracle.blogspot.com/2008/12/how-to-re-synchronize-streams.html

http://kubilaykara.blogspot.com/2010/10/oracle-11g-streams-synchronous-capture.html

http://krish-dba.blogspot.com/2009/01/re-synchronizingrefresh-table-in.html


 I. Oracle Stream
http://wedostreams.blogspot.com/2009/01/oracle-streams-101.html#streams101p5

http://orachat.com/10g-streams-configuration/

http://www.askmaclean.com/archives/tag/streams

http://anargodjaev.wordpress.com/2014/01/03/step-by-step-example-on-setting-up-streams-oracle-11g/

#http://blog.itpub.net/25198367/viewspace-715070

http://www.orafaq.com/wiki/Oracle_Streams#Components_of_Oracle_Streams

http://wenku.baidu.com/view/2fcbf64d2e3f5727a5e962fa.html

http://www.orafaq.com/wiki/Oracle_Streams#Components_of_Oracle_Streams

=== How do you get the datafile sizes from the oracle? ===
{{{
COL FILE_NAME FOR A70
COL TABLESPACE_NAME FOR A30
CLEAR BREAKS
CLEAR COMPUTES
COMPUTE SUM OF SIZE_IN_MB ON REPORT
BREAK ON REPORT
SELECT TABLESPACE_NAME,FILE_NAME,AUTOEXTENSIBLE,
INCREMENT_BY,MAXBYTES/1024/1024 "MAX IN MB",
BYTES/1024/1024 "SIZE_IN_MB"
FROM DBA_DATA_FILES ORDER BY TABLESPACE_NAME;
}}}

# Processing object type EXPORT/TABLE/INDEX/INDEX [message #505129 is a reply to message #505045]
 I solved my problem.I believe.It happened due to space problem.I did free up some space (around 50 gb). I ran the import again and it took 4 hrs to complete. Replying thinking it might help others.


{{{
sqlplus / as sysdba
SELECT name, open_mode FROM v$database ;
SELECT instance_name, host_name, version, status FROM v$instance ;
}}}

=== Estimate used space for database ===
{{{
SELECT DF.TOTAL/1073741824 "DataFile Size GB", LOG.TOTAL/1073741824 "Redo Log Size GB", CONTROL.TOTAL/1073741824 "Control File Size GB", (DF.TOTAL + LOG.TOTAL + CONTROL.TOTAL)/ 1073741824 "Total Size GB" from dual, (select sum(a.bytes) TOTAL from dba_data_files a) DF, (select sum(b.bytes) TOTAL from v$log b) LOG, (select sum((cffsz+1)*cfbsz) TOTAL from x$kcccf c) CONTROL;
}}}


== RAC about ==
=== Check the health of Cluster ===

 * You can run the below commands to check the health of the cluster as oracle or grid user.
{{{
/u01/crs/products/11.2.0/crs/bin/crsctl check cluster
/u01/crs/products/11.2.0/crs/bin/crsctl stat res -t
}}}

 * NODEAPPS Status
{{{
srvctl status nodeapps
srvctl config nodeapps
}}}

 * DATABASE Status
{{{
srvctl config database -d racdb -a
srvctl status database -d racdb
srvctl status instance -d racdb -i racdb1
}}}

 * LISTENER Status
{{{
srvctl status listener
srvctl config listener -a
}}}

 * SCAN Status
{{{
srvctl status scan
srvctl config scan
}}}

 * Verifying Clock Synchronization across the Cluster Nodes
{{{
cluvfy comp clocksync -verbose
}}}

{{{
set lines 200;
column HOST format a7;
SELECT     inst_id,
           instance_number inst_no,
           instance_name inst_name,
           parallel,
           status,
           database_status db_status,
           active_state state,
           host_name host
FROM       gv$instance
ORDER BY   inst_id;
}}}

=== Changing Resource Attributes in 11gR2 Grid Infrastructure ===
crsctl stat res -p
{{{
NAME=ora.racdb.db
TYPE=ora.database.type
ACL=owner:oracle:rwx,pgrp:oinstall:r--,other::r--,group:dba:r-x,group:oper:r-x,user:grid:r-x
ACTION_FAILURE_TEMPLATE=
ACTION_SCRIPT=
ACTIVE_PLACEMENT=1
AGENT_FILENAME=%CRS_HOME%/bin/oraagent%CRS_EXE_SUFFIX%
AUTO_START=restore
CARDINALITY=2
CHECK_INTERVAL=1
CHECK_TIMEOUT=30
CLUSTER_DATABASE=true
DATABASE_TYPE=RAC
DB_UNIQUE_NAME=racdb
DEFAULT_TEMPLATE=PROPERTY(RESOURCE_CLASS=database) PROPERTY(DB_UNIQUE_NAME=
CONCAT(PARSE(%NAME%, ., 2), %USR_ORA_DOMAIN%, .)) ELEMENT(INSTANCE_NAME=
%GEN_USR_ORA_INST_NAME%) ELEMENT(DATABASE_TYPE= %DATABASE_TYPE%)
DEGREE=1
DESCRIPTION=Oracle Database resource
ENABLED=1
FAILOVER_DELAY=0
FAILURE_INTERVAL=60
FAILURE_THRESHOLD=1
GEN_AUDIT_FILE_DEST=/u01/app/oracle/admin/racdb/adump
GEN_START_OPTIONS=
GEN_START_OPTIONS@SERVERNAME(rac1)=open
GEN_START_OPTIONS@SERVERNAME(rac2)=open
GEN_USR_ORA_INST_NAME=
GEN_USR_ORA_INST_NAME@SERVERNAME(rac1)=racdb1
GEN_USR_ORA_INST_NAME@SERVERNAME(rac2)=racdb2
HOSTING_MEMBERS=
INSTANCE_FAILOVER=0
LOAD=1
LOGGING_LEVEL=1
MANAGEMENT_POLICY=AUTOMATIC
NLS_LANG=
NOT_RESTARTING_TEMPLATE=
OFFLINE_CHECK_INTERVAL=0
ONLINE_RELOCATION_TIMEOUT=0
ORACLE_HOME=/u01/app/oracle/product/11.2.0.4/db_1
ORACLE_HOME_OLD=
PLACEMENT=restricted
PROFILE_CHANGE_TEMPLATE=
RESTART_ATTEMPTS=2
ROLE=PRIMARY
SCRIPT_TIMEOUT=60
SERVER_POOLS=ora.racdb
SPFILE=+DATA/racdb/spfileracdb.ora
START_DEPENDENCIES=hard(ora.DATA.dg,ora.FLASH.dg)
weak(type:ora.listener.type,global:type:ora.scan_listener.type,uniform:ora.ons,global:ora.gns)
pullup(ora.DATA.dg,ora.FLASH.dg)
START_TIMEOUT=600
STATE_CHANGE_TEMPLATE=
STOP_DEPENDENCIES=hard(intermediate:ora.asm,shutdown:ora.DATA.dg,shutdown:ora.FLASH.dg)
STOP_TIMEOUT=600
TYPE_VERSION=3.2
UPTIME_THRESHOLD=1h
USR_ORA_DB_NAME=racdb
USR_ORA_DOMAIN=
USR_ORA_ENV=
USR_ORA_FLAGS=
USR_ORA_INST_NAME=
USR_ORA_INST_NAME@SERVERNAME(rac1)=racdb1
USR_ORA_INST_NAME@SERVERNAME(rac2)=racdb2
USR_ORA_OPEN_MODE=open
USR_ORA_OPI=false
USR_ORA_STOP_MODE=immediate
VERSION=11.2.0.4.0
}}}

=== Change the resource start attribute with ===
{{{
crsctl modify resource ora.racdb.db -attr "AUTO_START=always"
}}}

=== Verify the status change with '''crsctl status res -p''' ===

[[https://oracleracdba1.wordpress.com/2013/01/29/how-to-set-auto-start-resources-in-11g-rac]]/


https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=402031519388438&id=1533057.1&displayIndex=2&_afrWindowMode=0&_adf.ctrl-state=qjo2u6w0k_478#aref_section24

=== AIX HACMP 10g RAC ==> DOC ID 404474.1 ===

[[http://www.programering.com/a/MzM5QzNwATU.html|Oracle RAC 11GR2(11.2.0.4) For AIX6.1 installation manual]]


== Oracle Optimization ==

=== delete log ===
rlwrap adrci
show home 
set home xxx
purge -age 14

=== SHMMAX size about ===
http://www.wallcopper.com/database/657.html
SHMMAX Available physical memory Defines the maximum allowable size
of one shared memory segment. The SHMMAX setting should be large enough
to hold the entire SGA in one shared memory segment. A low setting can
cause creation of multiple shared memory segments which may lead to
performance degradation.

 * Oracle recommends half the RAM.
Edit /etc/sysctl.conf
kernel.shmmax = 7730941132

SQL> alter system set sga_max_size=6G scope=spfile;

  I. 检查v$librarycache中sql area的gethitratio是否超过90％，如果未超过90％，应该检查应用代码，提高应用代码的效率。
select gethitratio from v$librarycache where namespace='SQL AREA';

   
  I. v$librarycache中reloads/pins的比率应该小于1％，如果大于1％，应该增加参数shared_pool_size的值。
select sum(pins),sum(reloads),sum(reloads)/sum(pins) hits from v$librarycache;

 * reloads/pins>1%有两种可能，一种是library cache空间不足，一种是sql中引用的对象不合法。

  I. shared pool reserved size一般是shared pool size的10％，不能超过50％。V$shared_pool_reserved中的request misses＝0或没有持续增长，或者free_memory大于shared pool reserved size的50%，表明shared pool reserved size过大，可以压缩。


== Orion how to ==
http://hesonogoma.com/linux/oracle_orion_disk_performance_benchmark.html
