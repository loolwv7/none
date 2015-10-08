#!/bin/sh
# put other system startup commands here, the boot process will wait until they complete.
# Use bootlocal.sh for system startup commands that can run in the background 
# and therefore not slow down the boot process.
/usr/bin/sethostname systec
echo “booting” > /etc/sysconfig/noautol
/opt/bootlocal.sh &
