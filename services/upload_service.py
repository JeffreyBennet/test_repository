import boto3
import os

def upload_to_s3(local_path, bucket_name):
    s3_client = boto3.client('s3')
    
    for root, dirs, files in os.walk(local_path):
        for file in files:
            s3_client.upload_file(os.path.join(root, file), bucket_name, file)