Name:     	monodevelop-java
Version:	2.4
Release:	%mkrel 1
License:	GPLv2+
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://ftp.novell.com/pub/mono/sources/monodevelop-java/%{name}-%{version}.tar.bz2
BuildRequires:	ikvm
BuildRequires:  monodevelop >= %version
BuildRequires:  mono-devel
Summary:	Monodevelop Java Addin
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Monodevelop Java Addin

%prep
%setup -q

%build
./configure --prefix=%_prefix
make

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%_prefix/share/pkgconfig
mv $RPM_BUILD_ROOT%_prefix/lib/pkgconfig/*.pc $RPM_BUILD_ROOT%_prefix/share/pkgconfig

for langdir in %buildroot%_prefix/lib/monodevelop/AddIns/JavaBinding/locale/*; do
echo "%lang($(basename $langdir)) $(echo $langdir |sed s!%buildroot!!)" >> %name.lang
done


%clean
rm -rf "$RPM_BUILD_ROOT"

%files -f %name.lang
%defattr(-, root, root)
%_prefix/share/pkgconfig/monodevelop-java.pc
%dir %_prefix/lib/monodevelop/AddIns/JavaBinding/
%_prefix/lib/monodevelop/AddIns/JavaBinding/JavaBinding.dll*
%dir %_prefix/lib/monodevelop/AddIns/JavaBinding/locale/

