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
if credentials_check():
    user_input = str(input("\nDo you want to create S3 buckets(enter-> 1) or (any) to delete : ")).strip()
    if user_input == '1':
        bucket_created = create_buckets()
        if bucket_created != False:
            print("\n Created S3 buckets!")
            bucket_list = get_bucketlist()
            print(bucket_list)
        else:
            print("\n Check error logs!")
    else:
        bucket_list = get_bucketlist()
        print("\n Bucket list : ",bucket_list)
        if bucket_list != False:    
            delete_all_buckets = delete_duckets(bucket_list)
            if delete_all_buckets != False:
                print("\n All Buckets got deleted !")
            else:
                print("\n Check error details!")
        else:
            print("\n No S3 Buckets available!")
