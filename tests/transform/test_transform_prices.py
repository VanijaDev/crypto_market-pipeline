# from src.transform.transform_prices import extract_required_fields_from_raw_json
# from typing import Any
# from unittest.mock import patch, call, MagicMock


# def test_transform_prices_returns_only_keep_fields_all():
#   """transform_prices() returns a list of dicts with only the fields in KEEP_FIELDS when all fields are present."""
#   raw_data: list[dict[str, Any]] = [
#     {
#       "id": "bitcoin",
#       "symbol": "btc",
#       "name": "Bitcoin",
#       "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
#       "current_price": 70187,
#       "market_cap": 1381651251183,
#       "market_cap_rank": 1,
#       "fully_diluted_valuation": 1474623675796,
#       "total_volume": 20154184933,
#       "high_24h": 70215,
#       "low_24h": 68060,
#       "price_change_24h": 2126.88,
#       "price_change_percentage_24h": 3.12502,
#       "market_cap_change_24h": 44287678051,
#       "market_cap_change_percentage_24h": 3.31157,
#       "circulating_supply": 19675987,
#       "total_supply": 21000000,
#       "max_supply": 21000000,
#       "ath": 73738,
#       "ath_change_percentage": -4.77063,
#       "ath_date": "2024-03-14T07:10:36.635Z",
#       "atl": 67.81,
#       "atl_change_percentage": 103455.83335,
#       "atl_date": "2013-07-06T00:00:00.000Z",
#       "roi": None,
#       "last_updated": "2024-04-07T16:49:31.736Z",
#       "market_cap_rank_with_rehypothecated": 1
#     }
#   ]

#   result = extract_required_fields_from_raw_json(raw_data)
#   assert result == [
#     {
#       "id": "bitcoin",
#       "symbol": "btc",
#       "name": "Bitcoin",
#       "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
#       "current_price": 70187,
#       "high_24h": 70215,
#       "low_24h": 68060,
#       "total_volume": 20154184933,
#       "market_cap": 1381651251183,
#       "market_cap_rank": 1,
#       "price_change_percentage_24h": 3.12502,
#       "circulating_supply": 19675987,
#       "last_updated": "2024-04-07T16:49:31.736Z"
#     }
#   ]


# @patch("src.transform.transform_prices.logger")
# def test_transform_prices_returns_only_keep_fields_some_missing(mock_logger: MagicMock):
#   """transform_prices() returns a list of dicts with only the fields in KEEP_FIELDS, filling in None for missing fields."""
#   raw_data: list[dict[str, Any]] = [
#     {
#       "id": "bitcoin",
#       "symbol": "btc",
#       "name": "Bitcoin",
#       "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
#       # "current_price": 70187,
#       "market_cap": 1381651251183,
#       "market_cap_rank": 1,
#       "fully_diluted_valuation": 1474623675796,
#       "total_volume": 20154184933,
#       # "high_24h": 70215,
#       "low_24h": 68060,
#       "price_change_24h": 2126.88,
#       "price_change_percentage_24h": 3.12502,
#       "market_cap_change_24h": 44287678051,
#       "market_cap_change_percentage_24h": 3.31157,
#       "circulating_supply": 19675987,
#       "total_supply": 21000000,
#       "max_supply": 21000000,
#       "ath": 73738,
#       "ath_change_percentage": -4.77063,
#       "ath_date": "2024-03-14T07:10:36.635Z",
#       "atl": 67.81,
#       "atl_change_percentage": 103455.83335,
#       "atl_date": "2013-07-06T00:00:00.000Z",
#       "roi": None,
#       "last_updated": "2024-04-07T16:49:31.736Z",
#       "market_cap_rank_with_rehypothecated": 1
#     }
#   ]

#   # test return values
#   result = extract_required_fields_from_raw_json(raw_data)
#   assert result == [
#     {
#       "id": "bitcoin",
#       "symbol": "btc",
#       "name": "Bitcoin",
#       "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
#       "current_price": None,
#       "high_24h": None,
#       "low_24h": 68060,
#       "total_volume": 20154184933,
#       "market_cap": 1381651251183,
#       "market_cap_rank": 1,
#       "price_change_percentage_24h": 3.12502,
#       "circulating_supply": 19675987,
#       "last_updated": "2024-04-07T16:49:31.736Z"
#     }
#   ]

#   # test logging
#   mock_logger.warning.assert_has_calls([
#     call("missing_field", field="current_price", coin_id="bitcoin"),
#     call("missing_field", field="high_24h", coin_id="bitcoin")
#   ], any_order=True)
