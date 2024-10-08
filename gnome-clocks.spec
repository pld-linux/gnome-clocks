# TODO: use gtk4-update-icon-cache

%define soup_api	%(pkg-config --variable=soupapiversion gweather4 2>/dev/null || echo 2.4)

Summary:	Clocks applications for GNOME
Summary(pl.UTF-8):	Aplikacje zegarów dla GNOME
Name:		gnome-clocks
Version:	47.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-clocks/47/%{name}-%{version}.tar.xz
# Source0-md5:	71c6c1f8127862043e996aef561a673e
Patch0:		%{name}-no-update.patch
URL:		https://wiki.gnome.org/Apps/Clocks
BuildRequires:	geoclue2-devel >= 2.4.0
%if "%{soup_api}" == "3.0"
BuildRequires:	geocode-glib2-devel >= 3.26
%else
BuildRequires:	geocode-glib-devel >= 1.0
%endif
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.72
BuildRequires:	gnome-desktop4-devel >= 42
BuildRequires:	gtk4-devel >= 4.5
BuildRequires:	libadwaita-devel >= 1.5
BuildRequires:	libgweather4-devel >= 4.0
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3 >= 1:3.2
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	vala-libadwaita >= 1.5
BuildRequires:	vala-libgweather4 >= 4.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.72
Requires(post,postun):	gtk-update-icon-cache
Requires:	geoclue2 >= 2.4.0
%if "%{soup_api}" == "3.0"
Requires:	geocode-glib2 >= 3.26
%else
Requires:	geocode-glib >= 1.0
%endif
Requires:	glib2 >= 1:2.72
Requires:	gnome-desktop4 >= 42
Requires:	gtk4 >= 4.5
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.5
Requires:	libgweather4 >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Clocks is a simple application to show the time, date and
alarms.

%description -l pl.UTF-8
GNOME Clocks to prosta aplikacja do wyświetlania czasu, daty i
alarmów.

%prep
%setup -q
%patch0 -p1

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
