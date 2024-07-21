import boto3

def upload_to_s3(repo_path, bucket_name='myBucket', s3_directory='repo'):
    s3_client = boto3.client('s3')
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            s3_client.upload_file(os.path.join(root, file), bucket_name, os.path.join(s3_directory, file))