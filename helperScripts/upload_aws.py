import boto3
import configparser
import os
import pickle
from collections import defaultdict


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

key_set = defaultdict(list)

for species_full in os.listdir(image_direc):

    species = species_full.split("-")[1]

    print("uploading %s" % (species))

    for i, dog in enumerate(os.listdir(image_direc + "/" + species_full)):
        key = species + "/" + str(i)
        data = open(image_direc + "/" + species_full + "/" + dog, 'rb')

        key_set[species].append(key)

        s3.Bucket(s3_bucket).put_object(Key=key, Body=data)

with open("dogs/dogKeys.pickle", "wb") as f:
    pickle.dump(key_set, f, protocol=pickle.HIGHEST_PROTOCOL)
