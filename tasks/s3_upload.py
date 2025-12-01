import boto3
import json

def upload_file_to_s3(data: dict, bucket_name: str, file_name: str) -> bool:
    """
    Upload a file to an S3 bucket.

    Args:
        data (dict): The data to be uploaded as a JSON file.
        bucket_name (str): The name of the S3 bucket.
        file_name (str): The name of the file to be created in the S3 bucket.

    Returns:
        bool: True if the file was uploaded successfully, False otherwise.
    """

    # Create an S3 client
    s3_client = boto3.client('s3')

    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=json.dumps(data, indent=2),
            ContentType="application/json",
            ACL="public-read"
        )
        print(f"Data uploaded to {bucket_name}/{file_name} successfully.")
        return True
    except Exception as e:
        print(f"An error occurred while uploading data to {bucket_name}/{file_name}:\n{e}")
        return False