# Created by pyp2rpm-1.1.2
%global pypi_name psycopg2

Name:           python-%{pypi_name}
Version:        2.6
Release:        1%{?dist}
Summary:        psycopg2 - Python-PostgreSQL Database Adapter

License:        LGPL and ZPLv%(TODO: version)s
URL:            http://initd.org/psycopg/
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python2-devel
BuildRequires:  python-sphinx
BuildRequires:  postgresql-devel

%description
Psycopg is the most popular PostgreSQL database adapter for the Python
programming language.  Its main features are the complete implementation of
the
Python DB API 2.0 specification and the thread safety (several threads can
share the same connection).  It was designed for heavily multi-threaded
applications that create and destroy lots of cursors and make a large number
of
concurrent "INSERT"s ...


%prep
%setup -q -n %{pypi_name}-%{version}

# generate html docs 
sphinx-build doc/src html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}



%files
%doc html README.rst LICENSE doc/COPYING.LESSER
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Jun 04 2015 John Doe <john@doe.com> - 2.6-1
- Initial package.
