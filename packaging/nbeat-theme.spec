Name:       nbeat-theme
Summary:    Beat theme files
Version:    0.1.1
Release:    1
Group:      themes
License:    Proprietary
Source0:    %{name}-%{version}.tar.gz
BuildRequires: edje, edje-bin, embryo, embryo-bin

%description
Beat theme for EFL

%package -n nbeat-black-theme
Summary: Beat Black theme files for EFL
Group: themes

%description -n nbeat-black-theme
Beat black theme for EFL

%package -n nbeat-hd-theme
Summary: Beat HD theme files for EFL
Group: themes

%description -n nbeat-hd-theme
Beat HD theme for EFL

%package -n nbeat-black-hd-theme
Summary: Beat Black HD theme files for EFL
Group: themes

%description -n nbeat-black-hd-theme
Beat black HD theme for EFL

%prep
%setup -q 

%build
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/nbeat.edj

%files -n nbeat-black-theme
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/nbeat-black.edj

%files -n nbeat-hd-theme
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/nbeat-hd.edj

%files -n nbeat-black-hd-theme
%defattr(-,root,root,-)
%{_datadir}/elementary/themes/nbeat-black-hd.edj
