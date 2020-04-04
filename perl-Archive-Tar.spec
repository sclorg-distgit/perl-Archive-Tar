%{?scl:%scl_package perl-Archive-Tar}

# Run optional test
%if ! (0%{?rhel}) || ! (0%{?scl:1})
%bcond_without perl_Archive_Tar_enables_optional_test
%else
%bcond_with perl_Archive_Tar_enables_optional_test
%endif

Name:           %{?scl_prefix}perl-Archive-Tar
Version:        2.32
Release:        451%{?dist}
Summary:        A module for Perl manipulation of .tar files
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Archive-Tar
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Archive-Tar-%{version}.tar.gz
# Remove annoying sleep after warnings in the build script
Patch0:         Archive-Tar-2.02-Do-not-sleep-in-Makefile.PL.patch
BuildArch:      noarch
# Most of the BRS are needed only for tests, compression support at run-time
# is optional soft dependency.
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
# File::Copy not used
BuildRequires:  %{?scl_prefix}perl(Getopt::Std)
BuildRequires:  %{?scl_prefix}perl(strict)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.82
BuildRequires:  %{?scl_prefix}perl(File::Spec::Unix)
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
BuildRequires:  %{?scl_prefix}perl(IO::File)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(IO::Zlib) >= 1.01
BuildRequires:  %{?scl_prefix}perl(Pod::Usage)
# Time::Local not used on Linux
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Optional run-time:
BuildRequires:  %{?scl_prefix}perl(IO::Compress::Bzip2) >= 2.015
# IO::String not used if perl supports useperlio which is true
# Use Compress::Zlib's version for IO::Uncompress::Bunzip2
BuildRequires:  %{?scl_prefix}perl(IO::Uncompress::Bunzip2) >= 2.015
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(Text::Diff)
%endif
# Tests:
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(FindBin)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(Test::Harness) >= 2.26
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests:
%if %{with perl_Archive_Tar_enables_optional_test} && !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(IPC::Cmd)
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 0.95
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(IO::Zlib) >= 1.01
# Optional run-time:
Requires:       %{?scl_prefix}perl(IO::Compress::Bzip2) >= 2.015
# IO::String not used if perl supports useperlio which is true
# Use Compress::Zlib's version for IO::Uncompress::Bunzip2
Requires:       %{?scl_prefix}perl(IO::Uncompress::Bunzip2) >= 2.015
%if !%{defined perl_bootstrap}
Requires:       %{?scl_prefix}perl(Text::Diff)
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(IO::Zlib\\)$

%description
Archive::Tar provides an object oriented mechanism for handling tar
files.  It provides class methods for quick and easy files handling
while also allowing for the creation of tar file objects for custom
manipulation.  If you have the IO::Zlib module installed, Archive::Tar
will also support compressed or gzipped tar files.

%prep
%setup -q -n Archive-Tar-%{version}
%patch0 -p1

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
%{_fixperms} %{buildroot}/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc CHANGES README
%{_bindir}/*
%{perl_vendorlib}/Archive/
%{_mandir}/man3/*.3*
%{_mandir}/man1/*.1*


%changelog
* Wed Nov 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.32-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.32-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.32-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.32-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.32-1
- 2.32 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.30-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.30-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.30-416
- Increase release to favour standalone package

* Tue Jun 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.30-1
- 2.30 bump

* Fri Jun 08 2018 Petr Pisar <ppisar@redhat.com> - 2.28-1
- 2.28 bump
- Fixes CVE-2018-12015 (directory traversal) (bug #1588761)

* Wed Apr 04 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-6
- Do not run optional test on RHEL

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-2
- Perl 5.26 rebuild

* Mon May 15 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-1
- 2.26 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.24-1
- 2.24 bump

* Fri Dec 16 2016 Petr Pisar <ppisar@redhat.com> - 2.22-1
- 2.22 bump

* Fri Dec 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.20-1
- 2.20 bump

* Tue Nov 08 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.18-1
- 2.18 bump

* Wed Nov 02 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.16-1
- 2.16 bump

* Fri Oct 21 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.14-1
- 2.14 bump

* Mon Oct 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.12-1
- 2.12 bump

* Fri Jul 29 2016 Petr Pisar <ppisar@redhat.com> - 2.10-1
- 2.10 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-2
- Perl 5.24 rebuild

* Thu May 12 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.08-1
- 2.08 bump

* Tue Apr 26 2016 Petr Pisar <ppisar@redhat.com> - 2.06-1
- 2.06 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-2
- Perl 5.22 rebuild

* Tue Dec 16 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-1
- 2.04 bump

* Wed Dec 10 2014 Petr Pisar <ppisar@redhat.com> - 2.02-2
- Remove unneeded dependencies
- Remove annoying sleep after warnings in the build script

* Thu Sep 18 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.02-1
- 2.02 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-3
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-2
- Perl 5.20 rebuild

* Mon Jun 23 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-1
- 2.00 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 25 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.96-1
- 1.96 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.92-4
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1.92-2
- Perl 5.18 rebuild

* Thu Jun 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.92-1
- 1.92 bump
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Update dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 18 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.90-2
- Add BRs perl(lib), perl(IO::File)

* Thu Sep 13 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.90-1
- 1.90 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.88-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1.88-4
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1.88-3
- Perl 5.16 rebuild

* Mon Jun 04 2012 Petr Šabata <contyk@redhat.com> - 1.88-2
- 1.88 bump
- Drop command macros

* Fri Jun 01 2012 Petr Pisar <ppisar@redhat.com> - 1.84-2
- Omit optional Test::Pod tests on bootstrap

* Wed Mar 14 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.84-1
- 1.84 bump #802981 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.82-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Petr Šabata <contyk@redhat.com> - 1.82-1
- 1.82 bump

* Fri Oct 14 2011 Petr Sabata <contyk@redhat.com> - 1.80-1
- 1.80 bump

* Fri Sep 09 2011 Petr Pisar <ppisar@redhat.com> - 1.78-1
- 1.78 bump
- Remove BuildRoot and defattr code from spec

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.76-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Petr Pisar <ppisar@redhat.com> - 1.76-1
- 1.76 bump

* Mon Jan 03 2011 Petr Sabata <psabata@redhat.com> - 1.74-1
- 1.74 bump

* Fri Nov 19 2010 Petr Pisar <ppisar@redhat.com> - 1.72-1
- 1.72 bump

* Tue Sep 14 2010 Petr Pisar <ppisar@redhat.com> - 1.68-1
- 1.68 bump

* Tue Jul 13 2010 Petr Pisar <ppisar@redhat.com> - 1.64-1
- 1.64 bump

* Tue Jul 13 2010 Petr Pisar <ppisar@redhat.com> - 1.62-1
- 1.62 bump (bug #607687)

* Thu Aug 23 2007 Robin Norwood <rnorwood@redhat.com> - 1.34-1
- Upgrade to latest upstream version: 1.34
- Fix license tag
- Fix BuildRequires for ExtUtils::MakeMaker and Test::Pod

* Mon Jun 04 2007 Robin Norwood <rnorwood@redhat.com> - 1.32-1
- Upgrade to latest upstream version: 1.32

* Mon Mar 05 2007 Robin Norwood <rnorwood@redhat.com> - 1.30-4
- Fix changelog

* Mon Feb 19 2007 Robin Norwood <rnorwood@redhat.com> - 1.30-3
- Incorporate specfile improvements from Jose Oliveira.

* Fri Feb 16 2007 Robin Norwood <rnorwood@redhat.com> - 1.30-2
- Resolves: rhbz#226239 - Remove tabs from spec file for package review

* Tue Sep 19 2006 Robin Norwood <rnorwood@redhat.com> - 1.30-1
- Bump to 1.30

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.29-1.1
- rebuild

* Wed Mar 08 2006 Jason Vas Dias <jvdias@redhat.com> - 1.29-1
- Upgrade to upstream version 1.29

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 1.28-1
- Upgrade to upstream version 1.28
- Rebuild for perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Sun Nov 06 2005 Florian La Roche <laroche@redhat.com>
- 1.26

* Mon Apr 25 2005 Warren Togami <wtogami@redhat.com> - 1.23-4
- remove beehive workaround

* Sun Apr 03 2005 Jose Pedro Oliveira <jpo@di.uminho.pt> - 1.23-1
- Update to 1.23.
- Bring up to date with current Fedora.Extras perl spec template.

* Wed Sep 22 2004 Chip Turner <cturner@redhat.com> 1.08-3
- rebuild

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 1.08-1
- update to upstream 1.08

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Aug  6 2002 Chip Turner <cturner@redhat.com>
- automated release bump and build

* Fri Feb 08 2002 cturner@redhat.com
- Specfile autogenerated

