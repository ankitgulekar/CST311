sudo echo "export JAVA_HOME=/usr/lib/jvm/jre" >> ~/.bashrc
sudo mkdir /etc/network
sudo touch /etc/network/interfaces
sudo echo "# the host-only network interface
auto enp0s8
iface enp0s8 inet dhcp" >> /etc/network/interfaces
sudo yum -y update
sudo yum -y install java-1.8.0-openjdk
sudo echo "export JAVA_HOME=/usr/lib/jvm/jre" >> /home/vagrant/.bashrc
sudo wget https://nexus.opendaylight.org/content/groups/public/org/opendaylight/integration/distribution-karaf/0.4.0-Beryllium/distribution-karaf-0.4.0-Beryllium.tar.gz
tar -xvf distribution-karaf-0.4.0-Beryllium.tar.gz

