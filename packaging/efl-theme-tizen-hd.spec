Name:          efl-theme-tizen-hd
Summary:       Tizen theme files
Version:       1.0.34
Release:       1
Group:         TO_BE/FILLED_IN
License:       TO_BE/FILLED_IN
Source0:       %{name}-%{version}.tar.gz
BuildRequires: edje, edje-bin, embryo, embryo-bin


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


%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/tizen-hd.edj


%files -n efl-theme-tizen-devel
%defattr(-,root,root,-)
/opt/var/efl-theme-tizen-edc/*
