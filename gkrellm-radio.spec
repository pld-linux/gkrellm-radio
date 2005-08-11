#
# Conditional build:
%bcond_without	lirc    # without LIRC support
#
Summary:	BTTV tuners plugin for gkrellm
Summary(pl):	Plugin gkrellm do radio BTTV
Summary(pt_BR):	Plugin gkrellm para o BTTV radio
Name:		gkrellm-radio
Version:	2.0.4
Release:	1.1
License:	GPL
Group:		X11/Applications
Source0:	http://gkrellm.luon.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	32dbaf2aa22c79708ed9d0635025dd94
URL:		http://gkrellm.luon.net/gkrellm-radio.phtml
BuildRequires:	gkrellm-devel >= 2.0.0
%{?with_lirc:BuildRequires:     lirc-devel}
Requires:	gkrellm >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A GKrellM plugin which allows you to control BTTV tuners from within
GKrellM.

%description -l pl
Plugin GKrellM pozwalaj±cy na sterowanie tunerami BTTV.

%description -l pt_BR
Um plugin GKrellM para controlar o BTTV radio a partir do GKrellM.

%prep
%setup -q -n %{name}

%build
%{__make} \
	%{?with_lirc:WITH_LIRC=1} \
	OPT="%{rpmcflags}" \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT

install -D radio.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/radio.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%{?with_lirc:%doc lirc.example} 
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/radio.so
