import boto3
import configparser
# import os

config = configparser.ConfigParser()
config.read('config.ini')

IAMAccessKey = config['DEFAULT']["IAMAccessKey"]
IAMSecretKey = config['DEFAULT']["IAMSecretKey"]
s3_region = config['DEFAULT']["s3_region"]

s3_bucket = config['DEFAULT']["s3_bucket"]

s3 = boto3.client(
    's3',
    aws_access_key_id=IAMAccessKey,
    aws_secret_access_key=IAMSecretKey,
    region_name=s3_region
    )

image_direc = "dogs/static/Images"

url = s3.generate_presigned_url('get_object',
                                Params={
                                    'Bucket': s3_bucket,
                                    'Key': 'African_hunting_dog/n02116738_10169.jpg', # noqa
                                },
                                ExpiresIn=3600)
print(url)
