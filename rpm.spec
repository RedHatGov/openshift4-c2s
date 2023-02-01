# %commit and %os_git_vars are intended to be set by tito custom builders provided
# in the .tito/lib directory. The values in this spec file will not be kept up to date.
%{!?commit: %global commit HEAD }
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# os_git_vars needed to run hack scripts during rpm builds
%{!?os_git_vars: %global os_git_vars OS_GIT_VERSION='' OS_GIT_COMMIT='' OS_GIT_MAJOR='' OS_GIT_MINOR='' OS_GIT_TREE_STATE='' }

Summary: OpenShift 4 Install Tool for AWS ISO Regions
Name: openshift4-aws-iso
Version:        %{version}
Release:        %{release}%{?dist}
License: ASL 2.0
Vendor: Red Hat
Group: Utility
BuildArch: noarch
URL:            https://%{import_path}

%if ! 0%{?local_build:1}
Source0:        https://%{import_path}/archive/%{commit}/%{name}-%{version}.tar.gz
%endif

%description
Ansible playbooks and roles to deploy an OpenShift 4
cluster in the AWS US ISO regions.

%prep
%if ! 0%{?local_build:1}
%setup -q
%endif

%install
install -d %{buildroot}%{_datadir}/%{name}
install -m 644 requirements.txt %{buildroot}%{_datadir}/%{name}/requirements.txt
install -m 644 README.md %{buildroot}%{_datadir}/%{name}/README.md
install -m 644 LICENSE %{buildroot}%{_datadir}/%{name}/LICENSE
#install -d %{buildroot}%{_datadir}/%{name}/docs
install -d %{buildroot}%{_datadir}/%{name}/playbooks
cp -r playbooks/* %{buildroot}%{_datadir}/%{name}/playbooks/
install -d %{buildroot}%{_datadir}/%{name}/cloudformation
cp -r cloudformation %{buildroot}%{_datadir}/%{name}/cloudformation/


%files
%defattr(-,root,root)
%{_datadir}/%{name}/requirements.txt
%doc %{_datadir}/%{name}/README.md
%license %{_datadir}/%{name}/LICENSE
%{_datadir}/%{name}/playbooks
%{_datadir}/%{name}/cloudformation

%changelog
* Tue Dec 13 2022 Initial RPM Build
- Initial example of spec.