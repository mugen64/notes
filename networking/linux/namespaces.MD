# NETWORK NS

Namespaces are used to implement network isolation

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