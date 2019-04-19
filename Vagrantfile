Vagrant.configure("2") do |config|
  config.vm.box = "comnets/mininet"
  config.vm.network "public_network", ip: "192.168.50.5",
    virtualbox__intnet: true
config.ssh.insert_key = false
end
