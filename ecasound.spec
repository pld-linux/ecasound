%include	/usr/lib/rpm/macros.python
Summary:	Software package for multitrack audio processing
Summary(pl):	Oprogramowanie do wielo¶cie¿kowego przetwarzania d¼wiêku
Name:		ecasound
Version:	2.1.0
Release:	4
License:	GPL
Group:		Applications/Sound
Source0:	http://ecasound.seul.org/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fix.patch
Patch1:		%{name}-ac_fix.patch
Patch2:		%{name}-readline.patch
Patch3:		%{name}-am15.patch
Patch4:		%{name}-comment.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	audiofile-devel >= 0.2.0
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-pythonprov
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules >= 2.2
Requires:	lame
Requires:	mpg123
Requires:	libecasound = %{version}
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
wielo¶cie¿kowego nak³adania efektów, miksowania (przenikania,
wyciszania), nagrywania i odzyskiwania (w domy¶le odszumiania lub
wyrzucania zniekszta³ceñ) sygna³u.

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
Group:		Libraries

%description -n libecasound
Ecasound libraries.

%description -n libecasound -l pl
Biblioteki programu ecasound.

%package -n libecasound-devel
Summary:	Ecasound headers
Summary(pl):	Pliki nag³ówkowe bibliotek programu ecasound
Group:		Development/Libraries
Requires:	libecasound = %{version}

%description -n libecasound-devel
Ecasound headers.

%description -n libecasound-devel -l pl
Pliki nag³ówkowe bibliotek programu ecasound.

%package -n libecasound-static
Summary:	Ecasound static libraries
Summary(pl):	Biblioteki statyczne programu ecasound
Group:		Development/Libraries
Requires:	libecasound-devel = %{version}

%description -n libecasound-static
Ecasound static libraries.

%description -n libecasound-static -l pl
Biblioteki statyczne programu ecasound.

%package plugins
Summary:	Ecasound plugins (ALSA, Audio File Library, aRts)
Summary(pl):	Wtyczki dla programu ecasound (ALSA, Audio File Library, aRts)
Group:		Applications/Sound
Requires:	ecasound = %{version}

%description plugins
This package contains ecasound plugins, which give support for ALSA,
Audio File Library and aRts.

%description plugins -l pl
Pakiet ten zawiera wtyczki dla programu ecasound, które umo¿liwiaj±
wspó³pracê z bibliotekami takich projektów jak ALSA, Audio File
Library oraz aRts.

%package -n python-%{name}
Summary:	Python module for Ecasound
Summary(pl):	Modu³ jêzyka Python dla biblioteki programu ecasound
Group:		Libraries/Python
%pyrequires_eq	python

%description -n python-%{name}
Python module for Ecasound library.

%description -n python-%{name} -l pl
Modu³ jêzyka Python dla biblioteki programu ecasound.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
%ifarch sparc sparc64
%{__libtoolize}
%endif
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -D_REENTRANT %{!?debug:-DNDEBUG}"
%configure \
	--enable-sys-readline \
	--with-python-includes=%{py_incdir} \
	--with-python-modules=%{py_libdir} \
	%{?_without_alsa:--disable-alsa}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

%{__make} DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install

install pyecasound/*.py $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%post   -n libecasound -p /sbin/ldconfig
%postun -n libecasound -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecaconvert
%attr(755,root,root) %{_bindir}/ecafixdc
%attr(755,root,root) %{_bindir}/ecanormalize
%attr(755,root,root) %{_bindir}/ecaplay
%attr(755,root,root) %{_bindir}/ecasignalview
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
%attr(755,root,root) %{_bindir}/ecasound-config
%attr(755,root,root) %{_bindir}/ecasoundc-config
%{_includedir}/ecasound
%{_includedir}/kvutils
%attr(755,root,root) %{_libdir}/libkvutils.so
%attr(755,root,root) %{_libdir}/libkvutils.la
%attr(755,root,root) %{_libdir}/libecasound*.so
%attr(755,root,root) %{_libdir}/libecasound*.la

%files -n libecasound-static
%defattr(644,root,root,755)
%{_libdir}/libkvutils.a
%{_libdir}/libecasound.a
%{py_sitedir}/*.a

%files plugins
%defattr(644,root,root,755)
%dir %{_libdir}/ecasound-plugins
%attr(755,root,root) %{_libdir}/ecasound-plugins/lib*.so*
%{_libdir}/ecasound-plugins/lib*.la
%{_libdir}/ecasound-plugins/lib*.a

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
