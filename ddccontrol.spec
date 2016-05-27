%define _disable_rebuild_configure 1
%define dbversion 20061014
%define ddcdb %{name}-db-%{dbversion}

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: Control the monitor parameters
Name: ddccontrol
Version: 0.4.2
Release: 7
Source0: %{name}-%{version}.tar.bz2
Source1: %{ddcdb}.tar.bz2
Patch0: ddccontrol-0.4.2-fix-str-fmt.patch
License: GPL 
Group: System/Kernel and hardware 
Url: http://ddccontrol.sourceforge.net/
BuildRequires: pciutils-devel
BuildRequires: libxml2-devel
BuildRequires: perl(XML::Parser)
BuildRequires: pkgconfig(gtk+-2.0)

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
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}ddccontrol0-devel < %{version}-%{release}

%description -n %{libnamedev}
libddccontrol devel files.

%prep
%setup -q -a 1
%patch0 -p0

%build
%configure
%make

cd %{ddcdb}
%configure --prefix=%{_prefix}/%{name}
%make

%install
%makeinstall_std

cd %{ddcdb}
%makeinstall_std
chmod 755 %{buildroot}/%{_bindir}/ddcpci

%files
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
%_libdir/*.so.*

%files -n %libnamedev
%{_libdir}/*.so
%{_libdir}/*.*a
%{_includedir}/%{name}
