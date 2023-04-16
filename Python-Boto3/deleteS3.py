import boto3
from botocore.exceptions import ClientError
import logging
from createS3 import credentials_check


def get_bucketlist():
    if credentials_check():
        try:
            # get the list of buckets from S3
            s3_client = boto3.client("s3")
            get_response = s3_client.list_buckets()
            buckets = get_response["Buckets"] 
            bucket_list = []

            if buckets != []:
                for bucket in buckets:
                    # print("S3 bucket name : ",bucket["Name"])
                    bucket_list.append(bucket["Name"])        
                return bucket_list
            else:
                return False
        except ClientError as e:
            logging.error(e)

def delete_duckets(bucket_list):
    '''Deletes all the S3 buckets in the account which are empty!'''
    if bucket_list != False:
        try:
            s3_client = boto3.client("s3")
            for bucket_name in bucket_list:
                response = s3_client.delete_bucket(Bucket=bucket_name)
            print(response)
            return True
        except ClientError as e:
            logging.error(e)
            return False



