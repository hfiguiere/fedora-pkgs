%global debug_package %{nil}

Name:           syncthing
Version:        0.12.22
Release:        1%{?dist}
Summary:        Syncthing
License:        MIT
URL:            http://syncthing.net/

Source0:        https://github.com/syncthing/syncthing/releases/download/v%{version}/syncthing-source-v%{version}.tar.gz

Source1:        syncthing.service
Source2:        syncthing@.service


BuildRequires:  golang
BuildRequires:  systemd

ExclusiveArch:  %{go_arches}


%if 0%{?fedora}
Requires:	syncthing-inotify
%endif


%description
Syncthing replaces Dropbox and BitTorrent Sync with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

Using syncthing, that control is returned to you.


%prep
%setup -q -n syncthing


%build
mkdir -p ./_build/src/github.com/syncthing
ln -s $(pwd) ./_build/src/github.com/syncthing/syncthing

export GOPATH=$(pwd)/_build:%{gopath}
go run build.go -no-upgrade


%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 bin/* %{buildroot}%{_bindir}/

mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/usr/lib/systemd/user

%if 0%{?rhel}
install -p -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/user/
install -p -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/
%endif

%if 0%{?fedora}
install -p -m 0644 etc/linux-systemd/system/syncthing@.service %{buildroot}/usr/lib/systemd/system/
install -p -m 0644 etc/linux-systemd/system/syncthing-resume.service %{buildroot}/usr/lib/systemd/system/
install -p -m 0644 etc/linux-systemd/user/syncthing.service %{buildroot}/usr/lib/systemd/user/
%endif


%clean
rm -rf %{buildroot}


%files
%license LICENSE

%{_bindir}/*
/usr/lib/systemd/system/syncthing@.service
/usr/lib/systemd/user/syncthing.service

%if 0%{?fedora}
/usr/lib/systemd/system/syncthing-resume.service
%endif


%changelog
* Wed Apr 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.22-1
- Update to version 0.12.22.

* Wed Mar 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.21-1
- Update to version 0.12.21.

* Sun Mar 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.20-2
- Fix build on epel7.

* Sun Mar 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.20-1
- Update to version 0.12.20.
- add syncthing-resume.service

* Tue Feb 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.19-2
- rebuild for golang1.6

* Sun Feb 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.19-1
- Update to version 0.12.19.

* Mon Feb 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.18-1
- Update to version 0.12.18.

* Sun Jan 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.17-1
- Update to version 0.12.17.

* Sun Jan 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.16-1
- Update to version 0.12.16.

* Sun Jan 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.15-3
- Fix build on RHEL.

* Mon Jan 18 2016 Fabio Valentini <decathorpe@gmail.com>
- Try enabling syncthing-inotify on fedora (does not build on rhel).

* Mon Jan 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.15-1
- Update to version 0.12.15.

* Fri Jan 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.14-1
- Update to version 0.12.14.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.12-1
- Update to version 0.12.12.

* Tue Jan 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.12.11-1
- Update to version 0.12.11.

* Mon Dec 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.12.10-1
- Update to version 0.12.10.

* Sun Dec 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.12.9-1
- Update to version 0.12.8.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.12.8-1
- Update to version 0.12.8.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.12.7-1
- Update to version 0.12.7.

* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.12.6-1
- Update to version 0.12.6.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.12.4-1
- Update to version 0.12.4.

* Mon Nov 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.12.3-1
- Update to release 0.12.3.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.12.2-1
- Update to upstream release 0.12.2.

* Fri Nov 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.12.1-1
- Update to version 0.12.1.

* Fri Nov 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.12.0-1
- Update to (incompatible) version 0.12.0.

* Mon Oct 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.11.26-3
- Use modified upstream systemd units (without syncthing-inotify dep).

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.11.26-2
- Use upstream systemd units.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.11.26-1
- Update to version v0.11.26.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.11.25-1
- Update to version v0.11.25.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.11.24-1
- Update to version 0.11.24.

* Sat Sep 20 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.17-2.0
- Version update to v0.9.17

* Fri Sep 12 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.15-9
- Version update to v0.9.15

* Wed Sep 10 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.14-8
- Version updated to v0.9.14
- Spec files fixed

* Tue Sep 9 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.13-7
- Version updated to v0.9.13

* Mon Sep 1 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.10-6
- Version updated to v0.9.10
- Spec files dates fixed and re-checked.

* Wed Aug 27 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.9-5
- Version updated to v0.9.9
- Readme fixes
- Source folder path fixed

* Mon Aug 25 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.8-4
- Version updated to v0.9.8

* Sun Aug 17 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.5-3
- Version updated to v0.9.5

* Sat Aug 16 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.9.4-2
- Version updated to v0.9.4

* Mon Jul 28 2014 Onuralp SEZER <thunderbirdtr@fedoraproject.org> 0.8.21-1
- Initial Version
