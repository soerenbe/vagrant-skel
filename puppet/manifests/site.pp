node default {
  include vagrant

  # If you enable this make sure you also have enabled the puppetlabs-apache module in scripts/puppet.sh
  #include vagrant::apache

  # If you enable one of this make sure you also have enabled the stankevich-python module in scripts/puppet.sh
  #include vagrant::python::venv
  #include vagrant::python::django
}
