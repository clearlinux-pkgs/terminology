#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : terminology
Version  : 1.14.0
Release  : 14
URL      : https://download.enlightenment.org/rel/apps/terminology/terminology-1.14.0.tar.xz
Source0  : https://download.enlightenment.org/rel/apps/terminology/terminology-1.14.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: terminology-bin = %{version}-%{release}
Requires: terminology-data = %{version}-%{release}
Requires: terminology-license = %{version}-%{release}
Requires: terminology-locales = %{version}-%{release}
Requires: terminology-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(edje)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
![Terminology](/data/readme/terminology.png)
# Terminology
-----
*Please report bugs/issues at*
[git.enlightenment.org](https://git.enlightenment.org/enlightenment/terminology/issues)

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
%setup -q -n terminology-1.14.0
cd %{_builddir}/terminology-1.14.0
pushd ..
cp -a terminology-1.14.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742826496
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/terminology
cp %{_builddir}/terminology-%{version}/COPYING %{buildroot}/usr/share/package-licenses/terminology/5c8dfc3f40802aaafd2043265ef330b2fedcf090 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang terminology
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/terminology
/V3/usr/bin/tyalpha
/V3/usr/bin/tybg
/V3/usr/bin/tycat
/V3/usr/bin/tyls
/V3/usr/bin/typop
/V3/usr/bin/tyq
/V3/usr/bin/tysend
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
"/usr/share/terminology/colorschemes/Belafonte Day.eet"
"/usr/share/terminology/colorschemes/Belafonte Night.eet"
/usr/share/terminology/colorschemes/Black.eet
/usr/share/terminology/colorschemes/Cobalt2.eet
/usr/share/terminology/colorschemes/Default.eet
/usr/share/terminology/colorschemes/Dracula.eet
/usr/share/terminology/colorschemes/Fahrenheit.eet
"/usr/share/terminology/colorschemes/Fir Dark.eet"
/usr/share/terminology/colorschemes/Material.eet
/usr/share/terminology/colorschemes/Mild.eet
/usr/share/terminology/colorschemes/Mustang.eet
/usr/share/terminology/colorschemes/Nord.eet
"/usr/share/terminology/colorschemes/Ocean Dark.eet"
"/usr/share/terminology/colorschemes/One Dark.eet"
/usr/share/terminology/colorschemes/PaleNight.eet
/usr/share/terminology/colorschemes/PaperColor.eet
"/usr/share/terminology/colorschemes/Selenized Black.eet"
"/usr/share/terminology/colorschemes/Selenized Dark.eet"
"/usr/share/terminology/colorschemes/Selenized Light.eet"
"/usr/share/terminology/colorschemes/Selenized White.eet"
/usr/share/terminology/colorschemes/Smyck.eet
"/usr/share/terminology/colorschemes/Soft Era.eet"
"/usr/share/terminology/colorschemes/Solarized Light.eet"
/usr/share/terminology/colorschemes/Solarized.eet
"/usr/share/terminology/colorschemes/Tango Dark.eet"
"/usr/share/terminology/colorschemes/Tango Light.eet"
"/usr/share/terminology/colorschemes/Tomorrow Night Burns.eet"
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
/usr/share/terminology/themes/default.edj
/usr/share/terminology/themes/nyanology.edj

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/terminology/5c8dfc3f40802aaafd2043265ef330b2fedcf090

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

