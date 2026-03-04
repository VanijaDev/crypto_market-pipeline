from airflow.sdk import DAG # pyright: ignore[reportUnknownVariableType, reportMissingImports]
from airflow.operators.python import PythonOperator # pyright: ignore[reportUnknownVariableType, reportMissingImports]
from datetime import datetime
from typing import Any

from src.extract.fetch_prices import fetch_prices
from src.transform.transform_prices import transform_raw_json_to_clean_df
from src.load.upload_to_s3 import upload_json_to_s3, upload_csv_to_s3
from src.load.load_to_snowflake import load_df_to_snowflake

def _fetch_and_upload_raw() -> list[dict[str, Any]]:
  fetched_prices = fetch_prices()
  now = datetime.now()
  s3_path = f"raw/prices/{now.year}/{now.month:02d}/{now.day:02d}/prices.json"
  upload_json_to_s3(fetched_prices, s3_path)
  return fetched_prices

def _transform_and_load(**context: Any) -> None:
  data = context["ti"].xcom_pull(task_ids="fetch_and_upload_raw")
  df = transform_raw_json_to_clean_df(data)
  now = datetime.now()
  s3_path = f"clean/prices/{now.year}/{now.month:02d}/{now.day:02d}/prices.csv"
  upload_csv_to_s3(df.to_csv(index=False), s3_path)
  load_df_to_snowflake(df)


with DAG(
  dag_id="crypto_market_pipeline",
  schedule="@daily",
  start_date=datetime(2025, 1, 1),
  catchup=False,
) as dag: # pyright: ignore[reportUnknownVariableType]
  fetch_task = PythonOperator( # pyright: ignore[reportUnknownVariableType]
    task_id="fetch_and_upload_raw",
    python_callable=_fetch_and_upload_raw,
  )
  transform_task = PythonOperator( # pyright: ignore[reportUnknownVariableType]
    task_id="transform_and_load",
    python_callable=_transform_and_load,
  )
  _ = fetch_task >> transform_task # pyright: ignore[reportUnknownVariableType]