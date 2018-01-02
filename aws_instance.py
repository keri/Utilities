import boto3



def create_bucket(bucket_name):
    s3 = boto3.client("s3")

    try:
        s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': 'us-west-2'},
    )
    except Exception as e:
        print(e)  # Note: BucketAlreadyOwnedByYou means you already created the bucket.

def list_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    buckets = response['Buckets']
    return([bucket['Name'] for bucket in buckets])

def list_contents(bucket_name):
    s3 = boto3.client("s3")
    response = s3.list_objects(
    Bucket=bucket_name
    )

    return([item['Key'] for item in response['Contents']])

def download_file(bucket, key, local_filename):
    '''grabs a file from a bucket to an instance or local machine'''
    '''local_filename is the file that is going to be saved as'''
    '''key is the file path in the bucket /file_name'''
    s3 = boto3.client("s3")
    s3.download_file(Bucket=bucket, Key=key, Filename=local_filename)

def upload_file(local_filename, bucket, key):
    '''upload a file from instance to bucket. Key is file name in the bucket'''
    s3 = boto3.client('s3')
    s3.upload_file(Bucket=bucket, Filename=local_filename, Key=key)

def create_instance(ImageId='ami-d0f506b0', InstanceType='t2.micro'):
    ec2.create_instances(ImageId=ImageId,
                     InstanceType=InstanceType,
                     MinCount=1, MaxCount=1,
                     )

def transfer_between_buckets(Bucket=from_bucket, key=key, local_filename=key):
    '''transfers a file from one bucket to another using the same file name as default'''
    '''key is the file_path and file name from the bucket and defaulting to same file name and file_path
    in new bucket.'''
    s3 = boto3.client('s3')
    download_file(from_bucket, key, key)
    upload_file(key, bucket, key)
