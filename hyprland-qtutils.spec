%define		qtver	6.5

Summary:	Hyprland QT/qml utility apps
Name:		hyprland-qtutils
Version:	0.1.4
Release:	1
License:	BSD
Group:		Applications
Source0:	https://github.com/hyprwm/hyprland-qtutils/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	77bc00692024befce435f7f4c87d0e77
URL:		https://hyprland.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	Qt6WaylandClient-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	hyprutils-devel
BuildRequires:	libstdc++-devel >= 6:11
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hyprland QT/qml utility apps.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/hyprland-dialog
%attr(755,root,root) %{_bindir}/hyprland-donate-screen
%attr(755,root,root) %{_bindir}/hyprland-update-screen
