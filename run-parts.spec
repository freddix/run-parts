Summary:	Runs scripts or programs in a directory
Name:		run-parts
Version:	4.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://ftp.debian.org/debian/pool/main/d/debianutils/debianutils_%{version}.tar.gz
# Source0-md5:	c0cb076754d7f4eb1e3397d00916647f
URL:		http://packages.qa.debian.org/d/debianutils.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Runs all the executable files found in directory <directory>.

%prep
%setup -qn debianutils-%{version}

%build
%configure
%{__make} run-parts

%install
rm -rf $RPM_BUILD_ROOT

install -D run-parts $RPM_BUILD_ROOT%{_bindir}/run-parts
install -D run-parts.8 $RPM_BUILD_ROOT%{_mandir}/man8/run-parts.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/run-parts
%{_mandir}/man8/run-parts.8*


