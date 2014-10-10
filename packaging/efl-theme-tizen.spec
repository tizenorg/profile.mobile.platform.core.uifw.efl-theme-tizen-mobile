Name:          efl-theme-tizen
Summary:       Tizen theme files
Version:       1.1.66
Release:       1
Group:         TO_BE/FILLED_IN
License:       TO_BE/FILLED_IN
Source0:       %{name}-%{version}.tar.gz
BuildRequires: sec-product-features
BuildRequires: edje-bin
%define _unpackaged_files_terminate_build 0

%description
Tizen heme for EFL

%prep
%setup -q

%build
export CFLAGS+=" --fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=/usr/lib"

%if 0%{?sec_product_feature_uifw_efl_b3_theme}
    export TARGET=2.3-wearable
%else
    export TARGET=2.3-mobile
    export SIZE=WVGA
%endif

make

%install

%if 0%{?sec_product_feature_uifw_efl_b3_theme}
    export TARGET=2.3-wearable
%else
    export TARGET=2.3-mobile
    export SIZE=WVGA
%endif

make install prefix=%{_prefix} DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{_datadir}/license/%{name}

%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/*.edj
%{_datadir}/license/%{name}
%manifest %{name}.manifest
