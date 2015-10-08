#!/bin/sh

pkill udhcpc
ifconfig eth0 192.168.8.111 netmask 255.255.255.0 broadcast 192.168.8.255 up
