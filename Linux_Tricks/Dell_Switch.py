
Commands used to create VLANs on a Dell PowerConnect 8024

*********************
To display current VLAN information:

top_switch> enable
top_switch # show vlan


*********************
Set the CLI to configuration mode and defines VLAN:

top_switch # configure
top_switch(config)# vlan database
top_switch(config-vlan)# vlan 101-102, 310
top_switch(config-vlan)# exit


*********************
Setting the port to an access VLAN port in VLAN 101 This means that the Ethernet traffic on this port will be untagged and all the traffic will be in VLAN 101. “GVRP enable” sets the port to dynamically register and de-register VLAN membership information with the MAC networking switches attached to the same segment:

top_switch(config)# interface Ethernet 1/xg1
top_switch(config)# switchport access vlan 101
top_switch(config-if-1/xg1)# gvrp enable
top_switch(config-if-1/xg1)# exit


*********************
Setting the port to an access VLAN port in VLAN 102 This means that the Ethernet traffic on this port will be untagged and all the traffic will be in VLAN 102:

top_switch(config)# interface Ethernet 1/xg2
top_switch(config-if-1/xg2)# switchport access vlan 102
top_switch(config-if-1/xg2)# gvrp enable
top_switch(config-if-1/xg2)# exit


*********************
Setting the port to an access VLAN port in VLAN 310 This means that the Ethernet traffic on this port will be untagged and all the traffic will be in VLAN 310:

top_switch(config)# interface range Ethernet 1/xg3-1/xg16
top_switch(config-if)# switchport access vlan 310
top_switch(config-if)# gvrp enable
top_switch(config-if)# exit


*********************
To set the port type to an 802.1Q VLAN (to allow multiple tagged VLANs) use the “switchport mode general” command. Also, remove the port membership from VLAN 1 (all ports are in VLAN 1 by default) by using “switchport mode general allowed vlan remove 1” command:

top_switch(config)# interface ethernet 1/xg20
top_switch(config-if-1/xg20)# switchport mode general
top_switch(config-if-1/xg20)# switchport general allowed vlan add 101,102-310
top_switch(config-if-1/xg20)# switchport general allowed vlan remove vlan 1
top_switch(config-if-1/xg20)# gvrp enable
top_switch(config-if-1/xg20)# exit
top_switch(config)# gvrp enable
top_switch(config)# end


*********************
Displaying interface status:

top_switch# show interfaces switchport ethernet 1/xg1
top_switch# show interfaces switchport ethernet 1/xg2
top_switch# show interfaces switchport ethernet 1/xg20
top_switch# show vlan


*********************
Removing the ports from the VLANS and disabling gvrp:

top_switch(config)# interface ethernet 1/xg20
top_switch(config-if-1/xg20)# switchport general allowed vlan remove 101-102,310
top_switch(config-if-1/xg20)# no gvrp enable
top_switch(config)# exit
top_switch(config)# interface ethernet 1/xg1
top_switch(config-if-1/xg1)# switchport access vlan 1
top_switch(config-if-1/xg1)# no gvrp enable
top_switch(config-if-1/xg1)# exit
top_switch(config)# interface Ethernet 1/xg2
top_switch(config-if-1/xg2)# switchport access vlan 1
top_switch(config-if-1/xg2)# no gvrp enable
top_switch(config-if-1/xg2)# exit
top_switch(config)# interface range ethernet 1/xg3-1/xg16
top_switch(config-if)# switchport access vlan 1
top_switch(config-if)# no gvrp enable
top_switch(config-if)# exit
top_switch(config)# vlan database
top_switch(config-vlan)# no vlan 101-102,310
top_switch(config-vlan)# end
top_switch(config)# no gvrp enable
top_switch(config)# exit
top_switch(config)# show vlan

