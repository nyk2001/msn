import json
import os
import boto3
import requests

def convert_image(event, context):
    # Get the bucket name
    bucket = event['Records']['s3']['bucket']['name']
    
    # Get the file name
    file_key = event['Records']['s3']['object']['key']
    
    print(bucket)
    print(file_key)