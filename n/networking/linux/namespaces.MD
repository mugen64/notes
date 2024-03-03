# NETWORK NS

Namespaces are used to implement network isolation eg containers like docker use them to implement n/w. while the containers themselves are isolated and cannot see other processes the host can view into the container including processes inside the container. 

Container processes can thus be viewed both in the container and host with different PIDs

```bash
ps aux
```



- CREATE 
```bash
ip netns add <namespace>
```
- LIST 
```bash
ip netns
```

- LIST INTERFACES ON HOST
```bash
ip link
```

- LIST INTERFACES IN NS
```bash
ip netns exec <namespace> ip link

OR

ip -n red link
```

- ARP TABLE ON HOST

```bash
arp
```

- ARP IN NS

```bash
ip netns exec <namespace> arp
```


- CONNECT 2/MORE namespaces

We can connect 2 namespaces using a Virtual ethernet pair/cable/pipe (VETH Pair) 

-  - Create a cable
```bash
ip link add veth-<namespace-1> type veth peer name veth-<namespace-2>
```
- - attach each interface to desired namespace
```bash
ip link set veth<namespace-1> netns <namespace-1>

ip link set veth<namespace-2> netns <namespace-2>
```

- - assign namespace ip
```bash
ip -n <namespace-1> addr add <192.168.15.1> dev veth-<namespace-1>
```

- - switch on (bring up) 
```bash
ip -n <namspace-1> link set veth-<namespace-1> up
```

- - now u can ping any of the namespaces with in the other
```bash
ip netns exec <namespace> ping <ip2>
```

- DELETE link
```bash
ip -n <namespace> link del <veth-namespace>
```

deleting one end of a link deletes the other

lets try connect the namespaces to a bridge we use linux switch but we can use alternative open vswitch

- - CREATE bridge/switch

```bash
ip link add v-net-0 type bridge
```

start up the bridge
```bash
ip link set dev v-net-0 up
```

create a cable to connect namespace with a peer that connects to bridge

after attaching new cable to namespace
attach the peer to the bridge

```bash
ip link set veth-red-br master v-net-0
```

to make  reachable from the host namespaces we assign ip to bridge

```bash

ip addr add 192.168.15.5/24 dev v-net-0

```

to allow ns to connect to ouside world we add nat to our host

```bash

iptables -t nat -A POSTROUTING -s 192.168.15.0/24 -j MASQUERADE

```

to see addresses use

```
ip address

# OR

ip addr

# user friendly

ip -4 -br addr show

# one line
ip -o address

```

SOME debugging

@ if lo device has status unknown



@ if pinging does not work and everything else is well setup try 
- check if ip forwarding is enabled `sysctl net.ipv4.ip_forward
` if it is = 0 then enable with `sudo sysctl -w net.ipv4.ip_forward=1.
` To make the change persistent across reboots, edit the /etc/sysctl.conf file and set net.ipv4.ip_forward = 1
- ip route