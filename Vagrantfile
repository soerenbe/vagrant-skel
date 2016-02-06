# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # debian/jessie64 have not virtualbox guest additionals, so you can not mount vboxfs (e.g. with synced_folder or puppet.module_path
  # It is strongly recommended to use the ARTACK/debian-jessie box instead
  #config.vm.box = "debian/jessie64"
  config.vm.box = "ARTACK/debian-jessie"
  #config.vm.box = "ubuntu/trusty64"
  #config.vm.box = "ubuntu/precise64"
  
  # Workaround to skip nasty tty errors during provisioning
  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"  
  # We are using the virtualbox provider. Feel free to match the number of CPUs and the memory to your needs
  config.vm.provider "virtualbox" do |vbox|
    vbox.memory = 512
    vbox.cpus = 1
    # USB 2.0 is enabled by default in virtualbox. Since most people dont't need ist and it causes a failure in the ARTACK/debian-jessie box,
    # we simply disable it.
    vbox.customize ["modifyvm", :id, "--usb", "off"]
    vbox.customize ["modifyvm", :id, "--usbehci", "off"]
  end
  # For a basic setup we run a basic 'apt-get update' That ensure that all the correct packages are available if you got into the VM
  config.vm.provision :shell, :inline => "test -e /var/cache/apt-updated || apt-get update"
  config.vm.provision :shell, :inline => "test -e /var/cache/apt-updated && echo 'Skipping apt-get update. /var/cache/apt-updated exists' || /bin/true"
  config.vm.provision :shell, :inline => "touch /var/cache/apt-updated"

  # If we want to use puppet we may execute a additional provisioning script.
  # We have to ensure that it is installed in the virtual machine. We also install some additional modules from puppetlabs there
  # If you don't use puppet for provisioning you can comment out the following lines.  
  config.vm.provision :shell, :inline => "test -e /usr/bin/puppet || apt-get install -y puppet"
  config.vm.provision :shell, :inline => "mkdir -p /etc/puppet/modules"
  config.vm.provision :shell, :inline => "mkdir -p /etc/puppet/hiera"
  config.vm.provision :shell, :inline => "test -e /etc/puppet/modules/locales || puppet module install saz-locales"
  #config.vm.provision :shell, :inline => "test -e /etc/puppet/modules/apache || puppet module install puppetlabs-apache"
  #config.vm.provision :shell, :inline => "test -e /etc/puppet/modules/postgresql || puppet module install puppetlabs-postgresql"
  #config.vm.provision :shell, :inline => "test -e /etc/puppet/modules/mysql || puppet module install puppetlabs-mysql"
  #config.vm.provision :shell, :inline => "test -e /etc/puppet/modules/logrotate || puppet module install rodjek-logrotate"
  #config.vm.provision :shell, :inline => "test -e /etc/puppet/modules/python || puppet module install stankevich-python"
  #config.vm.provision :shell, :inline => "test -e /etc/puppet/modules/rabbitmq || puppet module install puppetlabs-rabbitmq"

  # You can also add a provisioning script it should be located in the root repository directory (or a relative path
  # config.vm.provision "shell", path: "myscript.sh"
  # config.vm.provision "shell", path: "myscripts/bootstrap.sh"
  # config.vm.provision "shell", path: "myscripts/install_my_app.sh"
  
  # We define exactly one machine.
  # For advanced multi machine setups have a look at: https://docs.vagrantup.com/v2/multi-machine/index.html
  config.vm.define "default" do |default|
    # If you want a special network in the vagrant environment (especially in a multi machine setup), you can configure additional
    # IP adresses to the interface. If you want to learn more about the advanced network topics see:
    # # https://docs.vagrantup.com/v2/networking/index.html
    #
    #default.vm.network "private_network", ip: "192.168.10.1"
    #
    # We can configure some port forwards so make the internal services available on the outside. For example a Webserver with http and https:
    default.vm.network "forwarded_port", guest: 80, host: 8080
    default.vm.network "forwarded_port", guest: 443, host: 8443
    default.vm.network "forwarded_port", guest: 8000, host: 8000
    
    # If we have additional folder that we want to mount in the virtual machine (like your project root), we can define some synced_folders.
    # They will be mounted through the vboxfs filesystem.
    # E.g.: This will mount the current 'src/' folder to '/var/www' in the virtual machine.
    #default.vm.synced_folder ("src/", "/var/www")
    #default.vm.synced_folder("src/djtest", "/home/vagrant/djtest")
    
    # First note: If you dont want to use puppet for provisioning you can delete the paragraph bellow
    
    # When using hier we have to mount our hiera directory to the virtual environment
    # You also can mount your normal hiera envionment from somewhere else like
    # default.vm.synced_folder("/home/user/puppet/hiera", "/etc/puppet/hiera")
    default.vm.synced_folder("puppet/hiera", "/etc/puppet/hiera")
    default.vm.synced_folder("src/djtest", "/home/vagrant/djtest")
    
    default.vm.provision :puppet do |puppet|
      # If you have your own modules for your project you can put it in the puppet/modules directory. You can also add some
      # local modules - for example from your production environment.
      # puppet.module_path = ["puppet/modules", "/home/user/puppet/mymodules"]
      puppet.module_path = ["puppet/modules"]
      # This points to the manifest file for your node
      puppet.manifests_path = "puppet/manifests"
      puppet.manifest_file = "site.pp"
      # This lines are only required if using hiera
      puppet.hiera_config_path = "puppet/hiera/hiera.yaml"
      puppet.working_directory = "/etc/puppet/hiera"
      # Some additional puppet parameters
      puppet.options = "--verbose"
      # Its always useful to set some facter variables.
      puppet.facter = {
        "fqdn"     => "default.vagrant.up",
        "vagrant"  => 1,
        "virtual"  => "vmware"
      }
    end # puppet
  end # config
end #vagrant
