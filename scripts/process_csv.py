import boto3
import os
import os
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

def download_csv_from_s3():
    s3 = boto3.client('s3',
                      aws_access_key_id = AWS_ACCESS_KEY,
                      aws_secret_access_key = AWS_SECRET_KEY,
                      region_name = 'us-east-1')
    
    bucket_name = 'testorganizationbucket'
    object_key = 'netflix_titles.csv'
    local_file_path = './data/raw_movies.csv'

    if not os.path.exists('./data'):
        os.makedirs('./data')

    s3.download_file(bucket_name, object_key, local_file_path)
    print(f"Downloaded {object_key} to {local_file_path}", flush = True)
    return "Success"
    
download_csv_from_s3()