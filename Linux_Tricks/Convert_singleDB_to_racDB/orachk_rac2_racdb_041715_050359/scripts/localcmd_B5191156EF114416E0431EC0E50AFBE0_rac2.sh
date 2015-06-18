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
opatch_return_code=$($ORACLE_HOME/OPatch/opatch lsinventory -oh $ORACLE_HOME -local >/dev/null 2>&1;echo $?);if [ $opatch_return_code -eq 0 ]; then opatch_output=$($ORACLE_HOME/OPatch/opatch lsinventory -oh $ORACLE_HOME -local -bugs_fixed);opatch_output_main=$($ORACLE_HOME/OPatch/opatch lsinventory -oh $ORACLE_HOME -local|grep -wi "patch description");else opatch_output=$(cat $ORACLE_HOME/inventory/ContentsXML/comps.xml);fi;   
echo -e "$opatch_output_main\n\nexachk_patchlist_for_version_matrix\n\n$opatch_output"
echo -e "$opatch_output" >>/home/oracle/orachk/orachk_041715_050359/o_rdbms_patches_rac2_report.out
