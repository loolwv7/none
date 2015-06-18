#!/bin/env bash
if [ -e /home/oracle/.bash_profile ]; then . /home/oracle/.bash_profile>/dev/null 2>&1;fi
export ORACLE_HOME=/u01/app/oracle/product/11.2.0/db_1
export ORACLE_SID=racdb2
export CRS_HOME=/u01/11.2.0.4/grid
export OUTPUTDIR=/home/oracle/orachk/orachk_041715_050359
export TMPDIR=/home/oracle
export RTEMPDIR=/home/oracle/.orachk
if [[ "${LD_LIBRARY_PATH:-unset}"  = "unset" ]] ; then LD_LIBRARY_PATH=""; fi
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/u01/app/oracle/product/11.2.0/db_1/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/u01/app/oracle/product/11.2.0/db_1/lib:/u01/11.2.0.4/grid/lib

#!/bin/env bash

if [ -e "/etc/profile" ] ; then . /etc/profile >/dev/null 2>&1; fi; if [ -e "$HOME/.bash_profile" ] ; then . $HOME/.bash_profile >/dev/null 2>&1; elif [ -e "$HOME/.bash_login" ] ; then . $HOME/.bash_login >/dev/null 2>&1; elif [ -e "$HOME/.profile" ] ; then . $HOME/.profile >/dev/null 2>&1; fi;set +u
. /home/oracle/set_orcl_env.sh
vm_type=`grep VM_TYPE $TMPDIR/raccheck_env.out |awk '{print $3}'`;host_type=`grep HOST_TYPE $TMPDIR/raccheck_env.out |awk '{print $3}'`;host_role=`grep HOST_ROLE $TMPDIR/raccheck_env.out |awk '{print $3}'`;if [[ -z $host_type || $host_type = BAREMETAL ]]; then not_vm=1; else not_vm=0;fi;echo $not_vm; 2>>/home/oracle/orachk/orachk_041715_050359/orachk_error.log
if [ -n "$ALVL" ]; then echo "ALVL=$ALVL" > /home/oracle/.orachk/.localcmd.val; fi
if [ -n "$rat_exitcode" ]; then exit $rat_exitcode; else exit 0;fi
