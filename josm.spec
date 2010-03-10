# TODO:
# - move .jar to %%{_javadir}?
%include	/usr/lib/rpm/macros.java
Summary:	Java OpenStreetMap Editor
Summary(pl.UTF-8):	Edytor OpenStreetMap w Javie
Name:		josm
Version:	3094
Release:	1
License:	GPL v2+
Group:		Applications
# this should be the 'tested' snapshot, available also at
# http://josm.openstreetmap.de/josm-tested.jar
Source0:	http://josm.openstreetmap.de/download/%{name}-snapshot-%{version}.jar
# Source0-md5:	f3ad62809ae18bc02e31b360c2d1fcce
URL:		http://josm.openstreetmap.de/
BuildRequires:	rpm-javaprov
Requires:	jre-X11 >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JOSM is an editor for OpenStreetMap (OSM) written in Java 1.5.
Currently it supports loading stand alone GPX tracks and GPX track
data from the OSM database as well as loading and editing existing
nodes, ways, metadata tags and relations from the OSM database.

%prep
%setup -q -c -T

%build
cat > josm <<'EOF'
#!/bin/sh
exec java -jar %{_datadir}/%{name}/%{name}-snapshot-%{version}.jar ${1:+"$@"}
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}
install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/%{name}
install josm $RPM_BUILD_ROOT%{_bindir}/josm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/josm
%{_datadir}/%{name}
