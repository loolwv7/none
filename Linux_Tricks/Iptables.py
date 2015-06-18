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
