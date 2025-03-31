Summary:	An interactive, extensible editor for binary data
Summary(pl.UTF-8):	Interaktywny, rozszerzalny edytor do danych binarnych
Name:		poke
Version:	4.3
Release:	1
License:	GPL v3+
Group:		Applications/Editors
Source0:	https://ftp.gnu.org/gnu/poke/%{name}-%{version}.tar.gz
# Source0-md5:	95a2598593a2f4e11513cde814b6a024
Patch0:		%{name}-info.patch
URL:		http://www.jemarch.net/poke
BuildRequires:	automake
BuildRequires:	bison >= 3.6
BuildRequires:	flex
BuildRequires:	gawk
BuildRequires:	gc-devel
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	help2man
BuildRequires:	json-c-devel >= 0.11
BuildRequires:	libnbd-devel
BuildRequires:	libtextstyle-devel >= 0.20.5
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	texinfo
Requires:	libtextstyle >= 0.20.5
Obsoletes:	poke-gui < 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU poke is an interactive, extensible editor for binary data. Not
limited to editing basic entities such as bits and bytes, it provides
a full-fledged procedural, interactive programming language designed
to describe data structures and to operate on them.

%description -l pl.UTF-8
GNU poke to interaktywny, rozszerzalny edytor do danych binarnych. Nie
jest ograniczony do edycji podstawowych jednostek, takich jak bity czy
bajty - udostępnia dojrzały proceduralny, interaktywny język
programowania zaprojektowany do opisu struktur danych i operowania na
nich.

%package libs
Summary:	poke shared library
Summary(pl.UTF-8):	Biblioteka współdzielona poke
Group:		Libraries

%description libs
poke shared library.

%description libs -l pl.UTF-8
Biblioteka współdzielona poke.

%package devel
Summary:	Header file for libpoke library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki libpoke
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header file for libpoke library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki libpoke.

%package static
Summary:	Static libpoke library
Summary(pl.UTF-8):	Statyczna biblioteka libpoke
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpoke library.

%description static -l pl.UTF-8
Statyczna biblioteka libpoke.

%package -n emacs-poke-mode
Summary:	Poke mode for Emacs
Summary(pl.UTF-8):	Tryb poke dla Emacsa
Group:		Applications/Editors
Requires:	%{name} = %{version}-%{release}
Requires:	emacs

%description -n emacs-poke-mode
Poke mode for Emacs.

%description -n emacs-poke-mode -l pl.UTF-8
Tryb poke dla Emacsa.

%prep
%setup -q
%patch -P0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpoke.la

# already in vim-rt
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/vim

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/pk-bin2poke
%attr(755,root,root) %{_bindir}/pk-jojopatch
%attr(755,root,root) %{_bindir}/pk-strings
%attr(755,root,root) %{_bindir}/poke
%attr(755,root,root) %{_bindir}/poked
%attr(755,root,root) %{_bindir}/pokefmt
%{_datadir}/poke
%{_mandir}/man1/poke.1*
%{_mandir}/man1/poked.1*
%{_mandir}/man1/pokefmt.1*
%{_infodir}/poke.info*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoke.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpoke.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoke.so
%{_includedir}/libpoke.h
%{_pkgconfigdir}/poke.pc
%{_aclocaldir}/poke.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libpoke.a

%files -n emacs-poke-mode
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/poke-map-mode.el
%{_datadir}/emacs/site-lisp/poke-ras-mode.el
