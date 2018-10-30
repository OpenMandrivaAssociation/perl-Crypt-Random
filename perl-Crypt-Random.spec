%define	modname	Crypt-Random
%define	modver	1.25

Summary:	%{modname} Perl module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	18
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes README 
%{_bindir}/*
%{perl_vendorlib}/Crypt/*.pm
%{perl_vendorlib}/Crypt/Random
%{_mandir}/man3/*

