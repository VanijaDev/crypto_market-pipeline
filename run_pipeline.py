from datetime import datetime, timezone
from src.utils.config import get_config
from src.extract.fetch_prices import fetch_prices
from src.transform.transform_prices import transform_raw_json_to_clean_df
from src.load.upload_to_s3 import upload_json_to_s3, upload_csv_to_s3
from src.load.load_to_snowflake import load_df_to_snowflake

config = get_config()
now = datetime.now(timezone.utc)

data = fetch_prices()
s3_path = f"raw/prices/{now.year}/{now.month:02d}/{now.day:02d}/prices.json"
upload_json_to_s3(data, s3_path)
print(f"✅ Uploaded json with {len(data)} coins to s3://{config['aws_s3_bucket']}/{s3_path}")

clean_data = transform_raw_json_to_clean_df(data)
clean_s3_path = f"clean/prices/{now.year}/{now.month:02d}/{now.day:02d}/prices.csv"
upload_csv_to_s3(clean_data.to_csv(index=False), clean_s3_path)
print(f"✅ Uploaded cleaned csv with {len(clean_data)} coins to s3://{config['aws_s3_bucket']}/{clean_s3_path}")

load_df_to_snowflake(clean_data)
print(f"✅ Loaded cleaned data with {len(clean_data)} coins to Snowflake table {config['snowflake_table']}")