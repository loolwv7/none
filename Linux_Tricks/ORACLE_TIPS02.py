
//创建一个控制文件命令到跟踪文件
alter database backup controlfile to trace;

//增加一个新的日志文件组的语句
connect internal as sysdba
alter database
add logfile group 4
('/db01/oracle/CC1/log_1c.dbf',
'/db02/oracle/CC1/log_2c.dbf') size 5M;

alter database
add logfile member '/db03/oracle/CC1/log_3c.dbf'
to group 4;
//在Server Manager上MOUNT并打开一个数据库:
connect internal as sysdba
startup mount ORA1 exclusive;
alter database open;

//生成数据字典
@catalog
@catproc

//在init.ora 中备份数据库的位置
log_archive_dest_1 = '/db00/arch'
log_archive_dest_state_1 = enable
log_archive_dest_2 = "service=stby.world mandatory reopen=60"
log_archive_dest_state_2 = enable
//对用户的表空间的指定和管理相关的语句
create user USERNAME identified by PASSWORD
default tablespace TABLESPACE_NAME;
alter user USERNAME default tablespace TABLESPACE_NAME;
alter user SYSTEM quota 0 on SYSTEM;
alter user SYSTEM quota 50M on TOOLS;
create user USERNAME identified by PASSWORD
default tablespace DATA
temporary tablespace TEMP;
alter user USERNAME temporary tablespace TEMP;

//重新指定一个数据文件的大小 :
alter database
datafile '/db05/oracle/CC1/data01.dbf' resize 200M;

//创建一个自动扩展的数据文件:
create tablespace DATA
datafile '/db05/oracle/CC1/data01.dbf' size 200M
autoextend ON
next 10M
maxsize 250M;

//在表空间上增加一个自动扩展的数据文件:
alter tablespace DATA
add datafile '/db05/oracle/CC1/data02.dbf'
size 50M
autoextend ON
maxsize 300M;

//修改参数:
alter database
datafile '/db05/oracle/CC1/data01.dbf'
autoextend ON
maxsize 300M;

//在数据文件移动期间重新命名:
alter database rename file
'/db01/oracle/CC1/data01.dbf' to
'/db02/oracle/CC1/data01.dbf';

alter tablespace DATA rename datafile
'/db01/oracle/CC1/data01.dbf' to
'/db02/oracle/CC1/data01.dbf';

alter database rename file  
'/db05/oracle/CC1/redo01CC1.dbf' to
'/db02/oracle/CC1/redo01CC1.dbf';

alter database datafile '/db05/oracle/CC1/data01.dbf'  
resize 80M;

//创建和使用角色:
create role APPLICATION_USER;
grant CREATE SESSION to APPLICATION_USER;
grant APPLICATION_USER to username;

//回滚段的管理
create rollback segment SEGMENT_NAME
tablespace RBS;

alter rollback segment SEGMENT_NAME offline;

drop rollback segment SEGMENT_NAME;

alter rollback segment SEGMENT_NAME online;
//回滚段上指定事务
commit;
set transaction use rollback segment ROLL_BATCH;
insert into TABLE_NAME
select * from DATA_LOAD_TABLE;
commit;

//查询回滚段的 大小和优化参数
select * from DBA_SEGMENTS
where Segment_Type = 'ROLLBACK';
select N.Name,         /* rollback segment name */
       S.OptSize       /* rollback segment OPTIMAL size */
from V$ROLLNAME N, V$ROLLSTAT S
where N.USN=S.USN;

//回收回滚段
alter rollback segment R1 shrink to 15M;
alter rollback segment R1 shrink;

//例子
set transaction use rollback segment SEGMENT_NAME

alter tablespace RBS
default storage
(initial 125K next 125K minextents 18 maxextents 249)

create rollback segment R4 tablespace RBS
   storage (optimal 2250K);
alter rollback segment R4 online;

select Sessions_Highwater from V$LICENSE;
grant select on EMPLOYEE to PUBLIC;

//用户和角色  
create role ACCOUNT_CREATOR;
grant CREATE SESSION, CREATE USER, ALTER USER  
   to ACCOUNT_CREATOR;

alter user THUMPER default role NONE;
alter user THUMPER default role CONNECT;
alter user THUMPER default role all except ACCOUNT_CREATOR;

alter profile DEFAULT
limit idle_time 60;

create profile LIMITED_PROFILE limit
FAILED_LOGIN_ATTEMPTS 5;
create user JANE identified by EYRE
profile LIMITED_PROFILE;
grant CREATE SESSION to JANE;

alter user JANE account unlock;
alter user JANE account lock;

alter profile LIMITED_PROFILE limit
PASSWORD_LIFE_TIME 30;

alter user jane password expire;

//创建操作系统用户
REM  Creating OPS$ accounts
create user OPS$FARMER
identified by SOME_PASSWORD
default tablespace USERS
temporary tablespace TEMP;

REM  Using identified externally
create user OPS$FARMER
identified externally
default tablespace USERS
temporary tablespace TEMP;

//执行ORAPWD
ORAPWD FILE=filename PASSWORD=password ENTRIES=max_users

create role APPLICATION_USER;
grant CREATE SESSION to APPLICATION_USER;
create role DATA_ENTRY_CLERK;
grant select, insert on THUMPER.EMPLOYEE to DATA_ENTRY_CLERK;
grant select, insert on THUMPER.TIME_CARDS to DATA_ENTRY_CLERK;
grant select, insert on THUMPER.DEPARTMENT to DATA_ENTRY_CLERK;
grant APPLICATION_USER to DATA_ENTRY_CLERK;
grant DATA_ENTRY_CLERK to MCGREGOR;
grant DATA_ENTRY_CLERK to BPOTTER with admin option;

//设置角色
set role DATA_ENTRY_CLERK;
set role NONE;

//回收权利:
revoke delete on EMPLOYEE from PETER;
revoke all on EMPLOYEE from MCGREGOR;

//回收角色:
revoke ACCOUNT_CREATOR from HELPDESK;

drop user USERNAME cascade;

grant SELECT on EMPLOYEE to MCGREGOR with grant option;
grant SELECT on THUMPER.EMPLOYEE to BPOTTER with grant option;
revoke SELECT on EMPLOYEE from MCGREGOR;

create user MCGREGOR identified by VALUES '1A2DD3CCEE354DFA';

alter user OPS$FARMER identified by VALUES 'no way';

//备份与恢复
使用 export 程序
exp system/manager file=expdat.dmp compress=Y owner=(HR,THUMPER)
exp system/manager file=hr.dmp owner=HR indexes=Y compress=Y
imp system/manager file=hr.dmp full=Y buffer=64000 commit=Y

//备份表
exp system/manager FILE=expdat.dmp TABLES=(Thumper.SALES)
//备份分区
exp system/manager FILE=expdat.dmp TABLES=(Thumper.SALES:Part1)

//输入例子
imp system/manager file=expdat.dmp
imp system/manager file=expdat.dmp buffer=64000 commit=Y

exp system/manager file=thumper.dat owner=thumper grants=N
  indexes=Y compress=Y rows=Y
imp system/manager file=thumper.dat FROMUSER=thumper TOUSER=flower
      rows=Y indexes=Y
imp system/manager file=expdat.dmp full=Y commit=Y buffer=64000
imp system/manager file=expdat.dmp ignore=N rows=N commit=Y buffer=64000

//使用操作系统备份命令
REM  TAR examples
tar -cvf /dev/rmt/0hc /db0[1-9]/oracle/CC1
tar -rvf /dev/rmt/0hc /orasw/app/oracle/CC1/pfile/initcc1.ora
tar -rvf /dev/rmt/0hc /db0[1-9]/oracle/CC1 /orasw/app/oracle/CC1/pfile/initcc1.ora

//离线备份的shell脚本
ORACLE_SID=cc1; export ORACLE_SID
ORAENV_ASK=NO; export ORAENV_ASK
. oraenv
svrmgrl <connect internal as sysdba
shutdown immediate;
exit
EOF1
insert backup commands like the "tar" commands here
svrmgrl <connect internal as sysdba
startup
EOF2

//在Server Manager上设置为archivelog mode:
connect internal as sysdba
startup mount cc1;
alter database archivelog;
archive log start;
alter database open;

//在Server Manager上设置为archivelog mode:
connect internal as sysdba
startup mount cc1;
alter database noarchivelog;
alter database open;

select Name,
       Value
  from V$PARAMETER
where Name like 'log_archive%';

//联机备份的脚本
#
# Sample Hot Backup Script for a UNIX File System database
#
# Set up environment variables:
ORACLE_SID=cc1; export ORACLE_SID
ORAENV_ASK=NO; export ORAENV_ASK
. oraenv
svrmgrl <connect internal as sysdba
REM
REM   备份 SYSTEM tablespace
REM
alter tablespace SYSTEM begin backup;
!tar -cvf /dev/rmt/0hc /db01/oracle/CC1/sys01.dbf
alter tablespace SYSTEM end backup;
REM
REM  The SYSTEM tablespace has now been written to a
REM   tar saveset on the tape device /dev/rmt/0hc.  The
REM   rest of the tars must use the "-rvf" clause to append
REM   to that saveset.
REM
REM   备份  RBS tablespace
REM
alter tablespace RBS begin backup;
!tar -rvf /dev/rmt/0hc /db02/oracle/CC1/rbs01.dbf
alter tablespace RBS end backup;
REM
REM   备份  DATA tablespace
REM   For the purposes of this example, this tablespace
REM   will contain two files, data01.dbf and data02.dbf.
REM   The * wildcard will be used in the filename.
REM
alter tablespace DATA begin backup;
!tar -rvf /dev/rmt/0hc /db03/oracle/CC1/data0*.dbf
alter tablespace DATA end backup;
REM
REM   备份 INDEXES tablespace
REM
alter tablespace INDEXES begin backup;
!tar -rvf /dev/rmt/0hc /db04/oracle/CC1/indexes01.dbf
alter tablespace INDEXES end backup;
REM
REM   备份  TEMP tablespace
REM
alter tablespace TEMP begin backup;
!tar -rvf /dev/rmt/0hc /db05/oracle/CC1/temp01.dbf
alter tablespace TEMP end backup;
REM
REM   Follow the same pattern to back up the rest
REM   of the tablespaces.
REM
REM    
REM  Step 2.  备份归档日志文件.
archive log stop
REM
REM   Exit Server Manager, using the indicator set earlier.
exit
EOFarch1
#
#  Record which files are in the destination directory.
#     Do this by setting an environment variable that is
#  equal to the directory listing for the destination  
#  directory.
#  For this example, the log_archive_dest is  
#  /db01/oracle/arch/CC1.
#
FILES=`ls /db01/oracle/arch/CC1/arch*.dbf`; export FILES
#
#  Now go back into Server Manager and restart the
#  archiving process.  Set an indicator (called EOFarch2
#  in this example).
#
svrmgrl <connect internal
archive log start;
exit
EOFarch2
#
#  Now back up the archived redo logs to the tape
#  device via the "tar" command, then delete them
#  from the destination device via the "rm" command.
#  You may choose to compress them instead.
#
tar -rvf /dev/rmt/0hc $FILES
rm -f $FILES
#
#     Step 3.  备份控制文件到磁盘.
#
svrmgrl <connect internal
alter database backup controlfile to
   'db01/oracle/CC1/CC1controlfile.bck';
exit
EOFarch3
#
#  备份控制文件到磁带.
#
tar -rvf /dev/rmt/0hc /db01/oracle/CC1/CC1controlfile.bck
#
#  End of hot backup script.
//自动生成开始备份的脚本
set pagesize 0 feedback off
select  
    'alter tablespace '||Tablespace_Name||' begin backup;'
  from DBA_TABLESPACES
where Status <> 'INVALID'
spool alter_begin.sql
/
spool off

//自动生成备份结束的脚本
set pagesize 0 feedback off
select  
    'alter tablespace '||Tablespace_Name||' end backup;'
  from DBA_TABLESPACES
where Status <> 'INVALID'
spool alter_end.sql
/
spool off

//备份归档日志文件的脚本.
REM  See text for alternatives.
#     Step 1: Stop the archiving process. This will keep
#     additional archived redo log files from being written
#     to the destination directory during this process.
#
svrmgrl <connect internal as sysdba
archive log stop;
REM
REM   Exit Server Manager using the indicator set earlier.
exit
EOFarch1
#
#     Step 2: Record which files are in the destination  
#  directory.

#     Do this by setting an environment variable that is
#  equal to the directory listing for the destination  
#  directory.
#  For this example, the log_archive_dest is
#  /db01/oracle/arch/CC1.
#
FILES=`ls /db01/oracle/arch/CC1/arch*.dbf`; export FILES
#
#     Step 3: Go back into Server Manager and restart the
#  archiving process. Set an indicator (called EOFarch2
#  in this example).
#
svrmgrl <connect internal as sysdba
archive log start;
exit
EOFarch2
#
#     Step 4. Back up the archived redo logs to the tape
#  device via the "tar" command, then delete them
#  from the destination device via the "rm" command.
#
tar -rvf /dev/rmt/0hc $FILES
#
#     Step 5. Delete those files from the destination directory.
#
rm -f $FILES
#
#     End of archived redo log file backup script.

REM  磁盘到磁盘的备份
REM
REM   Back up the RBS tablespace - to another disk (UNIX)
REM
alter tablespace RBS begin backup;
!cp /db02/oracle/CC1/rbs01.dbf /db10/oracle/CC1/backups
alter tablespace RBS end backup;
REM

REM  移动归档日志文件的shell脚本
#
# Procedure for moving archived redo logs to another device
#
svrmgrl <connect internal as sysdba
archive log stop;
!mv /db01/oracle/arch/CC1 /db10/oracle/arch/CC1
archive log start;
exit
EOFarch2
#
# end of archived redo log directory move.

//生成创建控制文件命令
alter database backup controlfile to trace;

//时间点恢复的例子
connect internal as sysdba
startup mount instance_name;
recover database until time '1999-08-07:14:40:00';

//创建恢复目录
rman rcvcat rman/rman@

// 在(UNIX)下创建恢复目录
RMAN> create catalog tablespace rcvcat;

// 在(NT)下创建恢复目录
RMAN> create catalog tablespace "RCVCAT";

//连接描述符范例  
(DESCRIPTION=
      (ADDRESS=
            (PROTOCOL=TCP)
            (HOST=HQ)
            (PORT=1521))
      (CONNECT DATA=
            (SID=loc)))

// listener.ora 的条目entry

// listener.ora 的条目entry
LISTENER =
(ADDRESS_LIST =
(ADDRESS=
(PROTOCOL=IPC)
(KEY= loc.world)
)
)
SID_LIST_LISTENER =
(SID_LIST =
(SID_DESC =
(SID_NAME = loc)
(ORACLE_HOME = /orasw/app/oracle/product/8.1.5.1)
)
)

// tnsnames.ora 的条目
LOC=
(DESCRIPTION=
(ADDRESS =
(PROTOCOL = TCP)
(HOST = HQ)
(PORT = 1521))
)
(CONNECT_DATA =
(SERVICE_NAME = loc)
(INSTANCE_NAME = loc)
)
)

//连接参数的设置（sql*net）
LOC =(DESCRIPTION=
(ADDRESS=
(COMMUNITY=TCP.HQ.COMPANY)
(PROTOCOL=TCP)
(HOST=HQ)
(PORT=1521))
(CONNECT DATA=
(SID=loc)))
//参数文件配置范例
// tnsnames.ora
HQ =(DESCRIPTION=
(ADDRESS=
(PROTOCOL=TCP)
(HOST=HQ)
(PORT=1521))
(CONNECT DATA=
(SID=loc)))

// listener.ora
LISTENER =
(ADDRESS_LIST =
(ADDRESS=
(PROTOCOL=IPC)
(KEY= loc)
)
)
SID_LIST_LISTENER =
(SID_LIST =
(SID_DESC =
(SID_NAME = loc)
(ORACLE_HOME = /orasw/app/oracle/product/8.1.5.1)
)
)

// Oracle8I tnsnames.ora
LOC=
(DESCRIPTION=
(ADDRESS =
(PROTOCOL = TCP)
(HOST = HQ)
(PORT = 1521))
)
(CONNECT_DATA =
(SERVICE_NAME = loc)
(INSTANCE_NAME = loc)
)
)

//使用 COPY 实现数据库之间的复制
copy from
remote_username/remote_password@service_name
to
username/password@service_name
[append|create|insert|replace]
TABLE_NAME
using subquery;

REM COPY example
set copycommit 1
set arraysize 1000
copy from HR/PUFFINSTUFF@loc -
create EMPLOYEE -
using -
select * from EMPLOYEE


//监视器的管理
lsnrctl start
lsnrctl start my_lsnr
lsnrctl status
lsnrctl status hq

检查监视器的进程
ps -ef | grep tnslsnr
//在 lsnrctl 内停止监视器
set password lsnr_password
stop

//在lsnrctl 内列出所有的服务
set password lsnr_password
services
//启动或停止一个NT的listener
net start OracleTNSListener
net stop OracleTNSListener

// tnsnames.ora 文件的内容
fld1 =
(DESCRIPTION =
(ADDRESS_LIST =
(ADDRESS = (PROTOCOL = TCP)
(HOST = server1.fld.com)(PORT = 1521))
)
(CONNECT_DATA =
(SID = fld1)
)
)
//操作系统网络的管理

telnet host_name
ping host_name
/etc/hosts 文件
130.110.238.109 nmhost
130.110.238.101 txhost
130.110.238.102 azhost arizona
//oratab 表项
loc:/orasw/app/oracle/product/8.1.5.1:Y
cc1:/orasw/app/oracle/product/8.1.5.1:N
old:/orasw/app/oracle/product/8.1.5.0:Y



//创建一个控制文件命令到跟踪文件
alter database backup controlfile to trace;

//增加一个新的日志文件组的语句
connect internal as sysdba
alter database
add logfile group 4
('/db01/oracle/CC1/log_1c.dbf',
'/db02/oracle/CC1/log_2c.dbf') size 5M;

alter database
add logfile member '/db03/oracle/CC1/log_3c.dbf'
to group 4;
//在Server Manager上MOUNT并打开一个数据库:
connect internal as sysdba
startup mount ORA1 exclusive;
alter database open;

//生成数据字典
@catalog
@catproc

//在init.ora 中备份数据库的位置
log_archive_dest_1 = '/db00/arch'
log_archive_dest_state_1 = enable
log_archive_dest_2 = "service=stby.world mandatory reopen=60"
log_archive_dest_state_2 = enable
//对用户的表空间的指定和管理相关的语句
create user USERNAME identified by PASSWORD
default tablespace TABLESPACE_NAME;
alter user USERNAME default tablespace TABLESPACE_NAME;
alter user SYSTEM quota 0 on SYSTEM;
alter user SYSTEM quota 50M on TOOLS;
create user USERNAME identified by PASSWORD
default tablespace DATA
temporary tablespace TEMP;
alter user USERNAME temporary tablespace TEMP;

//重新指定一个数据文件的大小 :
alter database
datafile '/db05/oracle/CC1/data01.dbf' resize 200M;

//创建一个自动扩展的数据文件:
create tablespace DATA
datafile '/db05/oracle/CC1/data01.dbf' size 200M
autoextend ON
next 10M
maxsize 250M;

//在表空间上增加一个自动扩展的数据文件:
alter tablespace DATA
add datafile '/db05/oracle/CC1/data02.dbf'
size 50M
autoextend ON
maxsize 300M;

//修改参数:
alter database
datafile '/db05/oracle/CC1/data01.dbf'
autoextend ON
maxsize 300M;

//在数据文件移动期间重新命名:
alter database rename file
'/db01/oracle/CC1/data01.dbf' to
'/db02/oracle/CC1/data01.dbf';

alter tablespace DATA rename datafile
'/db01/oracle/CC1/data01.dbf' to
'/db02/oracle/CC1/data01.dbf';

alter database rename file  
'/db05/oracle/CC1/redo01CC1.dbf' to
'/db02/oracle/CC1/redo01CC1.dbf';

alter database datafile '/db05/oracle/CC1/data01.dbf'  
resize 80M;

//创建和使用角色:
create role APPLICATION_USER;
grant CREATE SESSION to APPLICATION_USER;
grant APPLICATION_USER to username;

//回滚段的管理
create rollback segment SEGMENT_NAME
tablespace RBS;

alter rollback segment SEGMENT_NAME offline;

drop rollback segment SEGMENT_NAME;

alter rollback segment SEGMENT_NAME online;
//回滚段上指定事务
commit;
set transaction use rollback segment ROLL_BATCH;
insert into TABLE_NAME
select * from DATA_LOAD_TABLE;
commit;

//查询回滚段的 大小和优化参数
select * from DBA_SEGMENTS
where Segment_Type = 'ROLLBACK';
select N.Name,         /* rollback segment name */
       S.OptSize       /* rollback segment OPTIMAL size */
from V$ROLLNAME N, V$ROLLSTAT S
where N.USN=S.USN;

//回收回滚段
alter rollback segment R1 shrink to 15M;
alter rollback segment R1 shrink;

//例子
set transaction use rollback segment SEGMENT_NAME

alter tablespace RBS
default storage
(initial 125K next 125K minextents 18 maxextents 249)

create rollback segment R4 tablespace RBS
   storage (optimal 2250K);
alter rollback segment R4 online;

select Sessions_Highwater from V$LICENSE;
grant select on EMPLOYEE to PUBLIC;

//用户和角色  
create role ACCOUNT_CREATOR;
grant CREATE SESSION, CREATE USER, ALTER USER  
   to ACCOUNT_CREATOR;

alter user THUMPER default role NONE;
alter user THUMPER default role CONNECT;
alter user THUMPER default role all except ACCOUNT_CREATOR;

alter profile DEFAULT
limit idle_time 60;

create profile LIMITED_PROFILE limit
FAILED_LOGIN_ATTEMPTS 5;
create user JANE identified by EYRE
profile LIMITED_PROFILE;
grant CREATE SESSION to JANE;

alter user JANE account unlock;
alter user JANE account lock;

alter profile LIMITED_PROFILE limit
PASSWORD_LIFE_TIME 30;

alter user jane password expire;

//创建操作系统用户
REM  Creating OPS$ accounts
create user OPS$FARMER
identified by SOME_PASSWORD
default tablespace USERS
temporary tablespace TEMP;

REM  Using identified externally
create user OPS$FARMER
identified externally
default tablespace USERS
temporary tablespace TEMP;

//执行ORAPWD
ORAPWD FILE=filename PASSWORD=password ENTRIES=max_users

create role APPLICATION_USER;
grant CREATE SESSION to APPLICATION_USER;
create role DATA_ENTRY_CLERK;
grant select, insert on THUMPER.EMPLOYEE to DATA_ENTRY_CLERK;
grant select, insert on THUMPER.TIME_CARDS to DATA_ENTRY_CLERK;
grant select, insert on THUMPER.DEPARTMENT to DATA_ENTRY_CLERK;
grant APPLICATION_USER to DATA_ENTRY_CLERK;
grant DATA_ENTRY_CLERK to MCGREGOR;
grant DATA_ENTRY_CLERK to BPOTTER with admin option;

//设置角色
set role DATA_ENTRY_CLERK;
set role NONE;

//回收权利:
revoke delete on EMPLOYEE from PETER;
revoke all on EMPLOYEE from MCGREGOR;

//回收角色:
revoke ACCOUNT_CREATOR from HELPDESK;

drop user USERNAME cascade;

grant SELECT on EMPLOYEE to MCGREGOR with grant option;
grant SELECT on THUMPER.EMPLOYEE to BPOTTER with grant option;
revoke SELECT on EMPLOYEE from MCGREGOR;

create user MCGREGOR identified by VALUES '1A2DD3CCEE354DFA';

alter user OPS$FARMER identified by VALUES 'no way';

//备份与恢复
使用 export 程序
exp system/manager file=expdat.dmp compress=Y owner=(HR,THUMPER)
exp system/manager file=hr.dmp owner=HR indexes=Y compress=Y
imp system/manager file=hr.dmp full=Y buffer=64000 commit=Y

//备份表
exp system/manager FILE=expdat.dmp TABLES=(Thumper.SALES)
//备份分区
exp system/manager FILE=expdat.dmp TABLES=(Thumper.SALES:Part1)

//输入例子
imp system/manager file=expdat.dmp
imp system/manager file=expdat.dmp buffer=64000 commit=Y

exp system/manager file=thumper.dat owner=thumper grants=N
  indexes=Y compress=Y rows=Y
imp system/manager file=thumper.dat FROMUSER=thumper TOUSER=flower
      rows=Y indexes=Y
imp system/manager file=expdat.dmp full=Y commit=Y buffer=64000
imp system/manager file=expdat.dmp ignore=N rows=N commit=Y buffer=64000

//使用操作系统备份命令
REM  TAR examples
tar -cvf /dev/rmt/0hc /db0[1-9]/oracle/CC1
tar -rvf /dev/rmt/0hc /orasw/app/oracle/CC1/pfile/initcc1.ora
tar -rvf /dev/rmt/0hc /db0[1-9]/oracle/CC1 /orasw/app/oracle/CC1/pfile/initcc1.ora

//离线备份的shell脚本
ORACLE_SID=cc1; export ORACLE_SID
ORAENV_ASK=NO; export ORAENV_ASK
. oraenv
svrmgrl <connect internal as sysdba
shutdown immediate;
exit
EOF1
insert backup commands like the "tar" commands here
svrmgrl <connect internal as sysdba
startup
EOF2

//在Server Manager上设置为archivelog mode:
connect internal as sysdba
startup mount cc1;
alter database archivelog;
archive log start;
alter database open;

//在Server Manager上设置为archivelog mode:
connect internal as sysdba
startup mount cc1;
alter database noarchivelog;
alter database open;

select Name,
       Value
  from V$PARAMETER
where Name like 'log_archive%';

//联机备份的脚本
#
# Sample Hot Backup Script for a UNIX File System database
#
# Set up environment variables:
ORACLE_SID=cc1; export ORACLE_SID
ORAENV_ASK=NO; export ORAENV_ASK
. oraenv
svrmgrl <connect internal as sysdba
REM
REM   备份 SYSTEM tablespace
REM
alter tablespace SYSTEM begin backup;
!tar -cvf /dev/rmt/0hc /db01/oracle/CC1/sys01.dbf
alter tablespace SYSTEM end backup;
REM
REM  The SYSTEM tablespace has now been written to a
REM   tar saveset on the tape device /dev/rmt/0hc.  The
REM   rest of the tars must use the "-rvf" clause to append
REM   to that saveset.
REM
REM   备份  RBS tablespace
REM
alter tablespace RBS begin backup;
!tar -rvf /dev/rmt/0hc /db02/oracle/CC1/rbs01.dbf
alter tablespace RBS end backup;
REM
REM   备份  DATA tablespace
REM   For the purposes of this example, this tablespace
REM   will contain two files, data01.dbf and data02.dbf.
REM   The * wildcard will be used in the filename.
REM
alter tablespace DATA begin backup;
!tar -rvf /dev/rmt/0hc /db03/oracle/CC1/data0*.dbf
alter tablespace DATA end backup;
REM
REM   备份 INDEXES tablespace
REM
alter tablespace INDEXES begin backup;
!tar -rvf /dev/rmt/0hc /db04/oracle/CC1/indexes01.dbf
alter tablespace INDEXES end backup;
REM
REM   备份  TEMP tablespace
REM
alter tablespace TEMP begin backup;
!tar -rvf /dev/rmt/0hc /db05/oracle/CC1/temp01.dbf
alter tablespace TEMP end backup;
REM
REM   Follow the same pattern to back up the rest
REM   of the tablespaces.
REM
REM    
REM  Step 2.  备份归档日志文件.
archive log stop
REM
REM   Exit Server Manager, using the indicator set earlier.
exit
EOFarch1
#
#  Record which files are in the destination directory.
#     Do this by setting an environment variable that is
#  equal to the directory listing for the destination  
#  directory.
#  For this example, the log_archive_dest is  
#  /db01/oracle/arch/CC1.
#
FILES=`ls /db01/oracle/arch/CC1/arch*.dbf`; export FILES
#
#  Now go back into Server Manager and restart the
#  archiving process.  Set an indicator (called EOFarch2
#  in this example).
#
svrmgrl <connect internal
archive log start;
exit
EOFarch2
#
#  Now back up the archived redo logs to the tape
#  device via the "tar" command, then delete them
#  from the destination device via the "rm" command.
#  You may choose to compress them instead.
#
tar -rvf /dev/rmt/0hc $FILES
rm -f $FILES
#
#     Step 3.  备份控制文件到磁盘.
#
svrmgrl <connect internal
alter database backup controlfile to
   'db01/oracle/CC1/CC1controlfile.bck';
exit
EOFarch3
#
#  备份控制文件到磁带.
#
tar -rvf /dev/rmt/0hc /db01/oracle/CC1/CC1controlfile.bck
#
#  End of hot backup script.
//自动生成开始备份的脚本
set pagesize 0 feedback off
select  
    'alter tablespace '||Tablespace_Name||' begin backup;'
  from DBA_TABLESPACES
where Status <> 'INVALID'
spool alter_begin.sql
/
spool off

//自动生成备份结束的脚本
set pagesize 0 feedback off
select  
    'alter tablespace '||Tablespace_Name||' end backup;'
  from DBA_TABLESPACES
where Status <> 'INVALID'
spool alter_end.sql
/
spool off

//备份归档日志文件的脚本.
REM  See text for alternatives.
#     Step 1: Stop the archiving process. This will keep
#     additional archived redo log files from being written
#     to the destination directory during this process.
#
svrmgrl <connect internal as sysdba
archive log stop;
REM
REM   Exit Server Manager using the indicator set earlier.
exit
EOFarch1
#
#     Step 2: Record which files are in the destination  
#  directory.

#     Do this by setting an environment variable that is
#  equal to the directory listing for the destination  
#  directory.
#  For this example, the log_archive_dest is
#  /db01/oracle/arch/CC1.
#
FILES=`ls /db01/oracle/arch/CC1/arch*.dbf`; export FILES
#
#     Step 3: Go back into Server Manager and restart the
#  archiving process. Set an indicator (called EOFarch2
#  in this example).
#
svrmgrl <connect internal as sysdba
archive log start;
exit
EOFarch2
#
#     Step 4. Back up the archived redo logs to the tape
#  device via the "tar" command, then delete them
#  from the destination device via the "rm" command.
#
tar -rvf /dev/rmt/0hc $FILES
#
#     Step 5. Delete those files from the destination directory.
#
rm -f $FILES
#
#     End of archived redo log file backup script.

REM  磁盘到磁盘的备份
REM
REM   Back up the RBS tablespace - to another disk (UNIX)
REM
alter tablespace RBS begin backup;
!cp /db02/oracle/CC1/rbs01.dbf /db10/oracle/CC1/backups
alter tablespace RBS end backup;
REM

REM  移动归档日志文件的shell脚本
#
# Procedure for moving archived redo logs to another device
#
svrmgrl <connect internal as sysdba
archive log stop;
!mv /db01/oracle/arch/CC1 /db10/oracle/arch/CC1
archive log start;
exit
EOFarch2
#
# end of archived redo log directory move.

//生成创建控制文件命令
alter database backup controlfile to trace;

//时间点恢复的例子
connect internal as sysdba
startup mount instance_name;
recover database until time '1999-08-07:14:40:00';

//创建恢复目录
rman rcvcat rman/rman@

// 在(UNIX)下创建恢复目录
RMAN> create catalog tablespace rcvcat;

// 在(NT)下创建恢复目录
RMAN> create catalog tablespace "RCVCAT";

//连接描述符范例  
(DESCRIPTION=
      (ADDRESS=
            (PROTOCOL=TCP)
            (HOST=HQ)
            (PORT=1521))
      (CONNECT DATA=
            (SID=loc)))

// listener.ora 的条目entry





//创建一个控制文件命令到跟踪文件
alter database backup controlfile to trace;

//增加一个新的日志文件组的语句
connect internal as sysdba
alter database
add logfile group 4
('/db01/oracle/CC1/log_1c.dbf',

'/db02/oracle/CC1/log_2c.dbf') size 5M;

alter database
add logfile member '/db03/oracle/CC1/log_3c.dbf'
to group 4;
//在Server Manager上MOUNT并打开一个数据库:
connect internal as sysdba
startup mount ORA1 exclusive;
alter database open;

//生成数据字典
@catalog
@catproc

//在init.ora 中备份数据库的位置
log_archive_dest_1 = '/db00/arch'
log_archive_dest_state_1 = enable
log_archive_dest_2 = "service=stby.world mandatory reopen=60"
log_archive_dest_state_2 = enable
//对用户的表空间的指定和管理相关的语句
create user USERNAME identified by PASSWORD
default tablespace TABLESPACE_NAME;
alter user USERNAME default tablespace TABLESPACE_NAME;
alter user SYSTEM quota 0 on SYSTEM;
alter user SYSTEM quota 50M on TOOLS;
create user USERNAME identified by PASSWORD
default tablespace DATA
temporary tablespace TEMP;
alter user USERNAME temporary tablespace TEMP;

//重新指定一个数据文件的大小 :
alter database
datafile '/db05/oracle/CC1/data01.dbf' resize 200M;

//创建一个自动扩展的数据文件:
create tablespace DATA
datafile '/db05/oracle/CC1/data01.dbf' size 200M
autoextend ON
next 10M
maxsize 250M;

//在表空间上增加一个自动扩展的数据文件:
alter tablespace DATA
add datafile '/db05/oracle/CC1/data02.dbf'
size 50M
autoextend ON
maxsize 300M;

//修改参数:
alter database
datafile '/db05/oracle/CC1/data01.dbf'
autoextend ON
maxsize 300M;

//在数据文件移动期间重新命名:
alter database rename file
'/db01/oracle/CC1/data01.dbf' to
'/db02/oracle/CC1/data01.dbf';

alter tablespace DATA rename datafile
'/db01/oracle/CC1/data01.dbf' to
'/db02/oracle/CC1/data01.dbf';

alter database rename file  
'/db05/oracle/CC1/redo01CC1.dbf' to
'/db02/oracle/CC1/redo01CC1.dbf';

alter database datafile '/db05/oracle/CC1/data01.dbf'  
resize 80M;
//创建和使用角色:
create role APPLICATION_USER;
grant CREATE SESSION to APPLICATION_USER;
grant APPLICATION_USER to username;

//回滚段的管理
create rollback segment SEGMENT_NAME

tablespace RBS;

alter rollback segment SEGMENT_NAME offline;

drop rollback segment SEGMENT_NAME;

alter rollback segment SEGMENT_NAME online;
//回滚段上指定事务
commit;
set transaction use rollback segment ROLL_BATCH;
insert into TABLE_NAME
select * from DATA_LOAD_TABLE;
commit;

//查询回滚段的 大小和优化参数
select * from DBA_SEGMENTS
where Segment_Type = 'ROLLBACK';
select N.Name,         /* rollback segment name */
       S.OptSize       /* rollback segment OPTIMAL size */
from V$ROLLNAME N, V$ROLLSTAT S
where N.USN=S.USN;

//回收回滚段
alter rollback segment R1 shrink to 15M;
alter rollback segment R1 shrink;

//例子
set transaction use rollback segment SEGMENT_NAME

alter tablespace RBS
default storage
(initial 125K next 125K minextents 18 maxextents 249)

create rollback segment R4 tablespace RBS
   storage (optimal 2250K);
alter rollback segment R4 online;

select Sessions_Highwater from V$LICENSE;
grant select on EMPLOYEE to PUBLIC;

//用户和角色  
create role ACCOUNT_CREATOR;
grant CREATE SESSION, CREATE USER, ALTER USER  
   to ACCOUNT_CREATOR;

alter user THUMPER default role NONE;
alter user THUMPER default role CONNECT;
alter user THUMPER default role all except ACCOUNT_CREATOR;

alter profile DEFAULT
limit idle_time 60;

create profile LIMITED_PROFILE limit
FAILED_LOGIN_ATTEMPTS 5;
create user JANE identified by EYRE
profile LIMITED_PROFILE;
grant CREATE SESSION to JANE;

alter user JANE account unlock;
alter user JANE account lock;

alter profile LIMITED_PROFILE limit
PASSWORD_LIFE_TIME 30;

alter user jane password expire;

//创建操作系统用户
REM  Creating OPS$ accounts
create user OPS$FARMER
identified by SOME_PASSWORD
default tablespace USERS
temporary tablespace TEMP;

REM  Using identified externally

create user OPS$FARMER
identified externally
default tablespace USERS
temporary tablespace TEMP;

//执行ORAPWD
ORAPWD FILE=filename PASSWORD=password ENTRIES=max_users

create role APPLICATION_USER;
grant CREATE SESSION to APPLICATION_USER;
create role DATA_ENTRY_CLERK;
grant select, insert on THUMPER.EMPLOYEE to DATA_ENTRY_CLERK;
grant select, insert on THUMPER.TIME_CARDS to DATA_ENTRY_CLERK;
grant select, insert on THUMPER.DEPARTMENT to DATA_ENTRY_CLERK;
grant APPLICATION_USER to DATA_ENTRY_CLERK;
grant DATA_ENTRY_CLERK to MCGREGOR;
grant DATA_ENTRY_CLERK to BPOTTER with admin option;

//设置角色
set role DATA_ENTRY_CLERK;
set role NONE;

//回收权利:
revoke delete on EMPLOYEE from PETER;
revoke all on EMPLOYEE from MCGREGOR;

//回收角色:
revoke ACCOUNT_CREATOR from HELPDESK;

drop user USERNAME cascade;

grant SELECT on EMPLOYEE to MCGREGOR with grant option;
grant SELECT on THUMPER.EMPLOYEE to BPOTTER with grant option;
revoke SELECT on EMPLOYEE from MCGREGOR;

create user MCGREGOR identified by VALUES '1A2DD3CCEE354DFA';

alter user OPS$FARMER identified by VALUES 'no way';

//备份与恢复
使用 export 程序
exp system/manager file=expdat.dmp compress=Y owner=(HR,THUMPER)
exp system/manager file=hr.dmp owner=HR indexes=Y compress=Y
imp system/manager file=hr.dmp full=Y buffer=64000 commit=Y

//备份表
exp system/manager FILE=expdat.dmp TABLES=(Thumper.SALES)
//备份分区
exp system/manager FILE=expdat.dmp TABLES=(Thumper.SALES:Part1)

//输入例子
imp system/manager file=expdat.dmp
imp system/manager file=expdat.dmp buffer=64000 commit=Y

exp system/manager file=thumper.dat owner=thumper grants=N
  indexes=Y compress=Y rows=Y
imp system/manager file=thumper.dat FROMUSER=thumper TOUSER=flower
      rows=Y indexes=Y
imp system/manager file=expdat.dmp full=Y commit=Y buffer=64000
imp system/manager file=expdat.dmp ignore=N rows=N commit=Y buffer=64000

//使用操作系统备份命令
REM  TAR examples

tar -cvf /dev/rmt/0hc /db0[1-9]/oracle/CC1
tar -rvf /dev/rmt/0hc /orasw/app/oracle/CC1/pfile/initcc1.ora
tar -rvf /dev/rmt/0hc /db0[1-9]/oracle/CC1 /orasw/app/oracle/CC1/pfile/initcc1.ora

//离线备份的shell脚本
ORACLE_SID=cc1; export ORACLE_SID
ORAENV_ASK=NO; export ORAENV_ASK
. oraenv
svrmgrl <connect internal as sysdba
shutdown immediate;
exit
EOF1
insert backup commands like the "tar" commands here
svrmgrl <connect internal as sysdba
startup
EOF2

//在Server Manager上设置为archivelog mode:
connect internal as sysdba
startup mount cc1;
alter database archivelog;
archive log start;
alter database open;

//在Server Manager上设置为archivelog mode:
connect internal as sysdba
startup mount cc1;
alter database noarchivelog;
alter database open;

select Name,
       Value
  from V$PARAMETER
where Name like 'log_archive%';

//联机备份的脚本
#
# Sample Hot Backup Script for a UNIX File System database
#
# Set up environment variables:
ORACLE_SID=cc1; export ORACLE_SID
ORAENV_ASK=NO; export ORAENV_ASK
. oraenv
svrmgrl <connect internal as sysdba
REM
REM   备份 SYSTEM tablespace
REM
alter tablespace SYSTEM begin backup;
!tar -cvf /dev/rmt/0hc /db01/oracle/CC1/sys01.dbf
alter tablespace SYSTEM end backup;
REM
REM  The SYSTEM tablespace has now been written to a
REM   tar saveset on the tape device /dev/rmt/0hc.  The
REM   rest of the tars must use the "-rvf" clause to append
REM   to that saveset.
REM
REM   备份  RBS tablespace
REM
alter tablespace RBS begin backup;
!tar -rvf /dev/rmt/0hc /db02/oracle/CC1/rbs01.dbf
alter tablespace RBS end backup;
REM
REM   备份  DATA tablespace

REM   For the purposes of this example, this tablespace
REM   will contain two files, data01.dbf and data02.dbf.
REM   The * wildcard will be used in the filename.

REM
alter tablespace DATA begin backup;
!tar -rvf /dev/rmt/0hc /db03/oracle/CC1/data0*.dbf
alter tablespace DATA end backup;
REM
REM   备份 INDEXES tablespace
REM
alter tablespace INDEXES begin backup;
!tar -rvf /dev/rmt/0hc /db04/oracle/CC1/indexes01.dbf
alter tablespace INDEXES end backup;
REM
REM   备份  TEMP tablespace
REM
alter tablespace TEMP begin backup;
!tar -rvf /dev/rmt/0hc /db05/oracle/CC1/temp01.dbf
alter tablespace TEMP end backup;
REM
REM   Follow the same pattern to back up the rest
REM   of the tablespaces.
REM
REM    
REM  Step 2.  备份归档日志文件.
archive log stop
REM
REM   Exit Server Manager, using the indicator set earlier.
exit
EOFarch1
#
#  Record which files are in the destination directory.
#     Do this by setting an environment variable that is
#  equal to the directory listing for the destination  
#  directory.
#  For this example, the log_archive_dest is  
#  /db01/oracle/arch/CC1.
#
FILES=`ls /db01/oracle/arch/CC1/arch*.dbf`; export FILES
#
#  Now go back into Server Manager and restart the
#  archiving process.  Set an indicator (called EOFarch2
#  in this example).
#
svrmgrl <connect internal
archive log start;
exit
EOFarch2
#
#  Now back up the archived redo logs to the tape
#  device via the "tar" command, then delete them
#  from the destination device via the "rm" command.
#  You may choose to compress them instead.
#
tar -rvf /dev/rmt/0hc $FILES
rm -f $FILES
#
#     Step 3.  备份控制文件到磁盘.
#
svrmgrl <connect internal
alter database backup controlfile to
   'db01/oracle/CC1/CC1controlfile.bck';

exit
EOFarch3
#
#  备份控制文件到磁带.
#
tar -rvf /dev/rmt/0hc /db01/oracle/CC1/CC1controlfile.bck
#
#  End of hot backup script.
//自动生成开始备份的脚本
set pagesize 0 feedback off
select  
    'alter tablespace '||Tablespace_Name||' begin backup;'
  from DBA_TABLESPACES
where Status <> 'INVALID'
spool alter_begin.sql
/
spool off

//自动生成备份结束的脚本
set pagesize 0 feedback off
select  
    'alter tablespace '||Tablespace_Name||' end backup;'
  from DBA_TABLESPACES
where Status <> 'INVALID'
spool alter_end.sql
/
spool off

//备份归档日志文件的脚本.
REM  See text for alternatives.
#     Step 1: Stop the archiving process. This will keep
#     additional archived redo log files from being written
#     to the destination directory during this process.
#
svrmgrl <connect internal as sysdba
archive log stop;
REM
REM   Exit Server Manager using the indicator set earlier.
exit
EOFarch1
#
#     Step 2: Record which files are in the destination  
#  directory.
#     Do this by setting an environment variable that is
#  equal to the directory listing for the destination  
#  directory.
#  For this example, the log_archive_dest is
#  /db01/oracle/arch/CC1.
#
FILES=`ls /db01/oracle/arch/CC1/arch*.dbf`; export FILES
#
#     Step 3: Go back into Server Manager and restart the
#  archiving process. Set an indicator (called EOFarch2
#  in this example).
#
svrmgrl <connect internal as sysdba
archive log start;
exit
EOFarch2
#
#     Step 4. Back up the archived redo logs to the tape
#  device via the "tar" command, then delete them

#  from the destination device via the "rm" command.
#
tar -rvf /dev/rmt/0hc $FILES
#
#     Step 5. Delete those files from the destination directory.
#
rm -f $FILES
#
#     End of archived redo log file backup script.

REM  磁盘到磁盘的备份
REM
REM   Back up the RBS tablespace - to another disk (UNIX)
REM
alter tablespace RBS begin backup;
!cp /db02/oracle/CC1/rbs01.dbf /db10/oracle/CC1/backups
alter tablespace RBS end backup;
REM

REM  移动归档日志文件的shell脚本
#
# Procedure for moving archived redo logs to another device
#
svrmgrl <connect internal as sysdba
archive log stop;
!mv /db01/oracle/arch/CC1 /db10/oracle/arch/CC1
archive log start;
exit
EOFarch2
#
# end of archived redo log directory move.

//生成创建控制文件命令
alter database backup controlfile to trace;

//时间点恢复的例子
connect internal as sysdba
startup mount instance_name;
recover database until time '1999-08-07:14:40:00';

//创建恢复目录
rman rcvcat rman/rman@

// 在(UNIX)下创建恢复目录
RMAN> create catalog tablespace rcvcat;

// 在(NT)下创建恢复目录
RMAN> create catalog tablespace "RCVCAT";

//连接描述符范例  
(DESCRIPTION=
      (ADDRESS=
            (PROTOCOL=TCP)
            (HOST=HQ)
            (PORT=1521))
      (CONNECT DATA=
            (SID=loc)))

// listener.ora 的条目entry
LISTENER =
  (ADDRESS_LIST =
        (ADDRESS=
          (PROTOCOL=IPC)
转贴于 学生大读书网 http://

(KEY= loc.world)
        )
   )  
SID_LIST_LISTENER =
  (SID_LIST =
    (SID_DESC =

(SID_NAME = loc)
      (ORACLE_HOME = /orasw/app/oracle/product/8.1.5.1)
   )
)

//  tnsnames.ora 的条目
LOC=
  (DESCRIPTION=  
   (ADDRESS =
        (PROTOCOL = TCP)
        (HOST = HQ)
        (PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = loc)
      (INSTANCE_NAME = loc)
    )
)

//连接参数的设置（sql*net）
LOC =(DESCRIPTION=
      (ADDRESS=
            (COMMUNITY=TCP.HQ.COMPANY)
            (PROTOCOL=TCP)
            (HOST=HQ)
            (PORT=1521))
      (CONNECT DATA=
            (SID=loc)))
//参数文件配置范例
// tnsnames.ora  
HQ =(DESCRIPTION=
      (ADDRESS=
            (PROTOCOL=TCP)
            (HOST=HQ)
            (PORT=1521))
      (CONNECT DATA=
            (SID=loc)))

// listener.ora  
LISTENER =
  (ADDRESS_LIST =
        (ADDRESS=
          (PROTOCOL=IPC)
          (KEY= loc)
        )
   )  
SID_LIST_LISTENER =
  (SID_LIST =
    (SID_DESC =
      (SID_NAME = loc)
      (ORACLE_HOME = /orasw/app/oracle/product/8.1.5.1)
    )
  )

// Oracle8I tnsnames.ora  
LOC=
  (DESCRIPTION=  
   (ADDRESS =
        (PROTOCOL = TCP)
        (HOST = HQ)

(PORT = 1521))
    )
    (CONNECT_DATA =
      (SERVICE_NAME = loc)
      (INSTANCE_NAME = loc)
    )
)  

//使用 COPY 实现数据库之间的复制
copy from
remote_username/remote_password@service_name
to
username/password@service_name
[append|create|insert|replace]
TABLE_NAME
using subquery;

REM  COPY example
set copycommit 1
set arraysize 1000
copy from HR/PUFFINSTUFF@loc -
create EMPLOYEE -
using -
select * from EMPLOYEE


//监视器的管理
lsnrctl start
lsnrctl start my_lsnr
lsnrctl status
lsnrctl status hq

检查监视器的进程
ps -ef | grep tnslsnr
//在 lsnrctl  内停止监视器
set password lsnr_password
stop

//在lsnrctl 内列出所有的服务
set password lsnr_password
services
//启动或停止一个NT的listener
net start OracleTNSListener
net stop OracleTNSListener

// tnsnames.ora 文件的内容
fld1 =
  (DESCRIPTION =
    (ADDRESS_LIST =
      (ADDRESS = (PROTOCOL = TCP)
      (HOST = server1.fld.com)(PORT = 1521))
    )
    (CONNECT_DATA =
      (SID = fld1)
    )
  )
//操作系统网络的管理

telnet host_name
ping host_name
/etc/hosts 文件
130.110.238.109 nmhost
130.110.238.101 txhost
130.110.238.102 azhost  arizona  
//oratab 表项
loc:/orasw/app/oracle/product/8.1.5.1:Y
cc1:/orasw/app/oracle/product/8.1.5.1:N
old:/orasw/app/oracle/product/8.1.5.0:Y 
