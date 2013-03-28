Summary:	Clocks applications for GNOME
Name:		gnome-clocks
Version:	3.8.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-clocks/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	6d0c387c1f11b30cb91fbe43e54d3d63
URL:		https://live.gnome.org/GnomeClocks
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gnome-desktop-devel >= 3.8.0
BuildRequires:	gtk+3-devel >= 3.8.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-devel >= 0.30
BuildRequires:	libgweather-devel >= 3.8.0
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	vala >= 2:0.18.0
Requires(post,postun):	glib2 >= 1:2.30.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Clocks is a simple application to show the time, date and
alarms.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4 -I libgd
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_icon_cache HighContrast
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%update_icon_cache HighContrast
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-clocks
%{_datadir}/gnome-clocks
%{_datadir}/glib-2.0/schemas/org.gnome.clocks.gschema.xml
%{_desktopdir}/gnome-clocks.desktop
%{_iconsdir}/HighContrast/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.png