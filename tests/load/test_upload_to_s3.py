import json
from unittest.mock import patch
from src.load.upload_to_s3 import upload_json_to_s3

@patch("src.load.upload_to_s3.get_config")
@patch("src.load.upload_to_s3.boto3.client")
def test_upload_to_s3_calls_put_object(mock_boto3_client, mock_config): # type: ignore
  """upload_to_s3() uploads JSON-encoded data to the correct s3 bucket and path."""

  mock_config.return_value = {
    "aws_access_key_id": "test_aws_access_key_id",
    "aws_secret_access_key": "test_aws_secret_access_key",
    "aws_s3_bucket": "test_aws_s3_bucket"
  }

  fake_data: list[dict[str, object]] = [{"id": "bitcoin", "current_price": 50000}]
  s3_path = "raw/prices/2026/02/18/prices.json"

  upload_json_to_s3(fake_data, s3_path)

  mock_boto3_client.return_value.put_object.assert_called_once_with( # type: ignore
    Bucket="test_aws_s3_bucket",
    Key=s3_path,
    Body=json.dumps(fake_data).encode("utf-8"),
    ContentType="application/json"
  )