%define name ddccontrol
%define version 0.4.2
%define release  5
%define dbversion 20061014
%define ddcdb	%{name}-db-%{dbversion}

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} -d

Summary: Control the monitor parameters
Name: %{name}
Version: %{version}
Release: %{release}
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
%makeinstall_std
cd %{ddcdb}
%makeinstall_std
chmod 755 %{buildroot}/%{_bindir}/ddcpci

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean

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
%_libdir/*.so
%_libdir/*.*a
%{_includedir}/%name



%changelog
* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 0.4.2-3mdv2011.0
+ Revision: 571894
- new devel package policy
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4.2-2mdv2009.0
+ Revision: 222088
- we need gtk+2-devel instead of gtk+1-devel in order to build...
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- do not hardcode lzma extension!!!

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + J√©r√¥me Soyer <saispo@mandriva.org>
    - Bump Release


* Wed Aug 02 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4.1-2mdv2007.0
- Rebuild with latest dbus

* Fri Jun 09 2006 Erwan Velu <erwan@seanodes.com> 0.4.1
- 0.4.1

* Wed Apr 26 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.3-3mdk
- Fix BuildRequires

* Tue Apr 25 2006 Nicolas LÈcureuil <neoclust@mandriva.org> 0.3-2mdk
- Fix BuildRequires
- use mkrel

* Wed Nov 16 2005 Lenny Cartier <lenny@mandriva.com> 0.3-1mdk
- 0.3
- newest ddb 20051114

* Fri Jul 22 2005 Erwan Velu <erwan@seanodes.com> 0.1.3-1mdk
- 0.1.3 & newest ddb (20050715)

* Thu Jun 09 2005 Erwan Velu <erwan@seanodes.com> 0.1.2-1mdk
- Inital release

