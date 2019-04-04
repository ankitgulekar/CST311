#!/usr/bin/python
# File: legacy_router.py
from mininet.net import Mininet
from mininet.node import Host, Node, Switch
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def myNetwork():
    
    net = Mininet ( topo=None,
                    build=False,
                    ipBase='10.0.0.0/8' )

    default_ip = '10.0.0.6/8'
    # info ( '*** Add Router\n' )
    # r1 = net.addHost ( 'r1', cls=Node, ip='10.0.0.1' )
    # r1.cmd ( 'sysctl -w net.ipv4.ip_forward=1' )

    info ( '*** Add hosts\n' )
    h1 = net.addHost ( 'h1', cls=Host, ip='10.0.0.2', defaultRoute='10.0.0.4' )
    h2 = net.addHost ( 'h2', cls=Host, ip='10.0.0.3', defaultRoute='10.0.0.5' )

    info ( '*** Add Switch\n' )
    switch = net.addSwitch('s1')
    # net.addLink (s1, r1, intfName2='r0-eth1', params2={'ip': default_ip} )

    info ( '*** Add links\n' )
    net.addLink ( h1, switch )
    net.addLink ( h2, switch )

    info ( '*** Starting network\n' )
    net.build ()
    CLI ( net )
    net.stop ()


if __name__ == '__main__':
    setLogLevel ( 'info' )
    myNetwork ()
