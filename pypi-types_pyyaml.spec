#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-types_pyyaml
Version  : 6.0.4
Release  : 1
URL      : https://files.pythonhosted.org/packages/7e/d8/95340802435bdac473f92da42fd29c0a8fdf676c72928ea6ea95dc63c53a/types-PyYAML-6.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/7e/d8/95340802435bdac473f92da42fd29c0a8fdf676c72928ea6ea95dc63c53a/types-PyYAML-6.0.4.tar.gz
Summary  : Typing stubs for PyYAML
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-types_pyyaml-python = %{version}-%{release}
Requires: pypi-types_pyyaml-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
No detailed description available

%package python
Summary: python components for the pypi-types_pyyaml package.
Group: Default
Requires: pypi-types_pyyaml-python3 = %{version}-%{release}

%description python
python components for the pypi-types_pyyaml package.


%package python3
Summary: python3 components for the pypi-types_pyyaml package.
Group: Default
Requires: python3-core
Provides: pypi(types_pyyaml)

%description python3
python3 components for the pypi-types_pyyaml package.


%prep
%setup -q -n types-PyYAML-6.0.4
cd %{_builddir}/types-PyYAML-6.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1645920395
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
