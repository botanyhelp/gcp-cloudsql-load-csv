from google.cloud import storage
#https://stackoverflow.com/questions/42555142/downloading-a-file-from-google-cloud-storage-inside-a-folder
# Initialise a client
storage_client = storage.Client("Retina-Production")
# Create a bucket object for our bucket
bucket = storage_client.get_bucket("retina-crocs-manhattan-clean-retina-prod-test1")
# Create a blob object from the filepath
blob = bucket.blob("/UAT/WMS/RUN_SUMMARY/RUN_MANIFEST_20240709T050000Z.json")
# Download the file to a destination
blob.download_to_filename("RUN_MANIFEST_20240709T050000Z.json")
