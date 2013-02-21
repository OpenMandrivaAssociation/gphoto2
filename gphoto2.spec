%define extraversion %nil

Summary:	Command line utilities to access digital cameras
Name:		gphoto2
Version:	2.5.1
Release:	1
License:	GPL+
Group:		Graphics
Url:		http://sourceforge.net/projects/gphoto/
Source0:	http://heanet.dl.sourceforge.net/sourceforge/gphoto/%{name}-%{version}%{?extraversion:%extraversion}.tar.bz2
Conflicts:	libgphoto2 < 2.1.1
Requires:	libgphoto-hotplug
BuildRequires:	pkgconfig(libgphoto2) >= %{version}
BuildRequires:	cdk-devel
BuildRequires:	libexif-devel >= 0.3.2
BuildRequires:	jpeg-devel
BuildRequires:	ncurses-devel
BuildRequires:	libaa-devel
BuildRequires:	popt-devel
BuildRequires:	readline-devel

%description
The gPhoto2 project is a universal, free application and library
framework that lets you download images from several different
digital camera models, including the newer models with USB
connections. Note that
a) for some older camera models you must use the old "gphoto" package.
b) for USB mass storage models you must use the driver in the kernel.

This package contains the command-line utility gphoto2.

%prep
%setup -q -n %{name}-%{version}%{?extraversion:%extraversion}

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS ChangeLog README TODO
%{_bindir}/*
%{_mandir}/*/*


%changelog
* Mon Aug 27 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2.5.0-1
+ Revision: 815860
- fix br
- update to new version 2.5.0

* Wed May 23 2012 Oden Eriksson <oeriksson@mandriva.com> 2.4.14-1
+ Revision: 800198
- fix deps
- 2.4.14

  + Götz Waschk <waschk@mandriva.org>
    - yearly rebuild

* Wed Apr 20 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.4.11-1
+ Revision: 656326
- new version 2.4.11

* Sat Apr 16 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.4.10-2
+ Revision: 653533
- rebuild

* Thu Sep 23 2010 Funda Wang <fwang@mandriva.org> 2.4.10-1mdv2011.0
+ Revision: 580779
- update to new version 2.4.10

  + Frederik Himpe <fhimpe@mandriva.org>
    - Update to new version 2.4.8

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.7-2mdv2010.1
+ Revision: 488758
- rebuilt against libjpeg v8

* Sun Aug 23 2009 Frederik Himpe <fhimpe@mandriva.org> 2.4.7-1mdv2010.0
+ Revision: 420018
- Update to new version 2.4.7

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 2.4.5-2mdv2010.0
+ Revision: 416657
- rebuilt against libjpeg v7

* Wed May 06 2009 Funda Wang <fwang@mandriva.org> 2.4.5-1mdv2010.0
+ Revision: 372375
- New version 2.4.5

* Wed Feb 25 2009 Thierry Vignaud <tv@mandriva.org> 2.4.3-2mdv2009.1
+ Revision: 344805
- rebuild for new libreadline

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 2.4.3-1mdv2009.1
+ Revision: 324733
- update to new version 2.4.3

* Wed Jul 16 2008 Frederic Crozat <fcrozat@mandriva.com> 2.4.2-1mdv2009.0
+ Revision: 236519
- Release 2.4.2

* Thu May 29 2008 Frederic Crozat <fcrozat@mandriva.com> 2.4.1-1mdv2009.0
+ Revision: 212973
- Release 2.4.1

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.4.0-2mdv2008.1
+ Revision: 150231
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Aug 03 2007 Adam Williamson <awilliamson@mandriva.org> 2.4.0-1mdv2008.0
+ Revision: 58526
- drop old obsoletes / provides hackgphoto2 (it's been long enough)
- correct license (it's GPL not LGPL, whatever the template spec says) and use Fedora license policy
- spec clean
- new release 2.4.0

* Wed Jun 13 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 2.3.1-2mdv2008.0
+ Revision: 38595
- Rebuild with libslang2.
- Small cleanups.

