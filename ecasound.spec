%include	/usr/lib/rpm/macros.python
Summary:	Software package for multitrack audio processing
Summary(pl):	Oprogramowanie do wielo∂cieøkowego przetwarzania dºwiÍku
Name:		ecasound
Version:	2.1.0
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(es):	Aplicaciones/Sonido
Group(pl):	Aplikacje/DºwiÍk
Group(pt_BR):	AplicaÁıes/Som
Source0:	http://ecasound.seul.org/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fix.patch
Patch1:		%{name}-ac_fix.patch
Patch2:		%{name}-readline.patch
Patch3:		%{name}-am15.patch
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
Ecasound jest programem do wielo∂cieøkowej edycji dºwiÍku, ktÛry moøe
byÊ uøywany tak do prostych zadaÒ typu odtwarzanie i nagrywanie muzyki
czy teø konwersji pomiÍdzy formatami plikÛw muzycznych jak i do
wielo∂cieøkowego nak≥adania efektÛw, miksowania (przenikania,
wyciszania), nagrywania i odzyskiwania (w domy∂le odszumiania lub
wyrzucania zniekszta≥ceÒ) sygna≥u.

Ecasound wspiera szerok± gamÍ ºrÛde≥ i wyj∂Ê dºwiÍku oraz algorytmÛw
do jego przetwarzania. Ecasound wspiera wiele wolnych (open source)
projektÛw, takich jak ALSA, OSS, mpg123, lame, libaudiofile czy teø
MikMod. Jedn± z zalet programu ecasound jest moøliwo∂Ê ≥aÒcuchowego
(szeregowego) lub rÛwnoleg≥ego ≥±czenia efektÛw, ktÛre mog± byÊ
kontrolowane poprzez oscylatory lub MIDI-CC. Pakiet ten zawiera
tekstowy interfejs uøytkownika oraz kilka innych narzÍdzi nadaj±cych
siÍ do przetwarzania wsadowego. DostÍpny jest takøe graficzny
interfejs uøytkownika - qtecasound.

%package -n libecasound
Summary:	Ecasound libraries
Summary(pl):	Biblioteki programu ecasound
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…

%description -n libecasound
Ecasound libraries.

%description -l pl -n libecasound
Biblioteki programu ecasound.

%package -n libecasound-devel
Summary:	Ecasound headers
Summary(pl):	Pliki nag≥Ûwkowe bibliotek programu ecasound
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	libecasound = %{version}

%description -n libecasound-devel
Ecasound headers.

%description -l pl -n libecasound-devel
Pliki nag≥Ûwkowe bibliotek programu ecasound.

%package -n libecasound-static
Summary:	Ecasound static libraries
Summary(pl):	Biblioteki statyczne programu ecasound
Group:		Development/Libraries
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	libecasound-devel = %{version}

%description -n libecasound-static
Ecasound static libraries.

%description -l pl -n libecasound-static
Biblioteki statyczne programu ecasound.

%package plugins
Summary:	Ecasound plugins (ALSA, Audio File Library, aRts)
Summary(pl):	Wtyczki dla programu ecasound (ALSA, Audio File Library, aRts)
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(es):	Aplicaciones/Sonido
Group(pl):	Aplikacje/DºwiÍk
Group(pt_BR):	AplicaÁıes/Som
Requires:	ecasound = %{version}

%description plugins
This package contains ecasound plugins, which give support for ALSA,
Audio File Library and aRts.

%description -l pl plugins
Pakiet ten zawiera wtyczki dla programu ecasound, ktÛre umoøliwiaj±
wspÛ≥pracÍ z bibliotekami takich projektÛw jak ALSA, Audio File
Library oraz aRts.

%package -n python-%{name}
Summary:	Python module for Ecasound
Summary(pl):	Modu≥ jÍzyka Python dla biblioteki programu ecasound
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(es):	Desarrollo/Lenguages/Python
Group(fr):	Development/Langues/Python
Group(pl):	Programowanie/JÍzyki/Python
%requires_eq	python

%description -n python-%{name}
Python module for Ecasound library.

%description -l pl -n python-%{name}
Modu≥ jÍzyka Python dla biblioteki programu ecasound.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm missing
%ifarch sparc sparc64
libtoolize --copy --force
%endif
aclocal
autoconf
automake -a -c
CXXFLAGS="%{rpmcflags} -D_REENTRANT %{!?debug:-DNDEBUG}"
%configure \
	--enable-sys-readline \
	--with-python-includes=%{py_incdir} \
	--with-python-modules=%{py_libdir} \
	%{?_without_alsa:--disable-alsa}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{py_sitedir}

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
%{py_dyndir}/*.a

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
