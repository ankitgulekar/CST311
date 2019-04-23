Run the following commands
`cd distribution-karaf-0.4.0-Beryllium`


`sudo ./bin/karaf clean`


`feature:install odl-restconf odl-l2switch-switch odl-mdsal-apidocs odl-dlux-all`


`sudo mn --topo linear,3 --mac --controller=remote,ip=192.168.50.4,port=6633 --switch ovs,protocols=OpenFlow13`
