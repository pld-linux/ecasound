Summary:	Software package for multitrack audio processing
Summary(pl):	Oprogramowanie do wielo¶cie¿kowego przetwarzania d¼wiêku
Name:		ecasound
Version:	1.7.8r12
Release:	1
License:	GPL
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://ecasound.seul.org/download/%{name}-%{version}.tar.gz
Patch0:		ecasound-ncurses_and_sys_readline.patch.bz2
Patch1:		ecasound-DESTDIR.patch.bz2
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
Ecasound is the software package for multitrack audio processing.

1. Supported audio inputs/outputs:
- ALSA - Advanced Linux Sound Architecture (PCM input, output and
  loopback support)
- OSS (/dev/dsp*) - Open Sound System
- RIFF WAVE (.wav) - 8/16bit non-compressed
- Ecasound Wave Files (.ewf) - simple wrapper format for recording
  purposes
- Raw/headerless sample data (.raw)
- CDDA (.cdr) - format used on audio-CDs
- MPEG 1.0/2.0 (layers 1, 2 and 3) (.mp3) - using mpg123 for input and
  lame for output
- Module formats supported by MikMod - XM, IT, S3M, MOD, MTM, 669,
  STM, ULT, FAR, MED, AMF, DSM, IMF, GDM, STX
- AIFF (.aiff) and Sun/NeXT audio (.au/.snd) formats using
  libaudiofile:
- standard input/output streams (stdin, stdout) and named pipes 2.
  Effects:
- Various amplifiers, panning, DC-fix, volume normalization
- Channel mixing and routing
- Noise gate, two compressors
- Filters: lowpass, highpass, bandpass, bandreject, resonant lowpass,
  resonant bandpass, resonator, inverse comb
- Time-based: multitap delay, reverb, fake-stereo 3. Controllers (for
  effect parameters):
- sine oscillator
- generic oscillator (either using an envelope table with static
  points or with linear interpolation)
- linear envelopes
- MIDI continuous controllers (CC)

This package contains ecasound with interactive textmode user program
and utilites which support batch processing:
- ecatools_fixdc: fix DC-offset
- ecatools_normalize: normalize volume level
- ecatools_play: play files using the default output

%description -l pl
N/A

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

%description -n qtecasound -l pl
N/A

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

%description -n libqtecasound-devel
Ecasound QT frontend library headers.

%description -l pl -n libqtecasound-devel
Pliki nag³ówkowe bibliotek interfejsu graficznego programu ecasound.


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
	--with-qt-includes=%{_prefix}/X11R6/include 
	--with-qt-libraries=%{_prefix}/X11R6/lib \
	--enable-sys-readline
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/libkvutils*.so*
%attr(755,root,root) %{_libdir}/libecasound*.so*

%files -n libecasound-devel
%defattr(644,root,root,755)
%{_includedir}/ecasound/[^qe]*
%{_includedir}/kvutils/*
%attr(755,root,root) %{_libdir}/libkvutils.a
%attr(755,root,root) %{_libdir}/libkvutils.la

%files -n qtecasound
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qtecasound
%{_mandir}/man1/qt*

%files -n libqtecasound
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqtecasound*.so*

%files -n libqtecasound-devel
%defattr(644,root,root,755)
%{_includedir}/ecasound/qe*
%attr(755,root,root) %{_libdir}/libqtecasound*.a
%attr(755,root,root) %{_libdir}/libqtecasound*.la
