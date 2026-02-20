import structlog
import pandas as pd
from enum import StrEnum
from typing import Any

logger = structlog.get_logger()

class Fields(StrEnum):
    ID = "id"
    SYMBOL = "symbol"
    NAME = "name"
    IMAGE = "image"
    CURRENT_PRICE = "current_price"
    HIGH_24H = "high_24h"
    LOW_24H = "low_24h"
    TOTAL_VOLUME = "total_volume"
    MARKET_CAP = "market_cap"
    MARKET_CAP_RANK = "market_cap_rank"
    PRICE_CHANGE_PERCENTAGE_24H = "price_change_percentage_24h"
    CIRCULATING_SUPPLY = "circulating_supply"
    LAST_UPDATED = "last_updated"
    PRICE_RANGE_24H = "price_range_24h"
    PRICE_RANGE_PCT_24H = "price_range_pct_24h"

KEEP_FIELDS = [Fields.ID, Fields.SYMBOL, Fields.NAME, Fields.IMAGE, Fields.CURRENT_PRICE, Fields.HIGH_24H, Fields.LOW_24H, Fields.TOTAL_VOLUME, Fields.MARKET_CAP, Fields.MARKET_CAP_RANK, Fields.PRICE_CHANGE_PERCENTAGE_24H, Fields.CIRCULATING_SUPPLY, Fields.LAST_UPDATED]
CRITICAL_FIELDS = [Fields.CURRENT_PRICE, Fields.MARKET_CAP, Fields.MARKET_CAP_RANK, Fields.CIRCULATING_SUPPLY]

## This was the original cleanup function
# def extract_required_fields_from_raw_json(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
#   """Transforms raw JSON data from the CoinGecko API to only include the fields we care about."""
#   result: list[dict[str, Any]] = []
#   for coin in data:
#     clean_coin: dict[str, Any] = {}
#     for field in KEEP_FIELDS:
#       if field in coin:
#         clean_coin[field] = coin[field]
#       else:
#         clean_coin[field] = None
#         logger.warning("missing_field", field=field, coin_id=coin.get("id", "unknown"))

#     result.append(clean_coin)

#   return result

def transform_raw_json_to_clean_df(data: list[dict[str, Any]]) -> pd.DataFrame:
  """Transforms raw JSON data to a cleaned pandas DataFrame."""
  df = _raw_json_to_clean_df(data)
  _validate_prices(df)
  df = _enrich_prices(df)

  return df


def _raw_json_to_clean_df(data: list[dict[str, Any]]) -> pd.DataFrame:
  """Transforms raw JSON data to a pandas DataFrame."""
  df = pd.DataFrame(data).reindex(columns=KEEP_FIELDS)

  for field in KEEP_FIELDS:
    if df[field].isnull().all():
      logger.warning("missing_field", field=field)

  return df

def _validate_prices(df: pd.DataFrame) -> None:
  """Validates the cleaned DataFrame to ensure it meets the required criteria."""
  if df.empty:
    logger.warning("empty_dataframe")
    return
  
  for field in CRITICAL_FIELDS:
    if df[field].isnull().any():
      logger.warning("missing_critical_field", field=field)

  if (df[Fields.CURRENT_PRICE] <= 0).any():
    logger.warning("invalid_price")

  if df[Fields.ID].duplicated().any():
    logger.warning("duplicate_ids")

  if (df[Fields.CURRENT_PRICE] < df[Fields.LOW_24H]).any() or (df[Fields.CURRENT_PRICE] > df[Fields.HIGH_24H]).any():
    logger.warning("price_out_of_range")

  if (df[Fields.MARKET_CAP_RANK] < 1).any():
    logger.warning("invalid_market_cap_rank")

def _enrich_prices(df: pd.DataFrame) -> pd.DataFrame:
  """Enriches the DataFrame with additional calculated fields."""
  df[Fields.PRICE_RANGE_24H] = df[Fields.HIGH_24H] - df[Fields.LOW_24H]
  df[Fields.PRICE_RANGE_PCT_24H] = (df[Fields.PRICE_RANGE_24H] / df[Fields.LOW_24H]) * 100
  df[Fields.LAST_UPDATED] = pd.to_datetime(df[Fields.LAST_UPDATED], utc=True)

  return df