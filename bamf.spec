%define	major	0
%define libname	%mklibname %{name} %{major}
%define develname	%mklibname 	%{name} -d

Name:           bamf
Version:		0.2.116
Release:		2
License:		LGPLv3
Summary:		Window matching library
Url:			http://launchpad.net/bamf
Group:			Graphical desktop/Other
Source0:		%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  vala-devel
BuildRequires:	gcc-c++, gcc, gcc-cpp

%description
Bamf matches application windows to desktop files.

%package daemon
Summary:        Window matching library - daemon
Group:          System/Servers

%description daemon
Bamf matches application windows to desktop files.
This package contains the daemon used by the library and a gio module that
facilitates the matching of applications started through GDesktopAppInfo.

%package -n %{libname}
Summary:        Window matching library - shared libraries
Group:          System/Libraries

%description -n %{libname}
Bamf matches application windows to desktop files.

This package contains shared libraries to be used by applications.

%package -n %{develname}
Summary:        Window matching library - development files
Group:          Development/C
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n %{develname}
Bamf matches application windows to desktop files.

This package contains files that are needed to build applications.

%prep
%setup -q

%build
export CC=gcc
export CXX=g++
export CFLAGS+=" -fno-strict-aliasing -Wno-error=deprecated-declarations" CXXFLAGS+=" -fno-strict-aliasing" FFLAGS+=" -fno-strict-aliasing"

%configure2_5x \
  --disable-static \
  --enable-introspection=yes
%make

%install
%makeinstall_std

find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files daemon
%defattr(-,root,root)
%doc COPYING
%{_datadir}/dbus-1/services/*.service
%{_libexecdir}/bamfdaemon

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/libbamf3/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/libbamf/



%changelog
* Sat May 19 2012 Crispin Boylan <crisb@mandriva.org> 0.2.116-1
+ Revision: 799665
- Disable strict aliasing
- New release

* Tue Nov 01 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.2.104-1
+ Revision: 708190
- spec clean up
- fixed group
- fixed group
- imported package bamf

