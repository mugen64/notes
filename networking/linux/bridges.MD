# LINUX BRIDGE
To create a virtual network where [namespaces](./namespaces.MD) can connect we need a virtual switch.


- CREATE by adding a new interface to the host
```bash
ip link add <bridge-name> type bridge
```
- BRING UP the interface
```bash
ip link set dev <bridge-name> up
```

- CREATE veth pair/cable

```bash
ip link add veth-<namespace> type veth peer name veth-<namespace>-br 
```

- ATTACH interface to namespace
```bash
ip link set veth-<namespace> netns <namespace>
```

- CONNECT to bridge
```bash
ip link set veth-<namespace>-br master <bridge-name>
```

- BRING namespace interface
```bash
ip -n <namespace> link set veth-<namespace> up
```

- GIVE BRIDGE Ip address
```bash
ip addr add 192.169.15.5/24 dev <bridge-name>
```

Now we can ping from host to namespace

- PREVIEW route table
```bash
sudo ip netns exec <namespace> route
```
- USE LAN / ROUTE traffic through gateway
```bash
ip netns exec <namespace> ip route add 192.168.1.0/24 via 192.169.15.5
```

- ADD masuqarade rule in iptables to enable nat

```bash
iptables -t nat -A POSTROUTING -s 192.168.15.0/24 -j MASQUERADE
```

- To allow namespaces to access internet just route all traffic to our host (as default gateway)
```bash
ip netns exec <namespace> pip oute add default via 192.168.15.5
```

- FORWARD TRAFFIC TO PORT
```bash
iptables -t nat -A PREROUTING --dport 90 --to-destination 192.168.15.2:80-j DNAT
```
