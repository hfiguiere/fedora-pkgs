Name:           obs-studio
Version:        0.13.2
Release:        1%{dist}
Summary:        Cross-platform video recording and streaming
License:        GPLv2
URL:            https://obsproject.com

Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gcc-objc

BuildRequires:  x264-devel

BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(zlib)


%description
This project is a rewrite of what was formerly known as "Open Broadcaster Software", software originally designed for recording and streaming live video content, efficiently.


%package        devel
Summary:        Cross-platform video recording and streaming (dev files)
%description    devel
This project is a rewrite of what was formerly known as "Open Broadcaster Software", software originally designed for recording and streaming live video content, efficiently.

This package contains the development headers.


%prep
%autosetup


%build
%cmake -DUNIX_STRUCTURE=1 -DCMAKE_INSTALL_PREFIX=/usr
%make_build


%install
%make_install


%clean
rm -rf %{buildroot}


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/obs.desktop


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig


%files
%{_bindir}/obs

/usr/lib/libobs*.so.0
/usr/lib/libobs*.so.0.0
/usr/lib/obs-plugins/

%{_datadir}/applications/obs.desktop
%{_datadir}/icons/hicolor/*/apps/obs.png
%{_datadir}/obs/


%files devel
%{_includedir}/obs/

/usr/lib/cmake/LibObs/
/usr/lib/libobs*.so


%changelog
* Tue Feb 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.13.2-1
- Update to version 0.13.2.

* Fri Feb 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.13.1-1
- Update to version 0.13.1.

* Thu Jan 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.13.0-1
- Update to version 0.13.0.

* Mon Dec 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.12.4-2
- Enable jack. Clean up spec.

* Mon Dec 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.12.4-1
- Initial package.


