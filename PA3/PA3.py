#!/usr/bin/python
# File: legacy_router.py
from mininet.net import Mininet
from mininet.node import Host, Node, Switch
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def myNetwork():
    
    net = Mininet ( topo=None,
                    build=False,
                   )

    default_ip = '10.0.0.1/8'
    info ( '*** Add Router\n' )
    r1 = net.addHost ( 'r1', cls=Node, ip=default_ip)
    r1.cmd ( 'sysctl -w net.ipv4.ip_forward=1' )

    info ( '*** Add Switch\n' )
    switch = net.addSwitch('s1')
    net.addLink (switch, r1 )

    info ( '*** Add hosts\n' )
    h1 = net.addHost ( 'h1', cls=Host, ip='10.0.0.2/8')
    h2 = net.addHost ( 'h2', cls=Host, ip='10.0.0.3/8')

    info ( '*** Add links\n' )
    net.addLink ( h1, switch )
    net.addLink ( h2, switch )

    info ( '*** Starting network\n' )
    net.build ()
    #net.start()
    info ( '*** Routing Table on Router:\n' )
    info ( net['r1'].cmd ( 'route' ) )
    CLI ( net )
    net.stop ()


if __name__ == '__main__':
    setLogLevel ( 'info' )
    myNetwork ()
