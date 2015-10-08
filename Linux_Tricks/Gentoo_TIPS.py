= Gentoo TIPs =
== Choose GCC ==
{{{
brightmoon fcitx # gcc-config -l
 * gcc-config: Active gcc profile is invalid!

  [1] x86_64-pc-linux-gnu-4.6.3
  brightmoon fcitx # gcc-config x86_64-pc-linux-gnu-4.6.3
   * Switching native-compiler to x86_64-pc-linux-gnu-4.6.3 \ldots
   >>> Regenerating /etc/ld.so.cache\ldots                                                                                                    [ ok ]

    * If you intend to use the gcc from the new profile in an already
     * running shell, please remember to do:

      *   . /etc/profile

brightmoon fcitx # . /etc/profile
}}}

== Chinese输入法 ==
{{{
~# USE=-static emerge -av fcitx
# USE=static-libs emerge =app-i18n/fcitx-4.2.6.1-r2
}}}

== Ruby On Gentoo with RVM ==
http://devblog.hedtek.com/2012/04/ruby-on-gentoo-with-rvm.html

== Gentoo upgrade how to ==
https://forums.gentoo.org/viewtopic-t-807345.html


== Portage troubleshooting ==
=== Failed Running aclocal ! ===
http://wiki.gentoo.org/wiki/Known_Problems
WANT_AUTOMAKE=``1.12''

http://wiki.gentoo.org/wiki/Project:Quality_Assurance/Autotools_failures

https://wiki.gentoo.org/wiki/Troubleshooting#Dependency_graph_slot_conflicts


=== /etc/portage/package.mask is the file, or a directory of files ===
that can be used to prevent certain packages from being installed. ===
{{{
https://wiki.gentoo.org/wiki//etc/portage/package.mask
http://liyanrui.is-programmer.com/posts/1376.html
http://www.gentoo.org/doc/zh_tw/handbook/handbook-x86.xml?part=3&chap=3
}}}



=== Multiple package instances within a single package slot have been pulled ===
 * into the dependency graph, resulting in a slot conflict:
{{{
emerge --ignore-built-slot-operator-deps=y -a -uDN @world 

emerge --ignore-built-slot-operator-deps=y -uDN @world
}}}

=== Broken orphaned files: No installed package was found for the following ===
{{{
  * /usr/lib64/kde4/kcm_adobe_flash_player.so
revdep-rebuild --library '/usr/lib64/libpng14.so.14' --pretend * Configuring search environment for revdep-rebuild
}}}

=== portage - This does not look like a tar archive ===
{{{
chown -R portage:portage /usr/portage/distfiles/
chown -R portage:portage /var/tmp/portage
}}}
https://forums.gentoo.org/viewtopic-t-976072.html

== TIP_Free_up_disk_space_in_Gentoo ==
{{{
emerge --sync 
or 
eix-sync  # if you use eix.

/var/tmp: Especially /var/tmp/portage/*
}}}


http://www.gentoo-wiki.info/TIP_Free_up_disk_space_in_Gentoo#Introduction

== Optimization Gentoo ==
https://wiki.gentoo.org/wiki/Knowledge_Base:Freeing_disk_space

https://wiki.sabayon.org/?title=How_to_optimize_and_accelerate_your_system

== Usefull tools ==
http://nsat.sourceforge.net/
http://knocker.sourceforge.net

== Exchange Server certificate ==
http://davmail.sourceforge.net/advanced.html

Manually accepted server certificate hash, contains the SHA1 hash of a manually
accepted certificate (invalid or self signed) 

davmail.server.certificate.hash=39\:47\:18\:63\:BE\:73\:32\:80\:5B\:76\:B5\:6D\:2B\:D2\:34\:94\:58\:AD\:84\:B6
