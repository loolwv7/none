= MUTT =

== Exchange Mail Server ==
{{{
layman -a sabayon 
echo net-mail/davmail-bin ~amd64 >> /etc/portage/package.accept_keywords
emerge davmail-bin
}}}

davmail.sh
{{{

https://wiki.debian.org/Mutt

http://blog.johanv.org/posts/old/node-206.html

http://www.emperor-it.com/techreviews/72-offlineimap-synchronisation-made-easy.html

http://donnlee.com/2010/01/22/do-you-love-mutt-use-offlineimap-fdm-and-rejoice/

http://www.bryceharrington.org/wordpress/2013/07/setting-up-mutt-and-imap-for-email-through-exchange-ews/

/opt/davmail/davmail.properties
{{{
#DavMail settings
#Wed Jun 24 21:05:34 HKT 2015
davmail.allowRemote=false
davmail.bindAddress=
davmail.caldavAlarmSound=
davmail.caldavEditNotifications=false
davmail.caldavPastDelay=90
davmail.caldavPort=1080
davmail.clientSoTimeout=
davmail.defaultDomain=
davmail.disableGuiNotifications=false
davmail.disableUpdateCheck=false
davmail.enableEws=auto
davmail.enableProxy=false
davmail.forceActiveSyncUpdate=false
davmail.imapAutoExpunge=true
davmail.imapIdleDelay=
davmail.imapPort=1143
davmail.keepDelay=30
davmail.ldapPort=1389
davmail.logFilePath=
davmail.logFileSize=
davmail.noProxyFor=
davmail.popMarkReadOnRetr=false
davmail.popPort=1110
davmail.proxyHost=
davmail.proxyPassword=
davmail.proxyPort=
davmail.proxyUser=
davmail.sentKeepDelay=90
davmail.server=false
davmail.server.certificate.hash=
davmail.showStartupBanner=true
davmail.smtpPort=1025
davmail.smtpSaveInSent=true
davmail.ssl.clientKeystoreFile=
davmail.ssl.clientKeystorePass=
davmail.ssl.clientKeystoreType=
davmail.ssl.keyPass=
davmail.ssl.keystoreFile=
davmail.ssl.keystorePass=
davmail.ssl.keystoreType=
davmail.ssl.nosecurecaldav=false
davmail.ssl.nosecureimap=false
davmail.ssl.nosecureldap=false
davmail.ssl.nosecurepop=false
davmail.ssl.nosecuresmtp=false
davmail.ssl.pkcs11Config=
davmail.ssl.pkcs11Library=
# systec mail server
davmail.url=https\://mail.systec.com.cn/ews/exchange.asmx
davmail.useSystemProxies=false
log4j.logger.davmail=DEBUG
log4j.logger.httpclient.wire=WARN
log4j.logger.org.apache.commons.httpclient=WARN
log4j.rootLogger=WARN
}}}


== Auto start ==

chmod +x /etc/init.d/davmail
{{{

#!/sbin/runscript
# Copyright 1999-2015 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

depend() {
        need net
        provide davmail
}

start() {
        ebegin "Starting DAVMAIL"
        start-stop-daemon --start --exec /opt/davmail-bin/davmail.sh \
           --pidfile /opt/davmail-bin/davmail.pid \
           --name davmail -- /opt/davmail-bin/davmail.properties

        eend $?
}

stop(){
        ebegin "Stopping DAVMAIL"
        start-stop-daemon --stop --exec /opt/davmail-bin/davmail.sh \
           --pidfile /opt/davmail-bin/davmail.pid --name davmail
        eend $?
}

}}}



http://gentoo-en.vfose.ru/wiki/DavMail

== Emacs Gnus mail ==
http://blog.binchen.org/posts/how-to-get-email-from-exchange-server-without-outlook.html#sec-1

== Mailcap open Attachment ==
http://unix.stackexchange.com/questions/65381/how-to-tell-mutt-not-to-wait-for-an-attachment-program-to-return

Every time an attempt to open an attachment is made, it's copied in a dedicated
temp directory and the copy is opened.
Every time you start mutt, any lingering copies are cleaned up.

.mailcap
{{{
application/*; mkdir -p /tmp/mutt \; cp %s /tmp/mutt \; xdg-open /tmp/mutt/$(basename %s) &
}}}

.muttrc
{{{
folder-hook . `rm -f /tmp/mutt/*`
}}}


== Pretty print ==

http://unix.stackexchange.com/questions/20456/pretty-print-mails-from-mutt

== .signature ==




http://blog.xvx.ca/
https://turanct.wordpress.com/2013/01/04/use-thunderbird-with-microsoft-exchange-through-davmail/

== Mutt builder ==

http://www.muttrcbuilder.org/
