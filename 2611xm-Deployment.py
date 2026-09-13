from netmiko import ConnectHandler

net_connect = ConnectHandler(
    device_type ="cisco_ios_telnet",
    ip = "192.168.10.61",
    username = "netmikodevmilk",
    password = "netmikoTestpassword",
)

globalConfig = [
    #logging parameters
    "service timestamps debug datetimemsec",
    "service timestamps log datetime",
    "service password-encryption",
    "service sequence-numbers",
    "logging 192.168.10.15",
    "logging buffered critical",
    "logging reload debugging",
    "logging console critical",
    "logging monitor critical",
    #disable dhcp
    "no service dhcp",
    "hostname bridgerouter",
    "no standby redirect",
    "ip routing",
    "ip domain-name .local",
    "ip name-server 192.168.10.11 172.16.2.10",
    #disable/configure cdp
    "no cdp run",
    "cdp timer 30",
    "cdp holdtime 120",
    #user config
    "username bridgemilk secret darKm1lk12345",
    "username netmikomilk privilege 15 secret netmikoTestpassword"
]

vtyConfig = [
    "line vty 0 2",
    "password 7 darKm1lk12345",
    "login local",
    "transport input telnet",
    "transport output all",
    "logging synchronous",
    "access-class 1 in",
]

consoleConfig = [
    "line con 0",
    "access-class 1 in",
    "logging synchronous",
    "login local",
    "password 7 darKm1lk12345",
    "transport output all",
]

physicalInterfaceConfig = [
    #nat outside fa0/1 interface config
    "interface fa0/1",
    "description wideHomeNetInterface",
    "ip address 192.168.1.254 255.255.255.0",
    "ip nat out",
    "full-duplex",
]

dot1QConfig = [
#dot1q2 Interface Config
"int fa0/0.2",
"encapsulation dot1q 2",
"description testVMSubinterface",
"ip add 172.16.2.253 255.255.255.0",
"ip ospf network broadcast",
"ip access-group inHostVlan2 in",
"ip access-group outHostVlan2 out",
#dot1q3 Interface Config
"int fa0/0.3",
"encapsulation dot1q 3",
"description sunshineStreamingSubinterface",
"ip add 172.16.3.13 255.255.255.240",
"ip ospf network broadcast",
#dot1q4 Interface Config
"int fa0/0.4",
"encapsulation dot1q 4",
"description proxmoxSubinterface",
"ip add 172.16.4.3 255.255.255.248",
"ip ospf network broadcast",
#dot1q5 Interface Config
"int fa0/0.5",
"encapsulation dot1q 5",
"description wirelessSubinterface",
"ip add 172.16.5.29 255.255.255.224",
"ip ospf network broadcast",
#dot1q10 Interface Config
"int fa0/0.10",
"encapsulation dot1q 10",
"description personalVMSubinterface",
"ip add 172.16.10.29 255.255.255.224",
"ip ospf network broadcast",
#dot1q20 Interface Config
"int fa0/0.20",
"encapsulation dot1q 20",
"description gamingConsoleSubinterface",
"ip add 172.16.20.13 255.255.255.240",
"ip ospf network broadcast",
#dot1q30 Interface Config
"int fa0/0.30",
"encapsulation dot1q 30",
"description personalServerSubinterface",
"ip add 172.16.30.13 255.255.255.240",
"ip ospf network broadcast",
#dot1q50 Interface Config
"int vlan fa0/0.50",
"encapsulation dot1q 50",
"description natInSubinterface",
"ip add 172.16.50.253 255.255.255.0",
"ip ospf network broadcast",
"ip nat in",
#dot1q51 Interface Config
"int fa0/0.51",
"encapsulation dot1q 51",
"description natOutSubinterface",
"ip add 172.16.51.253 255.255.255.0",
"ip ospf network broadcast",
"ip nat out",
#dot1q55 Interface Config
"int fa0/0.55",
"encapsulation dot1q 55",
"description piracySubinterface",
"ip add 172.16.55.3 255.255.255.248",
"ip ospf network broadcast",
#dot1q99 Interface Config
"interface fa0/0.99",
"encapsulation dot1q 99",
"description managementSubinterface",
"ip add 172.16.99.253 255.255.255.0",
"ip ospf network broadcast",
"ip access-group inHostManagementVLAN99 in",
#dot1q100 Interface Config
"int fa0/0.100",
"encapsulation dot1q 100",
"description dmzSubinterface",
"ip add 172.16.100.253 255.255.255.0",
"ip ospf network broadcast",
#dot1q255 Interface Config
"int fa0/0.255",
"encapsulation dot1q 255",
"description sunshineStreamingSubinterface",
"ip add 172.16.255.3 255.255.255.248",
"ip ospf network broadcast",
#dot1q500 Interface Config
"interface fa0/0.500",
"encapsulation dot1q 500",
"description routingUpdateSubinterface",
"ip address 10.250.250.3 255.255.255.248",
"ip ospf cost 5",
"ip ospf priority 253",
"ip ospf network broadcast",
"ip ospf message-digest-key 1 md5 darKm1lk12345",
"ip ospf authentication message-digest",
#dot1q1000 Interface Config
"interface fa0/0.1000",
"encapsulation dot1q 1000 native",
"description ctNetNativeSubinterface"
"ip address 192.168.10.61 255.255.255.192",
"ip nat inside",
"ip ospf broadcast",
]

loopbackIntConfig = [
    "interface loopback 1",
    "description OSPF area 0 process ID RID"
    "ip address 10.0.0.2 255.255.255.255.",
]

ospfConfig = [
"ip route 0.0.0.0 0.0.0.0 gig 0/1 name fallbackInternetDefaultRoute 200", #fallback route in case uplinks to coreGFS fails
"router ospf 1",
"router-id 10.0.0.3",
"default-information originate",
"area 0 authentication message-digest",
"event-log one-shot size 500",
"passive-interface default",
"no passive-interface fa0/0.500",
"log-adjacency-changes detail",
"default-information originate",
"network 10.0.0.2 0.0.0.0 area 0",
"network 172.16.2.0 0.0.0.255 area 0",
"network 172.16.3.0 0.0.0.15 area 0",
"network 172.16.4.0 0.0.0.15 area 0",
"network 172.16.5.0 0.0.0.31 area 0",
"network 10.250.250.0 0.0.0.7 area 0",
"network 192.168.10.0 0.0.0.63 area 0",
]

ripConfig = [
"router rip",
"auto-summary",
"default-infromation originate",
"passive-interface default",
"no passive-interface fa0/0.500",
"distance 190",
]

aclConfig = [
#access list 1 config (line control)
"access-list 1 permit 172.16.2.0 0.0.0.255",
"access-list 1 permit 172.16.99.0 0.0.0.255",
"access-list 1 permit 192.168.10.0 0.0.0.63",
#access list 2 config (vmNetControl)
    "ip access-list extended inHostVlan2",
    #Inbound DNS Traffic Control
    "deny tcp 192.168.1.0 0.0.0.255 host 172.16.2.3 eq 53 log",
    "deny udp 192.168.1.0 0.0.0.255 host 172.16.2.3 eq 53 log",
    "deny tcp 192.168.10.0 0.0.0.63 host 172.16.2.3 eq 53 log",
    "deny udp 192.168.10.0 0.0.0.63 host 172.16.2.3 eq 53 log",
    #Web Server Access Control
    "permit tcp 192.168.1.0 0.0.0.255 host 172.16.2.4 eq 80 log",
    "permit tcp 192.168.10.0 0.0.0.63 host 172.16.2.4 eq 80 log",
    "permit tcp 192.168.1.0 0.0.0.255 host 172.16.2.4 eq 443 log",
    "permit tcp 192.168.10.0 0.0.0.63 host 172.16.2.4 eq 443 log",
    #Syslog Access Control (only permit Gateway Addresses to log)
    "permit tcp host 192.168.10.62 host 172.16.2.4 eq 514 log",
    "permit tcp host 172.16.2.1 host 172.16.2.4 eq 514 log",
    "permit tcp host 172.16.10.1 host 172.16.2.4 eq 514 log",
    "permit tcp host 172.16.30.1 host 172.16.2.4 eq 514 log",
    "permit udp host 192.168.10.62 host 172.16.2.4 eq 514 log",
    "permit udp host 172.16.2.1 host 172.16.2.4 eq 514 log",
    "permit udp host 172.16.10.1 host 172.16.2.4 eq 514 log",
    "permit udp host 172.16.30.1 host 172.16.2.4 eq 514 log",
    #NetConnectivity Control
    "deny icmp any host 172.16.2.100 log",
    "deny icmp any host 172.16.2.254 log",
    "permit icmp any any log",
    "permit ip 172.16.2.0 0.0.0.255 172.16.2.0 0.0.0.255 log",
    #DHCP Traffic Control
    "permit udp host 0.0.0.0 eq 68 host 255.255.255.255 eq 67 log",
    "permit udp host 172.16.2.1 eq 67 172.16.2.0 0.0.0.255 eq 68 log",
    "ip access-list extended outHostVlan2",
    #Outbound DNS Traffic Control
    "permit tcp 172.16.2.0 0.0.0.255 host 172.16.2.3 eq 53 log",
    "permit udp 172.16.2.0 0.0.0.255 host 172.16.2.3 eq 53 log",
    "permit tcp 172.16.2.0 0.0.0.255 host 192.168.10.11 eq 53 log",
    "permit udp 172.16.2.0 0.0.0.255 host 192.168.10.11 eq 53 log", 
    #Outbound Jumpbox Traffic Control
    "permit tcp host 172.16.2.60 172.16.2.0 0.0.0.255 eq 3389 log",
    "permit tcp host 172.16.2.60 176.16.2.0 0.0.0.255 eq 22 log",
    "permit tcp host 172.16.2.60 176.16.2.0 0.0.0.255 eq 23 log",
    #ICMP Traffic Control
    "deny icmp any host 172.16.2.100 log",
    "deny icmp any host 172.16.2.254 log",
    "permit icmp any any log",
    "permit ip 172.16.2.0 0.0.0.255 172.16.2.0 0.0.0.255 log",
    #access list 99 config (management traffic control (due to hommelab scale and purpose not explicilty going to change much :/))
    "ip access-list extended inHostManagementVLAN99",
    "permit tcp 192.168.10.0 0.0.0.63 172.16.99.0 0.0.0.255 eq 22",
    "permit tcp 192.168.10.0 0.0.0.63 172.16.99.0 0.0.0.255 eq 23",
    "permit tcp 172.16.99.0 0.0.0.255 172.16.99.0 0.0.0.255 eq 22",
    "permit tcp 172.16.99.0 0.0.0.255 172.16.99.0 0.0.0.255 eq 23",
]


vrrpConfig = [
#vlan2Standby
    "int fa0/0.2",
    "vrrp 2 ip 172.16.2.1",
    "vrrp 2 preempt",
    "vrrp 2 priority 225",
    "vrrp 2 timers advertise 5",
    "vrrp 2 timers learn",
#vlan3Standby
    "int fa0/0.3",
    "vrrp 3 ip 172.16.3.1",
    "vrrp 3 preempt",
    "vrrp 3 priority 225",
    "vrrp 3 timers advertise 5",
    "vrrp 3 timers learn",
#vlan4Standby
    "int fa0/0.4",
    "vrrp 4 ip 172.16.4.1",
    "vrrp 4 preempt",
    "vrrp 4 priority 225",
    "vrrp 4 timers advertise 5",
    "vrrp 4 timers learn",
#vlan5Standby
    "int fa0/0.5",
    "vrrp 5 ip 172.16.5.1",
    "vrrp 5 preempt",
    "vrrp 5 priority 225",
    "vrrp 5 timers advertise 5",
    "vrrp 5 timers learn",
#vlan10Standby
    "interface fa0/0.10",
    "vrrp 10 ip 172.16.10.1",
    "vrrp 10 preempt",
    "vrrp 10 priority 225",
    "vrrp 10 timers advertise 5",
    "vrrp 10 timers learn",
#vlan20Standby
    "interface fa0/0.20",
    "vrrp 20 ip 172.16.20.1",
    "vrrp 20 preempt",
    "vrrp 20 priority 225",
    "vrrp 20 timers advertise 5",
    "vrrp 20 timers learn",
#vlan30Standby
    "interface fa0/0.30",
    "vrrp 30 ip 172.16.30.1",
    "vrrp 30 preempt",
    "vrrp 30 priority 225",
    "vrrp 30 timers advertise 5",
    "vrrp 30 timers learn",
#vlan50Standby
    "int fa0/0.50",
    "vrrp 50 ip 172.16.50.1",
    "vrrp 50 preempt",
    "vrrp 50 priority 225",
    "vrrp 50 timers advertise 5",
    "vrrp 50 timers learn",
#vlan51Standby
    "int fa0/0.51",
    "vrrp 51 ip 172.16.51.1",
    "vrrp 51 preempt",
    "vrrp 51 priority 225",
    "vrrp 51 timers advertise 5",
    "vrrp 51 timers learn",
#vlan55Standby
    "int fa0/0.55",
    "vrrp 55 ip 172.16.55.1",
    "vrrp 55 preempt",
    "vrrp 55 priority 225",
    "vrrp 55 timers advertise 5",
    "vrrp 55 timers learn",
#vlan99Standby
    "int fa0/0.99",
    "vrrp 99 ip 172.16.99.1",
    "vrrp 99 preempt",
    "vrrp 99 priority 225",
    "vrrp 99 timers advertise 5",
    "vrrp 99 timers learn",
#vlan100Standby
    "interface fa0/0.100",
    "vrrp 100 ip 172.16.100.1",
    "vrrp 100 preempt",
    "vrrp 100 priority 225",
    "vrrp 100 timers advertise 5",
    "vrrp 100 timers learn",
#vlan255Standby
    "interface fa0/0.255",
    "vrrp 255 ip 10.250.250.1",
    "vrrp 255 preempt",
    "vrrp 255 priority 225",
    "vrrp 255 timers advertise 5",
    "vrrp 255 timers learn",
#vlan1000Standby
    "interface fa0/0.1000",
    "vrrp 254 ip 192.168.10.1",
    "vrrp 254 preempt",
    "vrrp 254 priority 225",
    "vrrp 254 timers advertise 5",
    "vrrp 254 timers learn",
]

httpServerConfig = [
    "no ip http server",
]

dhcpToolConfig = [
    #enable dhcp relays/ip helpers
    "int fa0/0.2",
    "ip helper-add 10.250.250.1",
    "int fa0/0.3",
    "ip helper-add 10.250.250.1",
    "int fa0/0.4",
    "ip helper-add 10.250.250.1",
    "int fa0/0.5",
    "ip helper-add 10.250.250.1",
    "int fa0/0.10",
    "ip helper-add 10.250.250.1",
    "int fa0/0.20",
    "ip helper-add 10.250.250.1",
    "int fa0/0.30",
    "ip helper-add 10.250.250.1",
    "int fa0/0.50",
    "ip helper-add 10.250.250.1",
    "int fa0/0.51",
    "ip helper-add 10.250.250.1",
    "int fa0/0.55",
    "ip helper-add 10.250.250.1",
    "int fa0/0.99",
    "ip helper-add 10.250.250.1",
    "int fa0/0.100",
    "ip helper-add 10.250.250.1",
    "int fa0/0.255",
    "ip helper-add 10.250.250.1",
    "int fa0/0.500",
    "ip helper-add 10.250.250.1",
    "int fa0/0.1000",    
    "ip helper-add 10.250.250.1",
]

natConfig = [
"ip nat inside source static 192.168.10.11 192.168.1.252",
"ip nat inside source static 192.168.10.12 192.168.1.253",
]

#upload config sets to 2611xm router
ciscoCLI = [globalConfig, vtyConfig, consoleConfig, physicalInterfaceConfig, dot1QConfig, loopbackIntConfig, ospfConfig, ripConfig, aclConfig, vrrpConfig, httpServerConfig, dhcpToolConfig, natConfig]
for config in ciscoCLI:
    sendCLI = net_connect.send_config_set(config)
    print(sendCLI)