
%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)
%define python_ver %(echo `python -c "import sys; print sys.version[:3]"`)
%define python_basedir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3])"`)
%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile python -c "import compileall; compileall.compile_dir('.')"

Summary:	Software package for multitrack audio processing
Summary(pl):	Oprogramowanie do wielo�cie�kowego przetwarzania d�wi�ku
Name:		ecasound
Version:	2.0.1
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Source0:	http://ecasound.seul.org/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-am_fix.patch
Patch1:		%{name}-ac_fix.patch
Patch2:		%{name}-readline.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	readline-devel >= 4.2
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	audiofile-devel >= 0.2.0
BuildRequires:	python-devel >= 2.1
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
Ecasound jest programem do wielo�cie�kowej edycji d�wi�ku, kt�ry mo�e
by� u�ywany tak do prostych zada� typu odtwarzanie i nagrywanie muzyki
czy te� konwersji pomi�dzy formatami plik�w muzycznych jak i do
wielo�cie�kowego nak�adania efekt�w, miksowania (przenikania,
wyciszania), nagrywania i odzyskiwania (w domy�le odszumiania lub
wyrzucania zniekszta�ce�) sygna�u.

Ecasound wspiera szerok� gam� �r�de� i wyj�� d�wi�ku oraz algorytm�w
do jego przetwarzania. Ecasound wspiera wiele wolnych (open source)
projekt�w, takich jak ALSA, OSS, mpg123, lame, libaudiofile czy te�
MikMod. Jedn� z zalet programu ecasound jest mo�liwo�� �a�cuchowego
(szeregowego) lub r�wnoleg�ego ��czenia efekt�w, kt�re mog� by�
kontrolowane poprzez oscylatory lub MIDI-CC. Pakiet ten zawiera
tekstowy interfejs u�ytkownika oraz kilka innych narz�dzi nadaj�cych
si� do przetwarzania wsadowego. Dost�pny jest tak�e graficzny
interfejs u�ytkownika - qtecasound.

%package -n libecasound
Summary:	Ecasound libraries
Summary(pl):	Biblioteki programu ecasound
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description -n libecasound
Ecasound libraries.

%description -l pl -n libecasound
Biblioteki programu ecasound.

%package -n libecasound-devel
Summary:	Ecasound headers
Summary(pl):	Pliki nag��wkowe bibliotek programu ecasound
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	libecasound = %{version}

%description -n libecasound-devel
Ecasound headers.

%description -l pl -n libecasound-devel
Pliki nag��wkowe bibliotek programu ecasound.

%package -n libecasound-static
Summary:	Ecasound static libraries
Summary(pl):	Biblioteki statyczne programu ecasound
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
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
Group(pl):	Aplikacje/D�wi�k
Requires:	ecasound = %{version}

%description plugins
This package contains ecasound plugins, which give support for ALSA,
Audio File Library and aRts.

%description -l pl plugins
Pakiet ten zawiera wtyczki dla programu ecasound, kt�re umo�liwiaj�
wsp�prac� z bibliotekami takich projekt�w jak ALSA, Audio File
Library oraz aRts.

%package -n python-%{name}
Summary:	Python module for Ecasound
Summary(pl):	Modu� j�zyka Python dla biblioteki programu ecasound
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/J�zyki/Python
%requires_eq	python

%description -n python-%{name}
Python module for Ecasound library.

%description -l pl -n python-%{name}
Modu� j�zyka Python dla biblioteki programu ecasound.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm missing
%ifarch sparc sparc64
libtoolize --copy --force
%endif
aclocal
autoconf
automake -a -c
CXXFLAGS="%{rpmcflags} -D_REENTRANT"
%configure \
	--enable-sys-readline \
	--with-python-includes=%{_includedir}/python%{python_ver} \
	--with-python-modules=%{python_basedir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_libdir}/python2.0/site-packages

%{__make} DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install

( cd pyecasound
  %python_compile_opt
  %python_compile
  install *.pyc *.pyo $RPM_BUILD_ROOT%{python_sitepkgsdir}
)

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
%{_includedir}/ecasound/*
%{_includedir}/kvutils/*
%attr(755,root,root) %{_libdir}/libkvutils.so
%attr(755,root,root) %{_libdir}/libkvutils.la
%attr(755,root,root) %{_libdir}/libecasound*.so
%attr(755,root,root) %{_libdir}/libecasound*.la

%files -n libecasound-static
%defattr(644,root,root,755)
%{_libdir}/libkvutils.a
%{_libdir}/libecasound.a
%{python_sitepkgsdir}/*.a

%files plugins
%defattr(644,root,root,755)
%dir %{_libdir}/ecasound-plugins
%attr(755,root,root) %{_libdir}/ecasound-plugins/lib*.so*
%{_libdir}/ecasound-plugins/lib*.la
%{_libdir}/ecasound-plugins/lib*.a

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{python_sitepkgsdir}/*.so
%{python_sitepkgsdir}/*.py[co]
