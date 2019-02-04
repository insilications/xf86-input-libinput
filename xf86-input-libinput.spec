#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : xf86-input-libinput
Version  : 0.28.2
Release  : 18
URL      : https://www.x.org/releases/individual/driver/xf86-input-libinput-0.28.2.tar.bz2
Source0  : https://www.x.org/releases/individual/driver/xf86-input-libinput-0.28.2.tar.bz2
Source99 : https://www.x.org/releases/individual/driver/xf86-input-libinput-0.28.2.tar.bz2.sig
Summary  : Generic input driver for the X.Org server based on libinput
Group    : Development/Tools
License  : HPND MIT
Requires: xf86-input-libinput-data = %{version}-%{release}
Requires: xf86-input-libinput-lib = %{version}-%{release}
Requires: xf86-input-libinput-license = %{version}-%{release}
Requires: xf86-input-libinput-man = %{version}-%{release}
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)
BuildRequires : systemd-dev

%description
xf86-input-libinput - a libinput-based X driver
===============================================

%package data
Summary: data components for the xf86-input-libinput package.
Group: Data

%description data
data components for the xf86-input-libinput package.


%package dev
Summary: dev components for the xf86-input-libinput package.
Group: Development
Requires: xf86-input-libinput-lib = %{version}-%{release}
Requires: xf86-input-libinput-data = %{version}-%{release}
Provides: xf86-input-libinput-devel = %{version}-%{release}

%description dev
dev components for the xf86-input-libinput package.


%package lib
Summary: lib components for the xf86-input-libinput package.
Group: Libraries
Requires: xf86-input-libinput-data = %{version}-%{release}
Requires: xf86-input-libinput-license = %{version}-%{release}

%description lib
lib components for the xf86-input-libinput package.


%package license
Summary: license components for the xf86-input-libinput package.
Group: Default

%description license
license components for the xf86-input-libinput package.


%package man
Summary: man components for the xf86-input-libinput package.
Group: Default

%description man
man components for the xf86-input-libinput package.


%prep
%setup -q -n xf86-input-libinput-0.28.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549288769
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1549288769
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-input-libinput
cp COPYING %{buildroot}/usr/share/package-licenses/xf86-input-libinput/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/X11/xorg.conf.d/40-libinput.conf

%files dev
%defattr(-,root,root,-)
/usr/include/xorg/libinput-properties.h
/usr/lib64/pkgconfig/xorg-libinput.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/input/libinput_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-input-libinput/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/libinput.4
