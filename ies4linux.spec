# This spec file is released under the GNU General Public License version 2.0
# (http://www.gnu.org/licenses/gpl.txt).
#
# NOTE: Releasing this spec file under the GPL does not alter the licensing
# of Internet Explorer itself. Satisfying the terms of Internet Explorer's
# license remains the user's responsibility.

%define	_wine_cdrive	%{_datadir}/wine
%define	_wine_system	%{_wine_cdrive}/windows/system
%define	_wine_programs	%{_wine_cdrive}/'Program Files'
%define	_installdir	%{_wine_programs}/'Internet Explorer'

%define	_beta	beta6
%define	_rel	0.1

# NOTE
# - needs $DISPLAY and wine to package!

Summary:	Run IE 6, 5.5 and 5 on Linux with Wine
Summary(pl):	Uruchamianie IE 6, 5.5 i 5 pod Linuksem przy u¿yciu Wine
Name:		ies4linux
Version:	2.0
Release:	0.%{_beta}.%{_rel}
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://www.tatanka.com.br/ies4linux/downloads/%{name}-%{version}%{_beta}.tar.gz
# Source0-md5:	f96f3826dc041b0cdee9a87227db6a75
URL:		http://www.tatanka.com.br/ies4linux/index-en.html
BuildRequires:	cabextract
BuildRequires:	wine
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
%setup -q -n %{name}-%{version}%{_beta}

%install
rm -rf $RPM_BUILD_ROOT

bash ./ies4linux \
	--install-ie6 \
	--install-ie55 \
	--install-ie5 \
	--basedir $RPM_BUILD_ROOT%{_installdir} \
	--bindir $RPM_BUILD_ROOT%{_bindir} \
	--downloaddir %{_sourcedir} \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
