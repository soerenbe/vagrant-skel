# This sets up da default apache webserver.
# On port 80 (outside 8080) there is th default apache doc page
# On port 443 (outside 8443) there is the vagrant directory
class vagrant::apache {
  class { '::apache': }
  apache::vhost { 'https':
    port    => '443',
    ssl     => true,
    docroot => '/vagrant/',
  }
}