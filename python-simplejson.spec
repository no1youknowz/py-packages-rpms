# Created by pyp2rpm-1.1.2
%global pypi_name simplejson

Name:           python-%{pypi_name}
Version:        3.7.3
Release:        1%{?dist}
Summary:        Simple, fast, extensible JSON encoder/decoder for Python

License:        AFL and MIT
URL:            http://github.com/simplejson/simplejson
Source0:        https://pypi.python.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python2-devel


%description
simplejson is a simple, fast, complete, correct and extensible
JSON
<http://json.org> encoder and decoder for Python 2.5+
and Python 3.3+.  It is
pure Python code with no dependencies,
but includes an optional C extension for
a serious speed boost.

The latest documentation for simplejson can be read
online here:
http://simplejson.readthedocs.org/

simplejson is the externally
maintained ...


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info



%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc README.rst LICENSE.txt
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Jun 17 2015 root - 3.7.3-1
- Initial package.