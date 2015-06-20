# Created by pyp2rpm-1.1.2
%global pypi_name pyzmq
%global py_ver 2.7

Name:           python-%{pypi_name}
Version:        14.6.0
Release:        1%{?dist}
Summary:        Python bindings for 0MQ

License:        BSD and LGPL
URL:            http://github.com/zeromq/pyzmq
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-sphinx
BuildRequires:  zeromq-devel

%description
PyZMQ is the official Python binding for the ZeroMQ Messaging Library
(http://www.zeromq.org).

%prep
%setup -q -n %{pypi_name}-%{version}
find examples zmq -name "*.py" -exec sed -i "s|#\!\/usr\/bin\/env python||" {} \;

# generate html docs 
sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING.LESSER README.md examples docs
%{python_sitearch}/zmq/
%{python_sitearch}/%{pypi_name}-%{version}-py%{py_ver}.egg-info
%exclude %{python_sitearch}/zmq/utils/*.h

%changelog
* Thu Jun 04 2015 John Doe <john@doe.com> - 14.6.0-1
- Initial package.
