%define version 2.4.5
%define release %mkrel 10

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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.4.5-10mdv2010.0
+ Revision: 435059
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4.5-9mdv2009.0
+ Revision: 262285
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4.5-8mdv2009.0
+ Revision: 256686
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.4.5-6mdv2008.1
+ Revision: 136578
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Sep 12 2006 Guillaume Bedot <littletux@mandriva.org> 2.4.5-6mdv2007.0
- patch1: back to the rename get_info solution
- patch2: fix crashes when lauching apps from the tray

* Sun Sep 10 2006 Guillaume Bedot <littletux@mandriva.org> 2.4.5-5mdv2007.0
- drop previous patch for a better fix

* Sat Sep 09 2006 Guillaume Bedot <littletux@mandriva.org> 2.4.5-4mdv2007.0
- %%mkrel
- fix bug #24697

* Sun Jun 26 2005 Pascal Terjan <pterjan@mandriva.org> 2.4.5-3mdk
- add -fPIC
- move data to %%{_datadir}

* Sat Jun 25 2005 Pascal Terjan <pterjan@mandriva.org> 2.4.5-2mdk
- Enforce image path
- Don't ship Win32 icons
- root doesn't need execution right on the icons/doc

* Fri Dec 03 2004 Abel Cheung <deaddog@mandrake.org> 2.4.5-1mdk
- New version
- Software changed name long time ago
- rpmbuildupdate aware URL

* Mon Jan 26 2004 Abel Cheung <deaddog@deaddog.org> 2.4.0-1mdk
- New version
- Use MDK CFLAGS
- (Should this package change name?)

