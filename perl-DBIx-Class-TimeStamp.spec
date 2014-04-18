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
BuildRequires:	perl(strictures)

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
