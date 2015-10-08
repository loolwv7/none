To create an LED trigger for incoming SSH traffic:                                                                                     
  iptables -A INPUT -p tcp --dport 22 -j LED --led-trigger-id ssh --led-delay 1000                                                     
 Then attach the new trigger to an LED on your system:                                                                                ©¦  
   echo netfilter-ssh > /sys/class/leds/<ledname>/trigger                                                                             ©¦  
 For more information on the LEDs available on your system, see                                                                       
  Documentation/leds-class.txt                          

The following example redirects TCP port 25 to port 2525:

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 25 -j REDIRECT --to-port 2525

In this example all incoming traffic on port 80 redirect to port 8123

iptables -t nat -I PREROUTING --src 0/0 --dst 192.168.1.5 -p tcp --dport 80 -j REDIRECT --to-ports 8123

http://blog.softlayer.com/2011/iptables-tips-and-tricks-port-redirection/

# Redhat multiport

-A INPUT -m state --state NEW -m tcp -p tcp -m multiport --dports 5901:5903,6001:6003 -j ACCEPT


# Firewall configuration written by system-config-firewall
# Manual customization of this file is not recommended.
*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
-A INPUT -p icmp -j ACCEPT
-A INPUT -i lo -j ACCEPT
-A INPUT -i eth1 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp -m multiport --dports 5901:5903,6001:6003 -j ACCEPT
-A INPUT -j REJECT --reject-with icmp-host-prohibited
-A FORWARD -j REJECT --reject-with icmp-host-prohibited
COMMIT


= NAT how to =
== eth0 ==
nc -vv -n -l -p 33 -w 18000 -s 192.168.8.111

== wlan0 ==
nc -vv -n -l -p 33 -s 192.168.1.101 -w 18889

== iptables rules ==
{{{
iptables -t nat -A PREROUTING -p tcp --dport 33 -j DNAT --to-destination 192.168.1.101:33
iptables -t nat -A POSTROUTING -p tcp -d 192.168.1.101 --dport 33 -j SNAT --to-source 192.168.8.111
}}}

#!/bin/sh

echo 1 > /proc/sys/net/ipv4/ip_forward

iptables -F
iptables -t nat -F
iptables -X

iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 192.168.12.77:80
iptables -t nat -A POSTROUTING -p tcp -d 192.168.12.77 --dport 80 -j SNAT --to-source 192.168.12.87

{{{

{{{
iptables -L -n -v -t nat
Chain PREROUTING (policy ACCEPT 9 packets, 2758 bytes)
 pkts bytes target     prot opt in     out     source               destination
    2   127 DNAT       tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            tcp dpt:33 to:192.168.1.101:33

Chain INPUT (policy ACCEPT 3 packets, 159 bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain OUTPUT (policy ACCEPT 2 packets, 172 bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain POSTROUTING (policy ACCEPT 2 packets, 172 bytes)
 pkts bytes target     prot opt in     out     source               destination
    0     0 SNAT       tcp  --  *      *       0.0.0.0/0            192.168.1.101        tcp dpt:33 to:192.168.8.111
}}}


iptables -t nat -L -n -v
Chain PREROUTING (policy ACCEPT 1026 packets, 136K bytes)
 pkts bytes target     prot opt in     out     source               destination         
    60  5948 NFQUEUE    tcp  --  br0    *       0.0.0.0/0  192.168.254.30      tcp dpt:80 NFQUEUE num 0

    Chain POSTROUTING (policy ACCEPT 506 packets, 49229 bytes)
     pkts bytes target     prot opt in     out     source
     destination         

     Chain OUTPUT (policy ACCEPT 19 packets, 1310 bytes)
      pkts bytes target     prot opt in     out     source
      destination   

http://www.tecmint.com/setup-linux-as-router/
https://beginlinux.com/sec_train_m/10-traincat/1310-set-up-the-bridge
