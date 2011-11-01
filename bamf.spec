%define	major	0
%define libname	%mklibname %{name} %{major}
%define develname	%mklibname 	%{name} -d

Name:           bamf
Version:	0.2.104
Release:        1
License:        LGPLv3
Summary:        Window matching library
Url:            http://launchpad.net/bamf
Group:          Graphical desktop/Other
Source:         %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  vala-devel

%description
Bamf matches application windows to desktop files.

%package daemon
Summary:        Window matching library - daemon
Group:          System/GUI/Other

%description daemon
Bamf matches application windows to desktop files.
This package contains the daemon used by the library and a gio module that
facilitates the matching of applications started through GDesktopAppInfo.

%package -n %{libname}
Summary:        Window matching library - shared libraries
Group:          Development/Libraries/Other

%description -n %{libname}
Bamf matches application windows to desktop files.

This package contains shared libraries to be used by applications.

%package -n %{develname}
Summary:        Window matching library - development files
Group:          Development/Libraries/Other
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n %{develname}
Bamf matches application windows to desktop files.

This package contains files that are needed to build applications.

%prep
%setup -q

%build
%configure2_5x \
  --disable-static \
  --enable-introspection=yes
%make

%install
%makeinstall_std
# Remove unwanted files
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

