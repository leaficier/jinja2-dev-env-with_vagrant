Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "forwarded_port", guest: 5000, host:8080
  config.vm.provider "virtualbox" do |v|
    v.memory = 512
  end
  config.vm.provision "shell", path: "boot.sh"
end
