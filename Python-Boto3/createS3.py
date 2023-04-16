import boto3
from botocore.exceptions import ClientError
import logging
from user_choice import credentials_check


def create_buckets():
    '''Create S3 buckets from the list!'''

    if credentials_check():    
        try:
            s3_client = boto3.client('s3')            
            bucket_list = ["pythonboto3-test-s3bucket-1","pythonboto3-test-s3bucket-2", "pythonboto3-test-s3bucket-3"]
            for bucket_name in bucket_list:                
                s3_client.create_bucket(Bucket=bucket_name)
            print("\n Created S3 buckets!")
            return True
        except ClientError as e:
            logging.error(e)   
            return False         
    else:
        print("\n Check AWS credentials - missed!")