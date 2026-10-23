from netmiko import ConnectHandler

net_connect = ConnectHandler(
    device_type ="cisco_ios",
    ip = "192.168.10.61",
    username = "netmikodevmilk",
    password = "netmikoTestpassword",
    secret = "Hellothere#2455",  
)

loopedVariables = []

globalConfig = [
    #logging parameters
    "service timestamps debug datetimemsec",
    "service timestamps log datetime",
    "service password-encryption",
    "service sequence-numbers",
    "logging 192.168.10.15",
    "logging userinfo",
    "logging buffered critical",
    "logging reload debugging",
    "logging console critical",
    "logging monitor critical",
    #disable dhcp
    "no service dhcp",
    "hostname distGFS"
    #disable vtp
    "vtp mode transparent",
    "vtp domain cthomenet.local",
    "no standby redirect",
    "ip routing",
    "ip gratuitous arps",
    "ip domain-name home.local",
    "ip name-server 192.168.10.11, 172.16.2.10",
    "spanning-tree mode mst",
    #disable/configure cdp
    "no cdp enable",
    "cdp timer 30",
    "cdp holdtime 120",
    #enable/configure lldp
    "lldp enable",
    "lldp holdtime 300",
    "lldp reinit 5",
    #user config
    "username genderfluidmilk secret darKm1lk12345",
    "username netmikomilk privilege 15 secret netmikoTestpassword"
]

vtyConfig = [
    "crypto key gen rsa general-keys modulus 2048",
    "ip ssh authentication 3",
    "ip ssh version 2",
    "ip ssh timeout 120",
    "line vty 0 2",
    "password 7 darKm1lk12345",
    "login local",
    "transport input ssh",
    "transport output all",
    "logging synchronous",
    "access-class 1 inbound",
]

consoleConfig = [
    "line con 0",
    "access-class 1 in",
    "logging synchronous",
    "login local",
    "password 7 darKm1lk12345",
    "transport output all",
]

vlanConfig = [
"vlan 2",
"name testVMVlan",
"vlan 3",
"name sunshineStreamingVLAN",
"vlan 4",
"name proxmoxVLAN",
"vlan 5",
"name wirelessVLAN",
"vlan 10",
"name personalVMVLAN"
"vlan 20",
"name gamingConsoleVLAN",
"vlan 30",
"name personalServerVLAN",
"vlan 50",
"name networkAddressTranslationVLANIN",
"vlan 51",
"name networkAddressTranslationVLANOUT",
"vlan 55" 
"name piracyVLAN",
"vlan 99",
"name managementVLAN",
"vlan 100",
"name dmzVLAN",
"vlan 255",
"dhcpServerVLAN",
"vlan 500"
"name routingVLAN",
"vlan 1000",
"name ctNetNativeVLAN",
]

sviConfig = [
#svi2 Interface Config
"int vlan 2",
"description testVMSVI",
"ip add 172.16.2.252 255.255.255.0",
"ip o 1 area 0",
"ip ospf broadcast",
#svi3 Interface Config
"int vlan 3",
"description sunshineStreamingSVI",
"ip add 172.16.3.12 255.255.255.240",
"ip o 1 area 0",
"ip ospf broadcast",
#svi4 Interface Config
"int vlan 4",
"description proxmoxSVI",
"ip add 172.16.4.2 255.255.255.248",
"ip o 1 area 0",
"ip ospf broadcast",
#svi5 Interface Config
"int vlan 5",
"description wirelessSVI",
"ip add 172.16.5.28 255.255.255.224",
"ip o 1 area 0",
"ip ospf broadcast",
#svi10 Interface Config
"int vlan 10",
"description personalVMSVI",
"ip add 172.16.10.28 255.255.255.224",
"ip o 1 area 0",
"ip ospf broadcast",
#svi20 Interface Config
"int vlan 20",
"description gamingConsoleSVI",
"ip add 172.16.20.12 255.255.255.240",
"ip o 1 area 0",
"ip ospf broadcast",
#svi30 Interface Config
"int vlan 30",
"description personalServerSVI",
"ip add 172.16.30.12 255.255.255.240",
"ip o 1 area 0",
"ip ospf broadcast",
#svi50 Interface Config
"int vlan 50",
"description natInSVI",
"ip add 172.16.50.252 255.255.255.0",
"ip o 1 area 0",
"ip ospf broadcast",
#svi51 Interface Config
"int vlan 51",
"description natOutSVI",
"ip add 172.16.51.252 255.255.255.0",
"ip o 1 area 0",
"ip ospf broadcast",
#svi55 Interface Config
"int vlan 55",
"description piracySVI",
"ip add 172.16.55.2 255.255.255.248",
"ip o 1 area 0",
"ip ospf broadcast",
#svi99 Interface Config
"interface vlan 99",
"description managementSVI",
"ip add 172.16.99.252 255.255.255.0",
"ip ospf 1 area 0",
"ip ospf broadcast",
"ip access-group inHostManagementVLAN99 in",
#svi100 Interface Config
"int vlan 100",
"description dmzSVI",
"ip add 172.16.100.252 255.255.255.0",
"ip o 1 area 0",
"ip ospf broadcast",
#svi255 Interface Config
"int vlan 255",
"description sunshineStreamingSVI",
"ip add 172.16.255.2 255.255.255.248",
"ip o 1 area 0",
"ip ospf broadcast",
#svi500 Interface Config
"interface vlan 500",
"description routingUpdateSVI",
"ip address 10.250.250.2 255.255.255.248",
"ip ospf 1 area 0",
"ip ospf cost 5",
"ip ospf priority 253",
"ip ospf broadcast",
"ip ospf message-digest-key 1 md5 darKm1lk12345",
"ip ospf authentication message-digest",
#svi1000 Interface Config
"interface vlan 1000",
"description ctNetNativeSVI"
"ip address 192.168.10.60 255.255.255.192",
"ip ospf 1 area 0",
"ip ospf broadcast",
]

lacpConfig = [
    #upstream etherchannel config
    "interface range fa0/1-4, fa-7-8",
    "channel-group 1 mode active",
    "int port-channel 1",
    "description upstream L2 LACP bundle to gateway1"
    "switchport",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan none",
    "switchport trunk allowed vlan 2,3,4,5,10,20,30,50,51,55,99,100,255,500,1000"
    "switchport trunk native vlan 1000",
    "lldp receive",
    "lldp transmit",
    "power inline never",
    "switchport nonnegotiate",
    "ip arp inspection trust",
    "ip arp inspection limit rate 1000",
    "ip dhcp snooping trust"
    "exit",
    #downstream etherchannel config
    "interface range fa0/5-6",
    "channel-protocol lacp",
    "channel-group 2 mode active",
    "int port-channel 2",
    "description downstream L2 LACP bundle to gateway2"
    "switchport",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan none",
    "switchport trunk allowed vlan 2,3,4,5,10,20,30,50,51,55,99,100,255,500,1000"
    "switchport trunk native vlan 1000",
    "spanning-tree portfast trunk",
    "spanning-tree bpduguard enable",
    "switchport nonnegotiate",
    "ip arp inspection trust",
    "ip arp inspection limit rate 1000",
    "ip dhcp snooping trust"
    "lldp receive",
    "lldp transmit",
    "power inline never",
]

gig01Config = [
    "interface gig 0/1",
    "switchport",
    "switchport trunk encapsulation dot1q",
    "switchport trunk allowed vlan none",
    "switchport trunk allowed vlan add 500",
    "spanning-tree portfast trunk",
    "spanning-tree bpduguard enable",
]

mstConfig = [
#configures MST instance 10 (primary)    
"spanning-tree mst configuration",
"name cthomenetTree",
"revision 27",
"instance 10 vlan 2-5, vlan 10, vlan 20, vlan 30, vlan 50-51, vlan 55, vlan99-100, vlan 255, vlan 500, vlan 1000",
"exit",
#configures MST as secondary root
"spanning-tree mst 10 root secondary hello-time 2",
#configures MST interface commands
"int port-channel 1",
"spanning-tree mst 10 cost 1",
"spanning-tree mst 10 port-priority 64",
"int port-channel 2",
"spanning-tree mst 10 cost 5",
"spanning-tree mst 10 port-priority 96",
]

loopbackIntConfig = [
    "interface loopback 1",
    "description OSPF area 0 process ID RID"
    "ip address 10.0.0.3 255.255.255.255.",
    "ip ospf 1 area 0",
    "ip ospf cost 1",
    "ip ospf priority 0",
]

ospfConfig = [
"ip route 0.0.0.0 0.0.0.0 gig 0/1 name fallbackInternetDefaultRoute 200", #fallback route in case uplinks to coreGFS fails
"router ospf 1",
"router-id 10.0.0.3"
"default-information originate",
"area 0 authentication message-digest",
"event-log one-shot size 500",
"passive-interface default"
"no passive-interface vlan 500"
"log-adjacency-changes detail",
"default-information originate",
]

ripConfig = [
"router rip",
"auto-summary",
"default-infromation originate",
"passive-interface default",
"no passive-interface vlan 500",
"distance 190",
]

aclConfig = [
#access list 1 config
"access-list 1 permit 172.16.2.0 0.0.0.255",
"access-list 1 permit 172.16.99.0 0.0.0.255",
"access-list 1 permit 192.168.10.0 0.0.0.63",
"ip access-list extended inHostManagementVLAN99",
"permit tcp 192.168.10.0 0.0.0.63 172.16.99.0 eq 22",
"permit tcp 192.168.10.0 0.0.0.63 172.16.99.0 eq 23",
"permit tcp 172.16.99.0 0.0.0.255 172.16.99.0 eq 22",
"permit tcp 172.16.99.0 0.0.0.255 172.16.99.0 eq 23",
]

hsrpConfig = [
#vlan2Standby
    "int vlan 2",
    "standby 2 ip 172.16.2.1",
    "standby 2 timers 10 40",
    "standby 2 priority 100",
    "standby 2 preempt",
    "standby 2 authentication r3apeR",
    "standby 2 name vlan2Cluster",
#vlan3Standby
    "int vlan 3",
    "standby 3 ip 172.16.3.1",
    "standby 3 timers 10 40",
    "standby 3 priority 100",
    "standby 3 preempt",
    "standby 3 authentication r3apeR",
    "standby 3 name vlan3Cluster",
#vlan4Standby
    "int vlan 4",
    "standby 4 ip 172.16.4.1",
    "standby 4 timers 10 40",
    "standby 4 priority 100",
    "standby 4 preempt",
    "standby 4 authentication r3apeR",
    "standby 4 name vlan4Cluster",
#vlan5Standby
    "int vlan 5",
    "standby 5 ip 172.16.5.1",
    "standby 5 timers 10 40",
    "standby 5 priority 100",
    "standby 5 preempt",
    "standby 5 authentication r3apeR",
    "standby 5 name vlan5Cluster",
#vlan10Standby
    "interface vlan 10",
    "standby 10 ip 172.16.10.1",
    "standby 10 timers 10 40",
    "standby 10 priority 100",
    "standby 10 preempt",
    "standby 10 authentication r3apeR",
    "standby 10 name vlan10Cluster",
#vlan20Standby
    "interface vlan 20",
    "standby 20 ip 172.16.20.1",
    "standby 20 timers 10 40",
    "standby 20 priority 100",
    "standby 20 preempt",
    "standby 20 authentication r3apeR",
    "standby 20 name vlan20Cluster",
#vlan30Standby
    "interface vlan 30",
    "standby 30 ip 172.16.30.1",
    "standby 30 timers 10 40",
    "standby 30 priority 100",
    "standby 30 preempt",
    "standby 30 authentication r3apeR",
    "standby 30 name vlan30Cluster",
#vlan50Standby
    "int vlan 50",
    "standby 50 ip 172.16.50.1",
    "standby 50 timers 10 40",
    "standby 50 priority 100",
    "standby 50 preempt",
    "standby 50 authentication r3apeR",
    "standby 50 name vlan50Cluster",
#vlan51Standby
    "int vlan 51",
    "standby 51 ip 172.16.51.1",
    "standby 51 timers 10 40",
    "standby 51 priority 100",
    "standby 51 preempt",
    "standby 51 authentication r3apeR",
    "standby 51 name vlan51Cluster",
#vlan55Standby
    "int vlan 55",
    "standby 55 ip 172.16.55.1",
    "standby 55 timers 10 40",
    "standby 55 priority 100",
    "standby 55 preempt",
    "standby 55 authentication r3apeR",
    "standby 55 name vlan55Cluster",
#vlan99Standby
    "int vlan 99",
    "standby 99 ip 172.16.99.1",
    "standby 99 timers 10 40",
    "standby 99 priority 100",
    "standby 99 preempt",
    "standby 99 authentication r3apeR",
    "standby 99 name vlan99Cluster",
#vlan100Standby
    "interface vlan 100",
    "standby 100 ip 172.16.100.1",
    "standby 100 timers 10 40",
    "standby 100 priority 100",
    "standby 100 preempt",
    "standby 100 authentication r3apeR",
    "standby 100 name vlan100Cluster",
#vlan255Standby
    "interface vlan 255",
    "standby 255 ip 172.16.255.1",
    "standby 255 timers 10 40",
    "standby 255 priority 100",
    "standby 255 preempt",
    "standby 255 authentication r3apeR",
    "standby 255 name vlan20Cluster",
#vlan100Standby
    "interface vlan 1000",
    "standby 254 ip 192.168.10.1",
    "standby 254 timers 10 40",
    "standby 254 priority 100",
    "standby 254 preempt",
    "standby 254 authentication r3apeR",
    "standby 254 name vlan254Cluster",
]

httpServerConfig = [
    "no ip http server",
    "no ip http server-secure",
    "Secure cipher = 3des-ede-cbc-sha",
    "Enable client authentication",
    "Max connections = 3",
    "Cache ager interval = 1",
    "Client connection timeout = 30",
    "Client connection retry = 3",
    "Client idle timeout = 60",
    "Client username = genderfluidmilk",
    "Client password 7 = darKm1lk12345",
]

dhcpToolConfig = [
    #enable dhcp snooping
    "no ip dhcp snooping information option"
    "ip dhcp snooping database flash:"
    "ip dhcp snooping vlan 2 5",
    "ip dhcp snooping vlan 10",
    "ip dhcp snooping vlan 20",
    "ip dhcp snooping vlan 30",
    "ip dhcp snooping vlan 50",
    "ip dhcp snooping vlan 51",
    "ip dhcp snooping vlan 55",
    "ip dhcp snooping vlan 99",
    "ip dhcp snooping vlan 100",
    "ip dhcp snooping vlan 255",
    "ip dhcp snooping vlan 500",
    "ip dhcp snooping vlan 1000",
    #enable dhcp relays/ip helpers
    "int vlan 2",
    "ip helper-add 10.250.250.1",
    "int vlan 3",
    "ip helper-add 10.250.250.1",
    "int vlan 4",
    "ip helper-add 10.250.250.1",
    "int vlan 5",
    "ip helper-add 10.250.250.1",
    "int vlan 10",
    "ip helper-add 10.250.250.1",
    "int vlan 20",
    "ip helper-add 10.250.250.1",
    "int vlan 30",
    "ip helper-add 10.250.250.1",
    "int vlan 50",
    "ip helper-add 10.250.250.1",
    "int vlan 51",
    "ip helper-add 10.250.250.1",
    "int vlan 55",
    "ip helper-add 10.250.250.1",
    "int vlan 99",
    "ip helper-add 10.250.250.1",
    "int vlan 100",
    "ip helper-add 10.250.250.1",
    "int vlan 255",
    "ip helper-add 10.250.250.1",
    "int vlan 500",
    "ip helper-add 10.250.250.1",
    "int vlan 1000",    
    "ip helper-add 10.250.250.1",
]

arpInspection = [
"ip arp inspection validate ip dst-mac src-mac",
"ip arp inspection vlan 2",
"ip arp inspection vlan 3",
"ip arp inspection vlan 4",
"ip arp inspection vlan 5",
"ip arp inspectin vlan 10",
"ip arp inspection vlan 20",
"ip arp inspection vlan 30",
"ip arp inspection vlan 50",
"ip arp inspection vlan 51",
"ip arp inspection vlan 55",
"ip arp inspection vlan 99",
"ip arp inspection vlan 100",
"ip arp inspection vlan 255",
"ip arp inspection vlan 500",
"ip arp inspection vlan 1000",
]
