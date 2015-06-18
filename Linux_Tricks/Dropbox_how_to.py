= Gentoo Dropbox How To =
== Edit /etc/conf.d/dropbox ==
Set the DROPBOX_USERS variable to your regular $USER name in /etc/conf.d/dropbox.
Below is an example showing how to do so using the text editor ed(1): 
{{{
root# DBOXUSER=your_regular_user_name
root# ed /etc/conf.d/dropbox <<q
/DROPBOX_USERS/ s/".*"/"$DBOXUSER"/p
w
q
}}}

== Starting dropbox daemon ==
{{{
┌─╼ [~ #]
└────╼  /etc/init.d/dropbox start
dropbox                | * Caching service dependencies ...    [ ok ]
dropbox                | * Starting dropbox ...
dropbox                | * Detaching to start `/opt/bin/dropbox' ... 

rc-update add dropbox default
}}}

== USE $USER to login ==
└────╼ dropbox-cli  status
正在等待与 Dropbox 帐户关联...
}}}
    
Open Browser connect following link to Validate it.
{{{
┌─╼ [~]
└────╼ dropbox-cli  start
To link this computer to a dropbox account, visit the following url:
    https://www.dropbox.com/cli_link?host_id=1d391cbd7c78927739aca4e561281b94
}}}

== Then done ==
