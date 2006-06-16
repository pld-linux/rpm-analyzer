Summary:	A graphical interface for RPM analyze
Summary(pl):	Graficzny interfejs do analizy pakietów RPM
Name:		rpm-analyzer
Version:	1.22
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.maisondubonheur.com/rpm-analyzer/dl/%{name}-%{version}.tar.bz2
# Source0-md5:	438175254630409300c656a89c08f406
URL:		http://www.maisondubonheur.com/rpm-analyzer/
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

%description -l pl
rpm-analyzer udostêpnia graficzny interfejs pozwalaj±cy ogl±daæ
zale¿no¶ci pakietów RPM zgodnie z lokaln± lub zdefiniowan± przez
u¿ytkownika konfiguracj± rpm-a. To narzêdzie jest oparte o hdlist i
mo¿e wymagaæ do niektórych opcji pliku comps.xml, wiêc warto rozwa¿yæ
doinstalowanie comps.

%prep
%setup -q

%build
%{__make}
sed -ie 's!/usr/bin/python2!/usr/bin/python!g' src/*.py

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}
%{__make} install-man \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog
%attr(755,root,root) %{_bindir}/rpm-analyzer
%dir %{_datadir}/rpm-analyzer
%{_datadir}/rpm-analyzer/*.py
%dir %{_datadir}/rpm-analyzer/package_mgr
%{_datadir}/rpm-analyzer/package_mgr/*.py
%{_mandir}/man1/rpm-analyzer.*
