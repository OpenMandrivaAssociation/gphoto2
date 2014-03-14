%define extraversion %nil

Summary:	Command line utilities to access digital cameras
Name:		gphoto2
Version:	2.5.3
Release:	1
License:	GPL+
Group:		Graphics
Url:		http://sourceforge.net/projects/gphoto/
Source0:	http://heanet.dl.sourceforge.net/sourceforge/gphoto/%{name}-%{version}%{?extraversion:%extraversion}.tar.bz2

BuildRequires:	cdk-devel
BuildRequires:	jpeg-devel
BuildRequires:	libaa-devel
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libgphoto2) >= %{version}
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(popt)
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
%setup -qn %{name}-%{version}%{?extraversion:%extraversion}

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

