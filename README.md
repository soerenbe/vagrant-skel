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
* Execute the `sripts/bootstrap.sh` script
* [Optional] Puppet deployment
    * Execute the `scripts/puppet.sh` script to install additional modules. See bellow
    * Running puppet using `puppet/manifests/site.pp`. You may customize this file
    * Also have a look at `puppet/hiera/vagrant.yaml` for basic puppet class setup


## Additional puppetlabs modules
Add `scripts/puppet.sh` to your to your provisioning scripts to install additional [puppetlabs](https://forge.puppetlabs.com/) modules. This feature is enabled by default:
```ruby
config.vm.provision "shell", path: "scripts/puppet.sh"
```
You may add any puppetlabs module you can find to this script:
```bash
test -e /etc/puppet/modules/postgresql || puppet module install puppetlabs-postgresql
```
Now you can use them in your `puppet/manifests/site.pp`
```puppet
node default {
  include vagrant
  include postgresql
```

## Django Environment
Add `scripts/django.sh` to your to your provisioning scripts: 
```ruby
config.vm.provision "shell", path: "scripts/django.sh"
```
Modify `puppet/manifests/site.pp` to add a virutalenv for Django or any other Python project:

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
