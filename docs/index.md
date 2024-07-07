# GCP CloudSQL Load CSV

We will use GCP CloudShell and Cloud SQL to upload 100 million rows into a MySQL database. 


SQL_INSTANCE_IP_ADDRESS=$(gcloud sql instances list|grep PRIMARY_ADDRESS|sed 's/.* //') 
gcloud services enable sqladmin.googleapis.com
gcloud config get project
gcloud config get compute/zone
gcloud sql connect myinstance --user=root
gcloud services enable sqladmin.googleapis.com
echo $SQL_INSTANCE_IP_ADDRESS
# 34.44.240.91
gcloud config set compute/zone us-central1-b

gcloud config set project airy-berm-426714-j7
gcloud config set compute/zone us-central1-b
gcloud services enable container.googleapis.com
gcloud services enable sqladmin.googleapis.com
gcloud help sql instances create 
gcloud sql instances delete myinstance
gcloud sql instances create myinstance --region=us-central1 --tier=db-g1-small --assign-ip
