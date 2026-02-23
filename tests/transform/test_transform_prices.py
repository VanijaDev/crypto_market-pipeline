from src.transform.transform_prices import _raw_json_to_clean_df, _validate_prices, _enrich_prices, transform_raw_json_to_clean_df, KEEP_FIELDS # type: ignore[reportPrivateUsage]
from typing import Any
from unittest.mock import patch, MagicMock
import pandas as pd

# --- _raw_json_to_clean_df ---

@patch("src.transform.transform_prices.logger")
def test_raw_json_to_clean_df_warns_on_missing_field(mock_logger: MagicMock):
  RAW_DATA: list[dict[str, Any]] = [
    {
      "id": "bitcoin",
      "symbol": "btc",
      "name": "Bitcoin",
      "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
      "current_price": None,
      "market_cap": 1381651251183,
      "market_cap_rank": 1,
      "fully_diluted_valuation": 1474623675796,
      "total_volume": 20154184933,
      "high_24h": 70215,
      "low_24h": 68060,
      "price_change_24h": 2126.88,
      "price_change_percentage_24h": 3.12502,
      "market_cap_change_24h": 44287678051,
      "market_cap_change_percentage_24h": 3.31157,
      "circulating_supply": 19675987,
      "total_supply": 21000000,
      "max_supply": 21000000,
      "ath": 73738,
      "ath_change_percentage": -4.77063,
      "ath_date": "2024-03-14T07:10:36.635Z",
      "atl": 67.81,
      "atl_change_percentage": 103455.83335,
      "atl_date": "2013-07-06T00:00:00.000Z",
      "roi": None,
      "last_updated": "2024-04-07T16:49:31.736Z",
      "market_cap_rank_with_rehypothecated": 1
    },
    {
      "id": "bitcoin2",
      "symbol": "btc2",
      "name": "Bitcoin2",
      "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
      "current_price": None,
      "market_cap": 1381651251183,
      "market_cap_rank": 1,
      "fully_diluted_valuation": 1474623675796,
      "total_volume": 20154184933,
      "high_24h": 70215,
      "low_24h": 68060,
      "price_change_24h": 2126.88,
      "price_change_percentage_24h": 3.12502,
      "market_cap_change_24h": 44287678051,
      "market_cap_change_percentage_24h": 3.31157,
      "circulating_supply": 19675987,
      "total_supply": 21000000,
      "max_supply": 21000000,
      "ath": 73738,
      "ath_change_percentage": -4.77063,
      "ath_date": "2024-03-14T07:10:36.635Z",
      "atl": 67.81,
      "atl_change_percentage": 103455.83335,
      "atl_date": "2013-07-06T00:00:00.000Z",
      "roi": None,
      "last_updated": "2024-04-07T16:49:31.736Z",
      "market_cap_rank_with_rehypothecated": 1
    }
  ]
  _raw_json_to_clean_df(RAW_DATA)
  mock_logger.warning.assert_called_once_with("missing_field", field="current_price")

def test_raw_json_to_clean_df_must_return_all_the_required_fields():
  RAW_DATA: list[dict[str, Any]] = [
    {
      "id": "bitcoin",
      "symbol": "btc",
      "name": "Bitcoin",
      "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
      "current_price": 70187,
      "market_cap": 1381651251183,
      "market_cap_rank": 1,
      "fully_diluted_valuation": 1474623675796,
      "total_volume": 20154184933,
      "high_24h": 70215,
      "low_24h": 68060,
      "price_change_24h": 2126.88,
      "price_change_percentage_24h": 3.12502,
      "market_cap_change_24h": 44287678051,
      "market_cap_change_percentage_24h": 3.31157,
      "circulating_supply": 19675987,
      "total_supply": 21000000,
      "max_supply": 21000000,
      "ath": 73738,
      "ath_change_percentage": -4.77063,
      "ath_date": "2024-03-14T07:10:36.635Z",
      "atl": 67.81,
      "atl_change_percentage": 103455.83335,
      "atl_date": "2013-07-06T00:00:00.000Z",
      "roi": None,
      "last_updated": "2024-04-07T16:49:31.736Z",
      "market_cap_rank_with_rehypothecated": 1
    }
  ]
  res_df = _raw_json_to_clean_df(RAW_DATA)
  assert list(res_df.columns) == KEEP_FIELDS


# --- _validate_prices ---

@patch("src.transform.transform_prices.logger")
def test_validate_prices_not_empty(mock_logger: MagicMock):
  empty_df = pd.DataFrame()
  _validate_prices(empty_df)
  mock_logger.warning.assert_called_once_with("empty_dataframe")

@patch("src.transform.transform_prices.logger")
def test_validate_prices_any_value_is_null(mock_logger: MagicMock):
  RAW_DATA_BROKEN: list[dict[str, Any]] = [
    {
      "id": "bitcoin",
      "symbol": "btc",
      "name": "Bitcoin",
      "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
      "current_price": 70000,
      "market_cap": 1381651251183,
      "market_cap_rank": 1,
      "fully_diluted_valuation": 1474623675796,
      "total_volume": 20154184933,
      "high_24h": 70215,
      "low_24h": 68060,
      "price_change_24h": 2126.88,
      "price_change_percentage_24h": 3.12502,
      "market_cap_change_24h": 44287678051,
      "market_cap_change_percentage_24h": 3.31157,
      "circulating_supply": 19675987,
      "total_supply": 21000000,
      "max_supply": 21000000,
      "ath": 73738,
      "ath_change_percentage": -4.77063,
      "ath_date": "2024-03-14T07:10:36.635Z",
      "atl": 67.81,
      "atl_change_percentage": 103455.83335,
      "atl_date": "2013-07-06T00:00:00.000Z",
      "roi": None,
      "last_updated": "2024-04-07T16:49:31.736Z",
      "market_cap_rank_with_rehypothecated": 1
    },
    {
      "id": "bitcoin2",
      "symbol": "btc2",
      "name": "Bitcoin2",
      "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
      "current_price": None,
      "market_cap": 1381651251183,
      "market_cap_rank": 1,
      "fully_diluted_valuation": 1474623675796,
      "total_volume": 20154184933,
      "high_24h": 70215,
      "low_24h": 68060,
      "price_change_24h": 2126.88,
      "price_change_percentage_24h": 3.12502,
      "market_cap_change_24h": 44287678051,
      "market_cap_change_percentage_24h": 3.31157,
      "circulating_supply": 19675987,
      "total_supply": 21000000,
      "max_supply": 21000000,
      "ath": 73738,
      "ath_change_percentage": -4.77063,
      "ath_date": "2024-03-14T07:10:36.635Z",
      "atl": 67.81,
      "atl_change_percentage": 103455.83335,
      "atl_date": "2013-07-06T00:00:00.000Z",
      "roi": None,
      "last_updated": "2024-04-07T16:49:31.736Z",
      "market_cap_rank_with_rehypothecated": 1
    }
  ]
  df = pd.DataFrame(RAW_DATA_BROKEN)
  _validate_prices(df)
  mock_logger.warning.assert_called_once_with("missing_critical_field", field="current_price")

@patch("src.transform.transform_prices.logger")
def test_validate_prices_includes_duplicated_ids(mock_logger: MagicMock):
  RAW_DATA_BROKEN: list[dict[str, Any]] = [
    {
      "id": "bitcoin",
      "symbol": "btc",
      "name": "Bitcoin",
      "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
      "current_price": 70000,
      "market_cap": 1381651251183,
      "market_cap_rank": 1,
      "fully_diluted_valuation": 1474623675796,
      "total_volume": 20154184933,
      "high_24h": 70215,
      "low_24h": 68060,
      "price_change_24h": 2126.88,
      "price_change_percentage_24h": 3.12502,
      "market_cap_change_24h": 44287678051,
      "market_cap_change_percentage_24h": 3.31157,
      "circulating_supply": 19675987,
      "total_supply": 21000000,
      "max_supply": 21000000,
      "ath": 73738,
      "ath_change_percentage": -4.77063,
      "ath_date": "2024-03-14T07:10:36.635Z",
      "atl": 67.81,
      "atl_change_percentage": 103455.83335,
      "atl_date": "2013-07-06T00:00:00.000Z",
      "roi": None,
      "last_updated": "2024-04-07T16:49:31.736Z",
      "market_cap_rank_with_rehypothecated": 1
    },
    {
      "id": "bitcoin",
      "symbol": "btc2",
      "name": "Bitcoin2",
      "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
      "current_price": 70001,
      "market_cap": 1381651251183,
      "market_cap_rank": 1,
      "fully_diluted_valuation": 1474623675796,
      "total_volume": 20154184933,
      "high_24h": 70215,
      "low_24h": 68060,
      "price_change_24h": 2126.88,
      "price_change_percentage_24h": 3.12502,
      "market_cap_change_24h": 44287678051,
      "market_cap_change_percentage_24h": 3.31157,
      "circulating_supply": 19675987,
      "total_supply": 21000000,
      "max_supply": 21000000,
      "ath": 73738,
      "ath_change_percentage": -4.77063,
      "ath_date": "2024-03-14T07:10:36.635Z",
      "atl": 67.81,
      "atl_change_percentage": 103455.83335,
      "atl_date": "2013-07-06T00:00:00.000Z",
      "roi": None,
      "last_updated": "2024-04-07T16:49:31.736Z",
      "market_cap_rank_with_rehypothecated": 1
    }
  ]
  df = pd.DataFrame(RAW_DATA_BROKEN)
  _validate_prices(df)
  mock_logger.warning.assert_called_once_with("duplicate_ids")


# --- _enrich_prices ---

def test_enrich_prices():
  RAW_DATA: list[dict[str, Any]] = [
    {
      "id": "bitcoin",
      "symbol": "btc",
      "name": "Bitcoin",
      "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501401",
      "current_price": 68061,
      "market_cap": 1381651251183,
      "market_cap_rank": 1,
      "fully_diluted_valuation": 1474623675796,
      "total_volume": 20154184933,
      "high_24h": 70215,
      "low_24h": 68060,
      "price_change_24h": 2126.88,
      "price_change_percentage_24h": 3.12502,
      "market_cap_change_24h": 44287678051,
      "market_cap_change_percentage_24h": 3.31157,
      "circulating_supply": 19675987,
      "total_supply": 21000000,
      "max_supply": 21000000,
      "ath": 73738,
      "ath_change_percentage": -4.77063,
      "ath_date": "2024-03-14T07:10:36.635Z",
      "atl": 67.81,
      "atl_change_percentage": 103455.83335,
      "atl_date": "2013-07-06T00:00:00.000Z",
      "roi": None,
      "last_updated": "2024-04-07T16:49:31.736Z",
      "market_cap_rank_with_rehypothecated": 1
    },
    {
      "id": "bitcoin2",
      "symbol": "btc2",
      "name": "Bitcoin2",
      "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
      "current_price": 64000,
      "market_cap": 1381651251113,
      "market_cap_rank": 1,
      "fully_diluted_valuation": 1474623675796,
      "total_volume": 20154984933,
      "high_24h": 71215,
      "low_24h": 60060,
      "price_change_24h": 2126.88,
      "price_change_percentage_24h": 3.12502,
      "market_cap_change_24h": 44287678051,
      "market_cap_change_percentage_24h": 3.31157,
      "circulating_supply": 19675987,
      "total_supply": 21000000,
      "max_supply": 21000000,
      "ath": 73738,
      "ath_change_percentage": -4.77063,
      "ath_date": "2024-03-14T07:10:36.635Z",
      "atl": 67.81,
      "atl_change_percentage": 103455.83335,
      "atl_date": "2013-07-06T00:00:00.000Z",
      "roi": None,
      "last_updated": "2024-04-07T16:49:31.736Z",
      "market_cap_rank_with_rehypothecated": 1
    }
  ]
  df = pd.DataFrame(RAW_DATA)
  _enrich_prices(df)
  assert "volume_to_market_cap_ratio" in df.columns
  assert "price_position_in_range" in df.columns
  assert "price_distance_from_high_pct" in df.columns

  assert df["volume_to_market_cap_ratio"].iloc[0] == RAW_DATA[0]["total_volume"] / RAW_DATA[0]["market_cap"]
  assert df["price_position_in_range"].iloc[0] == (RAW_DATA[0]["current_price"] - RAW_DATA[0]["low_24h"]) / (RAW_DATA[0]["high_24h"] - RAW_DATA[0]["low_24h"])
  assert df["price_distance_from_high_pct"].iloc[0] == ((RAW_DATA[0]["current_price"] - RAW_DATA[0]["high_24h"]) / RAW_DATA[0]["high_24h"]) * 100
  assert pd.api.types.is_datetime64_any_dtype(df["last_updated"])

# --- transform_raw_json_to_clean_df ---

def test_transform_raw_json_to_clean_df():
  RAW_DATA: list[dict[str, Any]] = [
    {
      "id": "bitcoin",
      "symbol": "btc",
      "name": "Bitcoin",
      "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501401",
      "current_price": 65000,
      "market_cap": 1381651251183,
      "market_cap_rank": 1,
      "fully_diluted_valuation": 1474623675796,
      "total_volume": 20154184933,
      "high_24h": 70215,
      "low_24h": 68060,
      "price_change_24h": 2126.88,
      "price_change_percentage_24h": 3.12502,
      "market_cap_change_24h": 44287678051,
      "market_cap_change_percentage_24h": 3.31157,
      "circulating_supply": 19675987,
      "total_supply": 21000000,
      "max_supply": 21000000,
      "ath": 73738,
      "ath_change_percentage": -4.77063,
      "ath_date": "2024-03-14T07:10:36.635Z",
      "atl": 67.81,
      "atl_change_percentage": 103455.83335,
      "atl_date": "2013-07-06T00:00:00.000Z",
      "roi": None,
      "last_updated": "2024-04-07T16:49:31.736Z",
      "market_cap_rank_with_rehypothecated": 1
    },
    {
      "id": "bitcoin2",
      "symbol": "btc2",
      "name": "Bitcoin2",
      "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
      "current_price": 64000,
      "market_cap": 1381651251113,
      "market_cap_rank": 1,
      "fully_diluted_valuation": 1474623675796,
      "total_volume": 20154984933,
      "high_24h": 71215,
      "low_24h": 60060,
      "price_change_24h": 2126.88,
      "price_change_percentage_24h": 3.12502,
      "market_cap_change_24h": 44287678051,
      "market_cap_change_percentage_24h": 3.31157,
      "circulating_supply": 19675987,
      "total_supply": 21000000,
      "max_supply": 21000000,
      "ath": 73738,
      "ath_change_percentage": -4.77063,
      "ath_date": "2024-03-14T07:10:36.635Z",
      "atl": 67.81,
      "atl_change_percentage": 103455.83335,
      "atl_date": "2013-07-06T00:00:00.000Z",
      "roi": None,
      "last_updated": "2024-04-07T16:49:31.736Z",
      "market_cap_rank_with_rehypothecated": 1
    }
  ]
  clean_df = transform_raw_json_to_clean_df(RAW_DATA)
  assert not clean_df.empty
  assert set(clean_df.columns) == set(KEEP_FIELDS + ["volume_to_market_cap_ratio", "price_position_in_range", "price_distance_from_high_pct"])
  assert pd.api.types.is_datetime64_any_dtype(clean_df["last_updated"])
