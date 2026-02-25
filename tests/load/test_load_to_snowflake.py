import pytest
import pandas as pd
from unittest.mock import patch
from src.load.load_to_snowflake import load_df_to_snowflake, _get_snowflake_connection # pyright: ignore[reportPrivateUsage]


@patch("src.load.load_to_snowflake.write_pandas")
@patch("src.load.load_to_snowflake.get_config")
@patch("src.load.load_to_snowflake.connect")
def test_load_df_to_snowflake_calls_write_pandas(mock_connect, mock_get_config, mock_write_pandas): # type: ignore
  """Test that load_df_to_snowflake calls write_pandas with the correct arguments."""
  mock_get_config.return_value = {
    "snowflake_user": "test_user",
    "snowflake_password": "test_password",
    "snowflake_account": "test_account",
    "snowflake_warehouse": "test_warehouse",
    "snowflake_database": "test_database",
    "snowflake_schema": "test_schema",
    "snowflake_table": "test_snowflake_table"
  }
  df = pd.DataFrame({
    "coin": ["bitcoin", "ethereum"],
    "price": [50000, 4000]
  })
  load_df_to_snowflake(df)
  mock_write_pandas.assert_called_once_with(mock_connect.return_value, df, table_name="test_snowflake_table", quote_identifiers=False, use_logical_type=True) # pyright: ignore[reportUnknownMemberType]


@patch("src.load.load_to_snowflake.write_pandas")
@patch("src.load.load_to_snowflake.get_config")
@patch("src.load.load_to_snowflake.connect")
def test_load_df_to_snowflake_adds_ingested_at_column(mock_connect, mock_get_config, mock_write_pandas): # type: ignore
  """Test that load_df_to_snowflake adds an 'ingested_at' column to the DataFrame before loading."""
  mock_get_config.return_value = {
    "snowflake_user": "test_user",
    "snowflake_password": "test_password",
    "snowflake_account": "test_account",
    "snowflake_warehouse": "test_warehouse",
    "snowflake_database": "test_database",
    "snowflake_schema": "test_schema",
    "snowflake_table": "test_snowflake_table"
  }
  df = pd.DataFrame({
    "coin": ["bitcoin", "ethereum"],
    "price": [50000, 4000]
  })
  load_df_to_snowflake(df)
  assert "ingested_at" in df.columns
  assert pd.api.types.is_datetime64_any_dtype(df["ingested_at"])



@patch("src.load.load_to_snowflake.write_pandas")
@patch("src.load.load_to_snowflake.get_config")
@patch("src.load.load_to_snowflake.connect")
def test_load_df_to_snowflake_closes_connection_on_success(mock_connect, mock_get_config, mock_write_pandas): # type: ignore
  """Test that load_df_to_snowflake closes the Snowflake connection on success."""
  mock_get_config.return_value = {
    "snowflake_user": "test_user",
    "snowflake_password": "test_password",
    "snowflake_account": "test_account",
    "snowflake_warehouse": "test_warehouse",
    "snowflake_database": "test_database",
    "snowflake_schema": "test_schema",
    "snowflake_table": "test_snowflake_table"
  }
  df = pd.DataFrame({
    "coin": ["bitcoin", "ethereum"],
    "price": [50000, 4000]
  })
  load_df_to_snowflake(df)
  mock_connect.return_value.close.assert_called_once() # pyright: ignore[reportUnknownMemberType]



@patch("src.load.load_to_snowflake.write_pandas")
@patch("src.load.load_to_snowflake.get_config")
@patch("src.load.load_to_snowflake.connect")
def test_load_df_to_snowflake_closes_connection_on_error(mock_connect, mock_get_config, mock_write_pandas): # type: ignore
  """Test that load_df_to_snowflake closes the Snowflake connection on error."""
  mock_get_config.return_value = {
    "snowflake_user": "test_user",
    "snowflake_password": "test_password",
    "snowflake_account": "test_account",
    "snowflake_warehouse": "test_warehouse",
    "snowflake_database": "test_database",
    "snowflake_schema": "test_schema",
    "snowflake_table": "test_snowflake_table"
  }
  df = pd.DataFrame({
    "coin": ["bitcoin", "ethereum"],
    "price": [50000, 4000]
  })
  
  mock_write_pandas.side_effect = Exception("write failed")  
  with pytest.raises(Exception):
    load_df_to_snowflake(df)
  mock_connect.return_value.close.assert_called_once() # pyright: ignore[reportUnknownMemberType]



@patch("src.load.load_to_snowflake.get_config")
@patch("src.load.load_to_snowflake.connect")
def test_get_snowflake_connection(mock_connect, mock_get_config): # type: ignore
  """Test that _get_snowflake_connection returns a Snowflake connection with the correct parameters."""
  mock_get_config.return_value = {
    "snowflake_user": "test_user",
    "snowflake_password": "test_password",
    "snowflake_account": "test_account",
    "snowflake_warehouse": "test_warehouse",
    "snowflake_database": "test_database",
    "snowflake_schema": "test_schema",
    "snowflake_table": "test_snowflake_table"
  }
  conn = _get_snowflake_connection()
  mock_connect.assert_called_once_with( # pyright: ignore[reportUnknownMemberType]
    user="test_user",
    password="test_password",
    account="test_account",
    warehouse="test_warehouse",
    database="test_database",
    schema="test_schema"
  )
  assert conn == mock_connect.return_value # pyright: ignore[reportUnknownMemberType]