%define name	libopensync-plugin-palm
%define version	0.20
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	PALM plugin for opensync synchronization tool
Version: 	%{version}
Release: 	%{release}

Source:		svn://svn.opensync.org/plugins/palm/%{name}-%{version}.tar.bz2
URL:		http://www.opensync.org
License:	LGPL
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires:	opensync-devel >= 0.20
BuildRequires:	pilot-link-devel
BuildRequires:  libneon-devel
BuildRequires:  libcurl-devel

%description
This plugin allows applications using OpenSync to synchronise via OPIE

%package devel
Summary:        Header files, libraries and development documentation for libopensync-plugin-palm
Group:          Networking/Other
Requires:       %{name} = %{version}  opensync-devel pilot-link-devel

%description devel
This package contains the header files, static libraries and
development documentation for libopensync-plugin-palm. If you like to
develop programs using libopensync-plugin-palm, you will need to
install libopensync-plugin-palm-devel.

%prep
%setup -q
autoreconf -sfi

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL ChangeLog NEWS README
%{_libdir}/opensync/plugins/*.so
%{_libdir}/opensync/formats/*.so
%{_datadir}/opensync/defaults/palm-sync

%files devel
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL ChangeLog NEWS README
%{_includedir}/opensync-1.0/opensync/*.h
%{_libdir}/opensync/plugins/*.la
%{_libdir}/opensync/formats/*.la


