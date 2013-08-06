#
# Knox spec file for RPM...
#

#
#  Licensed to the Apache Software Foundation (ASF) under one or more
#  contributor license agreements.  See the NOTICE file distributed with
#  this work for additional information regarding copyright ownership.
#  The ASF licenses this file to You under the Apache License, Version 2.0
#  (the "License"); you may not use this file except in compliance with
#  the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

Summary: Knox
Name: knox
Version: %{knox_base_version}
Release: %{knox_release}
License: Apache License, Version 2.0
Group: Applications/Server
Vendor: Hortonworks.
Packager: Hortonworks <packager@hortonworks.com>
BuildArch: noarch

#knox-0.3.0-SNAPSHOT.tar.gz
Source: %{name}-%{knox_version}.tar.gz

%description
Knox server...

%prep
echo "Knox installation preparation"

%setup -n %{name}-%{knox_version}-SNAPSHOT

%build
echo "Knox installation build"

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/knox/
cp -R ./ $RPM_BUILD_ROOT/usr/lib/knox/

#%clean
#rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR

%files
/usr/lib/knox/

%pre

%post
echo "Knox installation complete"

%postun
