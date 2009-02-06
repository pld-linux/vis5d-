Summary:        Vis5d+ weather visualizing system
Summary(pl.UTF-8):      Program do wizualizacji zmian pogody
Name:           vis5d+
Version:        1.2.1
Release:        0.1
License:        GPL
Group:          X11/Applications
Source0:        http://dl.sourceforge.net/vis5d/%{name}-%{version}.tar.bz2
URL:            http://www.ssec.wisc.edu/~billh/vis5d.html
BuildRequires:  docbook-utils
BuildRequires:  netcdf-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Vis5D is a software system for visualizing data made by numerical
weather models and similar sources. Vis5D works on data in the form of
a five- dimensional rectangle.

%description -l pl.UTF-8
Program do wizualizacji zmian pogody.

%package devel
Summary:        Vis5d development information
Summary(pl.UTF-8):      Vis5d - informacje dla programistw
Group:          Development
Requires:       %{name} = %{version}-%{release}

%description devel
Vis5d development information. API and script info.

%description devel -l pl.UTF-8
Informacje potrzebne do tworzenia aplikacji współpracujących z
programem Vis5d.

%package static
Summary:        Vis5d+ static library
Summary(pl.UTF-8):      Vis5d+ - biblioteki statyczne
Group:          Development
Requires:       %{name} = %{version}-%{release}

%description static
Vis5d+ static library

%description static -l pl.UTF-8
Biblioteki statyczne dla Vis5d+

%prep
%setup -q
# %patch0 -p1

%setup -q

%build
./configure prefix=/usr
make prefix=/usr

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README PORTING
%attr(755, root, root) %{_bindir}/*
%{_datadir}/*
%attr(755, root, root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc 
%attr(644, root, root) %{_includedir}/*
%attr(755, root ,root) %{_libdir}/*.so
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%doc 
%{_libdir}/*.a
