%define DEVEL_PREFIX /opt/var/efl-theme-tizen-mobile-devel
Summary: EFL themes for Tizen Mobile
Name: efl-theme-tizen-mobile
Version: 1.0
Release: 0
Group: Mobile/Themes
License: BSD 2-Clause
Source: %{name}-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: edje
BuildRequires: edje-bin
BuildRequires: embryo
BuildRequires: embryo-bin

%description -n efl-theme-tizen-mobile
EFL themes for Tizen Mobile

%package -n efl-theme-tizen-mobile-devel
Summary: Development package

%description -n efl-theme-tizen-mobile-devel
Development package for Tizen Mobile theme

%prep
%setup -q

%build
autoreconf -ivf
%configure
export CFLAGS+=" --fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=/usr/lib"
make

%install
rm -rf %{buildroot}
%make_install

#for efl-theme-tizen-mobile
%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/tizen-mobile.edj
%{_datadir}/elementary/themes/default.edj
#TODO
#%manifest %{name}.manifest
#license
#elementary config for mobile

%files -n efl-theme-tizen-mobile-devel
%defattr(-,root,root,-)
#TODO  - later
#%{DEVEL_PREFIX}/*
