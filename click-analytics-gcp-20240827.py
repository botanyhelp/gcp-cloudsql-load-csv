from google.cloud import logging
from datetime import datetime, timedelta, timezone

def read_gcp_logs(project_id):

    """Reads logs from specified Google Cloud project"""

    logger = logging.Client(project=project_id)
    time_format = "%Y-%m-%dT%H:%M:%S.%f%z"
    yesterday = datetime.now(timezone.utc) - timedelta(days=1)
    filter_str = (
        f'timestamp>="{yesterday.strftime(time_format)}"'
    )

    entries = logger.list_entries(filter_=filter_str)

    for entry in entries:
        print(entry)

if __name__ == "__main__":
    project_id = "airy-berm-426714-j7"
    read_gcp_logs(project_id)
