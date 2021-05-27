# SPDX-License-Identifier: GPL-3.0-or-later
#
# Copyright (c) 2020 Western Digital Corporation or its affiliates.
Name:		dm-zoned-tools
Version:	2.1.1
Release:	1%{?dist}
Summary:	Provides utilities to format, check and repair Linux dm-zoned devices

License:	GPLv3+
URL:		https://github.com/westerndigitalcorporation/%{name}
Source0:	https://github.com/westerndigitalcorporation/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:	device-mapper-devel
BuildRequires:	kmod-devel
BuildRequires:	libuuid-devel
BuildRequires:	libblkid-devel
BuildRequires:	autoconf
BuildRequires:	autoconf-archive
BuildRequires:	automake
BuildRequires:	libtool

%description
This package provides the dmzadm utility which can be used to format,
check and repair zoned block devices used with Linux dm-zoned device
mapper target driver.

%prep
%autosetup

%build
sh autogen.sh
%configure
%make_build

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%ldconfig_scriptlets

%files
%{_sbindir}/dmzadm
%{_mandir}/man8/dmzadm.*

%license COPYING.GPL
%doc README.md CONTRIBUTING

%changelog
* Thu May 27 2021 Damien Le Moal <damien.lemoal@wdc.com> 2.1.1-1
- Version 2.1.1 initial package
