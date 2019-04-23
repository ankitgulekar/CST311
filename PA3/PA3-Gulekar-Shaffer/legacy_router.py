#!/usr/bin/python
# File: legacy_router.py
from mininet.net import Mininet
from mininet.node import Host, Node, Switch
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def myNetwork():
    net = Mininet(topo=None,
                  build=False,
                  ipBase='192.168.1.1/24'
                  )

    default_ip = '192.168.1.1/24'
    info('*** Add Router\n')
    r1 = net.addHost('r1', cls=Node, ip=default_ip)
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')

    info('*** Add Switch\n')
    switch = net.addSwitch('s1')
    # net.addLink (switch, r1 )

    info('*** Add hosts\n')
    # The default route is the route that will connect the host to the route
    h1 = net.addHost('h1', cls=Host, ip='192.168.1.100/24', defaultRoute='via 192.168.1.1')
    h2 = net.addHost('h2', cls=Host, ip='172.16.0.100/12', defaultRoute='via 172.16.0.1')

    info('*** Add links\n')
    # We needed to add a link name (r0-ethX) and what subnet the link was on
    net.addLink(h1, r1, intfName2='r0-eth1', params2={'ip': '192.168.1.1/24'})
    net.addLink(h2, r1, intfName2='r0-eth2', params2={'ip': '172.16.0.1/12'})

    info('*** Starting network\n')
    net.build()

    info('*** Routing Table on Router:\n')
    info(net['r1'].cmd('route'))
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
