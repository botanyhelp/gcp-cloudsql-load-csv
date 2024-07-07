# Connect to GCP CloudSQL Instance/VM

## create database instance/VM in GCP CloudSQL

* this setp can be automated with gcloud or terraform, but
* we will do it in the GCP web console
* we create the smallest possible database with 1 CPU, make one like shown in these screenshots:

## Connect to MysQL server running on new CloudSQL instance from GCP CloudShell:

* we start CloudShell in the GCP web console:
    * ..by clicking on the CloudShell icon in the upper right side of the GCP web console
    * we see CloudShell starting, with black background beneath the GCP web console
* we copy the IP address we see in the GCP cloud web console on the CloudSQL page, for my project, that URL is here
    * https://console.cloud.google.com/sql/instances?cloudshell=true&project=airy-berm-426714-j7
    * yours will be different
* we copy to our clipboard the public IP address that we see for our CloudSQL instance/VM, that IP address for me is here:
    * 34.44.240.91
    * yours will be different
* we try to login to the mysql server running on the CloudSQL instance/VM:
    * **mysql -u root -p -h 34.44.240.91**
    * ..but it hangs for a long time and we press **CTRL-C** to quit waiting for our doomed connection attempt
    * it is doomed because we have not yet allowed connections to the mysql server from our IP address
    * our IP address is the one being used by our temporary/ephemeral CloudShell VM
    * we could discover that IP address, our CloudShell IP address, and go into CloudSQL to allow connections from that IP address
    * ..but that is a pain and we would have to do it again each time our CloudShell gets a new IP address
* we use **gcloud** to login to the mysql server running on the CloudSQL instance/VM:
    * instead we will use the **gcloud** cli to make the connection for us and to temporarily allow our IP address to connect again
    * unlike AWS, where every API is automatically available for our use, in GCP we must explicitly enable access to any APIs we want to use
        * we enable access to the CloudSQL API for our CloudShell:
        * **gcloud services enable sqladmin.googleapis.com**
    * we connect to the mysql server running on the CloudSQL instance/VM we created earlier:
        * **gcloud sql connect myinstance --user=root**
        * recall that we named our CloudSQL instance **myinstance** when we created it, earlier, in the GCP CloudSQL web console
        * we enter the password for the root user of our MySQL server
    * happily, we are connected 
        * but we will exit our MySQL client session with **exit;** or **quit;** at the MySQL prompt:
        * **quit;**
* we use **mysql** client to login to the mysql server running on the CloudSQL instance/VM:
    * when we used **gcloud sql connect** to connect to the MySQL server running on our CloudSQL instance/VM, we saw a message that connections were being allowed from our IP address for 5 minutes
    * that means that we can use the **mysql** client command to connect to the MySQL database from our CloudShell VM for 5 minutes, which we do:
        * **mysql -u root -p -h 34.44.240.91**
        * ..and we enter the password and see the **mysql>** prompt where we can enter SQL to interact with our database server
    * if it hangs forever after entering the password, that means that our temporary access has expired and we need to connect with **gcloud** again, as we did before:
        * **gcloud sql connect myinstance --user=root**
        * ..and then we can **quit** and then connect with **mysql** again for 5 minutes:
        * **mysql -u root -p -h 34.44.240.91**
* we have successfully connected to the MySQL server running on our new CloudSQL instance/VM and we are ready to do some SQL
