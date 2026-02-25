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
  
  # SNOWFLAKE
  snowflake_account = os.getenv("SNOWFLAKE_ACCOUNT")
  if snowflake_account is None:
    raise RuntimeError("SNOWFLAKE_ACCOUNT is not set. Add it to your .env file.")

  snowflake_user = os.getenv("SNOWFLAKE_USER")
  if snowflake_user is None:
    raise RuntimeError("SNOWFLAKE_USER is not set. Add it to your .env file.")

  snowflake_password = os.getenv("SNOWFLAKE_PASSWORD")
  if snowflake_password is None:
    raise RuntimeError("SNOWFLAKE_PASSWORD is not set. Add it to your .env file.")

  snowflake_database = os.getenv("SNOWFLAKE_DATABASE")
  if snowflake_database is None:
    raise RuntimeError("SNOWFLAKE_DATABASE is not set. Add it to your .env file.")
  
  snowflake_table = os.getenv("SNOWFLAKE_TABLE")
  if snowflake_table is None:
    raise RuntimeError("SNOWFLAKE_TABLE is not set. Add it to your .env file.")

  snowflake_schema = os.getenv("SNOWFLAKE_SCHEMA")
  if snowflake_schema is None:
    raise RuntimeError("SNOWFLAKE_SCHEMA is not set. Add it to your .env file.")

  snowflake_warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
  if snowflake_warehouse is None:
    raise RuntimeError("SNOWFLAKE_WAREHOUSE is not set. Add it to your .env file.")

  return {
    "coingecko_api_key": api_key,
    "aws_access_key_id": aws_access_key_id,
    "aws_secret_access_key": aws_secret_access_key,
    "aws_s3_bucket": aws_s3_bucket,
    "snowflake_account": snowflake_account,
    "snowflake_user": snowflake_user,
    "snowflake_password": snowflake_password,
    "snowflake_database": snowflake_database,
    "snowflake_table": snowflake_table,
    "snowflake_warehouse": snowflake_warehouse,
    "snowflake_schema": snowflake_schema
  }