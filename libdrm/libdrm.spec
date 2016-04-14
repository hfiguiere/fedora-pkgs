%define date 160413
%define rev cc9a53f0

Summary:        Direct Rendering Manager headers and kernel modules
Name:           libdrm
Version: 2.4.67~git%{date}~%{rev}
Release: 1%{?dist}
License:        MIT
URL:            http://www.mesa3d.org

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildRequires:  docbook-style-xsl
BuildRequires:  kernel-headers
BuildRequires:  libatomic_ops-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  xorg-x11-util-macros

%ifnarch s390
BuildRequires:  valgrind-devel
%endif

Requires:       systemd


%description
Direct Rendering Manager headers and kernel modules.


%package devel
Summary: Direct Rendering Manager headers and kernel modules
%description devel
Direct Rendering Manager headers and kernel modules.
This package contains the development headers.


%package -n drm-utils
Summary: Direct Rendering Manager utilities
Group: Development/Tools

%description -n drm-utils
Utility programs for the kernel DRM interface.  Will void your warranty.


%prep
%autosetup


%build
autoreconf --install
%configure \
    --enable-install-test-programs \
    --enable-udev
%make_build


%install
%make_install
rm %{buildroot}/%{_libdir}/*.la


%clean
rm -rf %{buildroot}

%check


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig


%files
%doc README
%{_libdir}/libdrm.so.*
%{_libdir}/libdrm_amdgpu.so.*
%{_libdir}/libdrm_intel.so.*
%{_libdir}/libdrm_nouveau.so.*
%{_libdir}/libdrm_radeon.so.*
%{_libdir}/libkms.so.*

%{_mandir}/*/*

%files devel
%{_includedir}/xf86drm.h
%{_includedir}/xf86drmMode.h
%{_includedir}/libdrm/
%{_includedir}/libkms/

%{_libdir}/libdrm.so
%{_libdir}/libdrm_amdgpu.so
%{_libdir}/libdrm_intel.so
%{_libdir}/libdrm_nouveau.so
%{_libdir}/libdrm_radeon.so
%{_libdir}/libkms.so
%{_libdir}/pkgconfig/*.pc

%files -n drm-utils
%{_bindir}/kms-steal-crtc
%{_bindir}/kms-universal-planes
%{_bindir}/kmstest
%{_bindir}/modeprint
%{_bindir}/modetest
%{_bindir}/proptest
%{_bindir}/vbltest


%changelog
* Wed Apr 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.67~git160413~cc9a53f0-1
- Update to new upstream snapshot.

* Thu Apr 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.67~git160408~65ea85d8-1
- Update to new upstream snapshot.

* Tue Mar 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.67~git160329~ea78c178-1
- Update to new upstream snapshot.

* Mon Mar 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.67~git160314~49041c36-1
- Update to new upstream snapshot.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.67~git160303~ea07de92-1
- Update to new upstream snapshot.

* Fri Feb 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.67~git160226~42745396-1
- Update to new upstream snapshot.

* Wed Feb 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.67~git160224~db7202d1-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.67~git160219~99ede3e6-1
- Update to new upstream snapshot.

* Mon Feb 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.67~git160216~add89360-1
- Update to new upstream snapshot.

* Sat Feb 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.66~git160213~9b77443f-1
- Update to new upstream snapshot.

* Thu Feb 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.66~git160211~f884af9b-1
- Update to new upstream snapshot.

* Thu Feb 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.66~git160204~682eaa05-1
- Update to new upstream snapshot.

* Thu Jan 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.66~git160129~432e08de-1
- Update to new upstream snapshot.

* Thu Jan 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.66~git160129~432e08de-1
- Update to new upstream snapshot.

* Thu Jan 28 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.66~git160129~432e08de-1
- Update to new upstream snapshot.

* Tue Jan 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.66~git160126~ff0c9caa-1
- Update to new upstream snapshot.

* Sun Jan 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.66~git160125~798022b6-1
- Update to new upstream snapshot.

* Fri Jan 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.66~git160122~3627f38d-1
- Update to new upstream snapshot.

* Wed Jan 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.66~git160120~25712f1d-1
- Update to new upstream snapshot.

* Thu Jan 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.4.66~git160107~e342c0fc-1
- Update to new upstream snapshot.

* Fri Dec 25 2015 Fabio Valentini <decathorpe@gmail.com> - 2.4.66~git151225~b38a4b23-1
- Initial package for mesa-git copr.


