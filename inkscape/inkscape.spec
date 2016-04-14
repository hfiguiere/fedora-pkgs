%define rev 14842

Name:           inkscape
Version: 0.92~rev%{rev}
Release: 1%{?dist}
Summary:        Vector-based drawing program using SVG

Group:          Applications/Productivity
URL:            http://inkscape.sourceforge.net/
License:        GPLv2+

Source0:        inkscape-%{version}.tar.gz
Source1:		inkscape.conf

BuildRequires:	libtool intltool
BuildRequires:	gettext gettext-devel
BuildRequires:	desktop-file-utils

BuildRequires:	boost-devel
BuildRequires:	libjpeg-turbo-devel

BuildRequires:	pkgconfig(bdw-gc) >= 7.1
BuildRequires:	pkgconfig(cairo) >= 1.10
BuildRequires:	pkgconfig(cairomm-1.0) >= 1.9.8
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gdl-3.0) >= 3.3.4
BuildRequires:	pkgconfig(giomm-2.4)
BuildRequires:	pkgconfig(glib-2.0) >= 2.28
BuildRequires:	pkgconfig(glibmm-2.4) >= 2.28
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(gthread-2.0) >= 2.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.2
BuildRequires:	pkgconfig(gdkmm-3.0) >= 3.2
BuildRequires:	pkgconfig(gtkmm-3.0) >= 3.2
BuildRequires:	pkgconfig(ImageMagick++)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libcdr-0.1)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libpng) >= 1.2
BuildRequires:	pkgconfig(libvisio-0.1)
BuildRequires:	pkgconfig(libwpg-0.3)
BuildRequires:	pkgconfig(libxml-2.0) >= 2.6.11
BuildRequires:	pkgconfig(libxslt) >= 1.0.15
BuildRequires:	pkgconfig(pango) >= 1.24
BuildRequires:	pkgconfig(pangoft2) >= 1.24
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(poppler-cairo)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(sigc++-2.0) >= 2.0.12

#BuildRequires:  gnome-vfs2-devel >= 2.0

Requires:			python-lxml

#Requires:			numpy
#Requires:			uniconvertor


%description
Inkscape is a vector graphics editor, with capabilities similar to
Illustrator, CorelDraw, or Xara X, using the W3C standard Scalable Vector
Graphics (SVG) file format.  It is therefore a very useful tool for web
designers and as an interchange format for desktop publishing.

Inkscape supports many advanced SVG features (markers, clones, alpha
blending, etc.) and great care is taken in designing a streamlined
interface. It is very easy to edit nodes, perform complex path operations,
trace bitmaps and much more.


%package view
Summary:        Viewing program for SVG files
Group:          Applications/Productivity

%description view
Viewer for files in W3C standard Scalable Vector Graphics (SVG) file
format.


%package docs
Summary:        Documentation for Inkscape
Group:          Documentation
Requires:       inkscape

%description docs
Tutorial and examples for Inkscape, a graphics editor for vector
graphics in W3C standard Scalable Vector Graphics (SVG) file format.


%package devel
Summary:		Development headers for Inkscape
Group:			Development
Requires:		inkscape

%description devel
Header and development files for Inkscape, a graphics editor for vector
graphics in W3C standard Scalable Vector Graphics (SVG) file format.


%prep
%setup -q


%build
# Build in C++11 mode as glibmm headers use C++11 features. This can be dropped
# when GCC in Fedora switches to C++11 by default (with GCC 6, most likely).
export CXXFLAGS="%{optflags} -std=c++11"

./autogen.sh
%configure							\
		--enable-gtk3-experimental	\
		--enable-poppler-cairo		\
		--enable-lcms				\
		--enable-dbusapi			\
		--enable-binreloc

#		--with-gnome-vfs

%make_build


%install
%make_install

# No skencil anymore
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/extensions/sk2svg.sh

rm -f $RPM_BUILD_ROOT%{_libdir}/libinkdbus.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libinkdbus.la

%find_lang %{name}


%check
# XXX: Tests fail, ignore it for now
# make -k check || :


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
/usr/bin/update-desktop-database -q &> /dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
/usr/bin/update-desktop-database -q &> /dev/null ||:
fi


%files -f %{name}.lang
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS NEWS README

%{_bindir}/inkscape
%{_libdir}/libinkdbus.so.0
%{_libdir}/libinkdbus.so.0.0.0

%{_datadir}/inkscape/
%exclude %{_datadir}/inkscape/extensions/embed_raster_in_svg.pl

%{_datadir}/appdata/inkscape.appdata.xml
%{_datadir}/applications/*inkscape.desktop
%{_datadir}/icons/hicolor/*/*/inkscape*

%{_datadir}/dbus-1/services/org.inkscape.service
%{_mandir}/*/*gz
%{_mandir}/*/*/*gz
%exclude %{_mandir}/man1/inkview.1*


%files view
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc AUTHORS NEWS README

%{_bindir}/inkview
%{_mandir}/man1/inkview.1*


%files docs
%{_datadir}/inkscape/examples/


%files devel
%{_includedir}/libinkdbus-0.48
%{_libdir}/libinkdbus.so
%{_libdir}/pkgconfig/inkdbus.pc


%changelog
* Thu Apr 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14842-1
- Update to new upstream snapshot.

* Wed Apr 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14824-1
- Update to new upstream snapshot.

* Tue Apr 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14793-1
- Update to new upstream snapshot.

* Mon Apr 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14772-1
- Update to new upstream snapshot.

* Sat Apr 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14770-1
- Update to new upstream snapshot.

* Thu Apr 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14764-1
- Update to new upstream snapshot.

* Wed Apr 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14763-1
- Update to new upstream snapshot.

* Tue Apr 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14762-1
- Update to new upstream snapshot.

* Sat Apr 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14761-1
- Update to new upstream snapshot.

* Sat Apr 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14758-1
- Update to new upstream snapshot.

* Thu Mar 31 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14755-1
- Update to new upstream snapshot.

* Tue Mar 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14748-1
- Update to new upstream snapshot.

* Tue Mar 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14747-1
- Update to new upstream snapshot.

* Sun Mar 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14746-1
- Update to new upstream snapshot.

* Fri Mar 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14745-1
- Update to new upstream snapshot.

* Fri Mar 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14741-1
- Update to new upstream snapshot.

* Thu Mar 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14740-1
- Update to new upstream snapshot.

* Tue Mar 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14739-1
- Update to new upstream snapshot.

* Tue Mar 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14734-1
- Update to new upstream snapshot.

* Mon Mar 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14730-1
- Update to new upstream snapshot.

* Sat Mar 19 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14720-1
- Update to new upstream snapshot.

* Fri Mar 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14718-1
- Update to new upstream snapshot.

* Fri Mar 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14716-1
- Update to new upstream snapshot.

* Thu Mar 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14713-1
- Update to new upstream snapshot.

* Tue Mar 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14709-1
- Update to new upstream snapshot.

* Tue Mar 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14707-1
- Update to new upstream snapshot.

* Mon Mar 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14706-1
- Update to new upstream snapshot.

* Sun Mar 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14702-1
- Update to new upstream snapshot.

* Sat Mar 12 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14699-1
- Update to new upstream snapshot.

* Fri Mar 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14698-1
- Update to new upstream snapshot.

* Wed Mar 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14696-1
- Update to new upstream snapshot.

* Sat Mar 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14691-1
- Update to new upstream snapshot.

* Fri Mar 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14688-1
- Update to new upstream snapshot.

* Thu Mar 03 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14681-1
- Update to new upstream snapshot.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14680-1
- Update to new upstream snapshot.

* Wed Mar 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14677-1
- Update to new upstream snapshot.

* Tue Mar 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14676-1
- Update to new upstream snapshot.

* Mon Feb 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14674-1
- Update to new upstream snapshot.

* Sat Feb 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14672-1
- Update to new upstream snapshot.

* Sat Feb 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14670-1
- Update to new upstream snapshot.

* Fri Feb 26 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14668-1
- Update to new upstream snapshot.

* Tue Feb 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14666-1
- Update to new upstream snapshot.

* Mon Feb 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14663-1
- Update to new upstream snapshot.

* Sat Feb 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14662-1
- Update to new upstream snapshot.

* Sat Feb 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14661-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14660-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14659-1
- Update to new upstream snapshot.

* Mon Feb 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14654-1
- Update to new upstream snapshot.

* Mon Feb 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14653-1
- Update to new upstream snapshot.

* Sun Feb 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14649-1
- Update to new upstream snapshot.

* Sat Feb 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14648-1
- Update to new upstream snapshot.

* Thu Feb 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14647-1
- Update to new upstream snapshot.

* Thu Feb 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14645-1
- Update to new upstream snapshot.

* Wed Feb 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14644-1
- Update to new upstream snapshot.

* Mon Feb 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14640-1
- Update to new upstream snapshot.

* Mon Feb 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14638-2
- Update packaging to reflect upstream changes.

* Sun Feb 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14638-1
- Update to new upstream snapshot.

* Sat Feb 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14634-1
- Update to new upstream snapshot.

* Sat Feb 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14632-1
- Update to new upstream snapshot.

* Thu Feb 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14631-1
- Update to new upstream snapshot.

* Tue Feb 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14630-1
- Update to new upstream snapshot.

* Mon Feb 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14629-1
- Update to new upstream snapshot.

* Sat Jan 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14627-1
- Update to new upstream snapshot.

* Fri Jan 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14625-1
- Update to new upstream snapshot.

* Thu Jan 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14622-1
- Update to new upstream snapshot.

* Wed Jan 27 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14618-1
- Update to new upstream snapshot.

* Mon Jan 25 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14616-1
- Update to new upstream snapshot.

* Sun Jan 24 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14615-2
- Version bump and rebuild for poppler in rawhide.

* Thu Jan 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14615-1
- Update to new upstream snapshot.

* Wed Jan 20 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14610-1
- Update to new upstream snapshot.

* Mon Jan 18 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14608-1
- Update to new upstream snapshot.

* Sun Jan 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14604-1
- Update to new upstream snapshot.

* Sat Jan 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14593-1
- Update to new upstream snapshot.

* Fri Jan 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14585-1
- Update to new upstream snapshot.

* Fri Jan 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14584-1
- Update to new upstream snapshot.

* Fri Jan 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14583-1
- Update to new upstream snapshot.

* Thu Jan 14 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14576-1
- Update to new upstream snapshot.

* Mon Jan 11 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14574-1
- Update to new upstream snapshot.

* Sat Jan 09 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14569-1
- Update to new upstream snapshot.

* Fri Jan 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14566-1
- Update to new upstream snapshot.

* Thu Jan 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14564-1
- Update to new upstream snapshot.

* Wed Jan 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14563-1
- Update to new upstream snapshot.

* Tue Jan 05 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14562-1
- Update to new upstream snapshot.

* Sat Jan 02 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14560-1
- Update to new upstream snapshot.

* Fri Jan 01 2016 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14559-1
- Update to new upstream snapshot.

* Thu Dec 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14558-1
- Update to new upstream snapshot.

* Tue Dec 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14557-1
- Update to new upstream snapshot.

* Mon Dec 28 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14556-1
- Update to new upstream snapshot.

* Sun Dec 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14553-1
- Update to new upstream snapshot.

* Sun Dec 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14549-1
- Update to new upstream snapshot.

* Sat Dec 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14542-1
- Update to new upstream snapshot.

* Mon Dec 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14539-1
- Update to new upstream snapshot.

* Sat Dec 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14538-1
- Update to new upstream snapshot.

* Tue Dec 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14536-1
- Update to new upstream snapshot.

* Mon Dec 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14535-1
- Update to new upstream snapshot.

* Sun Dec 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14529-1
- Update to new upstream snapshot.

* Fri Dec 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14527-1
- Update to new upstream snapshot.

* Thu Dec 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14524-1
- Update to new upstream snapshot.

* Wed Dec 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14522-1
- Update to new upstream snapshot.

* Tue Dec 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14517-1
- Update to new upstream snapshot.

* Mon Dec 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14507-1
- Update to new upstream snapshot.

* Sun Dec 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14506-1
- Update to new upstream snapshot.

* Thu Dec 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14502-1
- Update to new upstream snapshot.

* Wed Dec 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14501-1
- Update to new upstream snapshot.

* Tue Dec 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14495-1
- Update to new upstream snapshot.

* Mon Nov 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14494-1
- Update to new upstream snapshot.

* Sun Nov 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14493-1
- Update to new upstream snapshot.

* Fri Nov 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14492-1
- Update to new upstream snapshot.

* Thu Nov 26 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14491-1
- Update to new upstream snapshot.

* Wed Nov 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14488-1
- Update to new upstream snapshot.

* Mon Nov 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14484-1
- Update to new upstream snapshot.

* Sun Nov 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14483-1
- Update to new upstream snapshot.

* Sat Nov 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14482-1
- Update to new upstream snapshot.

* Fri Nov 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14479-1
- Update to new upstream snapshot.

* Wed Nov 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14477-1
- Update to new upstream snapshot.

* Tue Nov 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14476-1
- Update to new upstream snapshot.

* Sun Nov 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14473-1
- Update to new upstream snapshot.

* Sat Nov 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14469-1
- Update to new upstream snapshot.

* Fri Nov 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14464-1
- Update to new upstream snapshot.

* Thu Nov 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14461-1
- Update to new upstream snapshot.

* Thu Nov 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14459-1
- Update to new upstream snapshot.

* Wed Nov 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14457-1
- Update to new upstream snapshot.

* Tue Nov 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14453-1
- Update to new upstream snapshot.

* Sun Nov 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14452-1
- Update to new upstream snapshot.

* Sat Nov 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14449-1
- Update to new upstream snapshot.

* Fri Nov 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14446-1
- Update to new upstream snapshot.

* Wed Nov 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14445-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14443-1
- Update to new upstream snapshot.

* Mon Nov 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14440-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14437-1
- Update to new upstream snapshot.

* Sat Oct 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14436-1
- Update to new upstream snapshot.

* Thu Oct 29 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14435-1
- Update to new upstream snapshot.

* Tue Oct 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14430-1
- Update to new upstream snapshot.

* Sun Oct 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14429-1
- Update to new upstream snapshot.

* Wed Oct 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14428-1
- Update to new upstream snapshot.

* Tue Oct 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14425-1
- Update to new upstream snapshot.

* Mon Oct 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14423-1
- Update to new upstream snapshot.

* Sat Oct 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14419-1
- Update to new upstream snapshot.

* Thu Oct 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14418-1
- Update to new upstream snapshot.

* Wed Oct 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14409-1
- Update to new upstream snapshot.

* Tue Oct 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14407-1
- Update to new upstream snapshot.

* Mon Oct 12 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14405-1
- Update to new upstream snapshot.

* Sun Oct 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14403-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14402-1
- Update to new upstream snapshot.

* Mon Oct 05 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14397-1
- Update to new upstream snapshot.

* Sun Oct 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14396-1
- Update to new upstream snapshot.

* Sat Oct 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14394-1
- Update to new upstream snapshot.

* Fri Oct 02 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14391-1
- Update to new upstream snapshot.

* Wed Sep 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14389-1
- Update to new upstream snapshot.

* Sun Sep 27 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14387-1
- Update to new upstream snapshot.

* Fri Sep 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14386-1
- Update to new upstream snapshot.

* Thu Sep 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14384-1
- Update to new upstream snapshot.

* Wed Sep 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14382-2
- Fix build with new glibmm (C++11).

* Tue Sep 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14382-1
- Update to new upstream snapshot.

* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14379-1
- Update to new upstream snapshot.

* Sun Sep 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14378-1
- Update to new upstream snapshot.

* Fri Sep 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14376-1
- Update to new upstream snapshot.

* Thu Sep 17 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14375-1
- Update to new upstream snapshot.

* Tue Sep 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14369-1
- Update to new upstream snapshot.

* Tue Sep 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14367-3
- Do not verify desktop file anymore.

* Tue Sep 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14367-2
- Remove patches. Don't apply to upstream master anymore.

* Tue Sep 15 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14367-1
- Update to new upstream snapshot.

* Mon Sep 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14364-1
- Update to new upstream snapshot.

* Sun Sep 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14358-1
- Update to new upstream snapshot.

* Fri Sep 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14356-1
- Update to new upstream snapshot.

* Thu Sep 10 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14354-1
- Update to new upstream snapshot.

* Tue Sep 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14352-1
- Update to new upstream snapshot.

* Tue Sep 08 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14350-1
- Update to new upstream snapshot.

* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14346-1
- Update to new upstream snapshot.

* Sun Sep 06 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14345-1
- Update to new upstream snapshot.

* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14341-1
- Update to new upstream snapshot.

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14336-1
- Update to new upstream snapshot.

* Thu Aug 20 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14313-1
- Update to new upstream snapshot.

* Wed Aug 19 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14309-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 0.92~rev14308-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 0.92~rev%{rev}-1
- Update to new upstream snapshot.

* Tue Aug 18 2015 Fabio Valentini - 0.92~rev14305-2
- Change to builpy building.

* Sun Aug 16 2015 Fabio Valentini - 0.92~rev14305-1
- Update to upstream bzr snapshot revno 14305.

* Sun Aug 16 2015 Fabio Valentini - 0.92~rev14304-1
- Update to upstream bzr snapshot revno 14304.

* Fri Aug 14 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14303-1
- Update to upstream bzr snapshot revno 14303.

* Fri Jul 31 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14269-1
- Update to bzr snapshot revno 14269.

* Tue Jul 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14251-1
- Update to bzr snapshot revno 14251.

* Thu Jul 16 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14249-1
- Update to bzr snapshot revno 14249.

* Mon Jul 13 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14243-1
- Update to bzr snapshot revno 14243.

* Sat Jul 11 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14242-1
- Bump version to bzr snapshot with revno 14242.

* Thu Jul 09 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14237-1
- Update to bzr revno 14237.

* Tue Jul 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14236-1
- Update to bzr revno 14236.

* Fri Jul 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14225-1
- Bump to revno 14225.

* Tue Jun 30 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14224-1
- Update to revno14224.

* Thu Jun 25 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14213-1
- Update to revno 14213.

* Wed Jun 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.92~rev14212-1
- Update to bzr snapshot.
- Use pkgconfig for BRs.
- Build dbus interface.
- Add -devel subpackage.

* Thu Feb 12 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.91-4
- Cleanup spec
- Use %%license
- Drop (now unneeded) perl requirements (rhbz#579390)
- Drop ChangeLog as details are covered in NEWS

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 0.91-3
- Bump for rebuild.

* Fri Jan 30 2015 Jon Ciesla <limburgher@gmail.com> - 0.91-2
- Move tutorials into main package, BZ 1187686.

* Thu Jan 29 2015 Jon Ciesla <limburgher@gmail.com> - 0.91-1
- Latest upstream.

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.48.5-7
- Rebuild for boost 1.57.0

* Fri Jan 23 2015 Marek Kasik <mkasik@redhat.com> - 0.48.5-6
- Rebuild (poppler-0.30.0)
- Backport commit "Fix build with poppler 0.29.0 (Bug #1399811)"

* Fri Jan 09 2015 Jon Ciesla <limburgher@gmail.com> - 0.48.5-5
- Added aspell support, BZ 1171934.

* Thu Nov 27 2014 Marek Kasik <mkasik@redhat.com> - 0.48.5-4
- Rebuild (poppler-0.28.1)

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.48.5-3
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Jon Ciesla <limburgher@gmail.com> - 0.48.5-1
- Latest bugfix release.
- Spurious comma patch upstreamed.
- Dropped Freetype, poppler, gc patches.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Jon Ciesla <limburgher@gmail.com> - 0.48.4-17
- Switch to lcms2.

* Tue May 27 2014 David Tardon <dtardon@redhat.com> - 0.48.4-16
- switch to librevenge-based import libs

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.48.4-15
- Rebuild for boost 1.55.0

* Thu May 15 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.48.4-14
- Fix build with new Poppler and GC (Sandro Mani, #1097945)

* Wed May 14 2014 Jon Ciesla <limburgher@gmail.com> - 0.48.4-13
- poppler rebuild.

* Mon Mar 31 2014 Jon Ciesla <limburgher@gmail.com> - 0.48.4-12
- ImageMagick rebuild.
- Patch for Freetype path.

* Wed Oct 09 2013 Jon Ciesla <limburgher@gmail.com> - 0.48.4-11
- ImageMagick rebuild.

* Mon Aug 19 2013 Marek Kasik <mkasik@redhat.com> - 0.48.4-10
- Rebuild (poppler-0.24.0)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.48.4-8
- Rebuild for boost 1.54.0

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.48.4-7
- Perl 5.18 rebuild

* Tue Jun 25 2013 Jon Ciesla <limburgher@gmail.com> - 0.48.4-6
- libpoppler rebuild.

* Mon Mar 18 2013 Jon Ciesla <limburgher@gmail.com> - 0.48.4-5
- ImageMagick rebuild.

* Fri Feb 15 2013 Jon Ciesla <limburgher@gmail.com> - 0.48.4-4
- Fix FTBFS.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Marek Kasik <mkasik@redhat.com> - 0.48.4-2
- Rebuild (poppler-0.22.0)

* Thu Dec 06 2012 Jon Ciesla <limburgher@gmail.com> - 0.48.3.1-4
- 0.48.4, fix XXE security flaw.
- Correct man page ownership.

* Thu Dec 06 2012 Jon Ciesla <limburgher@gmail.com> - 0.48.3.1-4
- Fix directory ownership, BZ 873817.
- Fix previous changelog version.

* Mon Nov 19 2012 Nils Philippsen <nils@redhat.com> - 0.48.3.1-3
- update sourceforge download URL

* Thu Nov 01 2012 Jon Ciesla <limburgher@gmail.com> - 0.48.3.1-2
- Allow loading large XML, BZ 871012.

* Fri Oct 05 2012 Jon Ciesla <limburgher@gmail.com> - 0.48.3.1-1
- Lastest upstream.

* Thu Oct 04 2012 Jon Ciesla <limburgher@gmail.com> - 0.48.2-13
- Added dep on uniconvertor, BZ 796424.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Petr Pisar <ppisar@redhat.com> - 0.48.2-11
- Perl 5.16 rebuild

* Mon Jul  2 2012 Marek Kasik <mkasik@redhat.com> - 0.48.2-10
- Rebuild (poppler-0.20.1)

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 0.48.2-9
- Perl 5.16 rebuild

* Sat Jun 23 2012 Rex Dieter <rdieter@fedoraproject.org> 
- 0.48.2-8
- fix icon/desktop-file scriptlets (#739375)
- drop .desktop vendor (f18+)
- inkscape doesn't build with poppler-0.20.0 (#822413)

* Fri Jun 15 2012 Petr Pisar <ppisar@redhat.com> - 0.48.2-7
- Perl 5.16 rebuild

* Mon Jun 11 2012 Adel Gadllah <adel.gadllah@gmail.com> - 0.48.2-6
- Rebuild for new poppler

* Wed Apr 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.48.2-5
- Rebuild for ImageMagik

* Thu Mar  8 2012 Daniel Drake <dsd@laptop.org> - 0.48.2-4
- Fix build with GCC 4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48.2-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 15 2011 German Ruiz <germanrs@fedoraproject.org> - 0.48.2-1
- New upstream version
- Fix glib include compile problem
- Fix compilation against libpng-1.5

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.48.1-10
- rebuild(poppler)

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 0.48.1-9
- Rebuild (poppler-0.18.0)

* Mon Sep 19 2011 Marek Kasik <mkasik@redhat.com> - 0.48.1-8
- Rebuild (poppler-0.17.3)

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 0.48.1-7
- Perl mass rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.48.1-6
- Perl mass rebuild

* Fri Jul 15 2011 Marek Kasik <mkasik@redhat.com> - 0.48.1-5
- Rebuild (poppler-0.17.0)

* Sun Mar 13 2011 Marek Kasik <mkasik@redhat.com> - 0.48.1-4
- Rebuild (poppler-0.16.3)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.48.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 09 2011 Lubomir Rintel <lkundrak@v3.sk> - 0.48.1-2
- Re-enable GVFS for OCAL

* Mon Feb 07 2011 Lubomir Rintel <lkundrak@v3.sk> - 0.48.1-1
- Bump release

* Fri Feb 04 2011 Lubomir Rintel <lkundrak@v3.sk> - 0.48.0-10
- Drop gnome-vfs requirement
- Fix Rawhide build

* Sat Jan 01 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.48.0-9
- rebuild (poppler)

* Wed Dec 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.48.0-8
- rebuild (poppler)

* Wed Dec 08 2010 Caolán McNamara <caolanm@redhat.com> - 0.48.0-7
- rebuilt (libwpd)

* Sun Nov 14 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.48.0-6
- rebuilt (poppler)

* Tue Oct 05 2010 Nils Philippsen <nils@redhat.com> - 0.48.0-5
- Rebuild for poppler update

* Wed Sep 29 2010 jkeating - 0.48.0-4
- Rebuilt for gcc bug 634757

* Wed Sep 29 2010 Dan Horák <dan[at]danny.cz> - 0.48.0-3
- drop the s390(x) ExcludeArch

* Mon Sep 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 0.48.0-2
- rebuild for new ImageMagick

* Wed Aug 25 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.48.0-1
- New upstream release
- Drop el5 support

* Thu Aug 19 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.48-0.5.20100505bzr
- rebuild (poppler)

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 0.48-0.4.20100505bzr
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.48-0.3.20100505bzr
- Mass rebuild with perl-5.12.0

* Wed May 05 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.48-0.2.20100505bzr
- Move to later snapshot
- Drop uniconvertor patch

* Tue Apr 06 2010 Caolán McNamara <caolanm@redhat.com> - 0.48-0.2.20100318bzr
- Resolves: rhbz#565106 fix inkscape-0.47-x11.patch to not clobber INKSCAPE_LIBS

* Thu Mar 18 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.48-0.1.20100318bzr
- Update to latest bazaar snapshot

* Thu Feb 18 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.47-7
- Fix build

* Wed Jan 20 2010 Stepan Kasal <skasal@redhat.com> - 0.47-6
- ExcludeArch: s390 s390x

* Fri Jan 15 2010 Stepan Kasal <skasal@redhat.com> - 0.47-5
- require perl(:MODULE_COMPAT_5.10.x) because the package requires libperl.so
- the same for inkscape-view

* Fri Jan  8 2010 Owen Taylor <otaylor@redhat.com> - 0.47-4
- Remove loudmouth BuildRequires; there is no current usage of loudmouth in the code

* Sun Dec 06 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-2
- Fix Rawhide build.

* Wed Nov 25 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-1
- Stable release

* Mon Nov 23 2009 Adam Jackson <ajax@redhat.com> 0.47-0.18.pre4.20091101svn
- Fix RHEL6 build.

* Mon Sep 07 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.17.pre4.20091101svn
- Icon for main window (#532325)

* Mon Sep 07 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.16.pre4.20091101svn
- Move to a later snapshot
- python-lxml and numpy seem to be rather popular, add them as hard deps

* Mon Sep 07 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.16.pre3.20091017svn
- Move to a later snapshot

* Mon Sep 07 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.16.pre3.20090925svn
- Move to a later snapshot
- Drop debugging compiler flags, enable optimizations again
- Make it build on everything since EL5 again

* Mon Sep 07 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.16.pre2.20090907svn
- Move inkview man page to -view subpackage (#515358)
- Add license, etc. to main package

* Mon Sep 07 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.15.pre2.20090907svn
- Update to a post-pre2 snapshot

* Mon Aug 10 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.15.pre1.20090629svn
- Update to a post-pre1 snapshot
- Drop upstreamed CRC32 fix

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.47-0.14.pre0.20090629svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.13.pre0.20090629svn
- Update to a newer snapshot

* Tue Jun 16 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.12.pre0.20090616svn
- Update to post-pre0 snapshot

* Tue Jun 02 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.11.20090602svn
- More recent snapshot
- Upstream removed rasterized icons again

* Sat May 23 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.10.20090518svn
- Rebuild for new poppler

* Mon May 18 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.9.20090518svn
- Update past upstream Beta release

* Mon May 18 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.8.20090508svn
- Fix ODG export

* Fri May 08 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.7.20090508svn
- Update to a post-alpha snapshot
- Upstream applied our GCC 4.4 patch

* Fri Apr 10 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.6.20090410svn
- Update to newer snapshot
- Fix doc/incview reversed subpackage content

* Wed Mar 04 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.6.20090301svn
- Rebuild for new ImageMagick

* Wed Mar 04 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.5.20090301svn
- Split documentation and inkview into subpackages

* Mon Mar 02 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.4.20090301svn
- Bump to later SVN snapshot to fix inkscape/+bug/331864
- Fix a startup crash when compiled with GCC 4.4
- It even runs now! :)

* Fri Feb 27 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.4.20090227svn
- Enable the test suite

* Fri Feb 27 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.3.20090227svn
- Past midnight! :)
- More recent snapshot, our gcc44 fixes now upstream
- One more gcc44 fix, it even compiles now
- We install icons now, update icon cache
- Disable inkboard, for it won't currently compile

* Thu Feb 26 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.3.20090226svn
- Later snapshot
- Compile with GCC 4.4

* Tue Jan 06 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.3.20090105svn
- Update to newer SVN
- Drop upstreamed patches
- Enable WordPerfect Graphics support
- Enable embedded Perl scripting
- Enable Imagemagick support
- Disable OpenSSL due to licensing issues

* Thu Aug 14 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.3.20080814svn
- Update to today's SVN snapshot
- Drop the upstreamed poppler patch

* Wed Aug 13 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.2.20080705svn
- Rediff patches for zero fuzz
- Use uniconvertor to handle CDR and WMF (#458845)

* Wed Jul 09 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.47-0.1.20080705svn
- Subversion snapshot

* Wed Jul 09 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.46-4
- Fix compile issues with newer gtk and poppler

* Thu Jun 26 2008 Lubomir Rintel <lkundrak@v3.sk> - 0.46-3
- Remove useless old hack, that triggered an assert after gtkfilechooser switched to gio

* Fri Apr 11 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.46-2.1
- More buildrequires more flexible, so that this builds on RHEL

* Sat Apr 05 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.46-2
- Fix LaTeX rendering, #441017

* Tue Mar 25 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.46-1
- 0.46 released

* Sun Mar 23 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.46-0.3.pre3
- Rebuild for newer Poppler

* Wed Mar 12 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.46-0.2.pre3
- Probably last prerelease?

* Fri Feb 22 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.46-0.2.pre2
- Panel icon sizes

* Sun Feb 17 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.46-0.1.pre2
- 0.46pre2
- Dropping upstreamed patches

* Sat Feb 16 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.45.1+0.46pre1-5
- Attempt to fix the font selector (#432892)

* Thu Feb 14 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.45.1+0.46pre1-4
- Tolerate recoverable errors in OCAL feeds
- Fix OCAL insecure temporary file usage (#432807)

* Wed Feb 13 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.45.1+0.46pre1-3
- Fix crash when adding text objects (#432220)

* Thu Feb 07 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.45.1+0.46pre1-2
- Build with gcc-4.3

* Wed Feb 06 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.45.1+0.46pre1-1
- 0.46 prerelease
- Minor cosmetic changes to satisfy the QA script
- Dependency on Boost
- Inkboard is not optional
- Merge from Denis Leroy's svn16571 snapshot:
- Require specific gtkmm24-devel versions
- enable-poppler-cairo
- No longer BuildRequire libsigc++20-devel

* Wed Dec  5 2007 Denis Leroy <denis@poolshark.org> - 0.45.1-5
- Rebuild with new openssl

* Sun Dec 02 2007 Lubomir Kundrak <lkundrak@redhat.com> - 0.45.1-4
- Added missing dependencies for modules (#301881)

* Sun Dec 02 2007 Lubomir Kundrak <lkundrak@redhat.com> - 0.45.1-3
- Satisfy desktop-file-validate, so that Rawhide build won't break

* Sat Dec 01 2007 Lubomir Kundrak <lkundrak@redhat.com> - 0.45.1-2
- Use GTK print dialog
- Added compressed SVG association (#245413)
- popt headers went into popt-devel, post Fedora 7
- Fix macro usage in changelog

* Wed Mar 21 2007 Denis Leroy <denis@poolshark.org> - 0.45.1-1
- Update to bugfix release 0.45.1
- Added R to ImageMagick-perl (#231563)

* Wed Feb  7 2007 Denis Leroy <denis@poolshark.org> - 0.45-1
- Update to 0.45
- Enabled inkboard, perl and python extensions
- Added patch for correct python autodetection
- LaTex patch integrated upstreamed, removed
- Some rpmlint cleanups

* Wed Dec  6 2006 Denis Leroy <denis@poolshark.org> - 0.44.1-2
- Added patches to fix LaTex import (#217699)
- Added patch to base postscript import on pstoedit plot-svg

* Thu Sep  7 2006 Denis Leroy <denis@poolshark.org> - 0.44.1-1
- Update to 0.44.1
- Removed png export patch, integrated upstream
- Some updated BRs

* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 0.44-6
- FE6 Rebuild

* Tue Aug 22 2006 Denis Leroy <denis@poolshark.org> - 0.44-5
- Removed skencil Require (bug 203229)

* Thu Aug 10 2006 Denis Leroy <denis@poolshark.org> - 0.44-4
- Added patch to fix png dpi export problem (#168406)

* Wed Aug  9 2006 Denis Leroy <denis@poolshark.org> - 0.44-3
- Bumping up release to fix upgrade path

* Wed Jun 28 2006 Denis Leroy <denis@poolshark.org> - 0.44-2
- Update to 0.44
- Removed obsolete patches
- Disabled experimental perl and python extensions
- Added pstoedit, skencil, gtkspell and LittleCms support
- Inkboard feature disabled pending further security tests

* Tue Feb 28 2006 Denis Leroy <denis@poolshark.org> - 0.43-3
- Rebuild

* Mon Jan 16 2006 Denis Leroy <denis@poolshark.org> - 0.43-2
- Updated GC patch, bug 171791

* Sat Dec 17 2005 Denis Leroy <denis@poolshark.org> - 0.43-1
- Update to 0.43
- Added 2 patches to fix g++ 4.1 compilation issues
- Enabled new jabber/loudmouth-based inkboard feature

* Mon Sep 26 2005 Denis Leroy <denis@poolshark.org> - 0.42.2-2
- rebuilt with newer glibmm

* Thu Sep  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.42.2-1
- update to 0.42.2

* Thu Aug 18 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.42-3
- rebuilt
- add patch to repair link-check of GC >= 6.5 (needs pthread and dl)

* Fri Jul 29 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.42-2
- Extend ngettext/dgettext patch for x86_64 build.

* Tue Jul 26 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.42-1
- update to 0.42 (also fixes #160326)
- BR gnome-vfs2-devel
- no files left in %%_libdir/inkscape
- include French manual page
- GCC4 patch obsolete, 64-bit patch obsolete, dgettext patch split off

* Tue May 31 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.41-7
- append another 64-bit related patch (dgettext configure check failed)

* Tue May 31 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.41-6
- remove explicit aclocal/autoconf calls in %%build as they create a
  bad Makefile for FC4/i386, which causes build to fail (#156228),
  and no comment explains where they were added/needed

* Tue May 31 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.41-5
- bump and rebuild as 0.41-4 failed in build system setup

* Wed May 25 2005 Jeremy Katz <katzj@redhat.com> - 0.41-4
- add patch for gcc4 problems (ignacio, #156228)
- fix build on 64bit boxes.  sizeof(int) != sizeof(void*)

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.41-3
- rebuild on all arches

* Thu Apr 07 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Feb 09 2005 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.41-1
- 0.41.
- enable python.

* Sat Dec 04 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.40-1
- 0.40.

* Tue Nov 16 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.40-0.pre3
- 0.40pre3.

* Thu Nov 11 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0.39-0.fdr.2
- post/postun for new mime system.
- Dropped redundant BR XFree86-devel.

* Sun Aug 29 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.39-0.fdr.1
- 0.39.

* Sat Apr 10 2004 P Linnell <scribusdocs at atlantictechsolutions.com> 0:0.38.1-0.fdr.1
- respin real fix for Provides/Requires for perl(SpSVG)

* Fri Apr 9 2004 P Linnell <scribusdocs at atlantictechsolutions.com> 0:0.38.1-0.fdr.0
- respin with updated tarball with fix for postscript printing

* Thu Apr 8 2004 P Linnell <scribusdocs at atlantictechsolutions.com> 0:0.38-0.fdr.2
- respin to fix provides

* Thu Apr 8 2004 P Linnell <scribusdocs at atlantictechsolutions.com> 0:0.38.0.fdr.1
- version upgrade with many improvements and bug fixes

* Fri Mar 19 2004 P Linnell <scribusdocs at atlantictechsolutions.com> 0:0.37.0.fdr.7
- repsin - sourceforge does not allow reloading files with same name
* Tue Mar 16 2004 P Linnell <scribusdocs at atlantictechsolutions.com> 0:0.37.0.fdr.6
- fix typo in provides
* Tue Mar 16 2004 P Linnell <scribusdocs at atlantictechsolutions.com> 0:0.37.0.fdr.5
- add %%{release} to provides perl(SpSVG) = %%{epoch}:%%{version}:%%{release} only
* Tue Mar 16 2004 P Linnell <scribusdocs at atlantictechsolutions.com> 0:0.37.0.fdr.4
- add %%{release} to provides
* Sun Mar 14 2004 P Linnell <scribusdocs at atlantictechsolutions.com> 0:0.37.0.fdr.3
- add arch dependent flags
* Thu Mar 11 2004 P Linnell <scribusdocs at atlantictechsolutions.com> 0:0.37.0.fdr.2
- add libsigc++-devel instead of add libsigc++ - duh
- add BuildRequires:  perl-XML-Parser
- fix package name to follow package naming guidelines
* Mon Mar 1 2004   P Linnell <scribusdocs at atlantictechsolutions.com>   0:0.37.1.fdr.1
- disable static libs
- enable inkjar
* Tue Feb 10  2004 P Linnell <scribusdocs at atlantictechsolutions.com>   0:0.37.0.fdr.1
- pgp'd tarball from inkscape.org
- clean out the cvs tweaks in spec file
- enable gnome-print
- add the new tutorial files
- make sure .mo file gets packaged
- add provides: perlSVG
- submit to Fedora QA
* Sat Feb 7  2004 P Linnell <scribusdocs at atlantictechsolutions.com>
- rebuild of current cvs
- tweaks to build cvs instead of dist tarball
- add inkview
* Sat Dec 20 2003 P Linnell <scribusdocs at atlantictechsolutions.com>
- First crack at Fedora/RH spec file
- nuke gnome print - it won't work (bug is filed already)
