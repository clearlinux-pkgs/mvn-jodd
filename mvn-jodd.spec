#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jodd
Version  : 3.5.2
Release  : 3
URL      : https://repo1.maven.org/maven2/org/jodd/jodd-core/3.5.2/jodd-core-3.5.2-sources.jar
Source0  : https://repo1.maven.org/maven2/org/jodd/jodd-core/3.5.2/jodd-core-3.5.2-sources.jar
Source1  : https://repo1.maven.org/maven2/org/jodd/jodd-core/3.5.2/jodd-core-3.5.2.jar
Source2  : https://repo1.maven.org/maven2/org/jodd/jodd-core/3.5.2/jodd-core-3.5.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: mvn-jodd-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-jodd package.
Group: Data

%description data
data components for the mvn-jodd package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jodd/jodd-core/3.5.2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/jodd/jodd-core/3.5.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jodd/jodd-core/3.5.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/jodd/jodd-core/3.5.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jodd/jodd-core/3.5.2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/jodd/jodd-core/3.5.2


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/jodd/jodd-core/3.5.2/jodd-core-3.5.2-sources.jar
/usr/share/java/.m2/repository/org/jodd/jodd-core/3.5.2/jodd-core-3.5.2.jar
/usr/share/java/.m2/repository/org/jodd/jodd-core/3.5.2/jodd-core-3.5.2.pom
