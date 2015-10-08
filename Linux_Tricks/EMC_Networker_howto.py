== Troubleshooting ==
=== ORA 19554 27211 ===
RMAN-03009: failure of allocate command on t1 channel at 06/16/2015 17:07:28
ORA-19554: error allocating device, device type: SBT_TAPE, device name:
ORA-27211: Failed to load Media Management Library

it is possible that the symlinks were not created during the installation.
Solve the problem by creating the required symlink:
{{{
cd $ORACLE_HOME/lib
ln -s /usr/lib/libnsrora.so libobk.so 
}}}

http://sempike.blogspot.com/2013/04/emc-networker-installation-for-oracle.html

https://community.emc.com/thread/78426

http://www.orafaq.com/forum/t/171443/80704/

https://community.emc.com/thread/119162

https://community.emc.com/thread/129585

{{{
Hi,

The error 'failed to load media management library' means that the NMO software
and Oracle have not been integrated correctly.  There are many different
possible reasons for this.  One of the more common would be that you have
installed the wrong bit-version of NMO (if Oracle is 32 bit, you need 32 bit
    NMO even if it's running on a 64 bit OS.).  If this is not it, you should
    check out the Oracle RMAN User Guide for your Oracle version which should
    have details on integrating the media management layer.  Alternatively, you
    could type the error message into a powerlink search and you will get a
    list of articles that give possible reasons for this error.

     -Bobby
}}}

=== Backup Script ===
{{{
connect target user/password@{database to be backedup};
connect rcvcat user/password@{recovery catalog};

run {
change archivelog all crosscheck;
allocate channel t0 type 'SBT_TAPE' parms 'ENV=(NSR_DATA_VOLUME_POOL=Poolname)';
allocate channel t1 type 'SBT_TAPE' parms 'ENV=(NSR_DATA_VOLUME_POOL=Poolname)';
allocate channel t2 type 'SBT_TAPE' parms 'ENV=(NSR_DATA_VOLUME_POOL=Poolname)';
allocate channel t3 type 'SBT_TAPE' parms 'ENV=(NSR_DATA_VOLUME_POOL=Poolname)';
backup full filesperset 4
format '/FULL_%d_%u/'
database
include current controlfile
;
sql 'alter system switch logfile'
;
backup
(archivelog all);

release channel t0;
release channel t1;
release channel t2;
release channel t3;

}
}}}
