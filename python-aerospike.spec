# Created by pyp2rpm-1.1.2
%global pypi_name aerospike
%global py_ver 2.7

Name:           python-%{pypi_name}
Version:        1.0.45
Release:        1%{?dist}
Summary:        Aerospike Client Library for Python

License:        ASL %(TODO: version)s
URL:            http://aerospike.com
Source0:        https://pypi.python.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python2-devel


%description
Aerospike Python Client
=======================
|Build| |Release| |Downloads|
|License|

.. |Build| image:: https://travis-ci.org/aerospike/aerospike-client-
python.svg?branch=master
.. |Release| image::
https://pypip.in/version/aerospike/badge.svg
.. |Downloads| image::
https://pypip.in/download/aerospike/badge.svg
.. |License| image:: ...


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc README.rst LICENSE
%{python2_sitearch}/%{pypi_name}.so
%{python_sitearch}/%{pypi_name}-%{version}-py%{py_ver}.egg-info
/usr/aerospike/lua/aerospike.lua
/usr/aerospike/lua/as.lua
/usr/aerospike/lua/stream_ops.lua
#/usr/lib64/python2.7/site-packages/aerospike.so

%changelog
* Wed Jun 17 2015 root - 1.0.45-1
- Initial package.
