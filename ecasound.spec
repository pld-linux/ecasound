Summary:	Software package for multitrack audio processing
Summary(pl):	Oprogramowanie do wielo¶cie¿kowego przetwarzania d¼wiêku
Name:		ecasound
Version:	1.8.0d14
Release:	3
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://ecasound.seul.org/download/%{name}-%{version}.tar.gz
Patch0:		ecasound-ncurses.patch.bz2
Patch1:		ecasound-kvutils.patch.bz2
BuildRequires:	qt-devel >= 2.0
BuildRequires:	audiofile-devel >= 0.1.7
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	lame
Requires:	mpg123
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ecasound is a software package designed for multitrack audio
processing. It can be used for simple tasks like audio playback,
recording and format conversions, as well as for multitrack effect
processing, mixing, recording and signal recycling. Ecasound supports
a wide range of audio inputs, outputs and effect algorithms. Several
open-source audio packages, like for instance ALSA, OSS, mpg123, lame,
libaudiofile and MikMod, are directly supported. One of the advantages
of ecasound's chain-based design is that effects can easily be
combined both in series and in parallel. Oscillators and MIDI-CCs can
be used for controlling effect parameters. Included user-interfaces
are ecasound - a versatile console mode interface, qtecasound - a
Qt-based X-interface and various command-line utils suitable for batch
processing.

%description -l pl
Ecasound jest programem do wielo¶cie¿kowej edycji d¼wiêku, który mo¿e
byæ u¿ywany tak do prostych zadañ typu odtwarzanie i nagrywanie muzyki
czy te¿ konwersji pomiêdzy formatami plików muzycznych jak i do
wielo¶cie¿kowego nak³adania efektów, miksowania (przenikania, wyciszania),
nagrywania i odzyskiwania (w domy¶le odszumiania lub wyrzucania
zniekszta³ceñ) sygna³u.

Ecasound wspiera szerok± gamê ¼róde³ i wyj¶æ d¼wiêku oraz algorytmów
do jego przetwarzania. Ecasound wspiera wiele wolnych (open source)
projektów, takich jak ALSA, OSS, mpg123, lame, libaudiofile czy te¿
MikMod. Jedn± z zalet programu ecasound jest mo¿liwo¶æ ³añcuchowego
(szeregowego) lub równoleg³ego ³±czenia efektów, które mog± byæ
kontrolowane poprzez oscylatory lub MIDI-CC. Pakiet ten zawiera
tekstowy interfejs u¿ytkownika oraz kilka innych narzêdzi nadaj±cych
siê do przetwarzania wsadowego. Dostêpny jest tak¿e graficzny
interfejs u¿ytkownika - qtecasound.

%package -n libecasound
Summary:	Ecasound libraries
Summary(pl):	Biblioteki programu ecasound
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description -n libecasound
Ecasound libraries.

%description -l pl -n libecasound
Biblioteki programu ecasound.

%package -n libecasound-devel
Summary:	Ecasound headers
Summary(pl):	Pliki nag³ówkowe bibliotek programu ecasound
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	libecasound = %{version}

%description -n libecasound-devel
Ecasound headers.

%description -l pl -n libecasound-devel
Pliki nag³ówkowe bibliotek programu ecasound.

%package -n libecasound-static
Summary:	Ecasound static libraries
Summary(pl):	Biblioteki statyczne programu ecasound
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	libecasound-devel = %{version}

%description -n libecasound-static
Ecasound static libraries.

%description -l pl -n libecasound-static
Biblioteki statyczne programu ecasound.

%package -n qtecasound
Summary:	Ecasound QT frontend
Summary(pl):	Interfejs graficzny dla programu ecasound
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk

%description -n qtecasound
This is qtecasound, Qt-based X-interface for ecasound. It is usable
but isn't yet as powerful as the console mode version. This program
features:
- control panel (start, stop, rewind, forward, ...)
- session setup (load, save and view chainsetups)
- chainsetup view (add, remove, attach and view inputs, outputs and
  chains; enable/disable chains)
- waveform view (supports caching)
- chain view (chain and effect status)

%description -l pl -n qtecasound
N/A.

%package -n libqtecasound
Summary:	Ecasound QT frontend library
Summary(pl):	Biblioteki interfejsu graficznego programu ecasound
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description -n libqtecasound
Ecasound QT frontend library.

%description -l pl -n libqtecasound
Biblioteki interfejsu graficznego programu ecasound.

%package -n libqtecasound-devel
Summary:	Ecasound QT frontend library headers
Summary(pl):	Pliki nag³ówkowe bibliotek interfejsu graficznego programu ecasound
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	libqtecasound = %{version}

%description -n libqtecasound-devel
Ecasound QT frontend library headers.

%description -l pl -n libqtecasound-devel
Pliki nag³ówkowe bibliotek interfejsu graficznego programu ecasound.

%package -n libqtecasound-static
Summary:	Ecasound QT frontend static library
Summary(pl):	Biblioteki stayczne interfejsu graficznego programu ecasound
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	libqtecasound-devel = %{version}

%description -n libqtecasound-static
Ecasound QT frontend static library.

%description -l pl -n libqtecasound-static
Biblioteki stayczne interfejsu graficznego programu ecasound.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
automake
autoconf
LDFLAGS="-s"
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti"
export LDFLAGS CXXFLAGS
%configure \
	--with-qt-includes=%{_prefix}/X11R6/include \
	--with-qt-libraries=%{_prefix}/X11R6/lib \
	--enable-sys-readline
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -n libecasound -p /sbin/ldconfig
%postun -n libecasound -p /sbin/ldconfig

%post   -n libqtecasound -p /sbin/ldconfig
%postun -n libqtecasound -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecafixdc
%attr(755,root,root) %{_bindir}/ecanormalize
%attr(755,root,root) %{_bindir}/ecaplay
%attr(755,root,root) %{_bindir}/ecasound
%{_mandir}/man1/eca*
%{_mandir}/man5/eca*

%files -n libecasound
%defattr(644,root,root,755)
%dir %{_datadir}/ecasound
%{_datadir}/ecasound/*
%attr(755,root,root) %{_libdir}/libkvutils*.so.*.*
%attr(755,root,root) %{_libdir}/libecasound*.so.*.*

%files -n libecasound-devel
%defattr(644,root,root,755)
%{_includedir}/ecasound/[^qe]*
%{_includedir}/kvutils/*
%attr(755,root,root) %{_libdir}/libkvutils.so
%attr(755,root,root) %{_libdir}/libkvutils.la
%attr(755,root,root) %{_libdir}/libecasound*.so
%attr(755,root,root) %{_libdir}/libecasound*.la

%files -n libecasound-static
%defattr(644,root,root,755)
%{_libdir}/libkvutils.a
%{_libdir}/libecasound*.a

%files -n qtecasound
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtecasound
%{_mandir}/man1/qt*

%files -n libqtecasound
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqtecasound*.so.*.*

%files -n libqtecasound-devel
%defattr(644,root,root,755)
%{_includedir}/ecasound/qe*
%attr(755,root,root) %{_libdir}/libqtecasound*.so
%attr(755,root,root) %{_libdir}/libqtecasound*.la

%files -n libqtecasound-static
%defattr(644,root,root,755)
%{_libdir}/libqtecasound*.a
