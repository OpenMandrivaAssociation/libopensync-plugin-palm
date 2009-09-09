Name: 	 	libopensync-plugin-palm
Version: 	0.22
Epoch:		1
Release: 	%{mkrel 4}
Summary: 	Palm plugin for OpenSync synchronization framework
License:	LGPLv2+
Group:		Office
URL:		http://www.opensync.org
Source0:	http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	libopensync-devel < 0.30
BuildRequires:	pilot-link-devel
BuildRequires:  libneon-devel
BuildRequires:  libcurl-devel
Requires:	libopensync >= %{epoch}:%{version}
Obsoletes:	%{name}-devel < %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows Palm-based devices to synchronize using the OpenSync
framework.

%prep
%setup -q
autoreconf -sfi

%build
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{_includedir}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS INSTALL ChangeLog NEWS README
%{_libdir}/opensync/plugins/*
%{_libdir}/opensync/formats/*
%{_datadir}/opensync/defaults/palm-sync

