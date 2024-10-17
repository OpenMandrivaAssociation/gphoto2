%define extraversion %nil
# disable for now
%define _disable_lto 1

Summary:	Command line utilities to access digital cameras
Name:		gphoto2
Version:	2.5.28
Release:	2
License:	GPL+
Group:		Graphics
Url:		https://sourceforge.net/projects/gphoto/
Source0:	https://iweb.dl.sourceforge.net/project/gphoto/gphoto/%{version}/gphoto2-%{version}.tar.bz2

BuildRequires:	cdk-devel
BuildRequires:	jpeg-devel
BuildRequires:	libaa-devel
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libgphoto2) >= %{version}
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(x11)
BuildRequires:	gpm-devel
BuildRequires:	pkgconfig(slang)
Requires:	libgphoto-common

%description
The gPhoto2 project is a universal, free application and library
framework that lets you download images from several different
digital camera models, including the newer models with USB
connections. Note that
a) for some older camera models you must use the old "gphoto" package.
b) for USB mass storage models you must use the driver in the kernel.

This package contains the command-line utility gphoto2.

%prep
%autosetup -n %{name}-%{version}%{?extraversion:%extraversion} -p1

%build
%configure
%make_build

%install
%make_install
rm -rf  %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS ChangeLog README TODO
%{_bindir}/*
%{_mandir}/*/*
