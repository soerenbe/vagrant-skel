# vagrant-skel
This is a basic vagrant skeleton for setting up a vagrant machine with puppet and hiera.

## Requirements
You have to install `virtualbox` and `vagrant`. Virtualbox is typically shipped with your distribution. Vagrant may also be shipped this way, but typically you want the latest version. You can find it on https://www.vagrantup.com/.

## Usage
Its main focus is to provide a reproduceable and fast to bootstrap virtual machine environment. Its main focus is to bootstrap a [Django](https://www.djangoproject.com/) environment, but it also serve other purposes.
After you install all dependencies you may run

```bash
$ vagrant up
...
$ vagrant ssh
```
to have a basic virtual machine.

## How it works

The bootstrap of the virtual machine is processed in following steps:

* Importing the BOX
* Starting a new instance of the virtual machine
* Execute the some inline bootstrap scripts
* [Optional] Puppet deployment
    * Execute inline scripts to install additional modules. See bellow the comments in the `Vagrantfile`
    * Running puppet using `puppet/manifests/site.pp`. You may customize this file
    * Also have a look at `puppet/hiera/vagrant.yaml` for basic puppet class setup

## Useing puppet for deployment

Add some inline scripts to your `Vagrantfile`.

```ruby
  config.vm.provision :shell, :inline => "test -e /usr/bin/puppet || apt-get install -y puppet"
  config.vm.provision :shell, :inline => "mkdir -p /etc/puppet/modules"
  config.vm.provision :shell, :inline => "mkdir -p /etc/puppet/hiera"
```
If you are using the shipped hiera data make sure that the hiera directory is mounted inside the virtual machine:
```ruby
default.vm.synced_folder("puppet/hiera", "/etc/puppet/hiera")
```
This is enabled by default. Have a look to the comments in the `Vagrantfile`.

## Additional puppetlabs modules
Add some inline code to your to your `Vagrantfile` to install additional [puppetlabs](https://forge.puppetlabs.com/) modules. 
```ruby
  config.vm.provision :shell, :inline => "test -e /etc/puppet/modules/locales || puppet module install saz-locales"
  config.vm.provision :shell, :inline => "test -e /etc/puppet/modules/apache || puppet module install puppetlabs-apache"
```

Now you can use them in your `puppet/manifests/site.pp`
```puppet
node default {
  include vagrant
  include postgresql
```

## Django environment
Add `scripts/django.sh` to your to your provisioning scripts: 
```ruby
config.vm.provision "shell", path: "scripts/django.sh"
```
To add a basic Django project to the VM you have to add the `src/djtest` directory inside to the virtual machine.
```ruby
default.vm.synced_folder("src/djtest", "/home/vagrant/djtest")
```
You can use the automount in `/vagrant` but this to have it in the home directory is more comfortable. To use the Django environment modify `puppet/manifests/site.pp` to add a virutalenv for Django or any other Python project:

```puppet
node default {
  include vagrant
  include vagrant::python::django
}
```
This will install a `virtualenv` in the vagrant home directory. 
```bash
user@host:~$ vagrant ssh
vagrant@default:~$ source venv/bin/activate
(venv)vagrant@default:~$
```

This project comes with a basic app called `music` for easy testing different modules. You may also add more basic apps. You can either install them by hand or use `puppet/hiera/vagrant.yaml`

```yaml
---
    vagrant::locales: ["de_DE.UTF-8 UTF-8", "en_US.UTF-8 UTF-8", "fr_FR.UTF-8 UTF-8"]
    vagrant::python::django:packages: ["django-app1", "django-app2"]
```

