Name:          efl-theme-tizen
Summary:       Tizen theme files
Version:       1.1.0
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
    %if 0%{?sec_product_feature_profile_lite}
        export TARGET="2.2 2.3-mobile"
    %else
        export TARGET=2.2
    %endif
%endif

make

%install

%if 0%{?sec_product_feature_uifw_efl_b3_theme}
    export TARGET=2.3-wearable
%else
    %if 0%{?sec_product_feature_profile_lite}
        export TARGET="2.2 2.3-mobile"
    %else
        export TARGET=2.2
    %endif
%endif

make install prefix=%{_prefix} DESTDIR=%{buildroot}

# install redwood theme as fallback for lite temporarily
%if 0%{?sec_product_feature_profile_lite}
    mv %{buildroot}/%{_datadir}/elementary/themes/tizen-2.2-HD.edj %{buildroot}/%{_datadir}/elementary/themes/default.edj
%endif

mkdir -p %{buildroot}%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{_datadir}/license/%{name}

%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/*.edj
%{_datadir}/license/%{name}
%manifest %{name}.manifest


############# Temporary ###################
# Remove below after redwood is completed
#%if ! 0%{?sec_product_feature_profile_lite}
#%if ! 0%{?sec_product_feature_uifw_efl_b3_theme}
%package hd
Summary:       Tizen HD theme files
Group:         TO_BE/FILLED_IN
BuildRequires: sec-product-features
BuildRequires: edje-bin, embryo-bin

%description hd
Temporary package only for backward compatibility of redwood

%files hd
%defattr(-,root,root,-)
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/*.edj
%{_datadir}/license/%{name}
%manifest %{name}.manifest
#%endif
#%endif
#############################################3
