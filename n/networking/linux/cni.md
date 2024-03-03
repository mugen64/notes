# Container network interfaces

Most containers eg docker use more or less the same steps for networking for bridge we -
- Create n/w ns
- create bridge nw/ interface
- create veth pairs
- attach veth pairs to namespace
- attach veth to bridge
- assign ip addresses
- bring interfaces up
- enable nat - ip masquerade

CNI is a standard to solve networking challenges for programs in a container run time enviroment (CRE) eg how a standard way of how a bridge should work.

The programs are called plugins

Container Runtime

- so the container runtime creates a network namespace
- it identifies networker container must attach to
- it then invokes a network plugin (eg bridge) to ADD container
- when done it invokes plugin to DELETE 
- this is configured using JSON


Plugins 
- support ADD,DEL,CHECK commands
- must support params container id n/w ns etc
- assign ip address to container
- format of response


Example plugins
- bridge
- vlan
- ipvlan
- macvlan
- windows
- dhcp
- host-local

third part
- weaveworks
- flannel
- cilium
- nsx

Docker uses CNM (conatiner network model) so u have to work around docker network to use CNI eg create a docker container with no network config
`docker run --network=none nginx`