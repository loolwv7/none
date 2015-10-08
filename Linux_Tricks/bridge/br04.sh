#! /bin/bash

ebtables -t broute -A BROUTING -p IPv4 --ip-protocol 6  \
	--ip-destination-port 80 -j redirect --redirect-target ACCEPT
ebtables -t broute -A BROUTING -p IPv4 --ip-protocol 6  \
	--ip-destination-port 8080 -j redirect --redirect-target ACCEPT
iptables -t nat -A PREROUTING -i br0 -p tcp --dport 80  \
	-j REDIRECT --to-port 8080
