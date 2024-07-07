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
gcloud sql instances create myinstance --region=us-central1 --tier=db-g1-small --assign-ip --root-password=password12
gcloud sql connect myinstance --user=root
mysql> exit
mysql -u root -p -h $SQL_INSTANCE_IP_ADDRESS 
mysql> CREATE DATABASE ufos;
mysql> SHOW databases;
mysql> use ufos;
Database changed
mysql> CREATE TABLE ufosightings (sighted_at_year integer default null, sighted_at_month integer default null, sighted_at_day integer default null,  reported_at integer default null,  location_city text default null, location_state text default null, shape text default null,  duration text default null,  description text default null); 
Query OK, 0 rows affected (0.06 sec)

mysql> exit
