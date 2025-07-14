#
# Conditional build:
%bcond_without	alsa		# without ALSA support (implies without JACK)
%bcond_without	jack		# without JACK support
%bcond_without	ruby		# without ruby support
%bcond_with	arts		# with aRts support
#
Summary:	Software package for multitrack audio processing
Summary(pl.UTF-8):	Oprogramowanie do wielościeżkowego przetwarzania dźwięku
Name:		ecasound
Version:	2.9.1
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://ecasound.seul.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	13c7be1e4eddc0bbf3792dc17777e465
Patch0:		%{name}-link.patch
Patch1:		%{name}-acam.patch
Patch2:		%{name}-ruby.patch
URL:		http://www.eca.cx/ecasound/
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
%{?with_arts:BuildRequires:	arts-devel}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6.1
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
BuildRequires:	ladspa-devel
BuildRequires:	liblo-devel
BuildRequires:	liboil-devel >= 0.3
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel >= 1.0.12
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	lilv-devel >= 0.5.0
BuildRequires:	lv2core-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-modules >= 2.2
BuildRequires:	readline-devel >= 5.0
BuildRequires:	rpm-pythonprov
%if %{with ruby}
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%endif
Requires:	libsndfile >= 1.0.12
Requires:	lilv >= 0.5.0
Obsoletes:	libecasound
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ecasound is a software package designed for multitrack audio
processing. It can be used for simple tasks like audio playback,
recording and format conversions, as well as for multitrack effect
processing, mixing, recording and signal recycling. Ecasound supports
a wide range of audio inputs, outputs and effect algorithms. Several
open-source audio packages, like for instance ALSA, OSS, mpg123, lame
and MikMod, are directly supported. One of the advantages of
ecasound's chain-based design is that effects can easily be combined
both in series and in parallel. Oscillators and MIDI-CCs can be used
for controlling effect parameters. Included user-interfaces are
ecasound - a versatile console mode interface, ecawave - a Qt-based
X-interface and various command-line utils suitable for batch
processing.

%description -l pl.UTF-8
Ecasound jest programem do wielościeżkowej edycji dźwięku, który może
być używany tak do prostych zadań typu odtwarzanie i nagrywanie muzyki
czy też konwersji pomiędzy formatami plików muzycznych jak i do
wielościeżkowego nakładania efektów, miksowania (przenikania,
wyciszania), nagrywania i odzyskiwania (w domyśle odszumiania lub
wyrzucania zniekształceń) sygnału.

Ecasound wspiera szeroką gamę źródeł i wyjść dźwięku oraz algorytmów
do jego przetwarzania. Ecasound wspiera wiele wolnych (open source)
projektów, takich jak ALSA, OSS, mpg123, lame czy też MikMod. Jedną z
zalet programu ecasound jest możliwość łańcuchowego (szeregowego) lub
równoległego łączenia efektów, które mogą być kontrolowane poprzez
oscylatory lub MIDI-CC. Pakiet ten zawiera tekstowy interfejs
użytkownika oraz kilka innych narzędzi nadających się do przetwarzania
wsadowego. Dostępny jest także graficzny, oparty na Qt interfejs
użytkownika - ecawave.

%package devel
Summary:	Header files for ecasound libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek ecasound
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_alsa:Requires:	alsa-lib-devel}
%{?with_arts:Requires:	arts-devel}
%{?with_jack:Requires:	jack-audio-connection-kit-devel}
Requires:	liblo-devel
Requires:	liboil-devel >= 0.3
Requires:	libsamplerate-devel
Requires:	libsndfile-devel
Requires:	libstdc++-devel
Requires:	lilv-devel >= 0.5.0
Obsoletes:	libecasound-devel

%description devel
Header files for ecasound libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek ecasound.

%package static
Summary:	Static ecasound libraries
Summary(pl.UTF-8):	Statyczne biblioteki ecasound
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libecasound-static

%description static
Static ecasound libraries.

%description static -l pl.UTF-8
Statyczne biblioteki ecasound.

%package -n python-%{name}
Summary:	Python module for Ecasound
Summary(pl.UTF-8):	Moduł języka Python dla programu ecasound
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-modules

%description -n python-%{name}
Python module for Ecasound.

%description -n python-%{name} -l pl.UTF-8
Moduł języka Python dla programu ecasound.

%package -n ruby-%{name}
Summary:	Ruby module for Ecasound
Summary(pl.UTF-8):	Moduł języka Ruby dla programu ecasound
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%{?ruby_mod_ver_requires_eq}

%description -n ruby-%{name}
Ruby module for Ecasound.

%description -n ruby-%{name} -l pl.UTF-8
Moduł języka Ruby dla programu ecasound.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -D_REENTRANT %{!?debug:-DNDEBUG}"
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
	--enable-shared \
	--enable-sys-readline \
	--enable-pyecasound \
	%{?with_ruby:--enable-rubyecasound} \
	--with-largefile \
	--with-python-includes=%{py_incdir} \
	--with-python-modules=%{py_libdir}

%{__make} \
	termcap_library_ncurses="-lncurses -ltinfo" \
	ncurses_library="-lncurses -ltinfo"

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{py_sitedir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING is licensing note, not GPL/LGPL text
%doc AUTHORS BUGS COPYING NEWS README RELNOTES TODO
%attr(755,root,root) %{_bindir}/eca*
%attr(755,root,root) %{_libdir}/libecasound.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecasound.so.24
%attr(755,root,root) %{_libdir}/libecasoundc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecasoundc.so.1
%attr(755,root,root) %{_libdir}/libkvutils.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkvutils.so.10
%{_datadir}/ecasound
%{_mandir}/man1/eca*.1*
%{_mandir}/man5/ecasoundrc.5*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libecasound-config
%attr(755,root,root) %{_bindir}/libecasoundc-config
%attr(755,root,root) %{_libdir}/libecasound.so
%attr(755,root,root) %{_libdir}/libecasoundc.so
%attr(755,root,root) %{_libdir}/libkvutils.so
%{_libdir}/libecasound.la
%{_libdir}/libecasoundc.la
%{_libdir}/libkvutils.la
%{_includedir}/kvutils
%{_includedir}/libecasound
%{_includedir}/libecasoundc

%files static
%defattr(644,root,root,755)
%{_libdir}/libecasound.a
%{_libdir}/libecasoundc.a
%{_libdir}/libkvutils.a

%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitedir}/ecacontrol.py[co]
%{py_sitedir}/eci.py[co]
%{py_sitedir}/pyeca.py[co]

%if %{with ruby}
%files -n ruby-%{name}
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/ecasound.rb
%endif
