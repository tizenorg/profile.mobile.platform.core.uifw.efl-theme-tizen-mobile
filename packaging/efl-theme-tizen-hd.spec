Name:          efl-theme-tizen-hd
Summary:       Tizen theme files
Version:       1.0.327
Release:       1
Group:         TO_BE/FILLED_IN
License:       TO_BE/FILLED_IN
Source0:       %{name}-%{version}.tar.gz
BuildRequires: perl, edje, edje-bin, embryo, embryo-bin, eet-bin
%define _unpackaged_files_terminate_build 0

%description
Tizen HD theme for EFL


%package -n efl-theme-tizen-devel
Summary: Development package

%description -n efl-theme-tizen-devel
Development package

%prep
%setup -q 


%build
export CFLAGS+=" --fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=/usr/lib"

make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/usr/share/license/%{name}

%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/tizen-HD-dark.edj
%{_datadir}/elementary/themes/tizen-HD-light.edj
%{_datadir}/elementary/themes/tables/InputColors.cfg
%{_datadir}/elementary/themes/tables/ChangeableColorTable.xml
%{_datadir}/elementary/themes/tables/FontInfoTable.xml
%manifest %{name}.manifest
/usr/share/license/%{name}

%files -n efl-theme-tizen-devel
%defattr(-,root,root,-)
/opt/var/efl-theme-tizen-edc/*
