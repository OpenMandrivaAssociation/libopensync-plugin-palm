%define name	libopensync-plugin-palm
%define version	0.35
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	PALM plugin for opensync synchronization tool
License:	LGPLv2+
Group:		Office
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
Patch0:		libopensync-plugin-palm-0.34-find-libxml2.patch
BuildRequires:	opensync-devel >= %{version}
BuildRequires:	pilot-link-devel
BuildRequires:  libneon-devel
BuildRequires:  libcurl-devel
BuildRequires:	libxml2-devel
BuildRequires:	cmake
BuildRoot:	%{_tmppath}/%{name}-%{version}
# fwang: it does not produce devel pacakge
Obsoletes:	%name-devel

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
%patch0 -p0

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
%{_libdir}/opensync-1.0/*/*.so
%{_datadir}/opensync-1.0/defaults/palm-sync
