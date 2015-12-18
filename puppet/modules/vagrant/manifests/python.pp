class vagrant::python::venv (
  $virtualenv   = '/home/vagrant/venv',
  $requirements = undef,
) {
  class {'::python':
    dev        => 'present',
    virtualenv => 'present',
  }
  python::virtualenv {$virtualenv:
    mode         => '755',
    requirements => $requirements,
    owner        => 'vagrant',
    group        => 'vagrant',
  }
}


class vagrant::python::django (
  $virtualenv    = '/home/vagrant/venv',
  $packages      = undef,
  $base_packages = [
    'django-debug-toolbar',
    'ipython',
    'django-bootstrap3',
    'django-extensions',
    'django_tables2',
    'django_simple_menu',
    'ipaddress',
  ],
) {
  class { 'vagrant::python::venv':
    virtualenv => $virtualenv
  }
  python::pip { 'django' :
    virtualenv => $virtualenv,
    owner      => 'vagrant',
  }
  python::pip { $base_packages:
    virtualenv => $virtualenv,
    owner      => 'vagrant',
  }
  python::pip { $packages:
    virtualenv => $virtualenv,
    owner      => 'vagrant',
  }
}
