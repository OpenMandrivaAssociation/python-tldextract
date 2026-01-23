Name:		python-tldextract
Version:	5.3.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/tldextract/tldextract-%{version}.tar.gz
Summary:        Accurately separate the TLD from the registered domain and subdomains of a URL
URL:		https://pypi.org/project/tldextract/
License:	BSD-3-Clause
Group:		Development/Python
BuildRequires:	python
# testing
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-mock)
BuildRequires:	python%{pyver}dist(responses)

BuildSystem:	python

BuildArch:	noarch

%description
Accurately separate the TLD from the registered domain and
subdomains of a URL, using the Public Suffix List. By default,
this includes the public ICANN TLDs and their exceptions. You can
optionally support the Public Suffix List's private domains as
well.

%files
%doc README.md
%{_bindir}/tldextract
%{py_sitedir}/tldextract
%{py_sitedir}/tldextract-*.*-info

