
#
# todo:
# - jackit.sf.net
#

#
# Conditional build:
# _without_alsa	- without ALSA support
#

%include	/usr/lib/rpm/macros.python

Summary:	Software package for multitrack audio processing
Summary(pl):	Oprogramowanie do wielo¶cie¿kowego przetwarzania d¼wiêku
Name:		ecasound
Version:	2.2.0
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://ecasound.seul.org/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-link.patch
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules >= 2.2
BuildRequires:	readline-devel >= 4.2
BuildRequires:	rpm-pythonprov
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
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -D_REENTRANT %{!?debug:-DNDEBUG} -I/usr/include/ncurses"
# disable audiofile - ecasound has native support for wav and raw formats
# disable oss       - ecasound works nicely with alsa oss emulation;
#                     in case of alsa building conditional, the oss should
#                     be enabled
# disable arts      - 'not really useful' as said by ecasound author
%configure \
	--enable-sys-readline \
	--with-python-includes=%{py_incdir} \
	--with-python-modules=%{py_libdir} \
	--disable-audiofile \
	--disable-arts \
	%{?_without_alsa:--disable-alsa} \
	%{!?_without_alsa:--disable-oss}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

%{__make} DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install

install pyecasound/*.py $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS NEWS README TODO
%attr(755,root,root) %{_bindir}/eca*
%{_datadir}/ecasound

%{_mandir}/man1/eca*
%{_mandir}/man5/eca*

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
