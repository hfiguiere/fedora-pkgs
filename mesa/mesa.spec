%define date 160414
%define rev 171a570f

%if 0%{?rhel}
%define with_private_llvm 1
%define with_wayland 0
%else
%define with_private_llvm 0
%define with_wayland 1
%endif

# S390 doesn't have video cards, but we need swrast for xserver's GLX
# llvm (and thus llvmpipe) doesn't actually work on ppc32
%ifnarch s390 ppc
%define with_llvm 1
%endif

%define min_wayland_version 1.0
%if 0%{?with_llvm}
%define with_radeonsi 1
%endif

%ifarch s390 s390x ppc
%define with_hardware 0
%define base_drivers swrast
%else
%define with_hardware 1
%define with_vdpau 1
%define with_vaapi 1
%define with_nine 1
%define base_drivers swrast,nouveau,radeon,r200
%endif
%ifarch %{ix86} x86_64
%define platform_drivers ,i915,i965
%define with_ilo    1
%define with_vmware 1
%define with_xa     1
%define with_opencl 1
%define with_omx    1
%endif
%ifarch %{arm} aarch64
%define with_vc4       1
%define with_freedreno 1
%define with_xa        1
%define with_omx       1
%endif

%define dri_drivers --with-dri-drivers=%{?base_drivers}%{?platform_drivers}

Summary:        Mesa graphics libraries
Name:           mesa
Version: 11.3.0~devel~git%{date}~%{rev}
Release: 1%{?dist}
License:        MIT
Group:          System Environment/Libraries
URL:            http://www.mesa3d.org

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

# To have sha info in glxinfo
BuildRequires:  git-core

BuildRequires:  pkgconfig autoconf automake libtool
%if %{with_hardware}
BuildRequires:  kernel-headers
BuildRequires:  xorg-x11-server-devel
%endif
BuildRequires:  libdrm-devel >= 2.4.42
BuildRequires:  libXxf86vm-devel
BuildRequires:  expat-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  makedepend
BuildRequires:  libselinux-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libxshmfence-devel
BuildRequires:  elfutils
BuildRequires:  python
BuildRequires:  gettext
%if 0%{?with_llvm}
%if 0%{?with_private_llvm}
BuildRequires:  mesa-private-llvm-devel
%else
BuildRequires:  llvm-devel >= 3.4-7
%if 0%{?with_opencl}
BuildRequires:  clang-devel >= 3.0
%endif
%endif
%endif
BuildRequires:  elfutils-libelf-devel
BuildRequires:  libxml2-python
BuildRequires:  libudev-devel
BuildRequires:  bison flex
%if 0%{?with_wayland}
BuildRequires:  pkgconfig(wayland-client) >= %{min_wayland_version}
BuildRequires:  pkgconfig(wayland-server) >= %{min_wayland_version}
%endif
%if 0%{?with_vdpau}
BuildRequires:  libvdpau-devel
%endif
%if 0%{?with_vaapi}
BuildRequires:  libva-devel
%endif
BuildRequires:  zlib-devel
%if 0%{?with_omx}
BuildRequires:  libomxil-bellagio-devel
%endif
%if 0%{?with_opencl}
BuildRequires:  libclc-devel llvm-static opencl-filesystem
%endif
BuildRequires:  python-mako

%description
Mesa

%package        libGL
Summary:        Mesa libGL runtime libraries and DRI drivers
Group:          System Environment/Libraries
Provides:       libGL
%description    libGL
Mesa libGL runtime library.

%package        libEGL
Summary:        Mesa libEGL runtime libraries
Group:          System Environment/Libraries
%description    libEGL
Mesa libEGL runtime libraries

%package        libGLES
Summary:        Mesa libGLES runtime libraries
Group:          System Environment/Libraries
%description    libGLES
Mesa GLES runtime libraries

%package        filesystem
Summary:        Mesa driver filesystem
Group:          User Interface/X Hardware Support
Provides:       mesa-dri-filesystem = %{version}-%{release}
Obsoletes:      mesa-dri-filesystem < %{version}-%{release}
%description    filesystem
Mesa driver filesystem

%package        dri-drivers
Summary:        Mesa-based DRI drivers
Group:          User Interface/X Hardware Support
Requires:       mesa-filesystem%{?_isa}
Obsoletes:      mesa-dri-drivers-dri1 < 7.12
Obsoletes:      mesa-dri-llvmcore <= 7.12
%description    dri-drivers
Mesa-based DRI drivers.

%if 0%{?with_omx}
%package        omx-drivers
Summary:        Mesa-based OMX drivers
Group:          User Interface/X Hardware Support
Requires:       mesa-filesystem%{?_isa}
Requires:       libomxil-bellagio%{?_isa}
%description    omx-drivers
Mesa-based OMX drivers.
%endif

%if 0%{?with_vdpau}
%package        vdpau-drivers
Summary:        Mesa-based DRI drivers
Group:          User Interface/X Hardware Support
Requires:       mesa-filesystem%{?_isa}
%description    vdpau-drivers
Mesa-based VDPAU drivers.
%endif

%package        libGL-devel
Summary:        Mesa libGL development package
Group:          Development/Libraries
Requires:       mesa-libGL = %{version}-%{release}
Requires:       gl-manpages
Provides:       libGL-devel
%description    libGL-devel
Mesa libGL development package

%package        libEGL-devel
Summary:        Mesa libEGL development package
Group:          Development/Libraries
Requires:       mesa-libEGL = %{version}-%{release}
Provides:       khrplatform-devel = %{version}-%{release}
Obsoletes:      khrplatform-devel < %{version}-%{release}
%description    libEGL-devel
Mesa libEGL development package

%package        libGLES-devel
Summary:        Mesa libGLES development package
Group:          Development/Libraries
Requires:       mesa-libGLES = %{version}-%{release}
%description    libGLES-devel
Mesa libGLES development package


%package        libOSMesa
Summary:        Mesa offscreen rendering libraries
Group:          System Environment/Libraries
Provides:       libOSMesa
%description    libOSMesa
Mesa offscreen rendering libraries


%package        libOSMesa-devel
Summary:        Mesa offscreen rendering development package
Group:          Development/Libraries
Requires:       mesa-libOSMesa = %{version}-%{release}
%description    libOSMesa-devel
Mesa offscreen rendering development package


%package        libgbm
Summary:        Mesa gbm library
Group:          System Environment/Libraries
Provides:       libgbm
%description    libgbm
Mesa gbm runtime library.


%package        libgbm-devel
Summary:        Mesa libgbm development package
Group:          Development/Libraries
Requires:       mesa-libgbm%{?_isa} = %{version}-%{release}
Provides:       libgbm-devel
%description    libgbm-devel
Mesa libgbm development package


%if 0%{?with_wayland}
%package        libwayland-egl
Summary:        Mesa libwayland-egl library
Group:          System Environment/Libraries
Provides:       libwayland-egl
%description    libwayland-egl
Mesa libwayland-egl runtime library.


%package        libwayland-egl-devel
Summary:        Mesa libwayland-egl development package
Group:          Development/Libraries
Requires:       mesa-libwayland-egl%{?_isa} = %{version}-%{release}
Provides:       libwayland-egl-devel
%description    libwayland-egl-devel
Mesa libwayland-egl development package
%endif


%if 0%{?with_xa}
%package        libxatracker
Summary:        Mesa XA state tracker
Group:          System Environment/Libraries
Provides:       libxatracker
%description    libxatracker
Mesa XA state tracker

%package        libxatracker-devel
Summary:        Mesa XA state tracker development package
Group:          Development/Libraries
Requires:       mesa-libxatracker%{?_isa} = %{version}-%{release}
Provides:       libxatracker-devel
%description    libxatracker-devel
Mesa XA state tracker development package
%endif

%package        libglapi
Summary:        Mesa shared glapi
Group:          System Environment/Libraries
%description    libglapi
Mesa shared glapi


%if 0%{?with_opencl}
%package        libOpenCL
Summary:        Mesa OpenCL runtime library
Requires:       ocl-icd
Requires:       libclc
Requires:       mesa-libgbm = %{version}-%{release}
%description    libOpenCL
Mesa OpenCL runtime library.

%package        libOpenCL-devel
Summary:        Mesa OpenCL development package
Requires:       mesa-libOpenCL%{?_isa} = %{version}-%{release}
%description    libOpenCL-devel
Mesa OpenCL development package.
%endif

%if 0%{?with_nine}
%package        libd3d
Summary:        Mesa Direct3D9 state tracker
%description    libd3d
Mesa Direct3D9 state tracker

%package        libd3d-devel
Summary:        Mesa Direct3D9 state tracker development package
Requires:       mesa-libd3d%{?_isa} = %{version}-%{release}
%description    libd3d-devel
Mesa Direct3D9 state tracker development package
%endif


%prep
%setup -q

%if 0%{with_private_llvm}
sed -i 's/llvm-config/mesa-private-llvm-config-%{__isa_bits}/g' configure.ac
sed -i 's/`$LLVM_CONFIG --version`/&-mesa/' configure.ac
%endif


%build
autoreconf --install

export CFLAGS="$RPM_OPT_FLAGS"
# C++ note: we never say "catch" in the source.  we do say "typeid" once,
# in an assert, which is patched out above.  LLVM doesn't use RTTI or throw.
#
# We do say 'catch' in the clover and d3d1x state trackers, but we're not
# building those yet.
export CXXFLAGS="$RPM_OPT_FLAGS %{?with_opencl:-frtti -fexceptions} %{!?with_opencl:-fno-rtti -fno-exceptions}"
%ifarch %{ix86}
# i do not have words for how much the assembly dispatch code infuriates me
%define asm_flags --disable-asm
%endif

%configure \
    %{?asm_flags} \
    --enable-selinux \
    --enable-osmesa \
    --with-dri-driverdir=%{_libdir}/dri \
    --enable-egl \
    --disable-gles1 \
    --enable-gles2 \
    --disable-xvmc \
    %{?with_vdpau:--enable-vdpau} \
    %{?with_vaapi:--enable-va} \
    --with-egl-platforms=x11,drm,surfaceless%{?with_wayland:,wayland} \
    --enable-shared-glapi \
    --enable-gbm \
    %{?with_omx:--enable-omx} \
%if 0%{?fedora} < 24
    %{?with_opencl:--enable-opencl --enable-opencl-icd --with-clang-libdir=%{_prefix}/lib} %{!?with_opencl:--disable-opencl} \
%endif
%if 0%{?fedora} > 23
    %{?with_opencl:--enable-opencl --enable-opencl-icd} %{!?with_opencl:--disable-opencl} \
%endif
    --enable-glx-tls \
    --enable-texture-float=yes \
    %{?with_llvm:--enable-gallium-llvm} \
    %{?with_llvm:--enable-llvm-shared-libs} \
    --enable-dri \
%if %{with_hardware}
    %{?with_xa:--enable-xa} \
    %{?with_nine:--enable-nine} \
    --with-gallium-drivers=%{?with_vmware:svga,}%{?with_radeonsi:radeonsi,}%{?with_llvm:swrast,r600,}%{?with_freedreno:freedreno,}%{?with_vc4:vc4,}%{?with_ilo:ilo,}virgl,r300,nouveau \
%else
    --with-gallium-drivers=%{?with_llvm:swrast,}virgl \
%endif
%if 0%{?fedora} < 21
    --disable-dri3 \
%endif
    %{?dri_drivers}

%make_build


%install
%make_install

%if 0%{?rhel}
# remove pre-DX9 drivers
rm -f $RPM_BUILD_ROOT%{_libdir}/dri/{radeon,r200,nouveau_vieux}_dri.*
%endif

%if !%{with_hardware}
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/drirc
%endif

# libvdpau opens the versioned name, don't bother including the unversioned
rm -f $RPM_BUILD_ROOT%{_libdir}/vdpau/*.so

# strip out useless headers
rm -f $RPM_BUILD_ROOT%{_includedir}/GL/w*.h

# remove .la files
find $RPM_BUILD_ROOT -name '*.la' -delete

# this keeps breaking, check it early.  note that the exit from eu-ftr is odd.
pushd $RPM_BUILD_ROOT%{_libdir}
for i in libOSMesa*.so libGL.so ; do
    eu-findtextrel $i && exit 1
done
popd


%clean
rm -rf $RPM_BUILD_ROOT


%check


%post           libGL -p /sbin/ldconfig
%postun         libGL -p /sbin/ldconfig
%post           libOSMesa -p /sbin/ldconfig
%postun         libOSMesa -p /sbin/ldconfig
%post           libEGL -p /sbin/ldconfig
%postun         libEGL -p /sbin/ldconfig
%post           libGLES -p /sbin/ldconfig
%postun         libGLES -p /sbin/ldconfig
%post           libglapi -p /sbin/ldconfig
%postun         libglapi -p /sbin/ldconfig
%post           libgbm -p /sbin/ldconfig
%postun         libgbm -p /sbin/ldconfig
%if 0%{?with_wayland}
%post           libwayland-egl -p /sbin/ldconfig
%postun         libwayland-egl -p /sbin/ldconfig
%endif
%if 0%{?with_xa}
%post           libxatracker -p /sbin/ldconfig
%postun         libxatracker -p /sbin/ldconfig
%endif
%if 0%{?with_opencl}
%post           libOpenCL -p /sbin/ldconfig
%postun         libOpenCL -p /sbin/ldconfig
%endif
%if 0%{?with_nine}
%post           libd3d -p /sbin/ldconfig
%postun         libd3d -p /sbin/ldconfig
%endif


%files          libGL
%{_libdir}/libGL.so.1
%{_libdir}/libGL.so.1.*

%files          libEGL
%{_libdir}/libEGL.so.1
%{_libdir}/libEGL.so.1.*

%files          libGLES
%{_libdir}/libGLESv2.so.2
%{_libdir}/libGLESv2.so.2.*

%files          filesystem
%dir %{_libdir}/dri
%if %{with_hardware}
%if 0%{?with_vdpau}
%dir %{_libdir}/vdpau
%endif
%endif

%files          libglapi
%{_libdir}/libglapi.so.0
%{_libdir}/libglapi.so.0.*

%files          dri-drivers
%if %{with_hardware}
%config(noreplace) %{_sysconfdir}/drirc
%if !0%{?rhel}
%{_libdir}/dri/radeon_dri.so
%{_libdir}/dri/r200_dri.so
%{_libdir}/dri/nouveau_vieux_dri.so
%endif
%{_libdir}/dri/r300_dri.so
%if 0%{?with_llvm}
%{_libdir}/dri/r600_dri.so
%if 0%{?with_radeonsi}
%{_libdir}/dri/radeonsi_dri.so
%endif
%endif
%ifarch %{ix86} x86_64
%{_libdir}/dri/i915_dri.so
%{_libdir}/dri/i965_dri.so
%if 0%{?with_ilo}
%{_libdir}/dri/ilo_dri.so
%endif
%endif
%if 0%{?with_vc4}
%{_libdir}/dri/vc4_dri.so
%endif
%if 0%{?with_freedreno}
%{_libdir}/dri/kgsl_dri.so
%{_libdir}/dri/msm_dri.so
%endif
%{_libdir}/dri/nouveau_dri.so
%if 0%{?with_vmware}
%{_libdir}/dri/vmwgfx_dri.so
%endif
%endif
%if 0%{?with_llvm}
%ifarch %{ix86} x86_64
%dir %{_libdir}/gallium-pipe
%{_libdir}/gallium-pipe/*.so
%endif
%{_libdir}/dri/kms_swrast_dri.so
%endif
%{_libdir}/dri/swrast_dri.so
%if 0%{?with_vaapi}
%{_libdir}/dri/gallium_drv_video.so
%endif
%{_libdir}/dri/virtio_gpu_dri.so

%if %{with_hardware}
%if 0%{?with_omx}
%files omx-drivers
%{_libdir}/bellagio/libomx_mesa.so
%endif
%if 0%{?with_vdpau}
%files vdpau-drivers
%{_libdir}/vdpau/libvdpau_nouveau.so.1*
%{_libdir}/vdpau/libvdpau_r300.so.1*
%if 0%{?with_llvm}
%{_libdir}/vdpau/libvdpau_r600.so.1*
%if 0%{?with_radeonsi}
%{_libdir}/vdpau/libvdpau_radeonsi.so.1*
%endif
%endif
%endif
%endif

%files          libGL-devel
%{_includedir}/GL/gl.h
%{_includedir}/GL/gl_mangle.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glx_mangle.h
%{_includedir}/GL/glxext.h
%{_includedir}/GL/glcorearb.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/dri_interface.h
%{_libdir}/pkgconfig/dri.pc
%{_libdir}/libGL.so
%{_libdir}/libglapi.so
%{_libdir}/pkgconfig/gl.pc

%files          libEGL-devel
%dir %{_includedir}/EGL
%{_includedir}/EGL/eglext.h
%{_includedir}/EGL/egl.h
%{_includedir}/EGL/eglmesaext.h
%{_includedir}/EGL/eglplatform.h
%{_includedir}/EGL/eglextchromium.h
%dir %{_includedir}/KHR
%{_includedir}/KHR/khrplatform.h
%{_libdir}/pkgconfig/egl.pc
%{_libdir}/libEGL.so

%files          libGLES-devel
%dir %{_includedir}/GLES2
%{_includedir}/GLES2/gl2platform.h
%{_includedir}/GLES2/gl2.h
%{_includedir}/GLES2/gl2ext.h
%{_includedir}/GLES3/gl3platform.h
%{_includedir}/GLES3/gl3.h
%{_includedir}/GLES3/gl3ext.h
%{_includedir}/GLES3/gl31.h
%{_libdir}/pkgconfig/glesv2.pc
%{_libdir}/libGLESv2.so

%files          libOSMesa
%{_libdir}/libOSMesa.so.8*

%files          libOSMesa-devel
%dir %{_includedir}/GL
%{_includedir}/GL/osmesa.h
%{_libdir}/libOSMesa.so
%{_libdir}/pkgconfig/osmesa.pc

%files          libgbm
%{_libdir}/libgbm.so.1
%{_libdir}/libgbm.so.1.*

%files          libgbm-devel
%{_libdir}/libgbm.so
%{_includedir}/gbm.h
%{_libdir}/pkgconfig/gbm.pc

%if 0%{?with_wayland}
%files          libwayland-egl
%{_libdir}/libwayland-egl.so.1
%{_libdir}/libwayland-egl.so.1.*

%files          libwayland-egl-devel
%{_libdir}/libwayland-egl.so
%{_libdir}/pkgconfig/wayland-egl.pc
%endif

%if 0%{?with_xa}
%files          libxatracker
%if %{with_hardware}
%{_libdir}/libxatracker.so.2
%{_libdir}/libxatracker.so.2.*
%endif

%files          libxatracker-devel
%if %{with_hardware}
%{_libdir}/libxatracker.so
%{_includedir}/xa_tracker.h
%{_includedir}/xa_composite.h
%{_includedir}/xa_context.h
%{_libdir}/pkgconfig/xatracker.pc
%endif
%endif

%if 0%{?with_opencl}
%files          libOpenCL
%{_libdir}/libMesaOpenCL.so.*
%{_sysconfdir}/OpenCL/vendors/mesa.icd

%files          libOpenCL-devel
%{_libdir}/libMesaOpenCL.so
%endif

%if 0%{?with_nine}
%files          libd3d
%dir %{_libdir}/d3d/
%{_libdir}/d3d/*.so.*

%files          libd3d-devel
%{_libdir}/pkgconfig/d3d.pc
%{_includedir}/d3dadapter/
%{_libdir}/d3d/*.so
%endif


%changelog
* Thu Apr 14 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160414~171a570f-1
- Update to new upstream snapshot.

* Wed Apr 13 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160413~04f15e49-1
- Update to new upstream snapshot.

* Tue Apr 12 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160412~5b6a0b7f-1
- Update to new upstream snapshot.

* Mon Apr 11 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160411~4979cec8-1
- Update to new upstream snapshot.

* Sun Apr 10 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160410~ce84a92d-1
- Update to new upstream snapshot.

* Sat Apr 09 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160409~30b818d5-1
- Update to new upstream snapshot.

* Thu Apr 07 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160408~059308db-1
- Update to new upstream snapshot.

* Thu Apr 07 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160407~828d84c8-1
- Update to new upstream snapshot.

* Wed Apr 06 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160406~0293d72f-1
- Update to new upstream snapshot.

* Tue Apr 05 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160405~3e135728-1
- Update to new upstream snapshot.

* Sun Apr 03 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160404~d50ffb5e-1
- Update to new upstream snapshot.

* Sat Apr 02 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160403~2a529a8a-1
- Update to new upstream snapshot.

* Sat Apr 02 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160402~070e5a74-1
- Update to new upstream snapshot.

* Thu Mar 31 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160401~08ff5f4d-1
- Update to new upstream snapshot.

* Thu Mar 31 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160331~a94d8d51-2
- Remove no longer provided COPYING file.

* Thu Mar 31 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160331~a94d8d51-1
- Update to new upstream snapshot.

* Tue Mar 29 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160330~7087e0ab-1
- Update to new upstream snapshot.

* Tue Mar 29 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160329~cc68dc2b-1
- Update to new upstream snapshot.

* Sun Mar 27 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160328~50d653c2-1
- Update to new upstream snapshot.

* Sun Mar 27 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160327~fc3b000f-1
- Update to new upstream snapshot.

* Fri Mar 25 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160326~8683d54d-1
- Update to new upstream snapshot.

* Fri Mar 25 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160325~511ce292-1
- Update to new upstream snapshot.

* Thu Mar 24 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160324~0bea0e71-1
- Update to new upstream snapshot.

* Tue Mar 22 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160323~d7a25a9d-1
- Update to new upstream snapshot.

* Tue Mar 22 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160322~530593da-1
- Update to new upstream snapshot.

* Mon Mar 21 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160321~8f45691c-1
- Update to new upstream snapshot.

* Sat Mar 19 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160320~9184d9a0-1
- Update to new upstream snapshot.

* Fri Mar 18 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160319~9211b68a-1
- Update to new upstream snapshot.

* Fri Mar 18 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160318~d4714512-1
- Update to new upstream snapshot.

* Thu Mar 17 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160317~5aea0d69-1
- Update to new upstream snapshot.

* Tue Mar 15 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160316~9d9965c0-1
- Update to new upstream snapshot.

* Tue Mar 15 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160315~4de25fa7-1
- Update to new upstream snapshot.

* Mon Mar 14 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160314~e9d68cc3-1
- Update to new upstream snapshot.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160313~61b10b4e-1
- Update to new upstream snapshot.

* Sat Mar 12 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160312~6cf120ec-1
- Update to new upstream snapshot.

* Fri Mar 11 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160311~af3454ca-1
- Update to new upstream snapshot.

* Wed Mar 09 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160310~3dc2630e-1
- Update to new upstream snapshot.

* Tue Mar 08 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160308~6857420e-1
- Update to new upstream snapshot.

* Mon Mar 07 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160307~0941ef3d-1
- Update to new upstream snapshot.

* Sat Mar 05 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160306~a4678311-1
- Update to new upstream snapshot.

* Fri Mar 04 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160305~1f862e92-1
- Update to new upstream snapshot.

* Thu Mar 03 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160304~47392011-1
- Update to new upstream snapshot.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160303~0d047d10-1
- Update to new upstream snapshot.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160302~e8fd60e7-1
- Update to new upstream snapshot.

* Tue Mar 01 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160301~ac222626-1
- Update to new upstream snapshot.

* Mon Feb 29 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160229~07ed003f-1
- Update to new upstream snapshot.

* Sat Feb 27 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160228~aa3b85fd-1
- Update to new upstream snapshot.

* Sat Feb 27 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160227~e2dce1a3-1
- Update to new upstream snapshot.

* Fri Feb 26 2016 Fabio Valentini <decathorpe@gmail.com> - 11.3.0~devel~git160226~840aa52f-1
- Update to new upstream snapshot.

* Thu Feb 25 2016 Fabio Valentini <decathorpe@gmail.com>
- Update to new upstream snapshot.

* Wed Feb 24 2016 Fabio Valentini <decathorpe@gmail.com> - 11.2.0~devel~git20160224.0~c95d5c5f-1
- automatic build by kentauros


