Summary:	BTTV tuners plugin for gkrellm
Summary(pl):	Plugin gkrellm do radio BTTV
Summary(pt_BR):	Plugin gkrellm para o BTTV radio
Name:		gkrellm-radio
Version:	2.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gkrellm.luon.net/files/%{name}-%{version}.tar.gz
URL:		http://gkrellm.luon.net/gkrellm-radio.phtml
BuildRequires:	gkrellm-devel >= 2.0.0
Requires:	gkrellm >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
	OPT="%{rpmcflags}" \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm2

install radio.so $RPM_BUILD_ROOT%{_libdir}/gkrellm2

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/gkrellm2/radio.so
