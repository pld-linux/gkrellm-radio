Summary:	BTTV tuners plugin for gkrellm
Summary(pl):	Plugin gkrellm do radio BTTV
Summary(pt_BR):	Plugin gkrellm para o BTTV radio
Name:		gkrellm-radio
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.cs.auc.dk/~larsch/gkrellm-radio/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
URL:		http://www.cs.auc.dk/~larsch/gkrellm-radio/
BuildRequires:	gkrellm-devel
Requires:	gkrellm >= 1.0.2
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
%setup -q
%patch0 -p1

%build
%{__make} \
	OPT="%{rpmcflags}" \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gkrellm

install radio.so $RPM_BUILD_ROOT%{_libdir}/gkrellm

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/gkrellm/radio.so
