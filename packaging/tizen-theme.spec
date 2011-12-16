Name:       tizen-theme
Summary:    Tizen theme files
Version:    0.1.1
Release:    1
Group:      themes
License:    Proprietary
Source0:    %{name}-%{version}.tar.gz
BuildRequires: edje, edje-bin, embryo, embryo-bin

%description
Tizen theme for EFL

%package -n efl-theme-tizen-black
Summary: Tizen Black theme files for EFL
Group: themes

%description -n efl-theme-tizen-black
Tizen black theme for EFL

%package -n efl-theme-tizen-hd
Summary: Tizen HD theme files for EFL
Group: themes

%description -n efl-theme-tizen-hd
Tizen HD theme for EFL

%package -n efl-theme-tizen-black-hd
Summary: Tizen Black HD theme files for EFL
Group: themes

%description -n efl-theme-tizen-black-hd
Tizen black HD theme for EFL

%prep
%setup -q 

%build
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/tizen.edj

%files -n efl-theme-tizen-black
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/tizen-black.edj

%files -n efl-theme-tizen-hd
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/tizen-hd.edj

%files -n efl-theme-tizen-black-hd
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/tizen-black-hd.edj
