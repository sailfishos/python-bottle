%global __pythonapp_requires %nil

Name:           python3-bottle
Version:        0.13.3
Release:        0
Summary:        Fast and simple WSGI-framework for small web-applications

License:        MIT
URL:            https://github.com/sailfishos/python-bottle
Source0:        %{name}-%{version}.tar.gz
Patch1:		0001-Remove-shebang.patch
Patch2:         0002-Remove-scripts-from-setup.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Bottle is a fast and simple micro-framework for small web-applications.
It offers request dispatching (Routes) with URL parameter support, Templates,
a built-in HTTP Server and adapters for many third party WSGI/HTTP-server and
template engines. All in a single file and with no dependencies other than the
Python Standard Library.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc AUTHORS README.rst
%{_bindir}/bottle
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/*.py
