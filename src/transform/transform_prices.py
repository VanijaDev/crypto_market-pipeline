import structlog
from typing import Any

logger = structlog.get_logger()

KEEP_FIELDS = ["id", "symbol", "name", "image", "current_price", "high_24h", "low_24h", "total_volume", "market_cap", "market_cap_rank", "price_change_percentage_24h", "circulating_supply", "last_updated"]

def extract_required_fields_from_raw_json(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
  """Transforms raw JSON data from the CoinGecko API to only include the fields we care about."""
  result: list[dict[str, Any]] = []
  for coin in data:
    clean_coin: dict[str, Any] = {}
    for field in KEEP_FIELDS:
      if field in coin:
        clean_coin[field] = coin[field]
      else:
        clean_coin[field] = None
        logger.warning("missing_field", field=field, coin_id=coin.get("id", "unknown"))

    result.append(clean_coin)

  return result