from google.cloud import logging

def read_gcp_logs(project_id):

    """Reads logs from specified Google Cloud project"""

    logger = logging.Client(project=project_id)
    filter_str = "timestamp >= \"now() - 1h\""

    entries = logger.list_entries(filter_=filter_str)

    for entry in entries:
        print(entry)

if __name__ == "__main__":
    project_id = "PROJECT_ID"
    read_gcp_logs(project_id)
