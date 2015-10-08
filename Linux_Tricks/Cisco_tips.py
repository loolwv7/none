 Directing show Command Output to a File

 You can direct show command output to a file, either on the volatile file system, on slot0 CompactFlash memory, or on a remote server.

 The following example shows how to direct the show running-config output to a file on the volatile file system.

 switch1# show running-config > volatile:switch1-run.cfg


 The following example shows how to direct the show running-config output to a file on slot0 CompactFlash memory.

 switch2# show running-config > slot0:switch2-run.cfg


 The following example shows how to direct the show running-config output to a file on a TFTP server.

 switch3# show running-config > tftp://10.10.1.1/home/configs/switch3-run.cfg

 Preparing to copy\ldotsdone


  Use the format bootflash: command to only format the bootflash: file system. You can issue the format bootflash: command from either the switch# or the switch(boot)# prompts.

  If you issue the format bootflash: command, you must download the kickstart and system images again. 



  http://www.cisco.com/en/US/docs/storage/san_switches/mds9000/sw/rel_1_x/1_0_2/san-os/configuration/guide/SwImage.html

 Recovery from the switch(boot)# Prompt

To recover a system image using the kickstart image for a switch with a single supervisor module, follow these steps:

Step 1 Follow this step if you issued a init system command. Otherwise, skip to Step 2.

a. Change to configuration mode.

switch(boot)# config t


b. Configure the IP address of the switch's mgmt0 interface.

switch(boot)(config)# interface mgmt0


c. Enter the local IP address and the subnet mask for the switch, and press Enter.

switch(boot)(config-mgmt0)# ip address 172.16.1.2 255.255.255.0


Step 2 Issue the no shut command to enable the interface on the switch, and press Enter.

switch(boot)(config-mgmt0)# no shut


Step 3 Follow this step if you issued a init system command. Otherwise, skip to Step 4.

a. Enter the IP address of the default gateway, and press Enter.

switch(boot)(config-mgmt0)# ip default-gateway 172.16.1.1


Step 4 Exit to configuration mode.

switch(boot)(config-mgmt0)# exit


Step 5 Exit to EXEC mode:

switch(boot)(config)# exit


Step 6 Copy the system image from the required TFTP server, and press Enter.

switch(boot)# copy tftp://172.16.10.100/system-img bootflash:system-img

Trying to connect to tftp server......


Step 7 Copy the kickstart image from the required TFTP server, and press the Enter key.

switch(boot)# copy tftp://172.16.10.100/system-img bootflash:kickstart-img

Trying to connect to tftp server......


Step 8 Verify that the system and kickstart image files are copied to your bootflash: directory.

switch(boot)# dir bootflash:

total 100756

drwxrwxrwx    2 admin         1024 Fri Sep 27 17:35:13 2002 .ssh

drwxrwxrwx    2 admin         1024 Fri Sep 27 17:35:13 2002 .ssh2

-rw-r--r--    1 admin     13636096 Fri Sep 20 19:58:56 2002 kickstart-233b

-rw-rw-rw-    1 admin     13636096 Wed Sep 25 17:26:47 2002 kickstart-233d

-rw-rw-rw-    1 admin     14340096 Fri Sep 27 17:28:41 2002 kickstart-240

-rw-r--r--    1 admin     19280051 Fri Sep 20 20:02:33 2002 system-233b

-rw-rw-rw-    1 admin     19281464 Wed Sep 25 17:28:12 2002 system-233d

-rw-rw-rw-    1 admin     21917189 Fri Sep 27 17:29:51 2002 system-240

drwxr-xr-x    2 admin         3072 Tue Oct 01 10:54:18 2002 logs

-rwxr-xr-x    1 admin       636579 Mon Sep 30 05:32:42 2002 rdl

drwxr-xr-x    2 admin         1024 Mon Sep 30 05:37:55 2002 src

                         124688384 bytes total used

                         311350272 bytes free

                         459779072 bytes available


Step 9 Load the system image from the bootflash: directory:

switch(boot)# load bootflash:system-.img

Uncompressing system image: bootflash:/system.img

CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC


MDS Switch

Would you like to enter the initial configuration mode?(yes/no): yes



http://www.cisco.com/en/US/prod/collateral/ps4159/ps6409/ps4358/prod_white_paper09186a00801dc74d_ns514_Networking_Solutions_White_Paper.html
http://www.cisco.com/en/US/docs/switches/datacenter/mds9000/sw/5_2/command/reference/CR04_f.html#wp1311152



== UCS health check report ==
https://jeremywaldrop.wordpress.com/2012/04/04/cisco-ucs-powershell-health-check-report/

== System Board 0 SEL_FULLNESS ==
http://www.cyberfella.co.uk/2012/04/16/ucs-management-logs/

https://supportforums.cisco.com/discussion/11962486/system-board-0-selfullness-upper-critical-alert-100-unknown

vCenter Server, with a fault of System Board 0 SEL_FULLNESS.

This occurs when the UCS Management Log for a given blade breaches it’s own
monitoring threshold of 90% full.

To clear it, Log into UCS Manager, Equipment tab, Servers, Server n, SEL Logs
tab, and Backup or Clear the log.

Don’t forget to at least take a look at the log to make sure it hasn’t filled
due to real, unresolved hardware problems.  The SEL Log logs absolutely
everything that goes on to the extent of even logging LED’s as they turn on and
off on the equipment, so these logs fill quite quickly.

== Visual Guide to collect Tech Support files (B and C series) - Cisco ==
http://www.cisco.com/c/en/us/support/docs/servers-unified-computing/ucs-manager/115023-visg-tsfiles-00.html

== HOW TO: Upgrade Cisco UCS Manager, Fabric Interconnects, I/O Modules and
1, Before you start downloading firmware and upgrading UCS Manager and the blades, it may be a
good idea to go through some housekeeping:

a.Login to UCS Manager. Verify overall status of Fabric Interconnects, I/O
    Modules, Servers and Adapters;
b.Navigate to Admin tab, Faults, Events and Audit Log. Make sure there
         are no alerts or if they can be safely ignored;
c.Equipment tab, Fabric Interconnects, Fabric Interconnect A/B. Make
             sure you have enough space on bootflash;-Series blade server firmware ==
d.Backup your current configuration. Admin tab, All node, select Backup
Configuration, Create Backup Operation. Make sure you specify the file name and
extension, Click OK

2, Download firmware upgrade bundles from Cisco website
Downloads Home > Products > Unified Computing and Servers > Cisco UCS Infrastructure and UCS Manager Software:
a.UCS Infrastructure bundle – ucs-k9-bundle-infra.2.0.3a.A.bin
b.UCS B-Series blade server products bundle – ucs-k9-bundle-b-series.2.0.3a.B.bin
c.If you have any C-Series servers managed by UCS Manager then also download Software for the UCS C-Series rack-mount servers.
    ucs-k9-bundle-c-series.2.0.3a.C.bin

3, 


== Collect logs ==
show chassis inventory expand
show fabric-interconnect inventory expand


