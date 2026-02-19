import json
import boto3
from typing import Any
from src.utils.config import get_config
from src.extract.fetch_prices import fetch_prices
from mypy_boto3_s3 import S3Client
from datetime import datetime, timezone


def upload_to_s3(data: list[dict[str, Any]], s3_object_path: str) -> None:
  config = get_config()
  client: S3Client = boto3.client( # type: ignore
    "s3",
    aws_access_key_id=config["aws_access_key_id"],
    aws_secret_access_key=config["aws_secret_access_key"],
  )

  client.put_object(
    Bucket=config["aws_s3_bucket"],
    Key=s3_object_path,
    Body=json.dumps(data).encode("utf-8"),
    ContentType="application/json"
  )

# To test: python -m src.load.upload_to_s3
if __name__ == "__main__":
  config = get_config()
  now = datetime.now(timezone.utc)
  s3_path = f"raw/prices/{now.year}/{now.month:02d}/{now.day:02d}/prices.json"

  data = fetch_prices()
  upload_to_s3(data, s3_path)

  print(f"✅ Uploaded {len(data)} coins to s3://{config['aws_s3_bucket']}/{s3_path}")