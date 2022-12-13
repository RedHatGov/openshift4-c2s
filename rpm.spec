Summary: OpenShift 4 Install Tool for AWS ISO Regions
Name: openshift4-aws-iso
Version: 4.11
Release: 4.11
License: GPL2
Vendor: Red Hat
Group: Utility
BuildArch: x86_64
#Requires:

%description
Ansible playbooks and roles to deploy an OpenShift 4
cluster in the AWS US ISO regions.

%install
install -d %{buildroot}%{_datadir}/openshift4-aws-iso
install -m 644 requirements.txt %{buildroot}%{_datadir}/openshift4-aws-iso/requirements.txt
install -m 644 README.md %{buildroot}%{_datadir}/openshift4-aws-iso/README.md
install -m 644 LICENSE %{buildroot}%{_datadir}/openshift4-aws-iso/LICENSE
#install -d %{buildroot}%{_datadir}/openshift4-aws-iso/docs
install -d %{buildroot}%{_datadir}/openshift4-aws-iso/playbooks
cp -r playbooks/* %{buildroot}%{_datadir}/openshift4-aws-iso/playbooks/
install -d %{buildroot}%{_datadir}/openshift4-aws-iso/cloudformation
cp -r cloudformation %{buildroot}%{_datadir}/openshift4-aws-iso/cloudformation/


%files
%defattr(-,root,root)
%{_datadir}/openshift4-aws-iso/requirements.txt
%doc %{_datadir}/openshift4-aws-iso/README.md
%license %{_datadir}/openshift4-aws-iso/LICENSE
%{_datadir}/openshift4-aws-iso/playbooks
%{_datadir}/openshift4-aws-iso/cloudformation

%changelog
* Tue Dec 13 2022 Initial RPM Build
