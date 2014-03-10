Summary:	Faenza icon theme for MATE Desktop
Summary(pl.UTF-8):	Motyw ikon Faenza dla środowiska MATE Desktop
Name:		mate-icon-theme-faenza
Version:	1.8.0
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	ba0909462dab2362014f388a79099923
URL:		http://www.mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Faenza icon theme for MATE Desktop.

%description -l pl.UTF-8
Motyw ikon Faenza dla środowiska MATE Desktop.

%package dark
Summary:	Faenza Dark icon theme for MATE Desktop
Summary(pl.UTF-8):	Motyw ikon Faenza Dark dla środowiska MATE Desktop
Group:		Themes
Requires(post,postun):	gtk-update-icon-cache

%description dark
Faenza Dark icon theme for MATE Desktop

%description dark -l pl.UTF-8
Motyw ikon Faenza Dark dla środowiska MATE Desktop.

%package gray
Summary:	Faenza Gray icon theme for MATE Desktop
Summary(pl.UTF-8):	Motyw ikon Faenza Gray dla środowiska MATE Desktop
Group:		Themes
Requires(post,postun):	gtk-update-icon-cache

%description gray
Faenza Gray icon theme for MATE Desktop

%description gray -l pl.UTF-8
Motyw ikon Faenza Gray dla środowiska MATE Desktop.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	install_sh="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

> $RPM_BUILD_ROOT%{_iconsdir}/matefaenza/icon-theme.cache
> $RPM_BUILD_ROOT%{_iconsdir}/matefaenzadark/icon-theme.cache
> $RPM_BUILD_ROOT%{_iconsdir}/matefaenzagray/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache matefaenza

%postun
%update_icon_cache matefaenza

%post	dark
%update_icon_cache matefaenzadark

%postun	dark
%update_icon_cache matefaenzadark

%post	gray
%update_icon_cache matefaenzagray

%postun	gray
%update_icon_cache matefaenzagray

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_iconsdir}/matefaenza
%{_iconsdir}/matefaenza/actions
%{_iconsdir}/matefaenza/apps
%{_iconsdir}/matefaenza/categories
%{_iconsdir}/matefaenza/devices
%{_iconsdir}/matefaenza/emblems
%{_iconsdir}/matefaenza/extras
%{_iconsdir}/matefaenza/mimetypes
%{_iconsdir}/matefaenza/places
%{_iconsdir}/matefaenza/status
%{_iconsdir}/matefaenza/stock
%{_iconsdir}/matefaenza/index.theme
%ghost %{_iconsdir}/matefaenza/icon-theme.cache

%files dark
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_iconsdir}/matefaenzadark
%{_iconsdir}/matefaenzadark/actions
%{_iconsdir}/matefaenzadark/apps
%{_iconsdir}/matefaenzadark/categories
%{_iconsdir}/matefaenzadark/devices
%{_iconsdir}/matefaenzadark/extras
%{_iconsdir}/matefaenzadark/places
%{_iconsdir}/matefaenzadark/status
%{_iconsdir}/matefaenzadark/stock
%{_iconsdir}/matefaenzadark/index.theme
%ghost %{_iconsdir}/matefaenzadark/icon-theme.cache

%files gray
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_iconsdir}/matefaenzagray
%{_iconsdir}/matefaenzagray/apps
%{_iconsdir}/matefaenzagray/categories
%{_iconsdir}/matefaenzagray/devices
%{_iconsdir}/matefaenzagray/extras
%{_iconsdir}/matefaenzagray/places
%{_iconsdir}/matefaenzagray/status
%{_iconsdir}/matefaenzagray/stock
%{_iconsdir}/matefaenzagray/index.theme
%ghost %{_iconsdir}/matefaenzagray/icon-theme.cache
