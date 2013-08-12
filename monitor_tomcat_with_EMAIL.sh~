#! /bin/bash
#
# ---------------------------------
# Monitor TOMCAT server status.
# Create by Merlyn [][]
# Made in Wenzhou: 07/27 2013
# Modified by 08-08 2013
# ---------------------------------
# 
# 通过curl获取正常网页内容中的"关键字"来诊断网站能否提供正常服务，
#+同时对当天的日志文件中的相关“错误信息”进行查找，以确定问题，
#+然后尝试自动恢复tomcat服务，并发送Email告知管理员。
#
# -------------------------------------------------------------

LOGFILE="/var/log/tomcat/catalina.`date +%F`.log"

if [ -e ${LOGFILE} ]; then
  cat ${LOGFILE} >> ${LOGFILE}.bak
fi

SERVER_IP="www.zjpy.gov.cn"
KEYWORD="走进平阳"
TEST=$(curl ${SERVER_IP} 2>&1 | grep -m 1 -oh ${KEYWORD})
OOME=$(tail -100 ${LOGFILE} | egrep -m 1 -oh -i 'OutOfMemoryError|to prevent a memory leak')

if  [ ! -z '$TEST' ]; then 
	echo " Tomcat is OK. `date +%F_%T`" >> /tmp/tomcat_status.log
else
	echo "Warning!!! Tomcat isn't running?? Please CHECK IT IMMEDIATELY!!! `date +%F_%T`" >> /tmp/tomcat_status.log
	echo "警告，服务器'$SERVER_IP'运行不正常，请立刻检查!  `date +%F_%T`" | mutt -s "温州市平阳县电子政务服务器网站警告!" loolwv7@gmail.com

	if [ ! -z '$OOME' ]; then 
		/etc/init.d/tomcat restart
	sleep 33
                echo "" > ${LOGFILE}
		echo "注意，报'$OOME错误'! 已尝试自动重启tomcat服务，请检查服务器'$SERVER_IP'的情况!!!  `date +%F_%T`" >> /tmp/tomcat_status.log
		echo "注意，报'$OOME错误'! 已尝试自动重启tomcat服务，请检查服务器'$SERVER_IP'的情况!!!  `date +%F_%T`" | mutt -s "温州市平阳县电子政务服务器网站错误!" loolwv7@gmail.com
	fi
fi
