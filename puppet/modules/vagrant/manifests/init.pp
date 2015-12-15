class vagrant (
  $locales        = ['en_US.UTF-8 UTF-8'],
  $language       = 'en_US:en',
  $default_locale = 'en_US.UTF-8',
) {
  file {
    '/etc/hostname':
      ensure   => present,
      owner    => 'root',
      group    => 'root',
      content  => template("vagrant/hostname.erb");
    '/etc/hosts':
      ensure   => present,
      owner    => 'root',
      group    => 'root',
      content  => template("vagrant/hosts.erb"),
      require  => Exec['set_hostname'];
  }
  exec {'set_hostname':
    command     => '/etc/init.d/hostname.sh',
    subscribe   => File['/etc/hostname'],
    refreshonly => true
  }
  class {'locales':
    locales        => $locales,
    language       => $language,
    default_locale => $default_locale
  }
  package {['vim', 'git']:
  }
}

