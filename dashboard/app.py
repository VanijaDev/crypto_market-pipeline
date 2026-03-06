import pandas as pd
import streamlit as st
import snowflake.connector

from src.utils.config import get_config

st.set_page_config(
  page_title="Crypto Market Dashboard",
  page_icon="📈",
  layout="wide"
)

@st.cache_resource
def _get_snowflake_connection() -> snowflake.connector.SnowflakeConnection:
  config = get_config()
  return snowflake.connector.connect( # pyright: ignore[reportUnknownMemberType]
    user=config["snowflake_user"],
    password=config["snowflake_password"],
    account=config["snowflake_account"],
    warehouse=config["snowflake_warehouse"],
    database=config["snowflake_database"],
    schema=config["snowflake_schema"]
  )

@st.cache_data(ttl=300)
def _load_prices() -> pd.DataFrame:
  conn = _get_snowflake_connection()
  cursor = conn.cursor()
  cursor.execute("""
    SELECT * FROM prices
    QUALIFY ROW_NUMBER() OVER (PARTITION BY id ORDER BY ingested_at DESC) = 1
    ORDER BY market_cap_rank ASC
  """)
  return cursor.fetch_pandas_all()

def main() -> None:
  st.title("Crypto Market Dashboard")

  df = _load_prices()

  # Sidebar filter
  all_symbols = df["SYMBOL"].str.upper().unique().tolist()
  selected = st.sidebar.multiselect(
    "Filter coins",
    options=all_symbols,
    default=all_symbols
  )
  df = df[df["SYMBOL"].str.upper().isin(selected)]

  # Chart 1: Top 10 by Market Cap
  st.subheader("Top 10 by Market Cap")
  top10 = df.nsmallest(10, "MARKET_CAP_RANK")[["NAME", "MARKET_CAP"]].set_index("NAME")
  st.bar_chart(top10) # pyright: ignore[reportUnknownMemberType]

  # Chart 2: Price Change Leaderboard
  st.subheader("24h Price Change")
  leaderboard = (
    df[["NAME", "SYMBOL", "CURRENT_PRICE", "PRICE_CHANGE_PERCENTAGE_24H"]]
    .sort_values("PRICE_CHANGE_PERCENTAGE_24H", ascending=False)
    .reset_index(drop=True)
  )
  st.dataframe( # pyright: ignore[reportUnknownMemberType]
    leaderboard.style.background_gradient(
      subset=["PRICE_CHANGE_PERCENTAGE_24H"], cmap="RdYlGn"
    ),
    use_container_width=True,
  )

  # Chart 3: Volume vs Market Cap
  st.subheader("Volume vs Market Cap")
  st.scatter_chart( # pyright: ignore[reportUnknownMemberType]
    df,
    x = "MARKET_CAP",
    y = "TOTAL_VOLUME",
    color="PRICE_CHANGE_PERCENTAGE_24H",
    size="MARKET_CAP",
  )

main()