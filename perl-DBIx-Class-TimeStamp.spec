%define upstream_name    DBIx-Class-TimeStamp
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	DBIx::Class extension to update and create date and time based fields
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Grouped)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::DynamicDefault)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::MySQL)
BuildRequires:	perl(DateTime::Format::SQLite)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(Time::Warp)

BuildArch:	noarch

Requires:	perl(DBIx::Class::DynamicDefault)

%description
Works in conjunction with InflateColumn::DateTime to automatically set
update and create date and time based fields in a table.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.140.0-2mdv2011.0
+ Revision: 656899
- rebuild for updated spec-helper

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 595099
- update to new version 0.14

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 554167
- update to 0.13

* Mon Nov 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-2mdv2010.1
+ Revision: 471678
- adding missing requires:

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 471532
- adding missing buildrequires:
- tighten spec file
- import perl-DBIx-Class-TimeStamp


* Sun Nov 29 2009 cpan2dist 0.12-1mdv
- initial mdv release, generated with cpan2dist
