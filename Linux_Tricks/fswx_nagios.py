10.7.84.26
10.7.84.25
10.7.84.250,251,249,27

AIX snmp how to

snmpinfo -m dump -h localhost -c community -v
snmpinfo -m dump -h localhost -c community -v hrStorage/system

stopsrc -s aixmibd; stopsrc -s hostmibd; stopsrc -s snmpmibd; stopsrc -s snmpd
startsrc -s aixmibd -a ``-c public''; startsrc -s hostmibd -a ``-c public''
startsrc -s snmpmibd -a ``-c public''; startsrc -s snmpd

vi /etc/snmpdv3.conf
VACM_GROUP group1 SNMPv1  public  -

VACM_VIEW defaultView       internet                    - included -

VACM_VIEW defaultView        1.3.6.1.4.1.2.2.1.1.1.0    - included -
VACM_VIEW defaultView        1.3.6.1.4.1.2.6.191.1.6    - included -

# exclude snmpv3 related MIBs from the default view
VACM_VIEW defaultView        snmpModules                - excluded -
VACM_VIEW defaultView        1.3.6.1.6.3.1.1.4          - included -   
VACM_VIEW defaultView        1.3.6.1.6.3.1.1.5          - included -  

# include aixmibd managed MIBs into the default view for Nagios
VACM_VIEW defaultView        1.3.6.1.4.1.2.6.191        - included -

VACM_ACCESS  group1 - - noAuthNoPriv SNMPv1  defaultView - defaultView -

NOTIFY notify1 traptag trap -

TARGET_ADDRESS Target1 UDP 127.0.0.1       traptag trapparms1 - - -

TARGET_PARAMETERS trapparms1 SNMPv1  SNMPv1  public  noAuthNoPriv -

# The line below only sets the community string, but allows access 
# from any IP using the 0.0.0.0 (IP) and 0.0.0.0 (netmask) wildcard
#COMMUNITY SECro SECro noAuthNoPriv 0.0.0.0    0.0.0.0  -

# If we want to restrict access by IP, we need to allow localhost
# communication with the SNMP subagents (aixmibd, snmpmibd, ...)
COMMUNITY public public noAuthNoPriv 127.0.0.1    255.255.255.255  -

# Here we restrict the SNMP access to the Nagios server IP address
COMMUNITY public public noAuthNoPriv 192.168.1.34    255.255.255.255  -


DEFAULT_SECURITY no-access - -

logging         file=/usr/tmp/snmpdv3.log       enabled
logging         size=100000                     level=0

smux            1.3.6.1.4.1.2.3.1.2.1.2         gated_password  # gated
smux 1.3.6.1.4.1.2.3.1.2.3.1.1 muxatmd_password #muxatmd
