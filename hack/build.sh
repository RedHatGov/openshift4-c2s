#!/bin/bash

if ! test -e ./openshift-client-linux.tar.gz
then
  wget https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp/latest/openshift-client-linux.tar.gz
fi

if ! test -e ./openshift-install-linux.tar.gz
then
  wget https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp/latest/openshift-install-linux.tar.gz
fi

# Don't want to overwrite my own README.md file
tar -xzf ./openshift-client-linux.tar.gz oc
tar -xzf ./openshift-client-linux.tar.gz kubectl
tar -xzf ./openshift-install-linux.tar.gz openshift-install

podman build -t quay.io/danclark/openshift4-c2s:latest -f Dockerfile .
