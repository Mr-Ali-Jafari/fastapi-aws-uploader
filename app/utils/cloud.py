import boto3

async def upload_file_to_s3(file_content: bytes, filename: str, aws_access_key: str, aws_secret_key: str, bucket_name: str):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name='us-east-1'
    )

    s3_client.put_object(
        Bucket=bucket_name,
        Key=filename,
        Body=file_content
    )
    print(f"File {filename} uploaded to S3.")
