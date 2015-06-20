# Created by pyp2rpm-1.1.2
%global pypi_name redis
%global version 2.7

Name:           python-%{pypi_name}
Version:        2.10.3
Release:        1%{?dist}
Summary:        Python client for Redis key-value store

License:        MIT
URL:            http://github.com/andymccurdy/redis-py
Source0:        https://pypi.python.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
#BuildRequires:  python-pytest >= 2.5.0


%description
redis-py
========

The Python interface to the Redis key-value store.

..
image:: https://secure.travis-ci.org/andymccurdy/redis-py.png?branch=master
:target: http://travis-ci.org/andymccurdy/redis-py

Installation
------------
redis-py requires a running Redis server. See `Redis's quickstart
<http://redis.io/topics/quickstart>`_ for installation instructions.

To
install redis-py, ...


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc README.rst LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sat Jun 20 2015 root - 2.10.3-1
- Initial package.
