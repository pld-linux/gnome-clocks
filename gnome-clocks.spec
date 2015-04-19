Summary:	Clocks applications for GNOME
Name:		gnome-clocks
Version:	3.16.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-clocks/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	5f1d7ce5774de60f3f8b6995ba69ca5e
URL:		https://live.gnome.org/GnomeClocks
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	geoclue2-devel >= 1.99.3
BuildRequires:	geocode-glib-devel >= 0.99.4
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-desktop-devel >= 3.8.0
BuildRequires:	gsound-devel >= 0.98
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libcanberra-devel >= 0.30
BuildRequires:	libgweather-devel >= 3.14.0
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.36.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.10.0
Requires:	hicolor-icon-theme
Requires:	libgweather >= 3.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Clocks is a simple application to show the time, date and
alarms.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

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
%{_datadir}/appdata/org.gnome.clocks.appdata.xml
%{_datadir}/gnome-clocks
%{_datadir}/gnome-shell/search-providers/org.gnome.clocks.search-provider.ini
%{_datadir}/glib-2.0/schemas/org.gnome.clocks.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.clocks.service
%{_desktopdir}/org.gnome.clocks.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
