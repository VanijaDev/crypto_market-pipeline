from unittest.mock import patch, MagicMock
from src.extract.fetch_prices import fetch_prices
import httpx
import pytest


@patch("src.extract.fetch_prices.get_config")
@patch("src.extract.fetch_prices.httpx.get")
def test_fetch_prices_returns_coin_data(mock_get, mock_config): # type: ignore
  """fetch_prices() returns the parsed JSON list from the API response."""

  mock_config.return_value = {"coingecko_api_key": "test_key"}

  fake_coins: list[dict[str, object]] = [{"id": "bitcoin", "current_price": 50000}]
  mock_get.return_value.json.return_value = fake_coins # type: ignore
  
  result = fetch_prices()

  assert result == fake_coins


@patch("src.extract.fetch_prices.get_config")
@patch("src.extract.fetch_prices.httpx.get")
def test_fetch_prices_calls_correct_url(mock_get, mock_config): # type: ignore
  """fetch_prices() calls the CoinGecko /coins/markets endpoint with correct URL, params, and API key header."""

  mock_config.return_value = {"coingecko_api_key": "test_key"}
  mock_get.return_value.json.return_value = [] # type: ignore

  fetch_prices()

  mock_get.assert_called_once_with( # type: ignore
    "https://api.coingecko.com/api/v3/coins/markets",
    params = {
      "vs_currency": "usd",
      "ids": "bitcoin,ethereum,solana,avalanche-2,dogecoin,crypto-com-chain,karbo",
    },
    headers={"x-cg-demo-api-key": "test_key"}
  )
  

@patch("src.extract.fetch_prices.get_config")
@patch("src.extract.fetch_prices.httpx.get")
def test_fetch_prices_raises_on_http_error(mock_get, mock_config): # type: ignore
  """fetch_prices() propagates HTTPStatusError when the API returns an error status."""

  mock_config.return_value = {"coingecko_api_key": "test_key"}
  mock_get.return_value.raise_for_status.side_effect = httpx.HTTPStatusError( # type: ignore
    "403 Forbidden",
    request=MagicMock(),
    response=MagicMock(status_code=403)
  )

  with pytest.raises(httpx.HTTPStatusError):
    fetch_prices()