#
# Conditional build:
%{?_without_alsa:%global _without_jack 1}
%bcond_without	alsa		# without ALSA support (implies without JACK)
%bcond_without	jack		# without JACK support
%bcond_with	arts		# with aRts support
#
%include	/usr/lib/rpm/macros.python
Summary:	Software package for multitrack audio processing
Summary(pl):	Oprogramowanie do wielo¶cie¿kowego przetwarzania d¼wiêku
Name:		ecasound
Version:	2.3.0
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://ecasound.seul.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	fb440a68466c8bd6f7bc8a14adf46ef7
Patch0:		%{name}-link.patch
%ifnarch sparc sparc64
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%endif
%{?with_arts:BuildRequires:	arts-devel}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
BuildRequires:	ladspa-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules >= 2.2
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-pythonprov
Obsoletes:	libecasound
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

%package devel
Summary:	Header files for ecasound libraries
Summary(pl):	Pliki nag³ówkowe bibliotek ecasound
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libsamplerate-devel
Requires:	libstdc++-devel
Obsoletes:	libecasound-devel

%description devel
Header files for ecasound libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek ecasound.

%package static
Summary:	Static ecasound libraries
Summary(pl):	Statyczne biblioteki ecasound
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	libecasound-static

%description static
Static ecasound libraries.

%description static -l pl
Statyczne biblioteki ecasound.

%package -n python-%{name}
Summary:	Python module for Ecasound
Summary(pl):	Modu³ jêzyka Python dla programu ecasound
Group:		Libraries/Python
%pyrequires_eq	python-modules

%description -n python-%{name}
Python module for Ecasound.

%description -n python-%{name} -l pl
Modu³ jêzyka Python dla programu ecasound.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -D_REENTRANT %{!?debug:-DNDEBUG} -I/usr/include/ncurses"
# disable audiofile - ecasound has native support for wav and raw formats
# disable oss       - ecasound works nicely with alsa oss emulation;
#                     in case of alsa building conditional, the oss should
#                     be enabled
# disable arts      - 'not really useful' as said by ecasound author
%configure \
	%{!?with_alsa:--disable-alsa} \
	%{!?with_arts:--disable-arts} \
	--disable-audiofile \
	%{!?with_jack:--disable-jack} \
	%{?with_alsa:--disable-oss} \
	--enable-samplerate \
	--enable-sys-readline \
	--enable-pyecasound \
	--with-largefile \
	--with-python-includes=%{py_incdir} \
	--with-python-modules=%{py_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir}

install pyecasound/*.py $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc BUGS NEWS README TODO
%attr(755,root,root) %{_bindir}/eca*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/ecasound
%{_mandir}/man1/eca*
%{_mandir}/man5/eca*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/kvutils
%{_includedir}/libecasound
%{_includedir}/libecasoundc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
