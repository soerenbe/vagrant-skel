#!/bin/bash
test -e /usr/bin/puppet || apt-get install -y puppet
mkdir -p /etc/puppet/modules
mkdir -p /etc/puppet/hiera
test -e /etc/puppet/modules/locales || puppet module install saz-locales
#test -e /etc/puppet/modules/apache || puppet module install puppetlabs-apache
#test -e /etc/puppet/modules/postgresql || puppet module install puppetlabs-postgresql
#test -e /etc/puppet/modules/mysql || puppet module install puppetlabs-mysql
#test -e /etc/puppet/modules/logrotate || puppet module install rodjek-logrotate
#test -e /etc/puppet/modules/python || puppet module install stankevich-python
#test -e /etc/puppet/modules/rabbitmq || puppet module install puppetlabs-rabbitmq