ebtables -t nat -A POSTROUTING -o br0 -j snat --to-src 00:26:55:E3:12:8C --snat-arp --snat-target ACCEPT
ebtables -t nat -A PREROUTING -p IPv4 -i br0 --ip-dst 192.168.0.30 --ip-protocol tcp --ip-dport 8080 -j dnat --to-dst 54:ee:75:03:69:a0 --dnat-target ACCEPT
ebtables -t nat -A PREROUTING -p ARP -i br0 --arp-ip-dst 192.168.0.30 -j dnat --to-dst 54:ee:75:03:69:a0 --dnat-target ACCEPT
