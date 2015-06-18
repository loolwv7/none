= webex on Linux 64bit =
== Fist method! ==
 * install strace 
{{{
emerge strace
}}}

In the below command I’m tracing webex and outputting trace information to files webex.$pid 
where $pid is each individual thread process id.
{{{
strace -ff -t -p `ps -ef|awk '/java/ && !/grep/ { print $2 }'` -o webex
}}}

Let’s search for open system call
{{{
grep open webex.*
}}}

Then install missing libs*.

== Method two ==
=== install 32bit firefox & jre ===

Create webex directory then copy firefox&jre to that directory

tree -L 1 /usr/local/share/webex/
{{{
tree -L 1 /usr/local/share/webex/
/usr/local/share/webex/
├── env.sh
├── firefox
└── jre1.8.0_45

tree -L 1 /usr/local/share/webex/firefox/plugins/
/usr/local/share/webex/firefox/plugins/
├── libjavaplugin.so -> /usr/local/share/webex/jre1.8.0_45/lib/i386/libnpjp2.so
└── libnpjp2.so -> /usr/local/share/webex/jre1.8.0_45/lib/i386/libnpjp2.so
}}}

Make an script to launch webex for conveniency. 
{{{
cat /usr/bin/webex
#! /bin/bash

cd /usr/local/share/webex/
. env.sh
./firefox/firefox
}}}

 * Do not forget make WEBEX as home page.



http://www.emsperformance.net/2013/03/25/making-webex-work-on-64bit-fedora-core-18/

http://linuxsagas.digitaleagle.net/2011/11/10/webex-in-fedora-15-64-bit/

http://askubuntu.com/questions/301146/how-do-i-get-webex-fully-working-with-ubuntu-12-04

https://forums.opensuse.org/showthread.php/485165-Firefox-and-Webex/page2
