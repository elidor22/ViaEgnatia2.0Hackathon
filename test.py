from azure.storage import *
import sys

def main():
    mime_type = content_type(file_name)

    blob_service = BlobService(account_name, account_key)

    # Upload the file and set content type
    blob_service.put_block_blob_from_path(container_name, file_name, file_path)

    # Show a blob listing which now includes the blobs just uploaded
    # Format for blobs is: <account>.blob.core.windows.net/<container>/<file>
    print
    ('All blobs in container ' + container_name)
    blobs = blob_service.list_blobs(container_name)
    for blob in blobs:
        print(blob.name)
        print(blob.url)