#! /usr/bin/env python

import boto3
from myconfig import S3_Storage

if __name__ == "__main__":
    session = boto3.Session()
    s3_client = session.client(service_name='s3',
                               endpoint_url=S3_Storage.aws_s3_endpoint_url,
                               aws_access_key_id=S3_Storage.aws_access_key_id,
                               aws_secret_access_key=S3_Storage.aws_secret_access_key)
    s3_client.put_object(Bucket=S3_Storage.aws_storage_bucket_name, Key='user1/1234', Body="Hello, world")
