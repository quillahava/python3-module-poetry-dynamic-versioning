%define pypi_name poetry-dynamic-versioning

Name:           python3-module-%pypi_name
Version:        1.2.0
Release:        alt1
Summary:        Plugin for Poetry to enable dynamic versioning based on VCS tags
Group:          Development/Python3

License:        MIT
URL:            https://github.com/eigenein/protobuf.git
Source0:        %{name}-%{version}.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-dev
BuildRequires:  python3(setuptools)
BuildRequires:  python3(wheel)
BuildRequires:  python3-module-poetry
BuildRequires:  python3-module-dunamai
BuildRequires:  python3-module-jinja2
BuildRequires:  python3-module-tomlkit


%py3_provides %pypi_name

BuildArch:      noarch

%description
pure-protobuf leverages the standard dataclasses module for defining message types, offering a modern alternative to the traditional approach. This method is recommended for new projects due to its simplicity and integration with Python's features. Compatible with Python 3.6 and later versions, the dataclasses interface streamlines the process of structuring your data. While the legacy interface remains accessible through pure_protobuf.legacy, it is considered deprecated and is not recommended for future use. This documentation aims to guide you in utilizing pure-protobuf effectively, aligning closely with the standard developer guide and presupposing a basic understanding of Protocol Buffers.

%prep
%setup -v

%build
%pyproject_build

%install
%pyproject_install
install -Dm644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE


%files
%doc *.md
%_licensedir/%name/LICENSE
%python3_sitelibdir/*

%changelog
* Thu Feb 8 2024 Aleksandr A. Voyt <vojtaa@basealt.ru> 3.0.0-alt1
- First package version



