FROM registry.access.redhat.com/ubi8/python-38

USER 0

COPY ./requirements.txt ./requirements.txt
COPY ./requirements.yml ./requirements.yml
COPY ./playbooks ./playbooks
COPY ./cloudformation ./cloudformation
COPY ./oc /usr/local/bin/oc
COPY ./kubectl /usr/local/bin/kubectl
COPY ./openshift-install /usr/local/bin/openshift-install

RUN chown -R 1001:0 ./ \
 && chmod 0755 /usr/local/bin/oc \
 && chmod 0755 /usr/local/bin/kubectl \
 && chmod 0755 /usr/local/bin/openshift-install

USER 1001

RUN /opt/app-root/bin/python3 -m pip install --no-cache-dir --upgrade -r ./requirements.txt \
 && ansible-galaxy collection install --requirements-file ./requirements.yml

