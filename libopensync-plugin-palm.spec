%define name	libopensync-plugin-palm
%define version	0.33
%define svnrel	2596
%define release %mkrel 1.%{svnrel}.1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	PALM plugin for opensync synchronization tool
License:	LGPL
Group:		Office
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-r%{svnrel}.tar.bz2
BuildRequires:	opensync-devel >= %{version}
BuildRequires:	pilot-link-devel
BuildRequires:  libneon-devel
BuildRequires:  libcurl-devel
# fwang: no devel package anymore
Obsoletes:	%name-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise via OPIE

%prep
%setup -q -n %{name}

%build
autoreconf -sfi
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
%doc AUTHORS README
%{_libdir}/opensync/plugins/*.so
%{_libdir}/opensync/formats/*.so
%{_datadir}/opensync/defaults/palm-sync
