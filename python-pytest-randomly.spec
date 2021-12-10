#
# Conditional build:
%bcond_with	tests	# unit tests (more dependencies required)
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-pytest-randomly.spec)

Summary:	Pytest plugin to randomly order tests and control random.seed
Summary(pl.UTF-8):	Wtyczka pytesta do losowej kolejności testów i sterowania random.seed
Name:		python-pytest-randomly
# keep 1.x here for python2 support
Version:	1.2.3
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-randomly/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-randomly/pytest-randomly-%{version}.tar.gz
# Source0-md5:	a14d9ac82ac744e7c3ddf51e62d5c751
URL:		https://pypi.org/project/pytest-randomly/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-factory_boy
BuildRequires:	python-faker
BuildRequires:	python-numpy
BuildRequires:	python-six
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-factory_boy
BuildRequires:	python3-faker
BuildRequires:	python3-numpy
BuildRequires:	python3-six
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pytest plugin to randomly order tests and control random.seed.

%description -l pl.UTF-8
Wtyczka pytesta do losowej kolejności testów i sterowania random.seed.

%package -n python3-pytest-randomly
Summary:	Pytest plugin to randomly order tests and control random.seed
Summary(pl.UTF-8):	Wtyczka pytesta do losowej kolejności testów i sterowania random.seed
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pytest-randomly
Pytest plugin to randomly order tests and control random.seed.

%description -n python3-pytest-randomly -l pl.UTF-8
Wtyczka pytesta do losowej kolejności testów i sterowania random.seed.

%prep
%setup -q -n pytest-randomly-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytester,pytest_randomly" \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytester,pytest_randomly" \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%{py_sitescriptdir}/pytest_randomly.py[co]
%{py_sitescriptdir}/pytest_randomly-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-randomly
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest_randomly.py
%{py3_sitescriptdir}/__pycache__/pytest_randomly.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_randomly-%{version}-py*.egg-info
%endif
