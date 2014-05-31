Name:          efl-theme-tizen
Summary:       Tizen theme files
Version:       1.0.233b48
Release:       1
Group:         TO_BE/FILLED_IN
License:       BSD
Source0:       %{name}-%{version}.tar.gz
BuildRequires: perl, edje, edje-bin, embryo, embryo-bin
%define _unpackaged_files_terminate_build 0

%description
Tizen theme for EFL

%if %{_repository} == "mobile"
%package -n efl-theme-tizen-devel
Summary: Development package

%description -n efl-theme-tizen-devel
Development package
%endif

%prep
%setup -q 

%build
export CFLAGS+=" --fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=/usr/lib"


cd %{_repository} && make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
cd %{_repository} && make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/usr/share/license/%{name}
%if %{_repository} == "mobile"
cp %{buildroot}/usr/share/elementary/themes/tizen-HD-dark.edj %{buildroot}/usr/share/elementary/themes/tizen-hd.edj
%endif

%files
%defattr(-,root,root,-)
%if %{_repository} == "wearable"
%{_datadir}/elementary/themes/tizen*.edj
%endif
%manifest %{name}.manifest
/usr/share/license/%{name}
%if %{_repository} == "mobile"
%{_datadir}/elementary/themes/tizen-HD-dark.edj
%{_datadir}/elementary/themes/tizen-HD-light.edj
%{_datadir}/elementary/themes/tizen-hd.edj

%files -n efl-theme-tizen-devel
%defattr(-,root,root,-)
/opt/var/efl-theme-tizen-edc/*
%endif
