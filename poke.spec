Summary:	An interactive, extensible editor for binary data
Name:		poke
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/Editors
Source0:	https://ftp.gnu.org/gnu/poke/%{name}-%{version}.tar.gz
# Source0-md5:	a7423661eed9705e7d2b9adc7f977139
URL:		http://www.jemarch.net/poke
BuildRequires:	gawk
BuildRequires:	gc-devel
BuildRequires:	json-c-devel
BuildRequires:	libnbd-devel
BuildRequires:	libtextstyle-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU poke is an interactive, extensible editor for binary data. Not
limited to editing basic entities such as bits and bytes, it provides
a full-fledged procedural, interactive programming language designed
to describe data structures and to operate on them.

%package libs
Summary:	%{name} library
Summary(pl.UTF-8):	Biblioteka %{name}
Group:		Libraries
Conflicts:	%{name} < 1:2.16-2

%description libs
%{name} library.

%description libs -l pl.UTF-8
Biblioteka %{name}.

%package devel
Summary:	Header files and development documentation for %{name}
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do %{name}
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files and development documentation for %{name}.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka libcap.

%package gui
Summary:	GUI for poke
Requires:	%{name} = %{version}-%{release}

%description gui
Tk GUI for poke.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %ghost %{_libdir}/libpoke.so.0
%attr(755,root,root) %{_libdir}/libpoke.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libpoke.h
%attr(755,root,root) %{_libdir}/libpoke.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libpoke.a
