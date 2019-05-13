#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : terminology
Version  : 1.4.0
Release  : 1
URL      : https://download.enlightenment.org/rel/apps/terminology/terminology-1.4.0.tar.xz
Source0  : https://download.enlightenment.org/rel/apps/terminology/terminology-1.4.0.tar.xz
Summary  : EFL based terminal emulator
Group    : Development/Tools
License  : BSD-2-Clause
Requires: terminology-bin = %{version}-%{release}
Requires: terminology-data = %{version}-%{release}
Requires: terminology-license = %{version}-%{release}
Requires: terminology-locales = %{version}-%{release}
Requires: terminology-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(edje)

%description
Terminology 1.3.2
=================
This is an EFL terminal emulator with some extra bells and whistles.

%package bin
Summary: bin components for the terminology package.
Group: Binaries
Requires: terminology-data = %{version}-%{release}
Requires: terminology-license = %{version}-%{release}

%description bin
bin components for the terminology package.


%package data
Summary: data components for the terminology package.
Group: Data

%description data
data components for the terminology package.


%package license
Summary: license components for the terminology package.
Group: Default

%description license
license components for the terminology package.


%package locales
Summary: locales components for the terminology package.
Group: Default

%description locales
locales components for the terminology package.


%package man
Summary: man components for the terminology package.
Group: Default

%description man
man components for the terminology package.


%prep
%setup -q -n terminology-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557719476
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/terminology
cp COPYING %{buildroot}/usr/share/package-licenses/terminology/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang terminology

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/terminology
/usr/bin/tyalpha
/usr/bin/tybg
/usr/bin/tycat
/usr/bin/tyls
/usr/bin/typop
/usr/bin/tyq
/usr/bin/tysend

%files data
%defattr(-,root,root,-)
/usr/share/applications/terminology.desktop
/usr/share/icons/hicolor/128x128/apps/terminology.png
/usr/share/terminology/backgrounds/mystic.png
/usr/share/terminology/backgrounds/texture_background.png
/usr/share/terminology/fonts/10x20.pcf
/usr/share/terminology/fonts/4x6.pcf
/usr/share/terminology/fonts/5x7.pcf
/usr/share/terminology/fonts/5x8.pcf
/usr/share/terminology/fonts/6x10.pcf
/usr/share/terminology/fonts/6x12.pcf
/usr/share/terminology/fonts/6x13.pcf
/usr/share/terminology/fonts/6x9.pcf
/usr/share/terminology/fonts/7x13.pcf
/usr/share/terminology/fonts/7x14.pcf
/usr/share/terminology/fonts/8x13.pcf
/usr/share/terminology/fonts/9x15.pcf
/usr/share/terminology/fonts/9x18.pcf
/usr/share/terminology/fonts/TERMINUS.txt
/usr/share/terminology/fonts/XFONT.txt
/usr/share/terminology/fonts/nexus.pcf
/usr/share/terminology/fonts/terminus-12.pcf
/usr/share/terminology/fonts/terminus-14-bold.pcf
/usr/share/terminology/fonts/terminus-14.pcf
/usr/share/terminology/fonts/terminus-16-bold.pcf
/usr/share/terminology/fonts/terminus-16.pcf
/usr/share/terminology/fonts/terminus-18-bold.pcf
/usr/share/terminology/fonts/terminus-18.pcf
/usr/share/terminology/fonts/terminus-20-bold.pcf
/usr/share/terminology/fonts/terminus-20.pcf
/usr/share/terminology/images/terminology.png
/usr/share/terminology/themes/base16_ocean_dark.edj
/usr/share/terminology/themes/black.edj
/usr/share/terminology/themes/default.edj
/usr/share/terminology/themes/mild.edj
/usr/share/terminology/themes/mustang.edj
/usr/share/terminology/themes/nord.edj
/usr/share/terminology/themes/nyanology.edj
/usr/share/terminology/themes/smyck.edj
/usr/share/terminology/themes/solarized.edj
/usr/share/terminology/themes/solarized_light.edj

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/terminology/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/terminology-helpers.1
/usr/share/man/man1/terminology.1
/usr/share/man/man1/tyalpha.1
/usr/share/man/man1/tybg.1
/usr/share/man/man1/tycat.1
/usr/share/man/man1/tyls.1
/usr/share/man/man1/typop.1
/usr/share/man/man1/tyq.1
/usr/share/man/man1/tysend.1

%files locales -f terminology.lang
%defattr(-,root,root,-)

