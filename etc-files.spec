Name:         etc-files
Version:      1.0
Release:      1
Summary:      Package to count /etc/ files
License:      GPL-3.0+
BuildArch:    noarch
Requires:     findutils coreutils bash
Source0:      etc-files-1.0.tar.gz


%description
Script file that will automatically count all the files in the /etc/ directory

%clean
%{__rm} -rf %{buildroot}

%prep
%setup -q

%build

%install
install -D -m 0755 script.sh %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}


%changelog
* Wed Oct 22 2025 Andrii Riabets <andriyriabets@gmail.com> 1.0-1
- Initial package release 