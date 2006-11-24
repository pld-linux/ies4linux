# TODO
# - wants (ie6 at least) to download gecko installer, but still fails
#
# This spec file is released under the GNU General Public License version 2.0
# (http://www.gnu.org/licenses/gpl.txt).
#
# NOTE: Releasing this spec file under the GPL does not alter the licensing
# of Internet Explorer itself. Satisfying the terms of Internet Explorer's
# license remains the user's responsibility.

# NOTE: For IE7 you should have normalize.dll and inetcomm.dll from your
#	WindowsXP SP2 installation!

%bcond_with	ie7	build ie7 package

%define	_installdir	%{_datadir}/ies4linux

# TODO:
# - *.desktop files for each ie
# - sources downloaded via install script as NoSourceXX
# - move profiles to $HOME directory
# - License tag specifies package license? then it should not be GPL

Summary:	Run IE 7, 6, 5.5 and 5 on Linux with Wine
Summary(pl):	Uruchamianie IE 7, 6, 5.5 i 5 pod Linuksem przy u¿yciu Wine
Name:		ies4linux
Version:	2.0
Release:	0.4
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://www.tatanka.com.br/ies4linux/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	c790d47e8aef5267037b1df5250352f8
Source1:	%{name}.ie.sh
%if %{with ie7}
Source2:	http://download.microsoft.com/download/3/8/8/38889DC1-848C-4BF2-8335-86C573AD86D9/IE7-WindowsXP-x86-enu.exe
NoSource:	2
Source3:	http://www.down-dll.com/dll/normaliz.zip
NoSource:	3
Source4:	inetcplc.dll
NoSource:	4
%endif
Source5:	%{name}.desktop
Patch0:		%{name}-destdir.patch
URL:		http://www.tatanka.com.br/ies4linux/index-en.html
BuildRequires:	cabextract
BuildRequires:	wine
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
#Requires:	dcom98
Requires:	wine
#Requires:	wine-programs
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IEs4Linux is the simpler way to have Microsoft Internet Explorer
running on Linux.

%description -l pl
IEs4Linux to prostszy sposób na uruchamianie Microsoft Internet
Explorera pod Linuksem.

%prep
%setup -q
%patch0 -p1
%if %{with ie7}
mkdir ie7
cd ie7
cabextract %{SOURCE2}
unzip %{SOURCE3}
cp %{SOURCE4} .
cd -
%endif

for a in 5.0 5.5 6.0 7.0; do
	v=$(echo "$a" | sed -e 's,\.0,,' | tr -d .)
	sed -e "
		s,ie6,ie$v,
		s,6.0,$a,
	" %{SOURCE5} > ie$v.desktop
done

%package ie5
Summary:	Internet Explorer 5
Summary(pl):	Internet Explorer 5
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie5
Internet Explorer 5.

%description ie5 -l pl
Internet Explorer 5.

%package ie55
Summary:	Internet Explorer 5.5
Summary(pl):	Internet Explorer 5.5
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie55
Internet Explorer 5.5.

%description ie55 -l pl
Internet Explorer 5.5.

%package ie6
Summary:	Internet Explorer 6
Summary(pl):	Internet Explorer 6
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6
Internet Explorer 6.

%description ie6 -l pl
Internet Explorer 6.

%package ie7
Summary:	Internet Explorer 7
Summary(pl):	Internet Explorer 7
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie7
Internet Explorer 7.

%description ie7 -l pl
Internet Explorer 7.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

bash ./ies4linux \
	--install-ie55 \
	--install-ie5 \
	--basedir %{_installdir} \
	--bindir %{_bindir} \
	--destdir $RPM_BUILD_ROOT \
	--downloaddir %{_sourcedir} \
	--locale EN-US \
	--install-flash << EOF
n
n
EOF

rm -rf $RPM_BUILD_ROOT%{_installdir}/{ie5,ie55,ie6}/drive_c/windows/profiles/%(id -u -n)
rm $RPM_BUILD_ROOT%{_installdir}/ie{5,55,6}/.firstrun

#
# Shell scripts
#
rm $RPM_BUILD_ROOT%{_bindir}/ie*
cp %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/ies4linux
ln -sf %{_bindir}/ies4linux $RPM_BUILD_ROOT%{_bindir}/ie5
ln -sf %{_bindir}/ies4linux $RPM_BUILD_ROOT%{_bindir}/ie55
ln -sf %{_bindir}/ies4linux $RPM_BUILD_ROOT%{_bindir}/ie6
cp -a ie[56]*.desktop $RPM_BUILD_ROOT%{_desktopdir}

%if %{with ie7}
ln -sf %{_bindir}/ies4linux $RPM_BUILD_ROOT%{_bindir}/ie7
cp -a ie7.desktop $RPM_BUILD_ROOT%{_desktopdir}/ie7.desktop

cp -a $RPM_BUILD_ROOT%{_installdir}/ie6 $RPM_BUILD_ROOT%{_installdir}/ie7
cp ie7/{wininet,iertutil,shlwapi,urlmon,jscript,vbscript,mshtml,mshtmled,mshtmler,advpack,inetcplc,normaliz}.dll \
	ie7/inetcpl.cpl \
	$RPM_BUILD_ROOT%{_installdir}/ie7/drive_c/windows/system

cat $RPM_BUILD_ROOT%{_installdir}/ie6/user.reg | \
	sed 's:"Version"="win98":"Version"="win98"\n\n[Software\\Wine\\AppDefaults\\iexplore.exe] 1161336541\n"Version"="winxp"\n:' \
	> $RPM_BUILD_ROOT%{_installdir}/ie7/user.reg
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 212 -r -f ies4linux

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<'EOF'
Remember to add users which will use IEs to ies4linux group or they won't be
able to create their profiles and running IEs will fail.
EOF
#'
fi

%postun
if [ "$1" = "0" ]; then
	%groupremove ies4linux
fi

%files
%defattr(644,root,root,755)
%doc README
%dir %{_installdir}
%attr(755,root,root) %{_bindir}/ies4linux
%{_installdir}/%{name}.svg

%files ie5
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ie5
%{_desktopdir}/ie5.desktop
%{_installdir}/ie5/*.reg
%dir %{_installdir}/ie5
%dir %{_installdir}/ie5/dosdevices
%{_installdir}/ie5/dosdevices/*:
%dir %{_installdir}/ie5/drive_c
%dir "%{_installdir}/ie5/drive_c/Program Files"
%dir "%{_installdir}/ie5/drive_c/Program Files/Common Files"
%dir "%{_installdir}/ie5/drive_c/Program Files/Internet Explorer"
"%{_installdir}/ie5/drive_c/Program Files/Internet Explorer/iexplore.exe"
%dir %{_installdir}/ie5/drive_c/windows
%attr(755,root,root) %{_installdir}/ie5/drive_c/windows/*.exe
%{_installdir}/ie5/drive_c/windows/*.ini
%dir %{_installdir}/ie5/drive_c/windows/command
%attr(755,root,root) %{_installdir}/ie5/drive_c/windows/command/start.exe
%dir %{_installdir}/ie5/drive_c/windows/fonts
%{_installdir}/ie5/drive_c/windows/fonts/*.ttf
%dir %{_installdir}/ie5/drive_c/windows/help
%{_installdir}/ie5/drive_c/windows/help/*.hlp
%dir %{_installdir}/ie5/drive_c/windows/inf
%{_installdir}/ie5/drive_c/windows/inf/*.inf
%dir %{_installdir}/ie5/drive_c/windows/options
%dir %{_installdir}/ie5/drive_c/windows/options/cabs
%{_installdir}/ie5/drive_c/windows/options/cabs/*.dll
%dir %attr(770,root,ies4linux) %{_installdir}/ie5/drive_c/windows/profiles
%dir "%{_installdir}/ie5/drive_c/windows/profiles/All Users"
%dir "%{_installdir}/ie5/drive_c/windows/profiles/All Users/Application Data"
%dir "%{_installdir}/ie5/drive_c/windows/profiles/All Users/Desktop"
%dir "%{_installdir}/ie5/drive_c/windows/profiles/All Users/Documents"
%dir "%{_installdir}/ie5/drive_c/windows/profiles/All Users/Favorites"
%dir "%{_installdir}/ie5/drive_c/windows/profiles/All Users/Start Menu"
%dir "%{_installdir}/ie5/drive_c/windows/profiles/All Users/Start Menu/Programs"
%dir "%{_installdir}/ie5/drive_c/windows/profiles/All Users/Start Menu/Programs/StartUp"
%dir "%{_installdir}/ie5/drive_c/windows/profiles/All Users/Templates"
%{_installdir}/ie5/drive_c/windows/system
%dir %{_installdir}/ie5/drive_c/windows/system32
%dir %{_installdir}/ie5/drive_c/windows/system32/Macromed
%dir %{_installdir}/ie5/drive_c/windows/system32/Macromed/Flash
%{_installdir}/ie5/drive_c/windows/system32/Macromed/Flash/*.ocx
%attr(755,root,root) %{_installdir}/ie5/drive_c/windows/system32/Macromed/Flash/*.exe
%dir %{_installdir}/ie5/drive_c/windows/system32/drivers
%dir %{_installdir}/ie5/drive_c/windows/system32/sfp
%dir %{_installdir}/ie5/drive_c/windows/system32/sfp/ie
%{_installdir}/ie5/drive_c/windows/system32/sfp/ie/vgx.cat
%attr(755,root,root) %{_installdir}/ie5/drive_c/windows/system32/*.exe
%{_installdir}/ie5/drive_c/windows/system32/*.dll
%{_installdir}/ie5/drive_c/windows/system32/*.ocx
%{_installdir}/ie5/drive_c/windows/system32/*.cat
%{_installdir}/ie5/drive_c/windows/system32/*.msc
%{_installdir}/ie5/drive_c/windows/system32/*.nls
%{_installdir}/ie5/drive_c/windows/system32/*.inf
%{_installdir}/ie5/drive_c/windows/system32/*.vxd
%{_installdir}/ie5/drive_c/windows/system32/*.txt
%{_installdir}/ie5/drive_c/windows/system32/*.cnv
%{_installdir}/ie5/drive_c/windows/system32/*.mof
%{_installdir}/ie5/drive_c/windows/system32/*.htm
%{_installdir}/ie5/drive_c/windows/system32/*.acm
%{_installdir}/ie5/drive_c/windows/system32/*.cpl
%{_installdir}/ie5/drive_c/windows/system32/*.gif
%{_installdir}/ie5/drive_c/windows/system32/*.tlb
%{_installdir}/ie5/drive_c/windows/system32/*.stf
%{_installdir}/ie5/drive_c/windows/system32/*.bat
%{_installdir}/ie5/drive_c/windows/system32/*.pdr
%{_installdir}/ie5/drive_c/windows/system32/*.rat
%{_installdir}/ie5/drive_c/windows/system32/*.icm
%{_installdir}/ie5/drive_c/windows/system32/*.wav
%{_installdir}/ie5/drive_c/windows/system32/*.crl
%{_installdir}/ie5/drive_c/windows/system32/*.drv
%dir %{_installdir}/ie5/drive_c/windows/temp

%files ie55
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ie55
%{_desktopdir}/ie55.desktop
%{_installdir}/ie55/*.reg
%dir %{_installdir}/ie55
%dir %{_installdir}/ie55/dosdevices
%{_installdir}/ie55/dosdevices/*:
%dir %{_installdir}/ie55/drive_c
%dir "%{_installdir}/ie55/drive_c/Program Files"
%dir "%{_installdir}/ie55/drive_c/Program Files/Common Files"
%dir "%{_installdir}/ie55/drive_c/Program Files/Internet Explorer"
"%{_installdir}/ie55/drive_c/Program Files/Internet Explorer/iexplore.exe"
%dir %{_installdir}/ie55/drive_c/windows
%attr(755,root,root) %{_installdir}/ie55/drive_c/windows/*.exe
%{_installdir}/ie55/drive_c/windows/*.ini
%dir %{_installdir}/ie55/drive_c/windows/command
%attr(755,root,root) %{_installdir}/ie55/drive_c/windows/command/start.exe
%dir %{_installdir}/ie55/drive_c/windows/fonts
%{_installdir}/ie55/drive_c/windows/fonts/*.ttf
%dir %{_installdir}/ie55/drive_c/windows/help
%{_installdir}/ie55/drive_c/windows/help/*.hlp
%dir %{_installdir}/ie55/drive_c/windows/inf
%{_installdir}/ie55/drive_c/windows/inf/*.inf
%dir %{_installdir}/ie55/drive_c/windows/options
%dir %{_installdir}/ie55/drive_c/windows/options/cabs
%{_installdir}/ie55/drive_c/windows/options/cabs/*.dll
%dir %attr(770,root,ies4linux) %{_installdir}/ie55/drive_c/windows/profiles
%dir "%{_installdir}/ie55/drive_c/windows/profiles/All Users"
%dir "%{_installdir}/ie55/drive_c/windows/profiles/All Users/Application Data"
%dir "%{_installdir}/ie55/drive_c/windows/profiles/All Users/Desktop"
%dir "%{_installdir}/ie55/drive_c/windows/profiles/All Users/Documents"
%dir "%{_installdir}/ie55/drive_c/windows/profiles/All Users/Favorites"
%dir "%{_installdir}/ie55/drive_c/windows/profiles/All Users/Start Menu"
%dir "%{_installdir}/ie55/drive_c/windows/profiles/All Users/Start Menu/Programs"
%dir "%{_installdir}/ie55/drive_c/windows/profiles/All Users/Start Menu/Programs/StartUp"
%dir "%{_installdir}/ie55/drive_c/windows/profiles/All Users/Templates"
%{_installdir}/ie55/drive_c/windows/system
%dir %{_installdir}/ie55/drive_c/windows/system32
%dir %{_installdir}/ie55/drive_c/windows/system32/Macromed
%dir %{_installdir}/ie55/drive_c/windows/system32/Macromed/Flash
%{_installdir}/ie55/drive_c/windows/system32/Macromed/Flash/*.ocx
%attr(755,root,root) %{_installdir}/ie55/drive_c/windows/system32/Macromed/Flash/*.exe
%dir %{_installdir}/ie55/drive_c/windows/system32/drivers
%dir %{_installdir}/ie55/drive_c/windows/system32/sfp
%dir %{_installdir}/ie55/drive_c/windows/system32/sfp/ie
%{_installdir}/ie55/drive_c/windows/system32/sfp/ie/vgx.cat
%attr(755,root,root) %{_installdir}/ie55/drive_c/windows/system32/*.exe
%{_installdir}/ie55/drive_c/windows/system32/*.dll
%{_installdir}/ie55/drive_c/windows/system32/*.ocx
%{_installdir}/ie55/drive_c/windows/system32/*.cat
%{_installdir}/ie55/drive_c/windows/system32/*.msc
%{_installdir}/ie55/drive_c/windows/system32/*.nls
%{_installdir}/ie55/drive_c/windows/system32/*.inf
%{_installdir}/ie55/drive_c/windows/system32/*.vxd
%{_installdir}/ie55/drive_c/windows/system32/*.txt
%{_installdir}/ie55/drive_c/windows/system32/*.cnv
%{_installdir}/ie55/drive_c/windows/system32/*.mof
%{_installdir}/ie55/drive_c/windows/system32/*.htm
%{_installdir}/ie55/drive_c/windows/system32/*.acm
%{_installdir}/ie55/drive_c/windows/system32/*.cpl
%{_installdir}/ie55/drive_c/windows/system32/*.gif
%{_installdir}/ie55/drive_c/windows/system32/*.tlb
%{_installdir}/ie55/drive_c/windows/system32/*.stf
%{_installdir}/ie55/drive_c/windows/system32/*.bat
%{_installdir}/ie55/drive_c/windows/system32/*.pdr
%{_installdir}/ie55/drive_c/windows/system32/*.rat
%{_installdir}/ie55/drive_c/windows/system32/*.icm
%{_installdir}/ie55/drive_c/windows/system32/*.wav
%{_installdir}/ie55/drive_c/windows/system32/*.crl
%{_installdir}/ie55/drive_c/windows/system32/*.drv
%dir %{_installdir}/ie55/drive_c/windows/temp

%files ie6
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ie6
%{_desktopdir}/ie6.desktop
%{_installdir}/ie6/*.reg
%dir %{_installdir}/ie6
%dir %{_installdir}/ie6/dosdevices
%{_installdir}/ie6/dosdevices/*:
%dir %{_installdir}/ie6/drive_c
%dir "%{_installdir}/ie6/drive_c/Program Files"
%dir "%{_installdir}/ie6/drive_c/Program Files/Common Files"
%dir "%{_installdir}/ie6/drive_c/Program Files/Internet Explorer"
"%{_installdir}/ie6/drive_c/Program Files/Internet Explorer/iexplore.exe"
%dir %{_installdir}/ie6/drive_c/windows
%attr(755,root,root) %{_installdir}/ie6/drive_c/windows/*.exe
%{_installdir}/ie6/drive_c/windows/*.ini
%dir %{_installdir}/ie6/drive_c/windows/command
%attr(755,root,root) %{_installdir}/ie6/drive_c/windows/command/start.exe
%dir %{_installdir}/ie6/drive_c/windows/fonts
%{_installdir}/ie6/drive_c/windows/fonts/*.ttf
%dir %{_installdir}/ie6/drive_c/windows/help
%{_installdir}/ie6/drive_c/windows/help/*.hlp
%dir %{_installdir}/ie6/drive_c/windows/inf
%{_installdir}/ie6/drive_c/windows/inf/*.inf
%dir %{_installdir}/ie6/drive_c/windows/options
%dir %{_installdir}/ie6/drive_c/windows/options/cabs
%{_installdir}/ie6/drive_c/windows/options/cabs/*.dll
%dir %attr(770,root,ies4linux) %{_installdir}/ie6/drive_c/windows/profiles
%dir "%{_installdir}/ie6/drive_c/windows/profiles/All Users"
%dir "%{_installdir}/ie6/drive_c/windows/profiles/All Users/Application Data"
%dir "%{_installdir}/ie6/drive_c/windows/profiles/All Users/Desktop"
%dir "%{_installdir}/ie6/drive_c/windows/profiles/All Users/Documents"
%dir "%{_installdir}/ie6/drive_c/windows/profiles/All Users/Favorites"
%dir "%{_installdir}/ie6/drive_c/windows/profiles/All Users/Start Menu"
%dir "%{_installdir}/ie6/drive_c/windows/profiles/All Users/Start Menu/Programs"
%dir "%{_installdir}/ie6/drive_c/windows/profiles/All Users/Start Menu/Programs/StartUp"
%dir "%{_installdir}/ie6/drive_c/windows/profiles/All Users/Templates"
%{_installdir}/ie6/drive_c/windows/system
%dir %{_installdir}/ie6/drive_c/windows/system32
%dir %{_installdir}/ie6/drive_c/windows/system32/Macromed
%dir %{_installdir}/ie6/drive_c/windows/system32/Macromed/Flash
%{_installdir}/ie6/drive_c/windows/system32/Macromed/Flash/*.ocx
%attr(755,root,root) %{_installdir}/ie6/drive_c/windows/system32/Macromed/Flash/*.exe
%dir %{_installdir}/ie6/drive_c/windows/system32/drivers
%dir %{_installdir}/ie6/drive_c/windows/system32/sfp
%dir %{_installdir}/ie6/drive_c/windows/system32/sfp/ie
%{_installdir}/ie6/drive_c/windows/system32/sfp/ie/vgx.cat
%attr(755,root,root) %{_installdir}/ie6/drive_c/windows/system32/*.exe
%{_installdir}/ie6/drive_c/windows/system32/*.dll
%{_installdir}/ie6/drive_c/windows/system32/*.ocx
%{_installdir}/ie6/drive_c/windows/system32/*.cat
%{_installdir}/ie6/drive_c/windows/system32/*.msc
%{_installdir}/ie6/drive_c/windows/system32/*.nls
%{_installdir}/ie6/drive_c/windows/system32/*.inf
%{_installdir}/ie6/drive_c/windows/system32/*.vxd
%{_installdir}/ie6/drive_c/windows/system32/*.txt
%{_installdir}/ie6/drive_c/windows/system32/*.cnv
%{_installdir}/ie6/drive_c/windows/system32/*.mof
%{_installdir}/ie6/drive_c/windows/system32/*.htm
%{_installdir}/ie6/drive_c/windows/system32/*.acm
%{_installdir}/ie6/drive_c/windows/system32/*.cpl
%{_installdir}/ie6/drive_c/windows/system32/*.gif
%{_installdir}/ie6/drive_c/windows/system32/*.tlb
%{_installdir}/ie6/drive_c/windows/system32/*.stf
%{_installdir}/ie6/drive_c/windows/system32/*.bat
%{_installdir}/ie6/drive_c/windows/system32/*.pdr
%{_installdir}/ie6/drive_c/windows/system32/*.rat
%{_installdir}/ie6/drive_c/windows/system32/*.icm
%{_installdir}/ie6/drive_c/windows/system32/*.wav
%{_installdir}/ie6/drive_c/windows/system32/*.crl
%{_installdir}/ie6/drive_c/windows/system32/*.drv
%dir %{_installdir}/ie6/drive_c/windows/temp

%if %{with ie7}
%files ie7
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ie7
%{_desktopdir}/ie7.desktop
%{_installdir}/ie7/*.reg
%dir %{_installdir}/ie7
%dir %{_installdir}/ie7/dosdevices
%{_installdir}/ie7/dosdevices/*:
%dir %{_installdir}/ie7/drive_c
%dir "%{_installdir}/ie7/drive_c/Program Files"
%dir "%{_installdir}/ie7/drive_c/Program Files/Common Files"
%dir "%{_installdir}/ie7/drive_c/Program Files/Internet Explorer"
"%{_installdir}/ie7/drive_c/Program Files/Internet Explorer/iexplore.exe"
%dir %{_installdir}/ie7/drive_c/windows
%attr(755,root,root) %{_installdir}/ie7/drive_c/windows/*.exe
%{_installdir}/ie7/drive_c/windows/*.ini
%dir %{_installdir}/ie7/drive_c/windows/command
%attr(755,root,root) %{_installdir}/ie7/drive_c/windows/command/start.exe
%dir %{_installdir}/ie7/drive_c/windows/fonts
%{_installdir}/ie7/drive_c/windows/fonts/*.ttf
%dir %{_installdir}/ie7/drive_c/windows/help
%{_installdir}/ie7/drive_c/windows/help/*.hlp
%dir %{_installdir}/ie7/drive_c/windows/inf
%{_installdir}/ie7/drive_c/windows/inf/*.inf
%dir %{_installdir}/ie7/drive_c/windows/options
%dir %{_installdir}/ie7/drive_c/windows/options/cabs
%{_installdir}/ie7/drive_c/windows/options/cabs/*.dll
%dir %attr(770,root,ies4linux) %{_installdir}/ie7/drive_c/windows/profiles
%dir "%{_installdir}/ie7/drive_c/windows/profiles/All Users"
%dir "%{_installdir}/ie7/drive_c/windows/profiles/All Users/Application Data"
%dir "%{_installdir}/ie7/drive_c/windows/profiles/All Users/Desktop"
%dir "%{_installdir}/ie7/drive_c/windows/profiles/All Users/Documents"
%dir "%{_installdir}/ie7/drive_c/windows/profiles/All Users/Favorites"
%dir "%{_installdir}/ie7/drive_c/windows/profiles/All Users/Start Menu"
%dir "%{_installdir}/ie7/drive_c/windows/profiles/All Users/Start Menu/Programs"
%dir "%{_installdir}/ie7/drive_c/windows/profiles/All Users/Start Menu/Programs/StartUp"
%dir "%{_installdir}/ie7/drive_c/windows/profiles/All Users/Templates"
%{_installdir}/ie7/drive_c/windows/system
%dir %{_installdir}/ie7/drive_c/windows/system32
%dir %{_installdir}/ie7/drive_c/windows/system32/Macromed
%dir %{_installdir}/ie7/drive_c/windows/system32/Macromed/Flash
%{_installdir}/ie7/drive_c/windows/system32/Macromed/Flash/*.ocx
%attr(755,root,root) %{_installdir}/ie7/drive_c/windows/system32/Macromed/Flash/*.exe
%dir %{_installdir}/ie7/drive_c/windows/system32/drivers
%dir %{_installdir}/ie7/drive_c/windows/system32/sfp
%dir %{_installdir}/ie7/drive_c/windows/system32/sfp/ie
%{_installdir}/ie7/drive_c/windows/system32/sfp/ie/vgx.cat
%attr(755,root,root) %{_installdir}/ie7/drive_c/windows/system32/*.exe
%{_installdir}/ie7/drive_c/windows/system32/*.dll
%{_installdir}/ie7/drive_c/windows/system32/*.ocx
%{_installdir}/ie7/drive_c/windows/system32/*.cat
%{_installdir}/ie7/drive_c/windows/system32/*.msc
%{_installdir}/ie7/drive_c/windows/system32/*.nls
%{_installdir}/ie7/drive_c/windows/system32/*.inf
%{_installdir}/ie7/drive_c/windows/system32/*.vxd
%{_installdir}/ie7/drive_c/windows/system32/*.txt
%{_installdir}/ie7/drive_c/windows/system32/*.cnv
%{_installdir}/ie7/drive_c/windows/system32/*.mof
%{_installdir}/ie7/drive_c/windows/system32/*.htm
%{_installdir}/ie7/drive_c/windows/system32/*.acm
%{_installdir}/ie7/drive_c/windows/system32/*.cpl
%{_installdir}/ie7/drive_c/windows/system32/*.gif
%{_installdir}/ie7/drive_c/windows/system32/*.tlb
%{_installdir}/ie7/drive_c/windows/system32/*.stf
%{_installdir}/ie7/drive_c/windows/system32/*.bat
%{_installdir}/ie7/drive_c/windows/system32/*.pdr
%{_installdir}/ie7/drive_c/windows/system32/*.rat
%{_installdir}/ie7/drive_c/windows/system32/*.icm
%{_installdir}/ie7/drive_c/windows/system32/*.wav
%{_installdir}/ie7/drive_c/windows/system32/*.crl
%{_installdir}/ie7/drive_c/windows/system32/*.drv
%dir %{_installdir}/ie7/drive_c/windows/temp
%endif
