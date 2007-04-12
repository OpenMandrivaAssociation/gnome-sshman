%define name	gnome-sshman
%define version 0.5.2
%define release %mkrel 4

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
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="terminals_section.png" needs="x11" title="Gnome-SSHMan" longtitle="Manage SSH connections" section="System/Terminals" xdg="true"
EOF

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
Encoding=UTF-8
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_datadir}/%name
%{_menudir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop


