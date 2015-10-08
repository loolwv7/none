#! /bin/bash


## interface facing clients
CLIENT_IFACE=eth1

## interface facing Internet
INET_IFACE=eth0


ebtables -t broute -A BROUTING \
        -i $CLIENT_IFACE -p ipv6 --ip6-proto tcp --ip6-dport 80 \
        -j redirect --redirect-target DROP

ebtables -t broute -A BROUTING \
        -i $CLIENT_IFACE -p ipv4 --ip-proto tcp --ip-dport 80 \
        -j redirect --redirect-target DROP

ebtables -t broute -A BROUTING \
        -i $INET_IFACE -p ipv6 --ip6-proto tcp --ip6-sport 80 \
        -j redirect --redirect-target DROP

ebtables -t broute -A BROUTING \
        -i $INET_IFACE -p ipv4 --ip-proto tcp --ip-sport 80 \
        -j redirect --redirect-target DROP

iptables -t nat -A PREROUTING -i br0 -p tcp -d 192.168.254.30 --dport 80 -j DNAT --to-destination 192.168.0.30:8080
iptables -t nat -A POSTROUTING  -o br0 -p tcp  -d 192.168.0.30 -j SNAT --to-source 192.168.254.30
