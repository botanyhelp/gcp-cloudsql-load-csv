# Easy GCP startup

We will use CloudShell in the GCP web console and the **gcloud** command to do most things. 
In AWS, everything is already available for us to use.  In GCP, nothing is available and we need to, firstly, beforehand, enable any APIs we will be using
We will only be using the Cloud SQL API and so we only need to enable that one service. 
Because we are using CloudShell, there is a chance that our CloudShell VM will simply die for inactivity.  
We click the **Reconnect** button to get our CloudShell back but we do not want to do everything all over again, everytime. 
For this reason, we will put commands that we want to be run for every CloudShell startup into a file in our home directory named **.bashrc**
That will ensure that we will maintain 3 things everytine we login:
project
compute/zone
Cloud SQL API enabled
here we will setup 3 things in GCP CloudShell so that we have everything we need: project, compute/zone and enable APIs
* Enable APIs we will use
* In AWS
* in github.com we create a fine-grained personal access token, PAT, so that we an authenticate to github more easily from GCP cloudshell
