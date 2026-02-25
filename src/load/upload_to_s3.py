import json
import boto3
from typing import Any
from src.utils.config import get_config
from mypy_boto3_s3 import S3Client


def upload_json_to_s3(data: list[dict[str, Any]], path: str) -> None:
  """
  Uploads json data to S3.
  
  :param data: The data to upload.
  :param path: The S3 path to upload the data to.
  """
  _upload_bytes_to_s3(json.dumps(data).encode("utf-8"), path, "application/json")


def upload_csv_to_s3(data: str, path: str) -> None:
  """
  Uploads csv data to S3.
  
  :param data: The CSV data to upload.
  :param path: The S3 path to upload the data to.
  """
  _upload_bytes_to_s3(data.encode("utf-8"), path, "text/csv")


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