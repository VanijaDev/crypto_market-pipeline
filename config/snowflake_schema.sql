--- 1
CREATE DATABASE IF NOT EXISTS CRYPTO_MARKET;
USE DATABASE CRYPTO_MARKET;
USE SCHEMA PUBLIC;

--- 2
USE DATABASE CRYPTO_MARKET;
USE SCHEMA PUBLIC;

CREATE TABLE IF NOT EXISTS Prices (
    id                              VARCHAR      NOT NULL,
    symbol                          VARCHAR      NOT NULL,
    name                            VARCHAR,
    image                           VARCHAR,
    current_price                   FLOAT,
    high_24h                        FLOAT,
    low_24h                         FLOAT,
    total_volume                    FLOAT,
    market_cap                      FLOAT,
    market_cap_rank                 INTEGER,
    price_change_percentage_24h     FLOAT,
    circulating_supply              FLOAT,
    last_updated                    TIMESTAMP_TZ,
    volume_to_market_cap_ratio      FLOAT,
    price_position_in_range         FLOAT,
    price_distance_from_high_pct    FLOAT,
    ingested_at                     TIMESTAMP_TZ DEFAULT CURRENT_TIMESTAMP()
);