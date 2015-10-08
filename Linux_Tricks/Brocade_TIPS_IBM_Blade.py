http://community.brocade.com/t5/Fibre-Channel-SAN/problem-with-module-for-IBM-bladecenter/td-p/14399
http://community.brocade.com/t5/Fibre-Channel-SAN/Swap-configuration-port-Dynamic-POD/td-p/26750

nys23bb89:USERID> configure

Configure...

  Fabric parameters (yes, y, no, n): [no] yes

    Domain: (1..239) [1] 101
    R_A_TOV: (4000..120000) [10000] 
    E_D_TOV: (1000..5000) [2000] 
    WAN_TOV: (0..30000) [0] 
    MAX_HOPS: (7..19) [7] 
    Data field size: (256..2112) [2112] 
    Sequence Level Switching: (0..1) [0] 
    Disable Device Probing: (0..1) [0] 
    Suppress Class F Traffic: (0..1) [0] 
    Switch PID Format: (1..2) [1] 
    Per-frame Route Priority: (0..1) [0] 
    Long Distance Fabric: (0..1) [0] 
    BB credit: (1..27) [16] 

  Insistent Domain ID Mode (yes, y, no, n): [no] 
  Virtual Channel parameters (yes, y, no, n): [no] 
  Zoning Operation parameters (yes, y, no, n): [no] 
  RSCN Transmission Mode (yes, y, no, n): [no] 
  Arbitrated Loop parameters (yes, y, no, n): [no] 
  System services (yes, y, no, n): [no] 
  Portlog events enable (yes, y, no, n): [no] 
  ssl attributes (yes, y, no, n): [no] 
  http attributes (yes, y, no, n): [no] 
  snmp attributes (yes, y, no, n): [no] 
  rpcd attributes (yes, y, no, n): [no] 
  cfgload attributes (yes, y, no, n): [no] 
  webtools attributes (yes, y, no, n): [no] 



WARNING: The domain ID will be changed. The port level zoning may be affected

nys23bb89:USERID> switchName  BladeE_FC_SW02
Committing configuration...
Done.
BladeE_FC_SW02:USERID>

BladeE_FC_SW02:USERID> switchEnable
BladeE_FC_SW02:USERID> switchShow

BladeE_FC_SW02:USERID> msPlMgmtDeactivate
Switch is in Offline state.

BladeE_FC_SW02:USERID> interopMode
InteropMode: Off

Usage: InteropMode 0|1
         0: to turn it off
         1: to turn it on
BladeE_FC_SW02:USERID> interopMode 1
The switch effective configuration will be lost when the operating mode is changed; do you want to continue? (yes, y, no, n): [no] yes
Interopmode is enabled

Note: It is recommended that you reboot this switch for the new change to take effect.
BladeE_FC_SW02:USERID> fastBoot


Broadcast message from root (pts/0) Wed Aug  1 11:02:57 2001...

The system is going down for reboot NOW !!



BladeE_FC_SW02:USERID> portcfgpersistentenable 15
BladeE_FC_SW02:USERID> switchshow
switchName:	BladeE_FC_SW02
switchType:	37.1
switchState:	Online   
switchMode:	Native
switchRole:	Principal
switchDomain:	107
switchId:	fffc6b
switchWwn:	10:00:00:05:1e:05:9c:df
zoning:	        OFF
switchBeacon:	OFF

Area Port Media Speed State 
==============================
  0   0   id    N4   No_Light  
  1   1   cu    N4   Online    F-Port  21:00:00:24:ff:2b:e9:15
  2   2   cu    N4   Online    F-Port  21:01:00:1b:32:b7:fe:50
  3   3   cu    N4   Online    F-Port  10:00:00:00:c9:b6:0b:85
  4   4   cu    N4   Online    F-Port  10:00:00:00:c9:b6:15:6f
  5   5   cu    N4   Online    F-Port  10:00:00:90:fa:49:8d:bb
  6   6   cu    N4   Online    F-Port  10:00:00:90:fa:49:aa:bf
  7   7   cu    AN   No_Sync   
  8   8   cu    N4   Online    F-Port  21:00:00:24:ff:59:f5:b5
  9   9   cu    N4   Online    F-Port  21:00:00:24:ff:59:f5:c3
 10  10   cu    N4   Online    F-Port  21:00:00:24:ff:59:f5:91
 11  11   cu    AN   No_Sync   
 12  12   cu    AN   No_Sync   
 13  13   cu    AN   No_Sync   
 14  14   cu    AN   No_Sync   
 15  15   id    N4   Online    E-Port  segmented,(FCSW version incompat)
 16  16   --    N4   No_Module Disabled (Persistent)
 17  17   --    N4   No_Module Disabled (Persistent)
 18  18   --    N4   No_Module Disabled (Persistent)
 19  19   --    N4   No_Module Disabled (Persistent)
BladeE_FC_SW02:USERID> portcfgpersistentenable 
Slot 0     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15 
---------+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---
Enabled   YES YES YES YES YES YES YES YES YES YES YES YES YES YES YES YES 

Slot 0    16  17  18  19 
---------+---+---+---+---
Enabled    -   -   -   -  


