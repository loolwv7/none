= Brocade's how to =
== Configure zones/cfg ==

1, New alias for HOST.

alicreate "DS3400_A1","20:24:00:a0:b8:5a:f6:c9"
alicreate "DS3400_A2","20:34:00:a0:b8:5a:f6:c9"

alicreate "BCE1_HBA1","21:00:00:1B:32:90:A3:E0"
alicreate "BCE1_HBA2","21:01:00:1B:32:B0:A3:E0"
alicreate "BCE2_HBA1","21:00:00:1B:32:90:3B:E0"
alicreate "BCE2_HBA2","21:01:00:1B:32:B0:3B:E0"


alicreate "BLADE1_HBA2","10:00:00:00:c9:cb:79:b1"
alicreate "BLADE2_HBA2","10:00:00:00:c9:cb:79:5b"
alicreate "BLADE3_HBA2","21:00:00:24:ff:43:16:ef"
alicreate "BLADE4_HBA2","10:00:00:00:c9:cb:a0:29"
alicreate "BLADE5_HBA2","10:00:00:00:c9:cb:a0:9f"
alicreate "BLADE6_HBA2","10:00:00:90:fa:2b:4e:bb"
alicreate "BLADE7_HBA2","10:00:00:90:fa:2b:4f:79"
alicreate "BLADE8_HBA2","10:00:00:90:fa:2b:4e:09"
alicreate "BLADE9_HBA2","10:00:00:90:fa:2b:4d:cd"
alicreate "BLADE10_HBA2","21:00:00:24:ff:41:46:c1"

alicreate "node01","10:00:00:90:fa:2b:4e:ba"
alicreate "node02","10:00:00:90:fa:2b:4f:78"

alicreate "H3CAS01","20:00:00:90:fa:3e:0d:82"
alicreate "H3CAS02","20:00:00:90:fa:3e:0c:1c"
alicreate "H3CAS03","20:00:00:90:fa:1c:64:98"
alicreate "H3CAS04","20:00:00:90:fa:1c:5a:4e"
#
alicreate "BLADE1_HBA1","10:00:00:00:c9:cb:79:b0"
alicreate "BLADE2_HBA1","10:00:00:00:c9:cb:79:5a"
alicreate "BLADE3_HBA1","21:00:00:24:ff:43:16:ee"
alicreate "BLADE4_HBA1","10:00:00:00:c9:cb:a0:28"
alicreate "BLADE5_HBA1","10:00:00:00:c9:cb:a0:9e"
alicreate "BLADE6_HBA1","10:00:00:90:fa:2b:4e:ba "
alicreate "BLADE7_HBA1","10:00:00:90:fa:2b:4f:78"
alicreate "BLADE8_HBA1","10:00:00:90:fa:2b:4e:08"
alicreate "BLADE9_HBA1","10:00:00:90:fa:2b:4d:cc"
alicreate "BLADE10_HBA1","21:00:00:24:ff:41:46:c0"

alicreate "R9300_B2","21:00:00:d0:23:10:00:01"

alicreate "N3400_A1","50:0a:09:81:88:2a:60:73"
alicreate "N3400_A2","50:0a:09:82:88:2a:60:73"
alicreate "N3400_B1","50:0a:09:81:98:2a:60:73"
alicreate "N3400_B2","50:0a:09:82:98:2a:60:73"

alicreate "V7000_A1","50:05:07:68:02:15:8b:8f"
alicreate "V7000_A3","50:05:07:68:02:35:8b:8f"
alicreate "V7000_B1","50:05:07:68:02:15:8b:90"
alicreate "V7000_B3","50:05:07:68:02:35:8b:90"

2, add New HBAs to zone.

zonecreate "BCE1_HBA1_TO_Storage","BCE1_HBA1;N3400_A1;N3400_A2;N3400_B1;N3400_B2"
zonecreate "BCE1_HBA2_TO_Storage","BCE1_HBA2;N3400_A1;N3400_A2;N3400_B1;N3400_B2"
zonecreate "BCE2_HBA1_TO_Storage","BCE2_HBA1;N3400_A1;N3400_A2;N3400_B1;N3400_B2"
zonecreate "BCE2_HBA2_TO_Storage","BCE2_HBA2;N3400_A1;N3400_A2;N3400_B1;N3400_B2"

zonecreate "BLADE1_P1_TO_Storage","BLADE1_HBA1;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE2_P1_TO_Storage","BLADE2_HBA1;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE3_P1_TO_Storage","BLADE3_HBA1;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE4_P1_TO_Storage","BLADE4_HBA1;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE5_P1_TO_Storage","BLADE5_HBA1;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE6_P1_TO_Storage","BLADE6_HBA1;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE7_P1_TO_Storage","BLADE7_HBA1;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE8_P1_TO_Storage","BLADE8_HBA1;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE9_P1_TO_Storage","BLADE9_HBA1;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE10_P1_TO_Storage","BLADE10_HBA1;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"

zonecreate "BLADE1_P2_TO_Storage","BLADE1_HBA2;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE2_P2_TO_Storage","BLADE2_HBA2;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE3_P2_TO_Storage","BLADE3_HBA2;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE4_P2_TO_Storage","BLADE4_HBA2;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE5_P2_TO_Storage","BLADE5_HBA2;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE6_P2_TO_Storage","BLADE6_HBA2;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE7_P2_TO_Storage","BLADE7_HBA2;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE8_P2_TO_Storage","BLADE8_HBA2;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE9_P2_TO_Storage","BLADE9_HBA2;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"
zonecreate "BLADE10_P2_TO_Storage","BLADE10_HBA2;N3400_A1;N3400_A2;N3400_B1;N3400_B2;V7000_A3;V7000_B1;V7000_A1;V7000_B3;R9300_B2"

zonecreate "node01_TO_v7000","node01;V7000_A1;V7000_B1;V7000_A3;V7000_B3"
zonecreate "node02_TO_v7000","node02;V7000_A1;V7000_B1;V7000_A3;V7000_B3"

3, create CFG
cfgcreate
"cfgport","BLADE1_P1_TO_Storage;BLADE2_P1_TO_Storage;BLADE3_P1_TO_Storage;BLADE4_P1_TO_Storage;BLADE5_P1_TO_Storage;BLADE6_P1_TO_Storage;BLADE7_P1_TO_Storage;BLADE8_P1_TO_Storage;BLADE9_P1_TO_Storage;BLADE10_P1_TO_Storage;BLADE1_P2_TO_Storage;BLADE2_P2_TO_Storage;BLADE3_P2_TO_Storage;BLADE4_P2_TO_Storage;BLADE5_P2_TO_Storage;BLADE6_P2_TO_Storage;BLADE7_P2_TO_Storage;BLADE8_P2_TO_Storage;BLADE9_P2_TO_Storage;BLADE10_P2_TO_Storage;node01_TO_v7000;node02_TO_v7000;H3CAS01_TO_Storrage;H3CAS02_TO_Storrage;H3CAS03_TO_Storrage;H3CAS04_TO_Storrage;BCE1_HBA1_TO_Storage;BCE1_HBA2_TO_Storage;BCE2_HBA1_TO_Storage;BCE2_HBA2_TO_Storage"

4, enable CFG
cfgenable cfgport
IBM_2498_B24:admin> switchname IBM_B24_02
Committing configuration...
Done.

== Configure Domain ID ==
{{{
IBM_B24_02:admin> ipaddrs
ipaddrset   ipaddrshow  
IBM_B24_02:admin> ipaddrset  
Ethernet IP Address [10.77.77.77]:172.20.101.57
Ethernet Subnetmask [255.255.255.0]:255.255.255.126
bad IP mask
Ethernet Subnetmask [255.255.255.0]:255.255.255.128
Gateway IP Address [none]:172.20.101.126
DHCP [Off]:

IBM_B24_02:admin> switchdisable 
IBM_B24_02:admin> switchshow
switchName: IBM_B24_02
switchType: 71.2
switchState:    Offline  
switchMode: Native
switchRole: Disabled
switchDomain:   1 (unconfirmed)
switchId:   fffc01
switchWwn:  10:00:50:eb:1a:09:40:52
zoning:     OFF
switchBeacon:   OFF

IBM_B24_02:admin> configure
Configure...
Fabric parameters (yes, y, no, n): [no] yes
Domain: (1..239) [1] 2

IBM_B24_02:admin> switchenable



IBM_B24_02:admin> switchshow
switchName:	IBM_B24_02
switchType:	71.2
switchState:	Online   
switchMode:	Native
switchRole:	Subordinate
switchDomain:	2
switchId:	fffc02
switchWwn:	10:00:50:eb:1a:09:40:52
zoning:		ON (ZONE_CONFIG)
switchBeacon:	OFF

Index Port Address Media Speed State     Proto
==============================================
  0   0   020000   id    N8   Online      FC  E-Port  10:00:00:05:33:f9:ff:fb "BladeH_BR_02" (downstream)
  1   1   020100   id    N8   Online      FC  F-Port  50:05:07:68:02:35:8b:8f 
  2   2   020200   id    N8   Online      FC  F-Port  50:05:07:68:02:15:8b:90 
  3   3   020300   id    N2   Online      FC  F-Port  21:00:00:d0:23:10:00:01 
  4   4   020400   id    N8   Online      FC  E-Port  10:00:00:05:33:d3:4a:3e "brocade8Gb_1" (upstream)
  5   5   020500   id    N8   No_Light    FC  
  6   6   020600   id    N4   Online      FC  F-Port  50:0a:09:82:88:2a:60:73 
  7   7   020700   id    N4   Online      FC  F-Port  50:0a:09:82:98:2a:60:73 
  8   8   020800   id    N8   No_Light    FC  
  9   9   020900   id    N8   No_Light    FC  
}}}



http://community.brocade.com/t5/User-Contributed/How-To-Configure-Interoperability-in-Mixed-Fabric-with-Brocade/ta-p/36382
