import boto3
import os
import numpy as np
from datetime import datetime
import json
import random

s3_client = boto3.client("s3", region_name='us-east-1')
k_client = boto3.client('kinesis', region_name='us-east-1')

str2date = lambda x: datetime.strptime(x.decode("utf-8"), '%Y-%m-%d')
str2time = lambda x: datetime.strptime(x.decode("utf-8"), '%H:%M:%S')
def lambda_handler(event, context):
    print(event)
    file="/tmp/"+event["Records"][0]["s3"]["object"]["key"].split('/')[-1]
    bucket=event["Records"][0]["s3"]["bucket"]["name"]
    key=event["Records"][0]["s3"]["object"]["key"]
    print(file)
    print(bucket)
    print(key)
    s3_client.download_file(bucket,key,file)
    data=np.genfromtxt(file, delimiter=',', skip_header=6,converters = {5: str2date,6: str2time})
    records=[{'Data':json.dumps({'lat':i[0],'long':i[1],'altitude':i[3],'days_since_1900':i[4],'log_date':datetime.strftime(i[5],'%Y%m%d'), 'log_time': datetime.strftime(i[6],'%H%M%S')}),'PartitionKey':str(random.randint(0, 100))} for i in data]
    out=k_client.put_records(Records=records,StreamName="myInputStream")
    print(out)
