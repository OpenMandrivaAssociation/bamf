%define	major	3
%define libname	%mklibname %{name} %{major}
%define develname	%mklibname 	%{name} -d
%define girname		%mklibname %{name}-gir %{major}
%define debug_package	%{nil}

Name:           bamf
Version:		0.5.5
Release:		1
License:		LGPLv3
Summary:		Window matching library
Url:			http://launchpad.net/bamf
Group:			Graphical desktop/Other
Source0:		https://launchpad.net/bamf/0.5/%{version}/+download/%{name}-%{version}.tar.xz
Patch0:     bamf-no-gtester2xunit.patch

BuildRequires:  gnome-common
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  vala-devel
BuildRequires:	gcc-c++, gcc, gcc-cpp
BuildRequires:  python-libxml2
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(systemd)

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
Requires:       %{name}-daemon = %{EVRD}
Requires:       %{libname} = %{EVRD}

%description -n %{develname}
Bamf matches application windows to desktop files.

This package contains files that are needed to build applications.

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}
Obsoletes:      %{girname} <= 0.5.4-1

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%setup -q
%autopatch -p1

# fix build with glib >= 2.62
sed -i -e '/CFLAGS/s,-Werror\s\?,,g' configure.ac

%build
#export CC=gcc
#export CXX=g++
export CFLAGS="%{optflags} -Wno-deprecated-declarations"

%configure \
  --disable-static \
  --enable-introspection=yes
%make_build

%install
%make_install

find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files daemon
%doc COPYING
%{_datadir}/dbus-1/services/*.service
#{_libexecdir}/bamfdaemon
%{_userunitdir}/bamfdaemon.service
%{_libexecdir}/bamf/bamfdaemon
%{_libexecdir}/bamf/bamfdaemon-dbus-runner
%{_datadir}/upstart/sessions/bamfdaemon.conf

%files -n %{libname}
%doc COPYING
%{_libdir}/libbamf%{major}.so.*

%files -n %{develname}
%doc COPYING
%{_includedir}/libbamf3/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/libbamf/
%{_datadir}/gir-1.0/Bamf-%{major}.gir
%{_datadir}/vala/vapi/libbamf3.vapi

%files -n %{girname}
%{_libdir}/girepository-1.0/Bamf-%{major}.typelib
