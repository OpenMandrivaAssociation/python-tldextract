%define module tldextract

Name:		python-tldextract
Version:	5.3.1
Release:	2
Summary:        Accurately separate the TLD from the registered domain and subdomains of a URL
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/tldextract/
Source0:	https://files.pythonhosted.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
# testing
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-mock)
BuildRequires:	python%{pyver}dist(responses)

%description
Accurately separate the TLD from the registered domain and
subdomains of a URL, using the Public Suffix List. By default,
this includes the public ICANN TLDs and their exceptions. You can
optionally support the Public Suffix List's private domains as
well.

%prep -a
# Remove bumdled egg-info
rm -rf %{module}.egg-info

%files
%doc README.md
%{_bindir}/tldextract
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
