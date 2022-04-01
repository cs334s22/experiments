from http import client
import os
import boto3
import botocore.exceptions as ClientError

access_key = '...'
access_secret = '...'
bucket_name = '...'


# Connect to S3 Server

client_s3 = boto3.client(
    's3',
    aws_access_key_id = access_key,
    aws_secret_access_key = access_secret
)

# Upload Files to S3 bucket

for file in os.listdir(...):
    if not file.startswith('~'):
        try:
            client_s3.upload_file(

            )

        except ClientError as e:
            print('Credential is incorrect')
            print(e)

        except Exception as e:
            print(e)