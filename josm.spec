%include	/usr/lib/rpm/macros.java
Summary:	Java OpenStreetMap Editor
Summary(pl.UTF-8):	Edytor OpenStreetMap w Javie
Name:		josm
Version:	3701
Release:	1
License:	GPL v2+
Group:		Applications
# this should be the 'tested' snapshot, as list on the web page
# svn export -r%{version} http://josm.openstreetmap.de/svn/trunk josm-src-snapshot-%{version}
Source0:	%{name}-src-snapshot-%{version}.tar.bz2
# Source0-md5:	08342ab1da6f5a8aa4165d481da26b58
Patch0:		%{name}-version.patch
URL:		http://josm.openstreetmap.de/
BuildRequires:	ant
%buildrequires_jdk
BuildRequires:	rpm-javaprov
Requires:	jre-X11 >= 1.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JOSM is an editor for OpenStreetMap (OSM) written in Java 1.5.
Currently it supports loading stand alone GPX tracks and GPX track
data from the OSM database as well as loading and editing existing
nodes, ways, metadata tags and relations from the OSM database.

%prep
%setup -qn %{name}-src-snapshot-%{version}
%undos build.xml
%patch0 -p1

%build
echo "%{version}" > rpm_version
%ant

cat > josm <<'EOF'
#!/bin/sh
exec java -jar %{_datadir}/%{name}/%{name}-custom.jar ${1:+"$@"}
EOF

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

# not into %{_javadir}, as it is not a library, but a stanalone application
install dist/%{name}-custom.jar $RPM_BUILD_ROOT%{_datadir}/%{name}
install josm $RPM_BUILD_ROOT%{_bindir}/josm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/josm
%{_datadir}/%{name}
