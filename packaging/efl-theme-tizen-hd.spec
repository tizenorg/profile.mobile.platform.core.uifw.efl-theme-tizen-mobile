Name:          efl-theme-tizen-hd
Summary:       Tizen theme files
Version:       1.0.315
Release:       1
Group:         TO_BE/FILLED_IN
License:       TO_BE/FILLED_IN
Source0:       %{name}-%{version}.tar.gz
BuildRequires: perl, edje, edje-bin, embryo, embryo-bin
%define _unpackaged_files_terminate_build 0

%description
Tizen HD theme for EFL

%prep
%setup -q 


%build
%if 0%{?sec_product_feature_profile_lite}
	export TARGET=2.2
%else
	export TARGET=2.2
%endif

export CFLAGS+=" --fPIC"
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed -Wl,--rpath=/usr/lib"
make %{?jobs:-j%jobs}


%install
%if 0%{?sec_product_feature_profile_lite}
	export TARGET=2.2
%else
	export TARGET=2.2
%endif

rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/usr/share/license/%{name}

%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/*.edj
%manifest %{name}.manifest
/usr/share/license/%{name}
