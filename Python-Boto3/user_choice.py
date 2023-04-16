import boto3
from botocore.exceptions import ClientError
import logging
import os
from createS3 import create_buckets
from deleteS3 import delete_duckets, get_bucketlist



def credentials_check():
    '''Verify if aws access key are valid to proceed!'''
    sts = boto3.client('sts')
    try:
        sts.get_caller_identity()   
        print("Valid AWS Credentials!")
        return True
    except ClientError as e:
        logging.error(e) 
        print("Invalid AWS Credentials!")
        return False
    
os.system('clear')
user_input = ""
if credentials_check():
    if user_input == str(input("\n Do you want to create S3 buckets(-y-) :")).strip():
        print(create_buckets)
    else:
        bucket_list = get_bucketlist()
        if bucket_list != False:    
            delete_all_buckets = delete_duckets(bucket_list)
            if delete_all_buckets != False:
                print("\n All Buckets got deleted !")
            else:
                print("\n Check error details!")
        else:
            print("\n No S3 Buckets available!")