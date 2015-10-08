
= CISCO Network =

== Configuring VLAN on a Cisco Switch.

On this page, we learn how to configure:

*   Telnet line and Password

*   Console line and Password

*   VLAN and names

*   Switch host names 

*   Delete a VLAN

*   Assigning a switch port

The following is a basic configuration of VLAN on Cisco Switch Interfaces:

Before you begin you must have worked out your IP addresses

 We are configuringVLAN ports for three departments:

VLAN 10, Name: orbit

VLAN 20, Name:cisco 

VLAN 30, Name: Student

We use the topology below as an example:

 

                              How to configure CCNA VLAN on Cisco Switch

 
Configuring Telnet line and password:

switch1#config t

Switch1(config)#enable secret cisco

Switch1(config)#line vty 0 15

Switch1(config-line)#password cisco

Switch1(config-line)#login

Switch1(config-line)#exit
 
Configuring console line and password:

Switch1(config)#line con 0

Switch1(config-line)#password cisco

Switch1(config-line)#login

Switch1(config-line)#exit
Create and Configure VLANs and Names  on Switch:

Switch1#config t

switch1(config)#vlan 10

switch1(config-vlan)#name orbit

switch1(config-vlan)#exit

switch1(config)#vlan 20

switch1(config-vlan)#name cisco

Switch11(config-vlan)#exit

Switch1(config)#vlan 30

Switch1(config-vlan)#name student

Switch1(config-vlan)#exit

Switch1(config)#exit

To view your configurations, use the show vlan command: -

Switch1#show vlan

VLAN Name                             Status    Ports

---- -------------------------------- --------- -------------------------------

1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4

                                             Fa0/5, Fa0/6, Fa0/7, Fa0/8

                                              Fa0/9, Fa0/10, Fa0/11, Fa0/12

                                              Fa0/13, Fa0/14, Fa0/15, Fa0/16

                                              Fa0/17, Fa0/18, Fa0/19, Fa0/20

                                              Fa0/21, Fa0/22, Fa0/23, Fa0/24

                                              Gig1/1, Gig1/2

10   orbit                            active   

20   cisco                            active   

30   student                          active   

1002 fddi-default                     active   

1003 token-ring-default               active   

1004 fddinet-default                  active   

005 trnet-default                    active  

<input omitted>
Switch#
 
 
How to assign a switchport to a VLAN.

After creating your VLAN, you can assign a switch port to the VLAN .

  VLAN 20, is statically assigned to port F0/8 on switch S1:

Switch1#config t

Switch1(config)#interface fa0/2

Switch1(config-if)#switchport mode access

Switch1(config-if)#switchport access vlan 20

Switch1(config-if)#no shut

Switch1(config-if)#exit

Switch1(config)#exit

Switch1#

use the above commands to assign the rest of the VLANs a switchport access.
How to delete VLANs

To delete a VLAN, use the global configuration command no vlan vlan-id to remove VLAN 20 from the switch.

e.g.

Switch1(config)#no vlan 10

Switch1(config)#end

Use the show vlan brief command to verify that VLAN 20 is no longer in the vlan.dat file.

Alternatively, the entire vlan.dat file can be deleted using the command delete flash:vlan.dat from privileged EXEC mode. After the switch is reloaded, the previously configured VLANs will no longer be present. This effectively places the switch into is "factory default" concerning VLAN configurations.



== vlan config ==
config t
vlan 192
interface range gigabitEthernet 1/0/3-6
switchport access vlan 192
exit

== Collect/redirect tech-support to TFTF/FTP/HTTP Server ==
New-core-C3560-1#show tech-support | redirect ftp://10.7.30.102/incoming/c3550
Writing incoming/c3550 

==  USERFULL COMMAND CISCO ==
ROUTER(CONFIG)# NO IP DOMAIN LOOKUP -disables domain lookup process

ROUTER# SHOW TECH-SUPPORT -generates configuration text files

ROUTER# SHOW CONTROLLERS SERIAL 0 -show dce/dte and clock rate information

ROUTER# SHOW RUN INTERFACE SERIAL 0 -shows running configuration of serial
interface

ROUTER# TERMINAL MONITOR

ROUTER# TERMINAL LENGTH 0 -show run command output without break

Router(config)# alias exec sr show run -create our own command

== compatiable ==
http://www.cisco.com/web/techdoc/ucs/interoperability/matrix/matrix.html
