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
