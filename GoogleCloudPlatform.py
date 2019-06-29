import numpy as np
import pandas as pd
import os
from google.cloud import storage
from google.cloud import bigquery
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Connecting with Google Cloud Storage~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'%path to your ServiceAccountKey(json file)%'
#os.environ['https_proxy'] = 'http://HOST:Port' ---> Only if neded while working on premises.


storage_client = storage.Client()
buckets = list(storage_client.list_buckets())
specific_bucket = storage_client.get_bucket('%name of specific bucket%')

blobs = list(specific_bucket.list_blobs())
specific_blob = specific_bucket.blob('%name of the blob%')
specific_blob.download_to_filename('name and extension of the file in which you want to download blob data')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Connecting with Google Cloud BigQuery~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'%path to your ServiceAccountKey (json file)%' '''Required only if the BQ project is different'''
