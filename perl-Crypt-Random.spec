%define	upstream_name	 Crypt-Random
%define	upstream_version 1.25

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	%{upstream_name} Perl module
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/%{upstream_name}-%{upstream_version}.tar.bz2

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
