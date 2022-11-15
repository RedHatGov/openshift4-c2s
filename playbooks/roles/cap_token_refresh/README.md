The cap-token-refresh project is used to refresh CAP credentials used by an OpenShift cluster.

#### Usage ####

##### Set up the secrets for CAP requests ##### 
In [manifests/cap-certs-secret.yaml](manifests/cap-certs-secret.yaml) set the `stringData` fields
with the certs needed for a CAP request.

##### Set up the cron job #####
In [manifests/cap-cronjob.yaml](manifests/cap-cronjob.yaml) set the following fields.
* Set the image to use for the pod. This should be an image located in the local image registry.
You can either copy the image from quay.io/staebler/cap-token-refresh:latest, or build it from
[Dockerfile](Dockerfile).
* Set the CAP_URL, AGENCY, and MISSION environment variables needed for a CAP request.
* Set the schedule so that the job refreshes the CAP tokens before they expire.
  
##### Create IAM roles for operators #####
Create an IAM role for each credentials request. Set the role in the appropriate secret manifest.

You can get the credentials requests by running the following command.
```
$ oc adm release extract $OPENSHIFT_RELEASE_IMAGE --credentials-requests --cloud=aws
```

For example, the role for the openshift-machine-api-operator credentials request would be set
in [manifests/cap-machine-api-secret.yaml](manifests/cap-machine-api-secret.yaml).
  
##### Get initial operator credentials #####
Set the initial credentials for each credentials request.

Let's use the openshift-machine-api-operator credentials request as an example. Get
credentials from CAP for the IAM role that you created for the openshift-machine-api-operator
credentials request. Fill out the aws_access_key_id and aws_secret_access_key in both places
in [manifests/cap-machine-api-secret.yaml](manifests/cap-machine-api-secret.yaml).

For testing purposes, if the role that you are using to perform the installation has all
of the permissions needed for all of the credentials requests, then you can use the
[hack/get_cap_token.sh](hack/get_cap_token.sh) script to initially use that role for all of
the operator's credentials. When the cron job refreshes the tokens, the new credentials for
each operator will use the role set in the secret for the operator's credentials request.

* Pipe the credentials received from CAP to the script.
    ```
    $ curl $CAP_URL | hack/get_cap_token.sh 
    ```
* Optionally, you can set the `profile` environment variable to have the script update the profile in your
~/.aws/credentials file.
    ```
    $ curl $CAP_URL | profile=$CAP_AWS_PROFILE hack/get_cap_token.sh
    ```
        
##### Use manifests during installation #####
After running `openshift-install create manifests`, copy all of the manifests from
[manifests](manifests) into `$INSTALL_DIR/manifests`.