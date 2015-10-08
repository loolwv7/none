#! /bin/bash

brctl addbr br0
brctl addif br0 eth0
brctl addif br0 eth1

ifconfig br0 192.168.20.102 netmask 255.255.255.0 up
brctl setageing br0 0
brctl stp br0 off

route add default gw 192.168.20.254 dev br0
ifconfig eth0 0.0.0.0 promisc up
ifconfig eth1 0.0.0.0 promisc up

# echo "1" /proc/sys/net/ipv4/ip_forward

# DEFAULT POLICY
ebtables -P INPUT DROP
ebtables -P OUTPUT DROP
ebtables -P FORWARD DROP
# FLUSH TABLES
ebtables -F FORWARD

# Forward Arp and IPv4 Traffic
ebtables -A FORWARD -p IPv4 -j ACCEPT
ebtables -A FORWARD -p ARP -j ACCEPT
ebtables -A FORWARD --log-level info --log-ip --log-prefix EBFW
