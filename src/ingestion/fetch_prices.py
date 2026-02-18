import json
import httpx
from typing import Any
from src.utils.config import get_config


def fetch_prices() -> list[dict[str, Any]]:
  config = get_config()

  url = "https://api.coingecko.com/api/v3/coins/markets"
  params = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum,solana,avalanche-2,dogecoin,crypto-com-chain,karbo",
  }
  headers={"x-cg-demo-api-key": config["coingecko_api_key"]}
  response = httpx.get(url, params=params, headers=headers)
  response.raise_for_status()
  return response.json()


# To test: python -m src.ingestion.fetch_prices
if __name__ == "__main__":
  data = fetch_prices()
  print(json.dumps(data, indent=2))