Summary:	Clocks applications for GNOME
Summary(pl.UTF-8):	Aplikacje zegarów dla GNOME
Name:		gnome-clocks
Version:	3.26.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-clocks/3.26/%{name}-%{version}.tar.xz
# Source0-md5:	7e9441c12b0c011fa0ba2c0cfcccaaa1
URL:		https://live.gnome.org/GnomeClocks
BuildRequires:	geoclue2-devel >= 2.4.0
BuildRequires:	geocode-glib-devel >= 1.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-desktop-devel >= 3.8.0
BuildRequires:	gsound-devel >= 0.98
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	libgweather-devel >= 3.14.0
BuildRequires:	meson
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.726
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	vala-gsound
BuildRequires:	vala-libgweather
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.44.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	geoclue2 >= 2.4.0
Requires:	geocode-glib >= 1.0
Requires:	glib2 >= 1:2.44.0
Requires:	gnome-desktop >= 3.8.0
Requires:	gsound >= 0.98
Requires:	gtk+3 >= 3.20.0
Requires:	hicolor-icon-theme
Requires:	libgweather >= 3.14.0
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
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

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
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gnome-clocks
%{_datadir}/appdata/org.gnome.clocks.appdata.xml
%{_datadir}/gnome-clocks
%{_datadir}/gnome-shell/search-providers/org.gnome.clocks.search-provider.ini
%{_datadir}/glib-2.0/schemas/org.gnome.clocks.gschema.xml
%{_datadir}/dbus-1/services/org.gnome.clocks.service
%{_desktopdir}/org.gnome.clocks.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.clocks.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.clocks-symbolic.svg
