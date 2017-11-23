import boto3
import json
import logging
import numpy

log = logging.getLogger('NumpyLoadTxtFunction')
log.setLevel(logging.ERROR)

def lambda_handler(event, context):
    """
    The function will be triggered when csv file is uploaded to an S3 bucket. 
    The function will read the CSV file and numpy will parse the CSV.
    Since numpy does not support reading from S3, we will need to download the file.
    """
    try:
        log.info("Creating an s3 client")
        s3 = boto3.resource('s3')
        records = event['Records']
        log.info("Number of records: " + str(len(records)))
        for record in records:
            log.info("Record: " + str(record))
            log.info("Reading newly put file: " + record['s3']['object']['key'])
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            # Download the file to lambda since numpy does not support reading from S3.
            log.info("Downloading file to lambda...")
            download_path = '/tmp/{}'.format(key)
            s3.meta.client.download_file(bucket, key, download_path)
            arr = dem_numpy_loadtxt(download_path)
            print len(arr)
    except Exception as e:
        log.error(e)

def dem_numpy_loadtxt(path):
    """
    The function demonstrates the usage of numpy.loadtxt to read the CSV file and 
    output a 1-D array
    """
    arr = numpy.loadtxt(path, delimiter='|', dtype=str)
    return arr
    
