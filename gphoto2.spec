%define name	gphoto2
%define version	2.4.7
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
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS ChangeLog README TODO
%{_bindir}/*
%{_mandir}/*/*
