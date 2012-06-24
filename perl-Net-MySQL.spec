#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	MySQL
Summary:	Net::MySQL - pure Perl MySQL network protocol interface
Summary(pl.UTF-8):	Net::MySQL - czysto perlowy interfejs do protokołu sieciowego MySQL-a
Name:		perl-Net-MySQL
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	35b62e0f55fa5e2a3d308f602751bb68
URL:		http://search.cpan.org/dist/Net-MySQL/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-SHA1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::MySQL is a Pure Perl client interface for the MySQL database.
This module implements network protocol between server and client of
MySQL, thus you don't need external MySQL client library like
libmysqlclient for this module to work. It means this module enables
you to connect to MySQL server from some operation systems which MySQL
is not ported.

%description -l pl.UTF-8
Net::MySQL to czysto perlowy interfejs kliencki do bazy danych MySQL.
Ten moduł jest implementacją protokołu sieciowego między serwerem a
klientem MySQL-a, przez co nie wymaga do działania zewnętrznej
biblioteki klienckiej MySQL-a, takiej jak libmysqlclient. Oznacza to,
że moduł ten umożliwia połączenie z serwerem MySQL nawet z systemu
operacyjnego, na który MySQL nie został sportowany.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/MySQL.pm
%{_mandir}/man3/*
