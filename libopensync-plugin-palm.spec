%define name	libopensync-plugin-palm
%define version	0.34
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	PALM plugin for opensync synchronization tool
License:	LGPLv2+
Group:		Office
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	opensync-devel >= %{version}
BuildRequires:	pilot-link-devel
BuildRequires:  libneon-devel
BuildRequires:  libcurl-devel
BuildRequires:	cmake
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%build
%cmake
%make
										
%install
rm -rf $RPM_BUILD_ROOT
cd build
%makeinstall_std
cd -

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS README
%{_libdir}/opensync/*/*.so
%{_datadir}/opensync/defaults/palm-sync

%files devel
%defattr(-, root, root)
%doc AUTHORS README
%{_includedir}/opensync-1.0/opensync/*.h
%{_libdir}/opensync/*/*.la
