import boto3
import os

def upload_repo_to_s3(local_path, bucket_name='your-bucket-name'):
    s3_client = boto3.client('s3')

    for root, dirs, files in os.walk(local_path):
        for file in files:
            file_path = os.path.join(root, file)
            s3_key = file_path[len(local_path):].lstrip(os.path.sep)

            try:
                s3_client.upload_file(file_path, bucket_name, s3_key)
                print(f'Uploaded {file_path} to s3://{bucket_name}/{s3_key}')
            except Exception as e:
                print(f'An error occurred while uploading {file_path}: {e}')