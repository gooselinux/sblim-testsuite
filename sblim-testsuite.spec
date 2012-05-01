%define debug_package %{nil}

Name:           sblim-testsuite
Version:        1.3.0
Release:        1%{?dist}
Summary:        SBLIM testsuite

Group:          Applications/System
License:        EPL
URL:            http://sblim.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       perl >= 5.6
Requires:       sblim-wbemcli >= 1.5

%description
SBLIM automated testsuite scripts.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}-%{version}
%{_datadir}/%{name}
%{_localstatedir}/lib/%{name}

%changelog
* Wed Jun 30 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.3.0-1
- Update to sblim-testsuite-1.3.0

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.2.5-4.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov  4 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.2.5-2
- Remove debug package, fix URL, make setup quiet
- Spec file cleanup, rpmlint check

* Fri Oct 24 2008 Vitezslav Crhonek <vcrhonek@redhat.com> - 1.2.5-1
- Update to 1.2.5
  Resolves: #468327

* Thu Oct 28 2005 Viktor Mihajlovski <mihajlov@de.ibm.com> - 1.2.4-1
- New release

* Thu Jul 28 2005 Viktor Mihajlovski <mihajlov@de.ibm.com> - 1.2.3-0
- Updates for rpmlint complaints
