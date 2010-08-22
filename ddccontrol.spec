%define name ddccontrol
%define version 0.4.2
%define release %mkrel 3
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
Patch0: ddccontrol-0.4.2-fix-str-fmt.patch
License: GPL 
Group: System/Kernel and hardware 
Url: http://ddccontrol.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: pciutils-devel
BuildRequires: libxml2-devel
BuildRequires: perl(XML::Parser)
BuildRequires: gtk+2-devel

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
%patch0 -p0

%build
%configure2_5x
%make
cd %{ddcdb}
%configure2_5x --prefix=%{_prefix}/%{name}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
cd %{ddcdb}
%makeinstall_std
chmod 755 $RPM_BUILD_ROOT/%{_bindir}/ddcpci

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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

