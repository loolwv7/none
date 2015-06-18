#!/bin/env bash
if [ -e /home/oracle/.bash_profile ]; then . /home/oracle/.bash_profile>/dev/null 2>&1;fi
export CRS_HOME=/u01/11.2.0.4/grid
export OUTPUTDIR=/home/oracle/orachk/orachk_041715_050359
export TMPDIR=/home/oracle
export RTEMPDIR=/home/oracle/.orachk
export ORACLE_SID=
export ORACLE_HOME=/u01/app/oracle/product/11.2.0.4/db_1
if [[ "${LD_LIBRARY_PATH:-unset}"  = "unset" ]] ; then LD_LIBRARY_PATH=""; fi
LD_LIBRARY_PATH=/u01/app/oracle/product/11.2.0.4/db_1/lib:${LD_LIBRARY_PATH}:/u01/app/oracle/product/11.2.0/db_1/lib
export LD_LIBRARY_PATH=/u01/app/oracle/product/11.2.0.4/db_1/lib:${LD_LIBRARY_PATH}:/u01/app/oracle/product/11.2.0/db_1/lib

#!/bin/env bash

if [ -e "/etc/profile" ] ; then . /etc/profile >/dev/null 2>&1; fi; if [ -e "$HOME/.bash_profile" ] ; then . $HOME/.bash_profile >/dev/null 2>&1; elif [ -e "$HOME/.bash_login" ] ; then . $HOME/.bash_login >/dev/null 2>&1; elif [ -e "$HOME/.profile" ] ; then . $HOME/.profile >/dev/null 2>&1; fi;set +u
. /home/oracle/set_orcl_env.sh
nm $ORACLE_HOME/bin/oracle | grep  -i 'getevents@@LIBAIO'|wc -l
if [ -n "$ALVL" ]; then echo "ALVL=$ALVL" > /home/oracle/.orachk/.localcmd.val; fi
if [ -n "$rat_exitcode" ]; then exit $rat_exitcode; else exit 0;fi
