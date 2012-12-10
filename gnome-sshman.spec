%define name	gnome-sshman
%define version 0.6
%define release %mkrel 5

Name: 	 	%{name}
Summary: 	SSH connection manager for GNOME and Nautilus
Version: 	%{version}
Release: 	%{release}

Source:		http://savannah.nongnu.org/download/gnome-sshman/%{name}-%{version}.tar.bz2
URL:		http://www.oronetes.net/webs/gnome-sshman/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	pygtk2.0-libglade gnome-terminal pygtk2.0 gnome-python python-vte python-pexpect pycrypto
BuildArch:	noarch

%description
Gnome-sshman is an SSH session manager for GNOME. It is easy and fast to use,
and is useful for system administrators that need to connect to many SSH
servers. Gnome-sshman saves ssh sessions and allows you to open a saved
session with a double click in nautilus or opening a new session running
gnome-sshman.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
cp bin/%name %buildroot/%_bindir/
mkdir -p %buildroot/%_datadir/%name
cp libs/* %buildroot/%_datadir/%name

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gnome-SSHMan
Comment=Manage SSH connections
Exec=%{_bindir}/%{name}
Icon=terminals_section
Terminal=false
Type=Application
Categories=GNOME;GTK;X-MandrivaLinux-System-Terminals;TerminalEmulator;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-5mdv2011.0
+ Revision: 619120
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.6-4mdv2010.0
+ Revision: 429234
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6-3mdv2009.0
+ Revision: 246425
- rebuild
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 05 2007 Jérôme Soyer <saispo@mandriva.org> 0.6-1mdv2008.1
+ Revision: 115737
- New release 0.6

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Mon Jan 08 2007 Crispin Boylan <crisb@mandriva.org> 0.5.2-4mdv2007.0
+ Revision: 106184
- Requires gnome-python not python-gnome
- Import gnome-sshman

* Tue Sep 12 2006 Emmanuel Andry <eandry@mandriva.org> 0.5.2-3mdv2007.0
- %%mkrel
- xdg menu

* Sun Feb 19 2006 Jerome Soyer <saispo@mandriva.org> 0.5.2-2mdk
- Fix Requires

* Mon Nov 28 2005 Austin Acton <austin@mandriva.org> 0.5.2-1mdk
- New release 0.5.2

* Tue Feb 22 2005 Austin Acton <austin@mandrake.org> 0.4.3-1mdk
- New release 0.4.3
- fix source URL

* Fri Feb 11 2005 Austin Acton <austin@mandrake.org> 0.4-1mdk
- 0.4

* Tue Feb 08 2005 Austin Acton <austin@mandrake.org> 0.3.2-1mdk
- 0.3.2
- require gnome-terminal instead of xterm

* Sun Feb 06 2005 Austin Acton <austin@mandrake.org> 0.3-1mdk
- initial package

