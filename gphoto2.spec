%define extraversion %nil

Summary:	Command line utilities to access digital cameras
Name:		gphoto2
Version:	2.4.14
Release:	1
License:	GPL+
Group:		Graphics
Source0:	http://heanet.dl.sourceforge.net/sourceforge/gphoto/%{name}-%{version}%{?extraversion:%extraversion}.tar.bz2
Url:		http://sourceforge.net/projects/gphoto/
Conflicts:	libgphoto2 < 2.1.1
Requires:	libgphoto-hotplug
BuildRequires:	gphoto2-devel >= %{version}
BuildRequires:	cdk-devel
BuildRequires:	libexif-devel >= 0.3.2
BuildRequires:	jpeg-devel
BuildRequires:	ncurses-devel
BuildRequires:	libaa-devel
BuildRequires:	libpopt-devel
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
