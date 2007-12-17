%define name ddccontrol
%define version 0.4.2
%define release %mkrel 1
%define dbversion 20061014
%define ddcdb	%{name}-db-%{dbversion}

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d
%define __libtoolize true

Summary: Ddccontrol control the monitor parameters
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Source1: %{ddcdb}.tar.bz2
License: GPL 
Group: System/Kernel and hardware 
Url: http://ddccontrol.sourceforge.net/
BuildRequires: pciutils-devel
BuildRequires: libxml2-devel
BuildRequires: perl(XML::Parser)
BuildRequires: gtk+-devel

%description
DDCcontrol is a program running on Linux, used to control monitor parameters,
like brightness and contrast, by software, i.e. without using the OSD
and the buttons in front of the monitor.

%package -n %{libname}
Summary: Libddccontrol library 
Group: Development/Other
Provides: lib%{name} = %{version}

%description -n %{libname}
DDCcontrol is a program running on Linux, used to control monitor parameters,
like brightness and contrast, by software, i.e. without using the OSD
and the buttons in front of the monitor.


%package -n %{libnamedev}
Summary: Libddccontrol library headers and development libraries
Group: Development/Other
Requires: %{libname} = %{version}
Provides: lib%{name}-devel = %{version}
Provides: libddccontrol-devel

%description -n %{libnamedev}
libddccontrol devel files


%prep
%setup -q -a 1

%build
%configure
%make
cd %{ddcdb}
%configure --prefix=%{_prefix}/%{name}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
cd %{ddcdb}
make install DESTDIR=$RPM_BUILD_ROOT
chmod 755 $RPM_BUILD_ROOT/%{_bindir}/ddcpci

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/ddccontrol
%{_bindir}/ddcpci
%{_bindir}/gddccontrol
%{_datadir}/locale/*/*/*
%{_datadir}/ddccontrol-db/*
#%{_datadir}/%name
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
#%{_libdir}/bonobo/servers/*
#%{_libdir}/%name
%{_mandir}/man1/*

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.*

%files -n %libnamedev
%defattr(-,root,root)
%_libdir/*.so
%_libdir/*.*a
%{_includedir}/%name

