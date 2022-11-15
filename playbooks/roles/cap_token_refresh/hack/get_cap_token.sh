#!/bin/bash

readarray -t creds <<< \
  "$(jq -r '.Credentials | .AccessKeyId, .SecretAccessKey')"

id=${creds[0]}
secret=${creds[1]}

echo ID=${id}
echo Secret=${secret}

if [ -n "${profile}" ]
then
  echo "Replacing credentials in ${profile} AWS profile"
  sed -i -E \
    -e '/^\['"${profile}"'\]$/,/^\[/ s|^(aws_access_key_id\s*=\s*).*$|\1'"${id}"'|' \
    -e '/^\['"${profile}"'\]$/,/^\[/ s|^(aws_secret_access_key\s*=\s*).*$|\1'"${secret}"'|' \
    ~/.aws/credentials
fi

sed -i -E \
  -e 's|^(\s*aws_access_key_id\s*[=:]\s*).*$|\1'"${id}"'|g' \
  -e 's|^(\s*aws_secret_access_key\s*[=:]\s*).*$|\1'"${secret}"'|g' \
  -- manifests/*-secret.yaml
