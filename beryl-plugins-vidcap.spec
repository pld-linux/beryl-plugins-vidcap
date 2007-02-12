Summary:	Beryl vidcap plugin
Summary(pl.UTF-8):	Wtyczka vidcap dla beryla
Name:		beryl-plugins-vidcap
Version:	0.1.9999.1
Release:	1
License:	GPL-like
Group:		X11
Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	b12fc4c7e8d338e2ae771da937e216e2
URL:		http://beryl-project.org/
BuildRequires:	OpenGL-devel
BuildRequires:	beryl-core-devel >= 1:%{version}
BuildRequires:	pkgconfig
BuildRequires:	seom-devel
Requires:	beryl-core >= 1:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Beryl vidcap plugin.

%description -l pl.UTF-8
Wtyczka vidcap dla beryla.

%prep
%setup -q

%build
%{__make} \
	PREFIX="%{_prefix}" \
	CC="%{__cc}" \
	LIB="%{_lib}" \
	CFLAGS="`pkg-config --cflags beryl` %{rpmcflags}" \
	LDFLAGS="%{rpmldflags} `pkg-config --libs beryl` -lseom"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/beryl,%{_datadir}/beryl}

install .libs/libcapture.so $RPM_BUILD_ROOT%{_libdir}/beryl
install seom.png $RPM_BUILD_ROOT%{_datadir}/beryl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/beryl/*.so
%{_datadir}/beryl/*
