%{?scl:%scl_package perl-Archive-Tar}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Archive-Tar
Version:        1.96
Release:        2%{?dist}
Summary:        A module for Perl manipulation of .tar files
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Archive-Tar/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Archive-Tar-%{version}.tar.gz
BuildArch:      noarch
# Most of the BRS are needed only for tests, compression support at run-time
# is optional soft dependency.
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Compress::Zlib) >= 2.015
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Spec::Unix)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(Getopt::Std)
BuildRequires:  %{?scl_prefix}perl(IO::Compress::Base) >= 2.015
BuildRequires:  %{?scl_prefix}perl(IO::Compress::Bzip2) >= 2.015
BuildRequires:  %{?scl_prefix}perl(IO::Compress::Gzip) >= 2.015
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(IO::String)
BuildRequires:  %{?scl_prefix}perl(IO::Zlib) >= 1.01
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Test::Harness) >= 2.26
BuildRequires:  %{?scl_prefix}perl(Test::More)
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Test::Pod)
%endif
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})
Requires:       %{?scl_prefix}perl(Compress::Zlib) >= 2.015
Requires:       %{?scl_prefix}perl(IO::Zlib) >= 1.01

%description
Archive::Tar provides an object oriented mechanism for handling tar
files.  It provides class methods for quick and easy files handling
while also allowing for the creation of tar file objects for custom
manipulation.  If you have the IO::Zlib module installed, Archive::Tar
will also support compressed or gzipped tar files.

%prep
%setup -q -n Archive-Tar-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc CHANGES README
%{_bindir}/*
%{perl_vendorlib}/Archive/
%{_mandir}/man3/*.3*
%{_mandir}/man1/*.1*


%changelog
* Mon Nov 25 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.96-2
- Re-rebuild of bootstrapped packages

* Fri Nov 08 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.96-1
- 1.96 bump

* Mon Feb 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.90-1
- Stack package - initial release
