import json


# def hello(event, context):
#     body = {
#         "message": "Go Serverless v1.0! Your function executed successfully!",
#         "input": event
#     }

#     response = {
#         "statusCode": 200,
#         "body": json.dumps(body)
#     }

#     return response

#     # Use this code if you don't use the http event with the LAMBDA-PROXY
#     # integration
#     """
#     return {
#         "message": "Go Serverless v1.0! Your function executed successfully!",
#         "event": event
#     }
#     """


  
# import boto3
# import csv

# def handle(event):
#     # Get key and bucket informaition
#     key = event['Records'][0]['s3']['object']['key']
#     bucket = event['Records'][0]['s3']['bucket']['name']
    
#     # use boto3 library to get object from S3
#     s3 = boto3.client('s3')
#     s3_object = s3.get_object(Bucket = bucket, Key = key)
#     data = s3_object['Body'].read().decode('utf-8')
    
#     # read CSV
#     csv_data = csv.reader(data.splitlines())
#     print(csv_data)


import boto3
import csv
s3 = boto3.client('s3')
def handler(event, context):
    # Get key and bucket informaition
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    # use boto3 library to get object from S3
    s3 = boto3.client('s3')
    s3_object = s3.get_object(Bucket=bucket, Key=key)
    data = s3_object['Body'].read().decode('utf-8')
    # read CSV
    csv_data = csv.reader(data.splitlines())
    # Form all the lines of data into a list of lists
    all_lines = []
    for lines in csv_data:
        all_lines.append(lines)
    print(all_lines)
    return {"message": "success!!! Check the cloud watch logs for this lambda in cloudwatch https://eu-west-1.console.aws.amazon.com/cloudwatch/home?region=eu-west-1#logsV2:log-groups"}