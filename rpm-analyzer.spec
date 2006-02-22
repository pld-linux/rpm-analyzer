Summary:	A graphical interface for RPM analyze
Name:		rpm-analyzer
Version:	1.0
Release:	1
Source0:	%{name}-%{version}.tar.bz2
#Source0-MD5:	af90f4cb43b21f4597a2fd3b6eb80f5d
Patch0:		%{name}-fhs.patch
License:	GPL
Group:		Applications
Requires:	python >= 2.2
Requires:	python-libxml2
Requires:	python-pygtk-gtk >= 2.0
Requires:	python-rhpl
Requires:	python-rpm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rpm-analyzer provides a graphical interface that allows the user to
view a RPM dependencies according to the local rpm configuration or a
user-defined rpm configuration. This tool is hdlist based and may
require a comps.xml file for some features so please consider
installing comps.

%prep
%setup -q
%patch0 -p1

%build
%{__make}
sed -ie 's!/usr/bin/python2!/usr/bin/python!g' src/*.py

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_bindir} install
%{__make} MANDIR=$RPM_BUILD_ROOT/%{_mandir} install-man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING Changelog
%attr(755,root,root) %{_bindir}/rpm-analyzer
%dir %{_datadir}/rpm-analyzer
%{_datadir}/rpm-analyzer/*.py
%dir %{_datadir}/rpm-analyzer/package_mgr
%{_datadir}/rpm-analyzer/package_mgr/*.py
%{_mandir}/man1/rpm-analyzer.*
