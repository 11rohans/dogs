import boto3
import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

IAMAccessKey = config['DEFAULT']["IAMAccessKey"]
IAMSecretKey = config['DEFAULT']["IAMSecretKey"]
s3_region = config['DEFAULT']["s3_region"]

s3_bucket = config['DEFAULT']["s3_bucket"]

s3 = boto3.resource(
    's3',
    aws_access_key_id=IAMAccessKey,
    aws_secret_access_key=IAMSecretKey,
    region_name=s3_region
    )

image_direc = "dogs/static/Images"

for species_full in os.listdir(image_direc):

    species = species_full.split("-")[1]

    print("uploading %s" % (species))

    for dog in os.listdir(image_direc + "/" + species_full):
        key = species + "/" + dog
        data = open(image_direc + "/" + species_full + "/" + dog, 'rb')

        s3.Bucket(s3_bucket).put_object(Key=key, Body=data)


# file_path = "Images/n02085620-Chihuahua/n02085620_199.jpg"
# data = open(image_direc + file_path, 'rb')
