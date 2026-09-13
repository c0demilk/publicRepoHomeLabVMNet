#ufw config, for purposes of ubuntuDevServer, permit inbound ports 22, 53, 80, 443, and 445

#install ufw 
apt install ufw -y 
apt update -y
apt upgrade -y

#list that contains permitted inbound ports and subnet
inPorts = ("22/tcp, 53/tcp, 53/udp, 80/tcp, 443/tcp, 445/tcp")
allowedSubnets = ("10.13.12.0/27")

#iterates through firewall rules
#permits port traffic
for rule in $inPorts; do
ufw allow $rule from $allowedSubnets to $rule
done

#creates default ufw statements
ufw default deny outgoing
ufw default allow incoming
#verify ufw status
ufw status verbose
