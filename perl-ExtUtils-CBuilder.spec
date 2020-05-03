#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	ExtUtils
%define	pnam	CBuilder
Summary:	ExtUtils::CBuilder - Compile and link C code for Perl modules
Summary(pl.UTF-8):	EXtUtils::CBuilder - kompilowanie i linkowanie kodu C dla modułów Perla
Name:		perl-ExtUtils-CBuilder
Version:	0.280230
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cf12adecda91703057e5b10e0898aeb6
URL:		https://metacpan.org/release/ExtUtils-CBuilder
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Perl-OSType >= 1
BuildRequires:	perl-Test-Simple >= 0.47
BuildRequires:	perl(File::Spec) >= 3.13
%endif
Requires:	perl-Perl-OSType >= 1
Requires:	perl(File::Spec) >= 3.13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was
motivated by the Module::Build project, but may be useful for other
purposes as well. However, it is not intended as a general
cross-platform interface to all your C building needs. That would have
been a much more ambitious goal!

%description -l pl.UTF-8
Ten moduł potrafi budować części modułów perlowych napisane w C
wywołując odpowiednie kompilatory i linkery w sposób wieloplatformowy.
Powstał z myślą o projekcie Module::Build, ale może być przydatny
także do innych celów. Nie jest jednak przeznaczony do używania jako
ogólny wieloplatformowy interfejs do wszelkich potrzeb budowania
programów w C. To byłby zbyt ambitny cel.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/ExtUtils/CBuilder.pm
%{perl_vendorlib}/ExtUtils/CBuilder
%{_mandir}/man3/ExtUtils::CBuilder*.3pm*
