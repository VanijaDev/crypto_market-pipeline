import os
import json
import httpx
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("COINGECKO_API_KEY")

def fetch_prices():
  url = "https://api.coingecko.com/api/v3/coins/markets"
  params = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum,solana,avalanche-2,dogecoin,crypto-com-chain,karbo",
  }
  headers={"x-cg-demo-api-key": api_key}
  response = httpx.get(url, params=params, headers=headers)
  return response.json()