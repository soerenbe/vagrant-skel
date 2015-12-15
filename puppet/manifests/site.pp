node default {
  include vagrant
  #include vagrant::apache
  #include vagrant::python::venv
  #include vagrant::python::django
}
