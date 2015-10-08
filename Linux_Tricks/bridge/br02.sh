#! /bin/bash

brctl addbr br0
brctl addif br0 eth0
brctl addif br0 eth1

ifconfig br0 192.168.0.250 netmask 255.255.255.0 up
brctl setageing br0 0
brctl stp br0 off

route add default gw 192.168.0.1 dev br0
