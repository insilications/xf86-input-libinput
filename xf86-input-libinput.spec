#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : xf86-input-libinput
Version  : 0.25.0
Release  : 2
URL      : https://www.x.org/releases/individual/driver/xf86-input-libinput-0.25.0.tar.gz
Source0  : https://www.x.org/releases/individual/driver/xf86-input-libinput-0.25.0.tar.gz
Source99 : https://www.x.org/releases/individual/driver/xf86-input-libinput-0.25.0.tar.gz.sig
Summary  : X.Org libinput input driver.
Group    : Development/Tools
License  : MIT
Requires: xf86-input-libinput-lib
Requires: xf86-input-libinput-data
Requires: xf86-input-libinput-doc
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)

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
Requires: xf86-input-libinput-lib
Requires: xf86-input-libinput-data
Provides: xf86-input-libinput-devel

%description dev
dev components for the xf86-input-libinput package.


%package doc
Summary: doc components for the xf86-input-libinput package.
Group: Documentation

%description doc
doc components for the xf86-input-libinput package.


%package lib
Summary: lib components for the xf86-input-libinput package.
Group: Libraries
Requires: xf86-input-libinput-data

%description lib
lib components for the xf86-input-libinput package.


%prep
%setup -q -n xf86-input-libinput-0.25.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491569197
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1491569197
rm -rf %{buildroot}
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man4/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/input/libinput_drv.so
