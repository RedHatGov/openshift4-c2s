FROM docker.io/stedolan/jq AS jq

FROM quay.io/openshift/origin-cli:latest
COPY --from=jq /usr/local/bin/jq /usr/bin/