%define date 160414
%define rev 82bdda6f

Summary:        sysprof
Name:           sysprof
Version: 3.19.90~git%{date}~%{rev}
Release: 2%{?dist}
License:        GPLv2+, GPLv3+
URL:            http://git.gnome.org/browse/sysprof

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  desktop-file-utils

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  libtool
BuildRequires:  polkit-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       dbus

%{?systemd_requires}


%description
Sysprof is a statistical, system-wide profiler for Linux.

Features:

- Detailed, accurate, and fast profiling of the entire Linux system, including the kernel and all userspace applications
- No recompiling necessary
- Load and Save> profiles
- Fast, no-nonsense graphical user interface
- Command line tool included


%package        devel
Summary:        sysprof development files
%description    devel
Sysprof is a statistical, system-wide profiler for Linux.

Features:

- Detailed, accurate, and fast profiling of the entire Linux system, including the kernel and all userspace applications
- No recompiling necessary
- Load and Save> profiles
- Fast, no-nonsense graphical user interface
- Command line tool included

This package includes the development files.


%prep
%autosetup


%build
autoreconf --install
%configure --disable-static
%make_build


%install
%make_install

rm -rf %{buildroot}/%{_libdir}/*.la

# %%find_lang %%{name}
rm -rf %{buildroot}/%{_datadir}/locale


%clean
rm -rf %{buildroot}


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/*.desktop


%post
%systemd_post sysprofd.service
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
/usr/bin/update-desktop-database -q &> /dev/null ||:

%preun
%systemd_preun sysprofd.service

%postun
%systemd_postun_with_restart sysprofd.service

if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/update-desktop-database -q &> /dev/null ||:
fi


%files
#%%files -f sysprof.lang
%{_bindir}/sysprof
%{_bindir}/sysprof-cli

%{_libdir}/libsysprof-2.so
%{_libdir}/libsysprof-ui-2.so

%{_libexecdir}/sysprof/

%{_unitdir}/sysprof2.service

%{_datadir}/applications/org.gnome.Sysprof2.desktop
%{_datadir}/dbus-1/system-services/org.gnome.Sysprof2.service
%{_datadir}/dbus-1/system.d/org.gnome.Sysprof2.conf
%{_datadir}/glib-2.0/schemas/org.gnome.sysprof2.gschema.xml
%{_datadir}/help/*/sysprof/
%{_datadir}/icons/hicolor/*/apps//sysprof.png
%{_datadir}/icons/hicolor/scalable/apps/sysprof-symbolic.svg
%{_datadir}/mime/packages/sysprof-mime.xml
%{_datadir}/polkit-1/actions/org.gnome.sysprof2.policy


%files      devel
%{_libdir}/pkgconfig/sysprof-2.pc
%{_libdir}/pkgconfig/sysprof-ui-2.pc

%{_includedir}/sysprof-2/


%changelog
* Thu Apr 14 2016 Fabio Valentini <decathorpe@gmail.com> - 3.19.90~git160414~82bdda6f-2
- packaging updates
- include localisation and localised help

* Thu Apr 14 2016 Fabio Valentini <decathorpe@gmail.com> - 3.19.90~git160414~82bdda6f-1
- Update to new upstream snapshot.

* Thu Apr 14 2016 Fabio Valentini <decathorpe@gmail.com> - 3.19.90~git160414~5d25b8a2-3
- split off devel package to avoid pulling in dependencies
- add systemd scriptlets as required

* Thu Apr 14 2016 Fabio Valentini <decathorpe@gmail.com> - 3.19.90~git160414~5d25b8a2-2
- Packaging updates.

* Thu Apr 14 2016 Fabio Valentini <decathorpe@gmail.com> - 3.19.90~git160414~5d25b8a2-1
- Initial package of sysprof2.
