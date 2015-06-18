#!/bin/ksh
#
# Set you environment here [ACC,FOP,PRD]
ENV=FOP
 
# Set your company name here
COMP=WARMETAL
 
#
# APP_HOME setting
APP_HOME=/opt/sft/${COMP}-${ENV}
 
# Change here the WAS userid, WAS group and sid if necessary
WAS_USER=wasuser
WAS_GROUP=wasgroup
WAS_PROCESSES="dmgr nodeagent Front_Server Security_Server APP_Server JMS_Server"
 
WAS_CELL="${COMP}-${ENV}.cell"
WAS_NODE_EB="${COMP}-${ENV}.AppSrv.node"
WAS_NODE_FE="${COMP}-${ENV}.AppSrv.node"
 
# Change the location of the directory in this variable of the WAS :
WAS_HOME=/opt/IBM/WebSphere/AppServer
WAS_BASE_HOME=/opt/sft/${COMP}-${ENV}/WAS_Profiles/${COMP}-${ENV}.AppSrv
WAS_BASE_DATA=/var/data/${COMP}-${ENV}/WAS
WAS_BASE_LOG=/var/log/${COMP}-${ENV}/WAS
WAS_BASE_DUMP=/var/dump/ibm/websphere/6.1/BASE
 
# Change the location of the directory in this variable of the WAS_ND :
WAS_ND_HOME=/opt/sft/${COMP}-${ENV}/WAS_Profiles/${COMP}-${ENV}.dmgr
WAS_ND_DATA=/var/data/${COMP}-${ENV}/WAS_ND
WAS_ND_LOG=/var/log/${COMP}-${ENV}/WAS_ND
WAS_ND_DUMP=/var/dump/${COMP}-${ENV}/WAS_ND
 
# Essential Homes
WAS_UPDATE_INSTALLER_HOME=/opt/IBM/UpdateInstaller
WAS_IHS_HOME=/opt/IBM/HTTPServer
 
BACKUPFILEND=${WAS_ND_DUMP}/wasbck_`date +%Y%m%d%H%M`.zip
BACKUPFILEBASE=${WAS_BASE_DUMP}/wasbck_`date +%Y%m%d%H%M`.zip
 
case "$1" in
 
start )
  echo "Starting the Network Deployment Manager"
  su - $WAS_USER $WAS_ND_HOME/bin/startManager.sh
 
  echo "Starting the Node"
  su - $WAS_USER $WAS_BASE_HOME/bin/startNode.sh
 
  for server in Front Security APP JMS; do
    echo "Starting server $server"
    su - $WAS_USER ${ALLSHARE_HOME}/WAS_Profiles/${COMP}-${ENV}.AppSrv/bin/startServer.sh ${server}_Server
  done
  su - $WAS_USER ${ALLSHARE_HOME}/WAS_Profiles/${COMP}-${ENV}.AppSrv/bin/startServer.sh Monitoring_server
 ;;
 
stop )
  echo "Stopping the Network Deployment Manager"
  su - $WAS_USER $WAS_ND_HOME/bin/stopManager.sh
 
  echo "Stopping the Node"
  su - $WAS_USER $WAS_BASE_HOME/bin/stopNode.sh -stopservers
  su - $WAS_USER ${ALLSHARE_HOME}/WAS_Profiles/${COMP}-${ENV}.AppSrv/bin/stopServer.sh Monitoring_server
 ;;
 
start-node )
  echo "Starting the Node"
  su - $WAS_USER $WAS_BASE_HOME/bin/startNode.sh
 ;;
 
stop-node )
  echo "Stopping the Node"
  su - $WAS_USER $WAS_BASE_HOME/bin/stopNode.sh -stopservers
  su - $WAS_USER ${APP_HOME}/WAS_Profiles/${COMP}-${ENV}.AppSrv/bin/stopServer.sh Monitoring_server
 ;;
 
start-dmgr )
  echo "Starting the Network Deployment Manager"
  su - $WAS_USER $WAS_ND_HOME/bin/startManager.sh
 ;;
 
stop-dmgr )
  echo "Stopping the Network Deployment Manager"
  su - $WAS_USER $WAS_ND_HOME/bin/stopManager.sh
 ;;
 
start-all )
  for server in JMS APP Security Front; do
    echo "Starting server $server"
    su - $WAS_USER ${APP_HOME}/WAS_Profiles/${COMP}-${ENV}.AppSrv/bin/startServer.sh ${server}_Server
  done
  su - $WAS_USER ${APP_HOME}/WAS_Profiles/${COMP}-${ENV}.AppSrv/bin/startServer.sh Monitoring_server
;;
 
stop-all )
  for server in Front Security APP JMS; do
    echo "Stopping server $server"
    su - $WAS_USER ${APP_HOME}/WAS_Profiles/${COMP}-${ENV}.AppSrv/bin/stopServer.sh ${server}_Server
  done
;;
 
backup )
  for profile in dmgr AppSrv; do
    su - $WAS_USER ${APP_HOME}/WAS_Profiles/${COMP}-${ENV}.${profile}/bin/backupConfig.sh \
      /var/backup/${COMP}-${ENV}/was/was-config-${profile}-`date +%Y%m%d`.zip \
      -nostop \
      -logfile /var/backup/${COMP}-${ENV}/was/was-config-${profile}-`date +%Y%m%d`.log \
      -profileName ${COMP}-${ENV}.${profile}
done
;;
 
restore )
  if [ -f /var/backup/${COMP}-${ENV}/was/was-config-dmgr-${2}.zip -a -f /var/backup/${COMP}-${ENV}/was/was-config-AppSrv-${2}.zip ]; then
    for profile in dmgr AppSrv; do
      su - $WAS_USER /opt/sft/${COMP}-${ENV}/WAS_Profiles/${COMP}-${ENV}.${profile}/bin/restoreConfig.sh \
        /var/backup/${COMP}-${ENV}/was/was-config-${profile}-`date +%Y%m%d`.zip \
        -logfile /var/backup/${COMP}-${ENV}/was/was-config-${profile}-`date +%Y%m%d`.log \
        -profileName ${COMP}-${ENV}.${profile}
    done
  else
     if [ ! "$2" = "" ]; then
       echo "Cannot find or read (all) backup files, searching for:"
       echo /var/backup/${COMP}-${ENV}/was/was-config-dmgr-${2}.zip
       echo /var/backup/${COMP}-${ENV}/was/was-config-AppSrv-${2}.zip
       echo
     else
       echo "Please specify the date (YYYYMMDD) to restore as argument"
       echo "Available dates currently under backup:"
       ls -1 /var/backup/${COMP}-${ENV}/was/was-config-*.zip | awk -F - '{ print $5 }' | \
       sed 's/.zip//g' | sort | uniq
       echo
     fi
    exit 1
  fi
;;
 
status )
for i in $WAS_PROCESSES; do
    unset pid
    pid=`ps -ef|grep $i| grep</

http://www.getshifting.com/wiki/webspherestartup
