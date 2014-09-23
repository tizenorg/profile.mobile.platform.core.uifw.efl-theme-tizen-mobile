Name:          efl-theme-tizen
Summary:       Tizen theme files
Version:       1.1.54
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
        %if "%{?sec_product_feature_display_resolution}" == "480x800"
            export SIZE=WVGA
        %else
        #This feature is for supporting Tizen SDK
            %if "%{?sec_product_feature_display_resolution}" == "HD"
                export SIZE=HD
            %else
                %if "%{?sec_product_feature_display_resolution}" == "FHD"
                   export SIZE=FHD
                %else
                   export SIZE=HVGA
                %endif
            %endif
        %endif
        export TARGET=2.3-mobile
    %else
        export TARGET=2.3-mobile
        export SIZE=HD
    %endif
%endif

make

%install

%if 0%{?sec_product_feature_uifw_efl_b3_theme}
    export TARGET=2.3-wearable
%else
    %if 0%{?sec_product_feature_profile_lite}
        %if "%{?sec_product_feature_display_resolution}" == "480x800"
            export SIZE=WVGA
        %else
        #This feature is for supporting Tizen SDK
            %if "%{?sec_product_feature_display_resolution}" == "HD"
                export SIZE=HD
            %else
                %if "%{?sec_product_feature_display_resolution}" == "FHD"
                   export SIZE=FHD
                %else
                   export SIZE=HVGA
                %endif
            %endif
        %endif
        export TARGET=2.3-mobile
    %else
        export TARGET=2.3-mobile
        export SIZE=HD
    %endif
%endif

make install prefix=%{_prefix} DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/license
cp %{_builddir}/%{buildsubdir}/COPYING %{buildroot}/%{_datadir}/license/%{name}

%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/*.edj
%{_datadir}/license/%{name}
%manifest %{name}.manifest
