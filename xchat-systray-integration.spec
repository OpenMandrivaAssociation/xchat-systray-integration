%define version 2.4.5
%define release %mkrel 8

Summary: 	Systray (Notification Area) Plugin for XChat
Name:		xchat-systray-integration
Version:	%{version}
Release:	%{release}
Source0:	http://prdownloads.sourceforge.net/xchat2-plugins/xchat-systray-integration-%{version}-src.tar.bz2
Patch0:		xchat-systray-integration-imagepath.patch
Patch1:		xchat-systray-integration-2.4.5-fix-confusion-with-malaga-function.patch
Patch2:		xchat-systray-integration-2.4.5-fix-double-free-crashes.patch
License:	GPL
Group:		Networking/IRC
Url:		http://blight.altervista.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	xchat >= 2.0.4
BuildRequires:	gtk2-devel
Obsoletes:	xchat-systray-plugin
Provides:	xchat-systray-plugin

%description
Allows you to minimize and maximize XChat to the systray,
to mark/unmark you away and use your away nick,
and alerts you when somebody is trying to talk to you.

%prep
%setup -q
%patch0
%patch1 -p0
%patch2 -p0

%build
%make CFLAGS="%optflags -Wall -fPIC" 

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}%{_prefix}

%if lib != %_lib
mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
%endif
rm -rf %{buildroot}%{_libdir}/xchat/plugins/Win32Tray
mkdir -p %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_libdir}/xchat/plugins/*/ %{buildroot}%{_datadir}/%{name}
chmod 0644 %{buildroot}%{_datadir}/%{name}/*/*.png
chmod 0644 Docs/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Docs/*
%{_datadir}/%{name}
%{_libdir}/xchat/plugins/*

