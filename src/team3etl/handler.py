import boto3
from src.loading import run_loading
from src.sql_script import *
import csv
import psycopg2
import os

# dbname = os.environ["DB"]
# host = os.environ["HOST"]
# port = os.environ["PORT"]
# user = os.environ["DB_USER"]
# password = os.environ["PASSWORD"]
# print(host) 
# print(user)

s3 = boto3.client('s3')

def handle(event, c):
    # connection = psycopg2.connect(dbname=dbname, host=host,
    #                        port=port, user=user, password=password)
    #   Get key and bucket informaition
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    # use boto3 library to get object from S3
    s3 = boto3.client('s3')
    s3_object = s3.get_object(Bucket=bucket, Key=key)
    data = s3_object['Body'].read().decode('utf-8')
    # read CSV
    file = data.splitlines()
    run_loading(file)
    # connection.close()
    return {"message": "success!!! Check the cloud watch logs for this lambda in cloudwatch https://eu-west-1.console.aws.amazon.com/cloudwatch/home?region=eu-west-1#logsV2:log-groups"}