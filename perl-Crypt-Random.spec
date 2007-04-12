%define	module	Crypt-Random
%define	name	perl-%{module}
%define	version	1.25
%define	release	1mdk

Name:		%{name}
Summary:	%{module} Perl module
Version:	%{version}
Release:	%{release}
License:	Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://search.cpan.org/dist/%{module}
Buildarch:	noarch

%description
Crypt::Random is an interface module to the /dev/random device found on most
modern Unix systems. The /dev/random driver gathers environmental noise from
various non-deterministic sources including inter-keyboard timings and
inter-interrupt timings that occur within the operating system environment.
The /dev/random driver maintains an estimate of true randomness in the pool and
decreases it every time random strings are requested for use. When the estimate
goes down to zero, the routine blocks and waits for the occurrence of
non-deterministic events to refresh the pool.
The /dev/random kernel module also provides another interface, /dev/urandom,
that does not wait for the entropy-pool to recharge and returns as many bytes
as requested. /dev/urandom is considerably faster at generation compared to
/dev/random, which should be used only when very high quality randomness is
desired.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc Changes README 
%{_bindir}/*
%{perl_vendorlib}/Crypt/*.pm
%{perl_vendorlib}/Crypt/Random
%{_mandir}/*/*

