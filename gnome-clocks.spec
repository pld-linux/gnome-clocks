Summary:	Clocks applications for GNOME
Summary(pl.UTF-8):	Aplikacje zegarów dla GNOME
Name:		gnome-clocks
Version:	40.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-clocks/40/%{name}-%{version}.tar.xz
# Source0-md5:	15b7ff01d11448e206595f660aa49e74
URL:		https://wiki.gnome.org/Apps/Clocks
BuildRequires:	geoclue2-devel >= 2.4.0
BuildRequires:	geocode-glib-devel >= 1.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.58
BuildRequires:	gnome-desktop-devel >= 3.8.0
BuildRequires:	gsound-devel >= 0.98
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	libgweather-devel >= 3.32.0
BuildRequires:	libhandy1-devel >= 1.0.0
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3 >= 1:3.2
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	vala-gsound >= 0.98
BuildRequires:	vala-libgweather >= 3.32.0
BuildRequires:	vala-libhandy1 >= 1.0.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.58
Requires(post,postun):	gtk-update-icon-cache
Requires:	geoclue2 >= 2.4.0
Requires:	geocode-glib >= 1.0
Requires:	glib2 >= 1:2.58
Requires:	gnome-desktop >= 3.8.0
Requires:	gsound >= 0.98
Requires:	gtk+3 >= 3.20.0
Requires:	hicolor-icon-theme
Requires:	libgweather >= 3.32.0
Requires:	libhandy1 >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Clocks is a simple application to show the time, date and
alarms.

%description -l pl.UTF-8
GNOME Clocks to prosta aplikacja do wyświetlania czasu, daty i
alarmów.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.md NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-clocks
%{_datadir}/dbus-1/services/org.gnome.clocks.service
%{_datadir}/glib-2.0/schemas/org.gnome.clocks.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.clocks.search-provider.ini
%{_datadir}/metainfo/org.gnome.clocks.metainfo.xml
%{_desktopdir}/org.gnome.clocks.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.clocks.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.clocks-symbolic.svg
