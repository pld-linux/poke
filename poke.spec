Summary:	An interactive, extensible editor for binary data
Summary(pl.UTF-8):	Interaktywny, rozszerzalny edytor do danych binarnych
Name:		poke
Version:	1.0
Release:	1
License:	GPL v3+
Group:		Applications/Editors
Source0:	https://ftp.gnu.org/gnu/poke/%{name}-%{version}.tar.gz
# Source0-md5:	a7423661eed9705e7d2b9adc7f977139
Patch0:		%{name}-info.patch
URL:		http://www.jemarch.net/poke
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
BuildRequires:	tcl-devel
BuildRequires:	texinfo
BuildRequires:	tk-devel
Requires:	libtextstyle >= 0.20.5
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

%package gui
Summary:	GUI for poke
Summary(pl.UTF-8):	Graficzny interfejs użytkownika do poke
Group:		X11/Applications/Editors
Requires:	%{name} = %{version}-%{release}

%description gui
Tk GUI for poke.

%description gui -l pl.UTF-8
Oparty na Tk graficzny interfejs użytkownika do poke.

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

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpoke.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun -p      /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/pk-elfextractor
%attr(755,root,root) %{_bindir}/poke
%{_datadir}/poke
%{_mandir}/man1/poke.1*
%{_infodir}/poke.info*

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/poke-gui

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoke.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpoke.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpoke.so
%{_includedir}/libpoke.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpoke.a
