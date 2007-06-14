#
# TODO
# - few install errors (ignored):
#   ln: creating symbolic link `/usr/bin/ie55': Permission denied
#   ln: creating symbolic link `/usr/bin/ie5': Permission denied
# - sources downloaded via install script as NoSourceXX
# - move profiles to $HOME directory
# - License tag specifies package license? then it should not be GPL
#
# This spec file is released under the GNU General Public License version 2.0
# (http://www.gnu.org/licenses/gpl.txt).
#
# NOTE: Releasing this spec file under the GPL does not alter the licensing
# of Internet Explorer itself. Satisfying the terms of Internet Explorer's
# license remains the user's responsibility.

# NOTE: For IE7 you should have normaliz.dll and inetcplc.dll from your
#	WindowsXP SP2 installation!

%bcond_with	ie7	build ie7 package

%bcond_with	all_locales	# build for all locales
%bcond_without	locale_en_US	# build without en_US version
%bcond_with	locale_ar	# build with ar version
%bcond_with	locale_cs	# build with cs version
%bcond_with	locale_da	# build with da version
%bcond_with	locale_de	# build with de version
%bcond_with	locale_el	# build with el version
%bcond_with	locale_es	# build with es version
%bcond_with	locale_fi	# build with fi version
%bcond_with	locale_fr	# build with fr version
%bcond_with	locale_he	# build with he version
%bcond_with	locale_hu	# build with hu version
%bcond_with	locale_it	# build with it version
%bcond_with	locale_ja	# build with ja version
%bcond_with	locale_ko	# build with ko version
%bcond_with	locale_nl	# build with nl version
%bcond_with	locale_no	# build with no version
%bcond_with	locale_pl	# build with pl version
%bcond_with	locale_pt	# build with pt version
%bcond_with	locale_pt_BR	# build with pt_BR version
%bcond_with	locale_ru	# build with ru version
%bcond_with	locale_sv	# build with sv version
%bcond_with	locale_tr	# build with tr version
%bcond_with	locale_zh_CN	# build with zh_CN version
%bcond_with	locale_zh_TW	# build with zh_TW version

Summary:	Run IE 7, 6, 5.5 and 5 on Linux with Wine
Summary(pl.UTF-8):	Uruchamianie IE 7, 6, 5.5 i 5 pod Linuksem przy użyciu Wine
Name:		ies4linux
Version:	2.0.5
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://www.tatanka.com.br/ies4linux/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	a2983360de355d1a407eb20077c39792
Source1:	%{name}.ie.sh
%if %{with ie7}
%if %{with locale_en_US}
Source2:	http://download.microsoft.com/download/3/8/8/38889DC1-848C-4BF2-8335-86C573AD86D9/IE7-WindowsXP-x86-enu.exe
NoSource:	2
%endif
Source3:	normaliz.dll
NoSource:	3
Source4:	inetcplc.dll
NoSource:	4
%if %{with locale_pl}
Source5:	http://download.microsoft.com/download/6/a/0/6a01b4fa-66e5-4447-8f36-9330a8725ecd/IE7-WindowsXP-x86-plk.exe
NoSource:	5
%endif
%endif
Patch0:		%{name}-destdir.patch
Patch1:		%{name}.patch
URL:		http://www.tatanka.com.br/ies4linux/page/Main_Page
#BuildRequires:	bash
BuildRequires:	cabextract
BuildRequires:	wine
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
#Requires:	dcom98
Requires:	wine >= 1:0.9.37
#Requires:	wine-programs
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_installdir	%{_datadir}/ies4linux

%if %{with all_locales}
%define with_locale_ar 1
%define with_locale_cs 1
%define with_locale_da 1
%define with_locale_de 1
%define with_locale_el 1
%define with_locale_en_US 1
%define with_locale_es 1
%define with_locale_fi 1
%define with_locale_fr 1
%define with_locale_he 1
%define with_locale_hu 1
%define with_locale_it 1
%define with_locale_ja 1
%define with_locale_ko 1
%define with_locale_nl 1
%define with_locale_no 1
%define with_locale_pl 1
%define with_locale_pt 1
%define with_locale_pt_BR 1
%define with_locale_ru 1
%define with_locale_sv 1
%define with_locale_tr 1
%define with_locale_zh_CN 1
%define with_locale_zh_TW 1
%endif

%define loc_en_US	en-US
%if %{without locale_en_US}
%define loc_en_US	""
%endif

%define loc_pt_BR 	""
%if %{with locale_pt_BR}
%define loc_pt_BR 	pt-BR
%endif

%define loc_de	""
%if %{with locale_de}
%define loc_de	de
%endif

%define loc_fr	""
%if %{with locale_fr}
%define loc_fr	fr
%endif

%define loc_es	""
%if %{with locale_es}
%define loc_es	es
%endif

%define loc_it	""
%if %{with locale_it}
%define loc_it	it
%endif

%define loc_nl	""
%if %{with locale_nl}
%define loc_nl	nl
%endif

%define loc_sv	""
%if %{with locale_sv}
%define loc_sv	sv
%endif

%define loc_ja	""
%if %{with locale_ja}
%define loc_ja	ja
%endif

%define loc_ko	""
%if %{with locale_ko}
%define loc_ko	ko
%endif

%define loc_no	""
%if %{with locale_no}
%define loc_no	no
%endif

%define loc_da	""
%if %{with locale_da}
%define loc_da	da
%endif

%define loc_cn	""
%if %{with locale_zh_CN}
%define loc_cn	cn
%endif

%define loc_tw	""
%if %{with locale_zh_TW}
%define loc_tw	tw
%endif

%define loc_fi	""
%if %{with locale_fi}
%define loc_fi	fi
%endif

%define loc_pl	""
%if %{with locale_pl}
%define loc_pl	pl
%endif

%define loc_hu	""
%if %{with locale_hu}
%define loc_hu	hu
%endif

%define loc_ar	""
%if %{with locale_ar}
%define loc_ar	ar
%endif

%define loc_he	""
%if %{with locale_he}
%define loc_he	he
%endif

%define loc_cs	""
%if %{with locale_cs}
%define loc_cs	cs
%endif

%define loc_pt	""
%if %{with locale_pt}
%define loc_pt	pt
%endif

%define loc_ru	""
%if %{with locale_ru}
%define loc_ru	ru
%endif

%define loc_el	""
%if %{with locale_el}
%define loc_el	el
%endif

%define loc_tr	""
%if %{with locale_tr}
%define loc_tr	tr
%endif

%define locales %{loc_en_US} %{loc_pt_BR} %{loc_de} %{loc_fr} %{loc_es} %{loc_it} %{loc_nl} %{loc_sv} %{loc_ja} %{loc_ko} %{loc_no} %{loc_da} %{loc_cn} %{loc_tw} %{loc_fi} %{loc_pl} %{loc_hu} %{loc_ar} %{loc_he} %{loc_cs} %{loc_pt} %{loc_ru} %{loc_el} %{loc_tr}

%description
IEs4Linux is the simpler way to have Microsoft Internet Explorer
running on Linux.

%description -l pl.UTF-8
IEs4Linux to prostszy sposób na uruchamianie Microsoft Internet
Explorera pod Linuksem.

%package ie5-en_US
Summary:	Internet Explorer 5
Summary(pl.UTF-8):	Internet Explorer 5
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}
Obsoletes:	ies4linux-ie5

%description ie5-en_US
Internet Explorer 5.

%description ie5-en_US -l pl.UTF-8
Internet Explorer 5.

%package ie55-en_US
Summary:	Internet Explorer 5.5
Summary(pl.UTF-8):	Internet Explorer 5.5
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}
Obsoletes:	ies4linux-ie5

%description ie55-en_US
Internet Explorer 5.5.

%description ie55-en_US -l pl.UTF-8
Internet Explorer 5.5.

%package ie6-ar
Summary:	Internet Explorer 6 Arabic edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji arabskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-ar
Internet Explorer 6 Arabic edition.

%description ie6-ar -l pl.UTF-8
Internet Explorer 6 w wersji arabskiej.

%package ie6-cs
Summary:	Internet Explorer 6 Czech edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji czeskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-cs
Internet Explorer 6 Czech edition.

%description ie6-cs -l pl.UTF-8
Internet Explorer 6 w wersji czeskiej.

%package ie6-da
Summary:	Internet Explorer 6 Danish edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji duńskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-da
Internet Explorer 6 Danish edition.

%description ie6-da -l pl.UTF-8
Internet Explorer 6 w wersji duńskiej.

%package ie6-de
Summary:	Internet Explorer 6 German edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji niemieckiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-de
Internet Explorer 6 German edition.

%description ie6-de -l pl.UTF-8
Internet Explorer 6 w wersji niemieckiej.

%package ie6-el
Summary:	Internet Explorer 6 Greek edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji greckiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-el
Internet Explorer 6 Greek edition.

%description ie6-el -l pl.UTF-8
Internet Explorer 6 w wersji greckiej.

%package ie6-en_US
Summary:	Internet Explorer 6 US English edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji angielskiej (USA)
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}
Obsoletes:	ies4linux-ie55

%description ie6-en_US
Internet Explorer 6 US English edition.

%description ie6-en_US -l pl.UTF-8
Internet Explorer 6 w wersji angielskiej (USA).

%package ie6-es
Summary:	Internet Explorer 6 Spanish edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji hiszpańskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-es
Internet Explorer 6 Spanish edition.

%description ie6-es -l pl.UTF-8
Internet Explorer 6 w wersji hiszpańskiej.

%package ie6-fi
Summary:	Internet Explorer 6 Finnish edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji fińskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-fi
Internet Explorer 6 Finnish edition.

%description ie6-fi -l pl.UTF-8
Internet Explorer 6 w wersji fińskiej.

%package ie6-fr
Summary:	Internet Explorer 6 French edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji francuskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-fr
Internet Explorer 6 French edition.

%description ie6-fr -l pl.UTF-8
Internet Explorer 6 w wersji francuskiej.

%package ie6-he
Summary:	Internet Explorer 6 Hebrew edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji hebrajskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-he
Internet Explorer 6 Hebrew edition.

%description ie6-he -l pl.UTF-8
Internet Explorer 6 w wersji hebrajskiej.

%package ie6-hu
Summary:	Internet Explorer 6 Hungarian edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji węgierskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-hu
Internet Explorer 6 Hungarian edition.

%description ie6-hu -l pl.UTF-8
Internet Explorer 6 w wersji węgierskiej.

%package ie6-it
Summary:	Internet Explorer 6 Italian edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji włoskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-it
Internet Explorer 6 Italian edition.

%description ie6-it -l pl.UTF-8
Internet Explorer 6 w wersji włoskiej.

%package ie6-ja
Summary:	Internet Explorer 6 Japanese edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji japońskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-ja
Internet Explorer 6 Japanese edition.

%description ie6-ja -l pl.UTF-8
Internet Explorer 6 w wersji japońskiej.

%package ie6-ko
Summary:	Internet Explorer 6 Korean edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji koreańskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-ko
Internet Explorer 6 Korean edition.

%description ie6-ko -l pl.UTF-8
Internet Explorer 6 w wersji koreańskiej.

%package ie6-nl
Summary:	Internet Explorer 6 Dutch edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji holenderskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-nl
Internet Explorer 6 Dutch edition.

%description ie6-nl -l pl.UTF-8
Internet Explorer 6 w wersji holenderskiej.

%package ie6-no
Summary:	Internet Explorer 6 Norwegian edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji norweskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-no
Internet Explorer 6 Norwegian edition.

%description ie6-no -l pl.UTF-8
Internet Explorer 6 w wersji norweskiej.

%package ie6-pl
Summary:	Internet Explorer 6 Polish edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji polskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-pl
Internet Explorer 6 Polish edition.

%description ie6-pl -l pl.UTF-8
Internet Explorer 6 w wersji polskiej.

%package ie6-pt
Summary:	Internet Explorer 6 Portuguese edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji portugalskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-pt
Internet Explorer 6 Portuguese edition.

%description ie6-pt -l pl.UTF-8
Internet Explorer 6 w wersji portugalskiej.

%package ie6-pt_BR
Summary:	Internet Explorer 6 Brazilian Portuguese edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji portugalskiej (dla Brazylii)
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-pt_BR
Internet Explorer 6 Brazilian Portuguese edition.

%description ie6-pt_BR -l pl.UTF-8
Internet Explorer 6 w wersji portugalskiej (dla Brazylii).

%package ie6-ru
Summary:	Internet Explorer 6 Russian edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji rosyjskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-ru
Internet Explorer 6 Russian edition.

%description ie6-ru -l pl.UTF-8
Internet Explorer 6 w wersji rosyjskiej.

%package ie6-sv
Summary:	Internet Explorer 6 Swedish edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji szwedzkiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-sv
Internet Explorer 6 Swedish edition.

%description ie6-sv -l pl.UTF-8
Internet Explorer 6 w wersji szwedzkiej.

%package ie6-tr
Summary:	Internet Explorer 6 Turkish edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji tureckiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-tr
Internet Explorer 6 Turkish edition.

%description ie6-tr -l pl.UTF-8
Internet Explorer 6 w wersji tureckiej.

%package ie6-zh_CN
Summary:	Internet Explorer 6 Chinese (China) edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji chińskiej (dla Chin)
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-zh_CN
Internet Explorer 6 Chinese (China) edition.

%description ie6-zh_CN -l pl.UTF-8
Internet Explorer 6 w wersji chińskiej (dla Chin).

%package ie6-zh_TW
Summary:	Internet Explorer 6 Chinese (Taiwan) edition
Summary(pl.UTF-8):	Internet Explorer 6 w wersji chińskiej (dla Tajwanu)
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie6-zh_TW
Internet Explorer 6 Chinese (Taiwan) edition.

%description ie6-zh_TW -l pl.UTF-8
Internet Explorer 6 w wersji chińskiej (dla Tajwanu).

%package ie7-en_US
Summary:	Internet Explorer 7 US English edition
Summary(pl.UTF-8):	Internet Explorer 7 w wersji angielskiej (USA)
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}
Obsoletes:	ies4linux-ie7

%description ie7-en_US
Internet Explorer 7 US English edition.

%description ie7-en_US -l pl.UTF-8
Internet Explorer 7 w wersji angielskiej (USA).

%package ie7-pl
Summary:	Internet Explorer 7 Polish edition
Summary(pl.UTF-8):	Internet Explorer 7 w wersji polskiej
Group:		X11/Applications/Networking
Requires:	ies4linux = %{version}-%{release}

%description ie7-pl
Internet Explorer 7 Polish edition.

%description ie7-pl -l pl.UTF-8
Internet Explorer 7 w wersji polskiej.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

#
# IE 7
#
%if %{with ie7}

%if %{with locale_en_US}
mkdir -p ie7/en-US
cd ie7/en-US
cabextract %{SOURCE2}
cd -
%endif

%if %{with locale_pl}
mkdir -p ie7/pl
cd ie7/pl
cabextract %{SOURCE5}
cd -
%endif

cp %{SOURCE3} ie7
cp %{SOURCE4} ie7
%endif


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_bindir},%{_pixmapsdir}}

cp %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/ies4linux

gen_desktopfile()
{
	LOCALE=$1
	VERSION=$2
	VER=`echo $VERSION | sed 's:\.0::; s:\.::'`
	cat > $RPM_BUILD_ROOT%{_desktopdir}/ie$VER-$LOCALE.desktop << EOF
[Desktop Entry]
Name=Internet Explorer $VERSION ($LOCALE)
Name[pl]=Internet Explorer $VERSION ($LOCALE)
GenericName=Web Browser
GenericName[pl]=Przeglądarka WWW
Comment=Internet Explorer $VERSION ($LOCALE)
Comment[pl]=Internet Explorer $VERSION ($LOCALE)
Type=Application
Exec=ie$VER-$LOCALE
Icon=%{_pixmapsdir}/ies4linux.svg
Categories=Network;WebBrowser;
Encoding=UTF-8
# vi: encoding=utf-8
EOF
}

cat > add_file_to_list << 'EOF'
#!/bin/sh

	LOCALE="$1"
	VERSION="$2"
	FULLFILE="$3"
	PKGFILE=`echo "$FULLFILE" | sed "s:$RPM_BUILD_ROOT::"`
	LIST=ie$VERSION-$LOCALE.files

	if [ -d "$FULLFILE" ]; then
		echo "%%dir \"$PKGFILE\"" >> $LIST
	else
		EXE=`basename "$PKGFILE" | sed -r 's:.+.(exe):\1:g'`
		if [ "$EXE" = "EXE" ]; then
			echo "%%attr(755,root,root) \"$PKGFILE\"" >> $LIST
		else
			echo "\"$PKGFILE\"" >> $LIST
		fi
	fi
EOF
chmod +x add_file_to_list

gen_filelist()
{
	#
	# It seems that some files are written in background
	# so we have to wait for them to be available.
	#
	sleep 5s

	LOCALE="$1"
	VERSION="$2"
	LIST=ie$VERSION-$LOCALE.files
	echo "%defattr(644,root,root,755)" > $LIST

	find $RPM_BUILD_ROOT%{_installdir}/$LOCALE/ie$VERSION -exec ./add_file_to_list $LOCALE $VERSION '{}' ';'

	echo "%%attr(755,root,root) %{_bindir}/ie$VERSION-$LOCALE" >> $LIST
	[ "$LOCALE" = "en-US" ] && echo "%%attr(755,root,root) %{_bindir}/ie$VERSION" >> $LIST
	echo "%{_desktopdir}/ie$VERSION-$LOCALE.desktop" >> $LIST
	echo "%%dir %{_installdir}/$LOCALE" >> $LIST
}

# IE 5, 5.5 built only with en_US locale
# IE 7 needs more sources for other locales
for LOCALE in %{locales}; do
	[ "$LOCALE" = "" ] && continue
	OPTS=""
	[ "xen-US" = "x$LOCALE" ] && OPTS="--install-ie55 --install-ie5"

	bash ./ies4linux \
		$OPTS \
		--basedir %{_installdir}/$LOCALE \
		--bindir %{_bindir} \
		--destdir $RPM_BUILD_ROOT \
		--downloaddir %{_sourcedir} \
		--locale $LOCALE \
		--install-flash

	if [ ! -d $RPM_BUILD_ROOT%{_installdir}/profiles ]; then
		install -d $RPM_BUILD_ROOT%{_installdir}/profiles
		cp -a "$RPM_BUILD_ROOT%{_installdir}/$LOCALE/ie6/drive_c/windows/profiles/All Users" \
			$RPM_BUILD_ROOT%{_installdir}/profiles
	fi
	[ ! -f $RPM_BUILD_ROOT%{_pixmapsdir}/ies4linux.svg ] && \
		cp $RPM_BUILD_ROOT%{_installdir}/$LOCALE/ies4linux.svg \
			$RPM_BUILD_ROOT%{_pixmapsdir}
	rm -f $RPM_BUILD_ROOT%{_installdir}/$LOCALE/ies4linux.svg
	rm -rf $RPM_BUILD_ROOT%{_installdir}/$LOCALE/ie{5,55,6}/drive_c/windows/profiles
	rm -f $RPM_BUILD_ROOT%{_installdir}/$LOCALE/ie{5,55,6}/.firstrun

	#
	# Shell scripts
	#
	rm -rf $RPM_BUILD_ROOT%{_installdir}/$LOCALE/bin
	ln -sf ies4linux $RPM_BUILD_ROOT%{_bindir}/ie6-$LOCALE
	gen_desktopfile $LOCALE 6.0
	ln -sf %{_installdir}/profiles $RPM_BUILD_ROOT%{_installdir}/$LOCALE/ie6/drive_c/windows/profiles

	if [ "$LOCALE" = "en-US" ]; then
		ln -sf ies4linux $RPM_BUILD_ROOT%{_bindir}/ie5
		ln -sf ies4linux $RPM_BUILD_ROOT%{_bindir}/ie5-en-US
		ln -sf ies4linux $RPM_BUILD_ROOT%{_bindir}/ie55
		ln -sf ies4linux $RPM_BUILD_ROOT%{_bindir}/ie55-en-US
		ln -sf ies4linux $RPM_BUILD_ROOT%{_bindir}/ie6
		gen_desktopfile $LOCALE 5
		gen_desktopfile $LOCALE 5.5
		ln -sf %{_installdir}/profiles $RPM_BUILD_ROOT%{_installdir}/$LOCALE/ie5/drive_c/windows/profiles
		ln -sf %{_installdir}/profiles $RPM_BUILD_ROOT%{_installdir}/$LOCALE/ie55/drive_c/windows/profiles
		gen_filelist $LOCALE 5
		gen_filelist $LOCALE 55
	fi

	%if %{with ie7}
	if [ "$LOCALE" = "en-US" ] || [ "$LOCALE" = "pl" ]; then
		[ "$LOCALE" = "en-US" ] && ln -sf ies4linux $RPM_BUILD_ROOT%{_bindir}/ie7
		ln -sf ies4linux $RPM_BUILD_ROOT%{_bindir}/ie7-$LOCALE
		gen_desktopfile $LOCALE 7

		cp -a $RPM_BUILD_ROOT%{_installdir}/$LOCALE/ie6 $RPM_BUILD_ROOT%{_installdir}/$LOCALE/ie7
		cp ie7/$LOCALE/{wininet,iertutil,shlwapi,urlmon,jscript,vbscript,mshtml,mshtmled,mshtmler,advpack}.dll \
			ie7/$LOCALE/inetcpl.cpl ie7/inetcplc.dll ie7/normaliz.dll \
			$RPM_BUILD_ROOT%{_installdir}/$LOCALE/ie7/drive_c/windows/system

		cat $RPM_BUILD_ROOT%{_installdir}/$LOCALE/ie6/user.reg | \
			sed 's:"Version"="win98":"Version"="win98"\n\n[Software\\Wine\\AppDefaults\\iexplore.exe] 1161336541\n"Version"="winxp"\n:' \
			> $RPM_BUILD_ROOT%{_installdir}/$LOCALE/ie7/user.reg

		gen_filelist $LOCALE 7
	fi
	%endif

	gen_filelist $LOCALE 6
done

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
%{_pixmapsdir}/%{name}.svg
%dir %attr(770,root,ies4linux) %{_installdir}/profiles
%dir "%{_installdir}/profiles/All Users"
%dir "%{_installdir}/profiles/All Users/Application Data"
%dir "%{_installdir}/profiles/All Users/Desktop"
%dir "%{_installdir}/profiles/All Users/Documents"
%dir "%{_installdir}/profiles/All Users/Favorites"
%dir "%{_installdir}/profiles/All Users/Start Menu"
%dir "%{_installdir}/profiles/All Users/Start Menu/Programs"
%dir "%{_installdir}/profiles/All Users/Start Menu/Programs/StartUp"
%dir "%{_installdir}/profiles/All Users/Templates"

%if %{with locale_en_US}
%files ie5-en_US -f ie5-en-US.files
%defattr(644,root,root,755)
%files ie55-en_US -f ie55-en-US.files
%defattr(644,root,root,755)
%files ie6-en_US -f ie6-en-US.files
%defattr(644,root,root,755)
%endif

%if %{with locale_ar}
%files ie6-ar -f ie6-ar.files
%defattr(644,root,root,755)
%endif

%if %{with locale_cs}
%files ie6-cs -f ie6-cs.files
%defattr(644,root,root,755)
%endif

%if %{with locale_da}
%files ie6-da -f ie6-da.files
%defattr(644,root,root,755)
%endif

%if %{with locale_de}
%files ie6-de -f ie6-de.files
%defattr(644,root,root,755)
%endif

%if %{with locale_el}
%files ie6-el -f ie6-el.files
%defattr(644,root,root,755)
%endif

%if %{with locale_es}
%files ie6-es -f ie6-es.files
%defattr(644,root,root,755)
%endif

%if %{with locale_fi}
%files ie6-fi -f ie6-fi.files
%defattr(644,root,root,755)
%endif

%if %{with locale_fr}
%files ie6-fr -f ie6-fr.files
%defattr(644,root,root,755)
%endif

%if %{with locale_he}
%files ie6-he -f ie6-he.files
%defattr(644,root,root,755)
%endif

%if %{with locale_hu}
%files ie6-hu -f ie6-hu.files
%defattr(644,root,root,755)
%endif

%if %{with locale_it}
%files ie6-it -f ie6-it.files
%defattr(644,root,root,755)
%endif

%if %{with locale_ja}
%files ie6-ja -f ie6-ja.files
%defattr(644,root,root,755)
%endif

%if %{with locale_ko}
%files ie6-ko -f ie6-ko.files
%defattr(644,root,root,755)
%endif

%if %{with locale_nl}
%files ie6-nl -f ie6-nl.files
%defattr(644,root,root,755)
%endif

%if %{with locale_no}
%files ie6-no -f ie6-no.files
%defattr(644,root,root,755)
%endif

%if %{with locale_pl}
%files ie6-pl -f ie6-pl.files
%defattr(644,root,root,755)
%endif

%if %{with locale_pt}
%files ie6-pt -f ie6-pt.files
%defattr(644,root,root,755)
%endif

%if %{with locale_pt_BR}
%files ie6-pt_BR -f ie6-pt-BR.files
%defattr(644,root,root,755)
%endif

%if %{with locale_ru}
%files ie6-ru -f ie6-ru.files
%defattr(644,root,root,755)
%endif

%if %{with locale_sv}
%files ie6-sv -f ie6-sv.files
%defattr(644,root,root,755)
%endif

%if %{with locale_tr}
%files ie6-tr -f ie6-tr.files
%defattr(644,root,root,755)
%endif

%if %{with locale_zh_CN}
%files ie6-zh_CN -f ie6-cn.files
%defattr(644,root,root,755)
%endif

%if %{with locale_zh_TW}
%files ie6-zh_TW -f ie6-tw.files
%defattr(644,root,root,755)
%endif

%if %{with ie7}
%if %{with locale_en_US}
%files ie7-en_US -f ie7-en-US.files
%defattr(644,root,root,755)
%endif
%if %{with locale_pl}
%files ie7-pl -f ie7-pl.files
%defattr(644,root,root,755)
%endif
%endif
