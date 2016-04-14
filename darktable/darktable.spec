%define date 160414
%define rev d6a3758a

Summary: darktable
Name: darktable
Version: 2.1.0~git%{date}~%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://www.darktable.org

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: libappstream-glib
BuildRequires: libxslt

BuildRequires: cups-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: pugixml-devel >= 1.2

BuildRequires: pkgconfig(GraphicsMagick)
BuildRequires: pkgconfig(OpenEXR)
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(colord)
BuildRequires: pkgconfig(colord-gtk)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(flickcurl)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.10
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(lensfun)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libgphoto2)
BuildRequires: pkgconfig(libopenjpeg1)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(osmgpsmap-1.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(sqlite3)


%description
darktable is an open source photography workflow application and RAW developer. A virtual lighttable and darkroom for photographers. It manages your digital negatives in a database, lets you view them through a zoomable lighttable and enables you to develop raw images and enhance them.


%prep
%setup -q


%build
echo "#define PACKAGE_VERSION \"2.1.0\"" > src/version_gen.h

mkdir build && cd build
%cmake ..
%make_build


%install
cd build
%make_install
%find_lang darktable


%clean
rm -rf $RPM_BUILD_ROOT


%check
desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/darktable.desktop

appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/darktable.appdata.xml


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :



%files -f build/darktable.lang
%{_bindir}/darktable
%{_bindir}/darktable-*

%{_libdir}/darktable/

%{_datadir}/applications/darktable.desktop
%{_datadir}/appdata/darktable.appdata.xml
%{_datadir}/darktable/
%{_datadir}/doc/darktable

%{_datadir}/icons/hicolor/*/apps/darktable.png
%{_datadir}/icons/hicolor/scalable/apps/darktable.svg
%{_datadir}/icons/hicolor/scalable/apps/darktable-*.svg

%{_mandir}/man1/darktable*


%changelog
* Thu Apr 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160414~d6a3758a-1
- Update to new upstream snapshot.

* Wed Apr 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160413~fb7678f9-1
- Update to new upstream snapshot.

* Sun Apr 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160410~f85c0b3d-1
- Update to new upstream snapshot.

* Sat Apr 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160409~d6a0066b-1
- Update to new upstream snapshot.

* Thu Apr 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160408~3c2790c2-1
- Update to new upstream snapshot.

* Thu Apr 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160407~aac8892d-1
- Update to new upstream snapshot.

* Wed Apr 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160406~f37c22c8-1
- Update to new upstream snapshot.

* Tue Apr 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160405~64baafe5-1
- Update to new upstream snapshot.

* Sun Apr 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160404~236c7574-1
- Update to new upstream snapshot.

* Sat Apr 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160403~a47b66a4-1
- Update to new upstream snapshot.

* Sat Apr 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160402~ba1c8ca8-1
- Update to new upstream snapshot.

* Thu Mar 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160331~edf73d8d-1
- Update to new upstream snapshot.

* Tue Mar 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160330~33fa42bc-1
- Update to new upstream snapshot.

* Tue Mar 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160329~2b2f6c22-1
- Update to new upstream snapshot.

* Sun Mar 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160328~842546a3-1
- Update to new upstream snapshot.

* Sun Mar 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160327~00998c90-1
- Update to new upstream snapshot.

* Fri Mar 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160326~99cfcc9d-1
- Update to new upstream snapshot.

* Fri Mar 25 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160325~79cd9d32-1
- Update to new upstream snapshot.

* Thu Mar 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160324~5796f0a9-1
- Update to new upstream snapshot.

* Tue Mar 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160323~83b8dc6f-1
- Update to new upstream snapshot.

* Tue Mar 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160322~19576fb1-1
- Update to new upstream snapshot.

* Mon Mar 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160321~35cb9f28-1
- Update to new upstream snapshot.

* Sat Mar 19 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160320~aa3a8db4-1
- Update to new upstream snapshot.

* Fri Mar 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160318~b1ecc3d8-1
- Update to new upstream snapshot.

* Thu Mar 17 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160317~b7832e1b-1
- Update to new upstream snapshot.

* Tue Mar 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160316~a1e2408f-1
- Update to new upstream snapshot.

* Mon Mar 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160314~093c18dc-1
- Update to new upstream snapshot.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160313~bd8779e8-1
- Update to new upstream snapshot.

* Sat Mar 12 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160312~97547e0b-1
- Update to new upstream snapshot.

* Fri Mar 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160311~57307ed2-1
- Update to new upstream snapshot.

* Wed Mar 09 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160310~fa092391-1
- Update to new upstream snapshot.

* Tue Mar 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160308~c954ec7d-1
- Update to new upstream snapshot.

* Mon Mar 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160307~22b6bab9-1
- Update to new upstream snapshot.

* Sat Mar 05 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160306~bbbfe3cc-1
- Update to new upstream snapshot.

* Fri Mar 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160305~d60baf46-1
- Update to new upstream snapshot.

* Thu Mar 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160304~64c70a83-1
- Update to new upstream snapshot.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160303~db08ec3d-1
- Update to new upstream snapshot.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160302~d8de0873-1
- Update to new upstream snapshot.

* Tue Mar 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160301~301affb5-1
- Update to new upstream snapshot.

* Mon Feb 29 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160229~02f94bab-1
- Update to new upstream snapshot.

* Sat Feb 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160228~6dadfb48-1
- Update to new upstream snapshot.

* Sat Feb 27 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160227~3b96b0aa-1
- Update to new upstream snapshot.

* Fri Feb 26 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160226~64b202df-1
- Update to new upstream snapshot.

* Wed Feb 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160225~1b061675-1
- Update to new upstream snapshot.

* Wed Feb 24 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160224~7f41ab2f-1
- Update to new upstream snapshot.

* Tue Feb 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160223~954b4f63-1
- Update to new upstream snapshot.

* Mon Feb 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160222~6c00b657-1
- Update to new upstream snapshot.

* Mon Feb 22 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160222~a61c6a99-1
- Update to new upstream snapshot.

* Sun Feb 21 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160222~2f29b647-1
- Update to new upstream snapshot.

* Sat Feb 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160221~13feee13-1
- Update to new upstream snapshot.

* Sat Feb 20 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160220~2ee6a519-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160218~945d99fa-2
- Update packaging to fix build.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160218~945d99fa-1
- Update to new upstream snapshot.

* Mon Feb 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160216~e5fe1c56-1
- Update to new upstream snapshot.

* Mon Feb 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160215~22308348-1
- Update to new upstream snapshot.

* Sun Feb 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160214~f208e7d5-1
- Update to new upstream snapshot.

* Sun Feb 14 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160214~9477f7dd-1
- Update to new upstream snapshot.

* Sat Feb 13 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160213~938a1a77-1
- Update to new upstream snapshot.

* Thu Feb 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160212~d40660b1-1
- Update to new upstream snapshot.

* Thu Feb 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160211~81bc3cf5-2
- Update packaging to fix rpm build.

* Thu Feb 11 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160211~81bc3cf5-1
- Update to new upstream snapshot.

* Wed Feb 10 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160210~c1cec141-1
- Update to new upstream snapshot.

* Mon Feb 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160209~c25d0096-1
- Update to new upstream snapshot.

* Sun Feb 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160207~1e8377e4-1
- Update to new upstream snapshot.

* Sat Feb 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160206~9f4317bc-1
- Update to new upstream snapshot.

* Sat Feb 06 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160206~c40691ee-1
- Update to new upstream snapshot.

* Thu Feb 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160204~8e1dea3e-1
- Update to new upstream snapshot.

* Thu Feb 04 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160204~ed505889-1
- Update to new upstream snapshot.

* Wed Feb 03 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160203~2d70b685-1
- Update to new upstream snapshot.

* Tue Feb 02 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160202~9e808e2c-1
- Update to new upstream snapshot.

* Mon Feb 01 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160201~74e12833-1
- Update to new upstream snapshot.

* Sun Jan 31 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160131~659d6405-1
- Update to new upstream snapshot.

* Sat Jan 30 2016 Fabio Valentini <decathorpe@gmail.com> - 2.1.0~git160130~c2fc8e84-1
- Update to new upstream snapshot.

* Thu Dec 24 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151224~8cc7e85d-1
- Update to new upstream snapshot.

* Wed Dec 23 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151223~6623d7bc-1
- Update to new upstream snapshot.

* Tue Dec 22 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151222~6c386b0e-1
- Update to new upstream snapshot.

* Mon Dec 21 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151221~45a125d2-1
- Update to new upstream snapshot.

* Mon Dec 21 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151221~610c4968-1
- Update to new upstream snapshot.

* Sun Dec 20 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151220~26c1531b-1
- Update to new upstream snapshot.

* Sat Dec 19 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151219~6c23073d-1
- Update to new upstream snapshot.

* Fri Dec 18 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151218~85306970-1
- Update to new upstream snapshot.

* Thu Dec 17 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151217~355887da-1
- Update to new upstream snapshot.

* Wed Dec 16 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151216~6ef1840d-1
- Update to new upstream snapshot.

* Mon Dec 14 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151214~dd1e573f-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151213~14963c5d-1
- Update to new upstream snapshot.

* Sat Dec 12 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151212~601de8bf-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151211~16e7495a-1
- Update to new upstream snapshot.

* Thu Dec 10 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151210~79ae5fd8-1
- Update to new upstream snapshot.

* Wed Dec 09 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151210~e495ec3f-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151208~ca435602-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151207~f180a70c-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151206~f7af19aa-1
- Update to new upstream snapshot.

* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151203~08241ad6-1
- Update to new upstream snapshot.

* Wed Dec 02 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151202~d6b9c5ae-1
- Update to new upstream snapshot.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151201~e975e6f2-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151130~24803c56-1
- Update to new upstream snapshot.

* Sun Nov 29 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151129~f0944171-1
- Update to new upstream snapshot.

* Sat Nov 28 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151128~92f433d9-1
- Update to new upstream snapshot.

* Fri Nov 27 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151127~bcf7d3a9-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151126~07f0619a-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151126~33fae00a-1
- Update to new upstream snapshot.

* Wed Nov 25 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151125~ad25d885-1
- Update to new upstream snapshot.

* Mon Nov 23 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151123~828ec1dc-1
- Update to new upstream snapshot.

* Sun Nov 22 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151122~477d322f-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151121~8c1da7b7-1
- Update to new upstream snapshot.

* Fri Nov 20 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151120~df6a1b60-1
- Update to new upstream snapshot.

* Thu Nov 19 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151119~e1230ba8-1
- Update to new upstream snapshot.

* Wed Nov 18 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151118~72b6add8-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151117~ed073a45-1
- Update to new upstream snapshot.

* Mon Nov 16 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151116~d0fcae8b-1
- Update to new upstream snapshot.

* Sun Nov 15 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151115~bd995c34-1
- Update to new upstream snapshot.

* Sat Nov 14 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151114~cd074b46-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151113~e456b2bd-1
- Update to new upstream snapshot.

* Thu Nov 12 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151112~c184be65-1
- Update to new upstream snapshot.

* Wed Nov 11 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151111~1bc963d8-1
- Update to new upstream snapshot.

* Tue Nov 10 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151110~c120b377-1
- Update to new upstream snapshot.

* Mon Nov 09 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151109~dfa5fd2b-1
- Update to new upstream snapshot.

* Sun Nov 08 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151108~818cbd7d-1
- Update to new upstream snapshot.

* Sat Nov 07 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151107~84cbc875-1
- Update to new upstream snapshot.

* Fri Nov 06 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151106~55f61985-1
- Update to new upstream snapshot.

* Thu Nov 05 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151105~27958f9f-1
- Update to new upstream snapshot.

* Wed Nov 04 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151104~6bf271e5-1
- Update to new upstream snapshot.

* Tue Nov 03 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151103~9f1cdd0a-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151102~3c07c123-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151102~e12b90da-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151031~ce821399-1
- Update to new upstream snapshot.

* Wed Oct 28 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151028~f4f888c8-1
- Update to new upstream snapshot.

* Tue Oct 27 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151027~a17e969c-1
- Update to new upstream snapshot.

* Mon Oct 26 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151026~1d3e8cc8-1
- Update to new upstream snapshot.

* Sun Oct 25 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151025~48954b11-1
- Update to new upstream snapshot.

* Sun Oct 25 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151025~393976c6-1
- Update to new upstream snapshot.

* Fri Oct 23 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151023~b79d07d5-1
- Update to new upstream snapshot.

* Thu Oct 22 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151022~40120290-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151020~70b3d1c9-1
- Update to new upstream snapshot.

* Mon Oct 19 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151019~b21f5ad1-1
- Update to new upstream snapshot.

* Sun Oct 18 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151018~7aa5f146-1
- Update to new upstream snapshot.

* Sat Oct 17 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151017~ef6e7788-1
- Update to new upstream snapshot.

* Fri Oct 16 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151016~e4b7eba8-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151015~7478add2-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151014~cd50ac74-1
- Update to new upstream snapshot.

* Tue Oct 13 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151013~562f9843-1
- Update to new upstream snapshot.

* Mon Oct 12 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151012~858bcb70-1
- Update to new upstream snapshot.

* Sun Oct 11 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151011~3989fe0c-1
- Update to new upstream snapshot.

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151010~2535ca82-1
- Update to new upstream snapshot.

* Fri Oct 09 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151009~07c18105-1
- Update to new upstream snapshot.

* Wed Oct 07 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151007~814adcee-1
- Update to new upstream snapshot.

* Tue Oct 06 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151006~3f5f2687-1
- Update to new upstream snapshot.

* Mon Oct 05 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151005~afd54310-1
- Update to new upstream snapshot.

* Sun Oct 04 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151004~e6ce2377-1
- Update to new upstream snapshot.

* Sat Oct 03 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151003~eac3076f-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151002~7e5a5dc3-1
- Update to new upstream snapshot.

* Thu Oct 01 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git151001~64bcbef1-1
- Update to new upstream snapshot.

* Wed Sep 30 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150930~d48b6cc0-1
- Update to new upstream snapshot.

* Tue Sep 29 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150929~ccadd6e6-1
- Update to new upstream snapshot.

* Mon Sep 28 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150928~d5aea3c5-1
- Update to new upstream snapshot.

* Sun Sep 27 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150927~731f6af8-1
- Update to new upstream snapshot.

* Sat Sep 26 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150926~26f782b0-1
- Update to new upstream snapshot.

* Fri Sep 25 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150925~80f2f321-1
- Update to new upstream snapshot.

* Thu Sep 24 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150924~f31dc157-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150923~53b1d365-1
- Update to new upstream snapshot.

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150922~93ec1c86-2
- Add darktable-generate-cache binary to spec.

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150922~93ec1c86-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150921~9dfebd0e-1
- Update to new upstream snapshot.

* Fri Sep 18 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150918~43d687ae-1
- Update to new upstream snapshot.

* Thu Sep 17 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150917~7a7d457c-1
- Update to new upstream snapshot.

* Tue Sep 15 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150916~1fbaf410-1
- Update to new upstream snapshot.

* Tue Sep 15 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150915~a5ad4415-1
- Update to new upstream snapshot.

* Mon Sep 14 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150914~c5e3af5f-1
- Update to new upstream snapshot.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150913~39552776-1
- Update to new upstream snapshot.

* Sat Sep 12 2015 Fabio Valentini <decathorpe@gmail.com> - 1.99~git150912~41310814-1
- New spec and new version.



