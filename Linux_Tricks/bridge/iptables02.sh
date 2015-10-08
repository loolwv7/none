#! /bin/bash
#iptables -A FORWARD -i br0 -o  eth3 -j ACCEPT
iptables -t nat -A PREROUTING -i br0 -p tcp -d 192.168.254.30 --dport 80 -j DNAT --to-destination 192.168.0.30:8080
iptables -t nat -A POSTROUTING  -o br0 -p tcp  -d 192.168.0.30 -j SNAT --to-source 192.168.254.30
