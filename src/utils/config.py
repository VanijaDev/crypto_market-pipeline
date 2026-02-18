import os
from dotenv import load_dotenv

def get_config() -> dict[str, str]:
  load_dotenv()
  
  # COINGECKO_API_KEY
  api_key = os.getenv("COINGECKO_API_KEY")
  if api_key is None:
    raise RuntimeError("COINGECKO_API_KEY is not set. Add it to your .env file.")
  
  # AWS
  aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
  if aws_access_key_id is None:
    raise RuntimeError("AWS_ACCESS_KEY_ID is not set. Add it to your .env file.")

  aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
  if aws_secret_access_key is None:
    raise RuntimeError("AWS_SECRET_ACCESS_KEY is not set. Add it to your .env file.")

  aws_s3_bucket = os.getenv("AWS_S3_BUCKET")
  if aws_s3_bucket is None:
    raise RuntimeError("AWS_S3_BUCKET is not set. Add it to your .env file.")

  return {
    "coingecko_api_key": api_key,
    "aws_access_key_id": aws_access_key_id,
    "aws_secret_access_key": aws_secret_access_key,
    "aws_s3_bucket": aws_s3_bucket
  }