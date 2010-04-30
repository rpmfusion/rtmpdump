Name:		rtmpdump
Version:	2.2d
Release:	1%{?dist}
Summary:	Toolkit for RTMP streams

Group:		Applications/Internet
License:	GPLv2+
# Note that librtmp is actually LGPLv2, so if you package that separately
# (for which you'd probably want to make it a dynamic library) you should
# label its licence correctly. But the _tools_ are GPLv2.
URL:		http://rtmpdump.mplayerhq.hu/
Source0:	http://rtmpdump.mplayerhq.hu/download/rtmpdump-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gnutls-devel zlib-devel

%description
rtmpdump is a toolkit for RTMP streams. All forms of RTMP are supported,
including rtmp://, rtmpt://, rtmpe://, rtmpte://, and rtmps://. 

%prep
%setup -q

%build
make CRYPTO=GNUTLS OPT="$RPM_OPT_FLAGS" progs


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for FILE in rtmpdump rtmpgw rtmpsrv rtmpsuck; do
    install -m 0755 $FILE $RPM_BUILD_ROOT%{_bindir}
done
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 0644 rtmpdump.1 $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
install -m 0644 rtmpgw.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/rtmpdump
%{_bindir}/rtmpsrv
%{_bindir}/rtmpgw
%{_bindir}/rtmpsuck
%{_mandir}/man1/rtmpdump.1.*
%{_mandir}/man8/rtmpgw.8.*

%doc COPYING ChangeLog README



%changelog
* Fri Apr 30 2010 David Woodhouse <dwmw2@infradead.org> 2.2d-1
- Update to 2.2d

* Tue Apr 20 2010 David Woodhouse <dwmw2@infradead.org> 2.2c-2
- Link with libgcrypt explicitly since we call it directly

* Mon Apr 19 2010 David Woodhouse <dwmw2@infradead.org> 2.2c-1
- Initial package
