H3C 3600 
1, b

console 密码忘记了。

H3C设备认证模式默认是scheme,也就是在local-user里的用户和密码。

需要在user-interface vty 0 4接口下，输入“set authentication mode password”，然后新加的密码才生效>

<H3C>system-view

[H3C]user-interface aux 0

[H3C-ui-aux0]authentication-mode password

[H3C-ui-aux0]set authenticaton password simple 123456

只用密码的用户认证

[H3C]user-interface vty 0 4

[H3C-ui-vty0-4]authentication-mode password

[H3C-ui-vty0-4]set authentication password simple 123456




例1：用console口进行TELNET密码、命令级别设置

[H3C] user-interface vty 0 4                                                     //进入vty用户视图

[H3C-ui-vty0-4] authentication-mode password                       //在vty用户视图设置

[H3C-ui-vty0-4] set authentication password simple 123456   //设置明文密码

[H3C -ui-vty0-4]user  privilege level 3                                     //设置命令级别 

 

 例2：用console口进行TELNET用户名、密码、命令级别设置

 [H3C]user-interface vty 0 4                                                       //进入vty用户视图

 [H3C -ui-vty0-4]authentication-mode scheme                          //进行用户名称＋口令方式进行配置

 [H3C]local-user test                                                                 // 设置本地用户名为test

 [H3C -user-test]service-type telnet level 3                              //设置test用户命令级别为3

 [H3C -user-test]password simple 123456                               //设置test用户密码为123456

例3：TELNET登录后对用户test修改口令

[H3C] local-user test                                                               //进入test用户视图

[H3C -user-test]service-type telnet level 3                            //如果少此步，则不能进行口令修改

[H3C -user-test]password simple test999                             //修改test用户密码为test999


1, dis cur | begin ip route
2, ping gateway
3, tracert 8.8.8.8
4, find next
5, 


Result:
port: 16,17,18,19,20
gw:192.168.37.1
# 涓�灞�浜ゆ�㈢��缁�(VLAN)+RouterOS+澶�缃�娈�dhcp涓�缁�+���绾跨����硅�よ����规��


/ip address
add address=192.168.77.111/24  comment=WAN network=192.168.77.0 broadcast=192.168.77.255 interface=ether1
add address=10.10.0.1/24  comment=LAN network=10.10.0.0 broadcast=10.10.0.255 interface=ether2

/ip route 
add disabled=no comment="WAN Gateway" distance=1 dst-address=0.0.0.0/0 gateway=192.168.77.1 scope=30 target-scope=10

/ip pool
add name=hs-pool-1 ranges=10.10.0.10-10.10.0.254
add name="vlan3" ranges=192.168.3.10-192.168.3.253
add name="vlan6" ranges=192.168.6.10-192.168.6.253
add name="vlan8" ranges=10.0.0.2-10.0.0.200

/ip dns
set allow-remote-requests=yes cache-max-ttl=1w cache-size=10000KiB max-udp-packet-size=512 servers=208.67.222.220

/ip dhcp-server
add address-pool=hs-pool-1 authoritative=after-2sec-delay bootp-support=static disabled=no interface=ether2 lease-time=1h name=dhcp1
add name=vlan8 interface=ether2 address-pool=vlan8 authoritative=after-2sec-delay bootp-support=static 
add name=vlan6 interface=ether2 address-pool=vlan6 authoritative=after-2sec-delay bootp-support=static 
add name=vlan3 interface=ether2 address-pool=vlan3 authoritative=after-2sec-delay bootp-support=static 

/ip dhcp-server config set store-leases-disk=10m
 
/ip hotspot profile
set default dns-name="" hotspot-address=0.0.0.0 html-directory=hotspot http-cookie-lifetime=3h http-proxy=0.0.0.0:0 login-by=http-chap \
name=default rate-limit="" smtp-server=0.0.0.0 split-user-domain=no use-radius=no
add dns-name="logintest.zjsos.net" hotspot-address=10.10.0.1 html-directory=hotspot http-cookie-lifetime=1d http-proxy=0.0.0.0:0 login-by=http-chap name=hsprof1 rate-limit="" smtp-server=0.0.0.0 split-user-domain=no use-radius=no
 
/ip hotspot
add address-pool=hs-pool-1 addresses-per-mac=1 disabled=no idle-timeout=5m interface=ether2 keepalive-timeout=none name=hotspot1 profile=hsprof1
/ip hotspot user profile
set default idle-timeout=none keepalive-timeout=2m name=default shared-users=1 status-autorefresh=1m transparent-proxy=no
add address-pool=hs-pool-1 advertise=no idle-timeout=none keepalive-timeout=2m name="512k Limit" open-status-page=always rate-limit=512k/512k 
add address-pool=hs-pool-1 advertise=no idle-timeout=none keepalive-timeout=2m name="256k Limit" open-status-page=always rate-limit=256k/256k

/ip hotspot service-port set ftp disabled=no ports=21
/ip hotspot walled-garden ip add action=accept disabled=no dst-address=10.10.0.1

/ip hotspot set numbers=hotspot1 address-pool=none
/ip firewall nat add action=masquerade chain=srcnat disabled=no
 
/ip hotspot user
add disabled=no name=admin password=123 profile=default
add disabled=no name=cml password=123 profile="256k Limit" server=hotspot1
add disabled=no name=cj password=123 profile="512k Limit" server=hotspot1
add disabled=no name=wgq password=123 profile=default server=hotspot1
 
#/ip route
#add disabled=no distance=1 dst-address=0.0.0.0/0 gateway=10.10.0.2 scope=30 target-scope=10
# OR

/ip route add disabled=no dst-address=192.168.3.0/24 gateway=10.10.0.2 distance=1
/ip route add disabled=no dst-address=192.168.6.0/24 gateway=10.10.0.2 distance=1
/ip route add disabled=no dst-address=192.168.8.0/24 gateway=10.10.0.2 distance=1


# H3C 3600 setting
[H3C]interface Vlan-interface 1
[H3C-Vlan-interface8]ip address 10.10.0.2 255.255.255.0
#
[H3C] ip route 0.0.0.0 0.0.0.0 10.10.0.1
#
[H3C]dhcp-server 1 ip 10.10.0.1
[H3C]vlan 6                                 
[H3C-vlan6]port Ethernet 1/0/10 to Ethernet 1/0/12
[S5560-vlan1201]port GigabitEthernet 1/0/1 to GigabitEthernet 1/0/14


[H3C]interface Vlan-interface 6
[H3C-Vlan-interface8]ip address 192.168.6.254 255.255.255.0
[H3C]display current-configuration interface Vlan-interface 6
#
interface Vlan-interface6
ip address 192.168.6.254 255.255.255.0
dhcp-server 1
#


http://rbgeek.wordpress.com/2013/01/02/configure-mikrotik-dhcp-to-assign-ip-address-to-only-authorized-clients-2nd-method/
https://aacable.wordpress.com/2011/09/12/mikrotik-hotspot-quick-setup-guide-cli-version/
http://binaryheartbeat.blogspot.com/2014/02/setting-up-mikrotik-hotspot-with.html

/ip hotspot profile set hsprof1 use-radius=yes
/radius add service=hotspot address=127.0.0.1 secret=654321

/tool user-manager customer set admin password=654321
/tool user-manager router add ip-address=127.0.0.1 shared-secret=654321 
/tool user-manager profile limitation add name=1Mbps rate-limit-rx=1024k rate-limit-tx=1024k

/ip hotspot active print 
Flags: R - radius, B - blocked 
#    USER                                                      ADDRESS         UPTIME       SESSION-TIME-LEFT IDLE-TIMEOUT
0 R  test                                                       10.10.0.211     27s         


#http://www.marlwifi.org.nz/projects/basic-mt-hotspot
#you might want to enable logging for the hotspot and radius.
#http://wiki.mikrotik.com/wiki/Hotspot,_apply_different_limits_and_different_traffic_priorities
/system logging
add topics=hotspot action=memory
add topics=radius action=memory

#To set up a walled garden (pages people can access without authenticating), use the following command:

ip hotspot walled-garden add dst-host=www.website.com

# Bagill's ASCII Signature Generator Graffiti
http://www.bagill.com/ascii-sig.php

# http://wenku.baidu.com/view/c45ae21aed630b1c59eeb5ec.html
# http://blog.sina.com.cn/s/blog_96586f7401018x5s.html


    [H3C]di cu 
    # 
     version 5.20, Release 2202 
    # 
     sysname H3C 
    # 
     irf mac-address persistent timer 
     irf auto-update enable 
     undo irf link-delay 
    # 
     domain default enable system 
    # 
     telnet server enable 
    # 
     undo ip ttl-expires 
    # 
     dhcp-snooping 
    # 
    acl number 3000 
     rule 0 permit ip source 192.168.2.1 0 
    acl number 3001 
     rule 0 permit ip source 192.168.6.0 0.0.0.255 
    # 
    vlan 1 
     description default vlan 
    # 
    vlan 2 
     description Technology 
    # 
    vlan 3 
     description XXXX 
    # 
    vlan 4 
     description xx 
    # 
    vlan 5 
     description sssss 
    # 
    vlan 6 
     description Customer Service 
    # 
    vlan 7 
     description ssfff 
    # 
    vlan 8 
     description ssffweee 
    # 
    vlan 9           
     description ssdfsf 
    # 
    vlan 30 
     description Avaya VOIP Phone 
    # 
    vlan 40 
     description Shenzhen - IPLC - Hongkong 
    # 
    radius scheme system 
     server-type extended 
     primary authentication 127.0.0.1 1645 
     primary accounting 127.0.0.1 1646 
     user-name-format without-domain 
    # 
    domain system 
     access-limit disable 
     state active 
     idle-cut disable 
     self-service-url disable 
    # 
     public-key peer 192.168.4.254 
      public-key-code begin 
       30819F300D06092A864886F70D010101050003818D0030818902818100E8854810B9DD27CC 
       DFFA9873A201DA7D2523D9C3BF3765B9F4C8F94D698B79632FEC9EF03966F983EE78618D8D 
       87CCC737328A9BEF5D2C0077C212CA37E7FB1E236CD329C6A18EB80FCE99EB5AF550A57D49 
       A3D32D8114BC087950B2BFCA21B338A3BF7F77FC34C5531665988F7A240BC564A0C41CDA07 
       3392730C587282A7F90203010001 
      public-key-code end 
     peer-public-key end 
    # 
    traffic classifier 2 operator or 
     if-match acl 3000 
    traffic classifier 1 operator and 
     if-match acl 3001 
    # 
    traffic behavior 1 
     redirect next-hop 192.168.40.254 
    # 
    qos policy 2 
     classifier 2 behavior 1 
    qos policy 1 
     classifier 1 behavior 1 
    # 
    dhcp server ip-pool vlan2 
     network 192.168.2.0 mask 255.255.255.0 
     gateway-list 192.168.2.254 
     dns-list 202.96.134.133 8.8.8.8 
     expired day 7 
    # 
    dhcp server ip-pool vlan3 
     network 192.168.3.0 mask 255.255.255.0 
     gateway-list 192.168.3.254 
     dns-list 202.96.134.133 202.96.128.68 208.67.222.222 208.67.220.220 
    # 
    dhcp server ip-pool vlan4 
     network 192.168.4.0 mask 255.255.255.0 
     gateway-list 192.168.4.254 
     dns-list 202.96.134.133 202.96.128.68 208.67.222.222 208.67.220.220 
    # 
    dhcp server ip-pool vlan5 
     network 192.168.5.0 mask 255.255.255.0 
     gateway-list 192.168.5.254 
     dns-list 202.96.134.133 202.96.128.68 208.67.222.222 208.67.220.220 
    # 
    dhcp server ip-pool vlan6 
     network 192.168.6.0 mask 255.255.255.0 
     gateway-list 192.168.6.254 
     dns-list 208.67.222.222 208.67.220.220 8.8.8.8 4.4.4.4 
    #                
    dhcp server ip-pool vlan7 
     network 192.168.7.0 mask 255.255.255.0 
     gateway-list 192.168.7.254 
     dns-list 208.67.222.222 208.67.220.220 8.8.8.8 4.4.4.4 
    # 
    dhcp server ip-pool vlan8 
     network 192.168.8.0 mask 255.255.255.0 
     gateway-list 192.168.8.254 
     dns-list 208.67.222.222 208.67.220.220 8.8.8.8 4.4.4.4 
    # 
    dhcp server ip-pool vlan9 
     network 192.168.9.0 mask 255.255.255.0 
     gateway-list 192.168.9.254 
     dns-list 208.67.222.222 208.67.220.220 8.8.8.8 4.4.4.4 
    # 
    user-group system 
    # 
    local-user admin 
     password cipher '`7&+[]_T$CQ=^Q`MAF4<1!! 
     authorization-attribute level 3 
     service-type ssh telnet terminal 
    local-user h3c 
     password cipher OUM!K%F<+$[Q=^Q`MAF4<1!! 
     service-type telnet 
    # 
     stp enable 
    # 
    interface NULL0 
    # 
    interface LoopBack0 
     ip address 1.1.1.1 255.255.255.255 
    # 
    interface Vlan-interface1 
     ip address 192.168.1.254 255.255.255.0 
    # 
    interface Vlan-interface2 
     description Technology 
     ip address 192.168.2.254 255.255.255.0 
    # 
    interface Vlan-interface3 
     ip address 192.168.3.254 255.255.255.0 
    # 
    interface Vlan-interface4 
     ip address 192.168.4.254 255.255.255.0 
    # 
    interface Vlan-interface5 
     ip address 192.168.5.254 255.255.255.0 
    # 
    interface Vlan-interface6 
     description Customer Service 
     ip address 192.168.6.254 255.255.255.0 
    # 
    interface Vlan-interface7 
     ip address 192.168.7.254 255.255.255.0 
    # 
    interface Vlan-interface8 
     ip address 192.168.8.254 255.255.255.0 
    # 
    interface Vlan-interface9 
     ip address 192.168.9.254 255.255.255.0 
    # 
    interface Vlan-interface30 
     ip address 192.168.30.1 255.255.255.0 
    # 
    interface Vlan-interface40 
     description IPLC 
     ip address 192.168.40.253 255.255.255.240 
    # 
    interface GigabitEthernet1/0/1 
     port link-type trunk 
     port trunk permit vlan all 
    # 
    interface GigabitEthernet1/0/2 
     port link-type trunk 
     port trunk permit vlan all 
    # 
    interface GigabitEthernet1/0/3 
     port access vlan 2 
     qos apply policy 2 inbound 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/4 
     port access vlan 2 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/5 
     port access vlan 3 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/6 
     port access vlan 3 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/7 
     port access vlan 4 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/8 
     port access vlan 4 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/9 
     port access vlan 5 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/10 
     port access vlan 5 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/11 
     port access vlan 6 
     qos apply policy 1 inbound 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/12 
     port access vlan 6 
     qos apply policy 1 inbound 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/13 
     port access vlan 7 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/14 
     port access vlan 7 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/15 
     port access vlan 8 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/16 
     port access vlan 8 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/17 
     port access vlan 9 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/18 
     port access vlan 9 
     dhcp-snooping trust 
    # 
    interface GigabitEthernet1/0/19 
    # 
    interface GigabitEthernet1/0/20 
    # 
    interface GigabitEthernet1/0/21 
     port access vlan 30 
    # 
    interface GigabitEthernet1/0/22 
     port access vlan 30 
    # 
    interface GigabitEthernet1/0/23 
     port access vlan 40 
    # 
    interface GigabitEthernet1/0/24 
     port access vlan 40 
    # 
    interface GigabitEthernet1/0/25 
     shutdown        
    # 
    interface GigabitEthernet1/0/26 
     shutdown 
    # 
    interface GigabitEthernet1/0/27 
     shutdown 
    # 
    interface GigabitEthernet1/0/28 
     shutdown 
    # 
    ospf 1 
     area 0.0.0.1 
      network 192.168.40.240 0.0.0.15 
      network 192.168.2.0 0.0.0.255 
      network 192.168.3.0 0.0.0.255 
      network 192.168.4.0 0.0.0.255 
      network 192.168.5.0 0.0.0.255 
      network 192.168.6.0 0.0.0.255 
      network 192.168.7.0 0.0.0.255 
      network 192.168.8.0 0.0.0.255 
      network 192.168.9.0 0.0.0.255 
      network 172.16.0.0 0.0.0.255 
      network 192.168.30.0 0.0.0.255 
      network 172.16.100.0 0.0.0.255 
    # 
     ip route-static 0.0.0.0 0.0.0.0 192.168.1.1 
     ip route-static 4.4.4.4 255.255.255.255 192.168.40.254 description google dns 
     ip route-static 8.8.8.8 255.255.255.255 192.168.40.254 description google dns 
     ip route-static 64.4.61.215 255.255.255.255 192.168.40.254 
     ip route-static 74.125.71.94 255.255.255.255 192.168.40.254 
     ip route-static 192.168.30.112 255.255.255.255 192.168.30.254 
     ip route-static 203.208.46.146 255.255.255.255 192.168.40.254 
    # 
     snmp-agent 
     snmp-agent local-engineid 800063A2035866BA917F11 
     snmp-agent community write public 
     snmp-agent sys-info version all 
    # 
     dhcp server forbidden-ip 192.168.2.1 192.168.2.10 
     dhcp server forbidden-ip 192.168.2.200 192.168.2.254 
     dhcp server forbidden-ip 192.168.3.200 192.168.3.254 
     dhcp server forbidden-ip 192.168.4.1 192.168.4.10 
     dhcp server forbidden-ip 192.168.4.200 192.168.4.254 
     dhcp server forbidden-ip 192.168.3.1 192.168.3.10 
     dhcp server forbidden-ip 192.168.5.1 192.168.5.10 
     dhcp server forbidden-ip 192.168.5.200 192.168.5.254 
     dhcp server forbidden-ip 192.168.6.1 192.168.6.10 
     dhcp server forbidden-ip 192.168.6.200 192.168.6.254 
     dhcp server forbidden-ip 192.168.7.1 192.168.7.10 
     dhcp server forbidden-ip 192.168.7.200 192.168.7.254 
     dhcp server forbidden-ip 192.168.8.1 192.168.8.10 
     dhcp server forbidden-ip 192.168.8.200 192.168.8.254 
     dhcp server forbidden-ip 192.168.9.1 192.168.9.10 
     dhcp server forbidden-ip 192.168.9.200 192.168.9.254 
    # 
     dhcp enable 
    # 
     ssh server enable 
     ssh client source interface LoopBack0 
     ssh user admin service-type stelnet authentication-type password 
     ssh client authentication server 192.168.4.254 assign publickey 192.168.4.254 
    # 
    user-interface aux 0 8 
    user-interface vty 0 4 
     authentication-mode scheme 
     user privilege level 3 
    # 
    return 



