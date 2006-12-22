#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ExtUtils
%define	pnam	CBuilder
Summary:	ExtUtils::CBuilder - Compile and link C code for Perl modules
Summary(pl):	EXtUtils::CBuilder - kompilowanie i linkowanie kodu C dla modu³ów Perla
Name:		perl-ExtUtils-CBuilder
Version:	0.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d119f0c6c12787a8d5b255208c3c74c5
URL:		http://search.cpan.org/dist/ExtUtils-CBuilder/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was
motivated by the Module::Build project, but may be useful for other
purposes as well. However, it is not intended as a general
cross-platform interface to all your C building needs. That would
have been a much more ambitious goal!

%description -l pl
Ten modu³ potrafi budowaæ czê¶ci modu³óê perlowych napisane w C
wywo³uj±c odpowiednie kompilatory i linkery w sposób wieloplatformowy.
Powsta³ z my¶l± o projekcie Module::Build, ale mo¿e byæ przydatny
tak¿e do innych celów. Nie jest jednak przeznaczony do u¿ywania jako
ogólny wieloplatformowy interfejs do wszelkich potrzeb budowania
programów w C. To by³by zbyt ambitny cel.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes 
%{perl_vendorlib}/ExtUtils/CBuilder.pm
%{perl_vendorlib}/ExtUtils/CBuilder
%{_mandir}/man3/*
