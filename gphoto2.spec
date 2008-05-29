%define name	gphoto2
%define version	2.4.1
%define release	%mkrel 1

%define extraversion %nil

Summary:	Command line utilities to access digital cameras
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL+
Group:		Graphics
Source0:	http://heanet.dl.sourceforge.net/sourceforge/gphoto/%{name}-%{version}%{?extraversion:%extraversion}.tar.bz2
Url:		http://sourceforge.net/projects/gphoto/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts:	libgphoto2 < 2.1.1
Requires:	libgphoto-hotplug
BuildRequires:	glib-devel libusb-devel >= 0.1.6 zlib-devel findutils perl
BuildRequires:	libgphoto-devel >= 2.1.99
BuildRequires:	libexif-devel libaa-devel libcdk-devel
BuildRequires:	libpopt-devel readline-devel libjpeg-devel

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
rm -rf ${RPM_BUILD_DIR}/%{name}

%build
%configure2_5x
%make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%doc NEWS ChangeLog README TODO
%{_mandir}/*/*
