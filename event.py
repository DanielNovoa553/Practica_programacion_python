"""
Make an event that insert an object into s3 aws
"""
import boto3
import json
import os
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os  .environ)
    logger.info('## EVENT')
    logger.info(event)

    # Get the service resource.
    s3 = boto3.resource('s3')
    # Create a new bucket
    bucket = s3.Bucket('my-bucket')
    # Upload a new file
    bucket.upload_file('/tmp/hello.txt', 'hello.txt')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

# Path: event.py
