# https://github.com/cznic/lex
%global goipath github.com/cznic/lex
%global commit  68050f59b71a42ca5b94e7b832e5bc2cdb48af66

%gometa

Name:           golang-github-cznic-lex
Version:        0
Release:        0.8%{?dist}
Summary:        Support for (f)lex-like tool on .l source files
License:        BSD

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(github.com/cznic/fileutil)
BuildRequires:  golang(github.com/cznic/lexer)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTORS AUTHORS README


%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20170112git68050f5
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.7.20170112git68050f5
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.6.20170112git68050f5
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20170112.git68050f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20170112.git68050f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170112.git68050f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170112.git68050f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.20170112.git68050f5
- First package for Fedora

