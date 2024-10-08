%define dir /usr/libexec/argo/probes/globus

Summary: ARGO probes for Globus Toolkit services
Name: argo-probe-globus
Version: 0.3.0
Release: 1%{?dist}
License: ASL 2.0
Group: Network/Monitoring
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: perl-GridMon >= 1.0.28
Requires: voms-clients
Requires: globus-proxy-utils
Requires: uberftp
Requires: globus-gass-copy-progs

%description

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install --directory ${RPM_BUILD_ROOT}%{dir}
install --mode 755 ./GridFTP-probe  ${RPM_BUILD_ROOT}%{dir}
install --mode 755 ./GridProxy-probe  ${RPM_BUILD_ROOT}%{dir}
install --mode 755 ./refresh_proxy ${RPM_BUILD_ROOT}%{dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{dir}/GridFTP-probe
%{dir}/GridProxy-probe
%{dir}/refresh_proxy

%changelog
* Wed Aug 14 2024 Katarina Zailac <kzailac@srce.hr> - 0.3.0-1%{?dist}
- Migrate argo-probe-globus to Rocky 9
- Remove GRAM-probe & MyProxy-probe
* Wed Aug 31 2022 Katarina Zailac <kzailac@srce.hr> - 0.2.0-1%{?dist}
- Version bump.
* Thu May 4 2017 Emir Imamagic <eimamagi@srce.hr> - 0.1.5-1%{?dist}
- Version bump.
* Fri Feb 10 2017 Emir Imamagic <eimamagi@srce.hr> - 0.1.4-1%{?dist}
- Robot-based proxy should be RFC
* Fri Feb 10 2017 Emir Imamagic <eimamagi@srce.hr> - 0.1.3-1%{?dist}
- Removed CertLifetime-probe (nagios-plugins-cert)
- Probes location aligned with guidelines
* Wed Apr 6 2016 Emir Imamagic <eimamagi@srce.hr> - 0.1.2-1%{?dist}
- Modified MyProxy-probe not to enforce legacy proxy
* Thu Mar 24 2016 Emir Imamagic <eimamagi@srce.hr> - 0.1.1-1%{?dist}
- Changed default protocol to tls1 in CertLifetime probe 
* Fri Sep 18 2015 Emir Imamagic <eimamagi@srce.hr> - 0.1.0-1%{?dist}
- Initial version of Globus probes for Nagios
