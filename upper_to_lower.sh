#!/bin/sh
#
# Created by Merlyn From ChengDu
# Email:loolwv7@gmail.com
# 2011.3.30 released
#   Modified by 2011.12.03
#
#=================================

Usage(){
  echo "Usage: `basename $0` directory"
}

if [ $# -le 0 ]; then
  Usage 
  exit 1
fi

#
# main
#
for upper in `find $1 -depth`; 
  do ( mv -f $upper `echo $upper | sed 's%[^/]*$%%'``echo $upper | sed 's!.*/!!' | \
	  tr '[:upper:]' '[:lower:]'` 2>/dev/null );
	  #tr '[:lower:]' '[:upper:]'` &>/dev/null );
done
echo -e "\E[32m *** done ***"

tput sgr0
exit $?
