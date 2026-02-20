import json
import boto3
import csv
from typing import Any
from io import StringIO
from src.utils.config import get_config
from src.extract.fetch_prices import fetch_prices
from mypy_boto3_s3 import S3Client
from datetime import datetime, timezone
from src.transform.transform_prices import extract_required_fields_from_raw_json


def upload_json_to_s3(data: list[dict[str, Any]], path: str) -> None:
  """
  Uploads json data to S3.
  
  :param data: The data to upload.
  :param path: The S3 path to upload the data to.
  """
  _upload_bytes_to_s3(json.dumps(data).encode("utf-8"), path, "application/json")


def upload_csv_to_s3(data: list[dict[str, Any]], path: str) -> None:
  """
  Uploads csv data to S3.
  
  :param data: The CSV data to upload.
  :param path: The S3 path to upload the data to.
  """
  buffer = StringIO()
  writer = csv.DictWriter(buffer, fieldnames=data[0].keys())
  writer.writeheader()
  writer.writerows(data)
  _upload_bytes_to_s3(buffer.getvalue().encode("utf-8"), path, "text/csv")


def _upload_bytes_to_s3(data: bytes, path: str, content_type: str) -> None:
  """
  Uploads bytes data to S3.
  
  :param data: The bytes data to upload.
  :param path: The S3 path to upload the data to.
  :param content_type: The content type of the data.
  """
  config = get_config()
  client: S3Client = boto3.client( # type: ignore
    "s3",
    aws_access_key_id=config["aws_access_key_id"],
    aws_secret_access_key=config["aws_secret_access_key"],
  )

  client.put_object(
    Bucket=config["aws_s3_bucket"],
    Key=path,
    Body=data,
    ContentType=content_type
  )
  
# To test: python -m src.load.upload_to_s3
if __name__ == "__main__":
  config = get_config()
  now = datetime.now(timezone.utc)

  data = fetch_prices()
  s3_path = f"raw/prices/{now.year}/{now.month:02d}/{now.day:02d}/prices.json"
  upload_json_to_s3(data, s3_path)
  print(f"✅ Uploaded json with {len(data)} coins to s3://{config['aws_s3_bucket']}/{s3_path}")

  clean_data = extract_required_fields_from_raw_json(data)
  clean_s3_path = f"clean/prices/{now.year}/{now.month:02d}/{now.day:02d}/prices.csv"
  upload_csv_to_s3(clean_data, clean_s3_path)
  print(f"✅ Uploaded cleaned csv with {len(clean_data)} coins to s3://{config['aws_s3_bucket']}/{clean_s3_path}")