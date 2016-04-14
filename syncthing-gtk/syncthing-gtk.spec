%define debug_package %{nil}

Name:           syncthing-gtk
Version:        0.8.3
Release:        2%{?dist}
Summary:        Syncthing GTK+ GUI
License:        GPLv2
URL:            http://syncthing.net/

Source0:        https://github.com/syncthing/%{name}/archive/v%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  desktop-file-utils

Requires:       syncthing >= 0.12
Requires:       hicolor-icon-theme

Requires:       psmisc
Requires:       pygobject2
Requires:       python-dateutil

%if 0%{?fedora}
Recommends:     python-inotify
%else
Requires:       python-inotify
%endif


%description
Syncthing replaces Dropbox and BitTorrent Sync with something open, trustworthy and decentralized. Your data is your data alone and you deserve to choose where it is stored, if it is shared with some third party and how it's transmitted over the Internet.

Using syncthing, that control is returned to you.

This package contains the GTK+ GUI for syncthing.


%prep
%setup -q


%build
%py2_build


%install
%py2_install
%find_lang syncthing-gtk


%check
# desktop-file-validate %{buildroot}/%{_datadir}/applications/syncthing-gtk.desktop


%clean
rm -rf %{buildroot}


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f syncthing-gtk.lang
%license LICENSE

%{_bindir}/syncthing-gtk

%{_datadir}/applications/syncthing-gtk.desktop

%{_datadir}/icons/hicolor/*/apps/syncthing-gtk.png
%{_datadir}/icons/hicolor/64x64/apps/syncthing-gtk-error.png

%{_datadir}/icons/hicolor/16x16/apps/si-*.png
%{_datadir}/icons/hicolor/24x24/apps/si-*.png
%{_datadir}/icons/hicolor/32x32/apps/si-*.png

%{_datadir}/icons/hicolor/64x64/emblems/emblem-syncthing*.png
%{_datadir}/pixmaps/syncthing-gtk.png
%{_datadir}/syncthing-gtk/

%{python2_sitelib}/syncthing_gtk-v%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/syncthing_gtk/


%changelog
* Thu Mar 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.8.3-2
- Fix build on dists without support for Recommends: tag.

* Thu Mar 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.8.3-1
- Update to version 0.8.3.

* Wed Jan 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.8.2-2
- Add Requires: python-inotify.

* Mon Jan 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.8.2-1
- Update to version 0.8.2.

* Sun Dec 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.1-1
- Update to version 0.8.1.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8.0.1-1
- Update to version 0.8.0.1. Fixes two minor bugs.

* Fri Nov 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.8-1
- Update to (incompatible) version 0.8.

* Mon Oct 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.7.6.1-2
- Update icon database correctly.

* Mon Oct 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.7.6.1-1
- Update to version 0.7.6.1.

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.7.6-1
- Update to version 0.7.6.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.7.5.1-2
- Fix spec to include neccessary python module and package dependencies.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.7.5.1-1
- Initial package.


