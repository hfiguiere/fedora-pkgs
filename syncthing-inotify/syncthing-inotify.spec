%define debug_package %{nil}

Name:           syncthing-inotify
Version:        0.7
Release:        2%{?dist}
Summary:        Syncthing
License:        MIT
URL:            http://syncthing.net/

Source0:        syncthing-inotify-%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  systemd

BuildRequires:  golang-github-cenkalti-backoff-devel
BuildRequires:  golang-github-zillode-notify-devel

ExclusiveArch:  %{go_arches}


%description
Syncthing replaces Dropbox and BitTorrent Sync with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

Using syncthing, that control is returned to you.


%prep
%setup -q -n syncthing-inotify-%{version}


%build
mkdir -p ./_build/src/github.com/syncthing
ln -s $(pwd) ./_build/src/github.com/syncthing/syncthing-inotify

export GOPATH=$(pwd)/_build:%{gopath}
go build


%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 syncthing-inotify-%{version} %{buildroot}%{_bindir}/syncthing-inotify

mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/usr/lib/systemd/user

install -p -m 0644 etc/linux-systemd/user/syncthing-inotify.service %{buildroot}/usr/lib/systemd/user/
install -p -m 0644 etc/linux-systemd/system/syncthing-inotify@.service %{buildroot}/usr/lib/systemd/system/


%clean
rm -rf %{buildroot}


%post
%systemd_post syncthing-inotify@.service

%preun
%systemd_preun syncthing-inotify@.service

%postun
%systemd_postun_with_restart syncthing-inotify@.service


%files
%{_bindir}/syncthing-inotify
/usr/lib/systemd/system/syncthing-inotify@.service
/usr/lib/systemd/user/syncthing-inotify.service


%changelog
* Sun Apr 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7-2
- Fix version usage in scripts.

* Sun Apr 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.7-1
- Update to version 0.7.

* Wed Feb 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.8-4
- undo fix rhel build. doesn't work.

* Wed Feb 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.8-3
- Try to fix rhel7 build.

* Tue Feb 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.8-2
- rebuild for golang1.6

* Mon Jan 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.6.8-1
- Initial package for syncthing repo.

