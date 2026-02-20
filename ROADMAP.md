# Development Roadmap

## Phase 1: Project Setup ✅
- [x] Create Python virtual environment (3.12+)
- [x] Install initial dependencies (httpx, python-dotenv)
- [x] Create project folder structure
- [x] Create `.env` file (from template)
- [x] Git initial commit

## Phase 2: CoinGecko API
- [x] Register at CoinGecko
- [x] Get free Demo API key
- [x] Save API key in `.env`
- [x] Write Python script to fetch daily market snapshot data (`/coins/markets` endpoint)
- [x] Test locally, inspect and understand the response
- [x] Clean up `fetch_prices.py`: type hints, `raise_for_status()`, central config

> **API note:** Using `/coins/markets` endpoint — returns a daily snapshot per coin (not historical OHLCV).
> Each record includes: `id`, `symbol`, `name`, `image`, `current_price`, `high_24h`, `low_24h`,
> `total_volume`, `market_cap`, `market_cap_rank`, `price_change_percentage_24h`,
> `circulating_supply`, `last_updated`. Fields like `roi`, `ath`, `atl` will be dropped in transformation.

## Phase 3: AWS S3 Storage
- [x] Create AWS account (free tier)
- [x] Create IAM user with S3 permissions
- [x] Create S3 bucket
- [x] Save AWS credentials in `.env`
- [x] Write upload script (raw JSON, partitioned by date)
- [x] Test: fetch from API -> upload to S3
- [x] Write unit tests for `fetch_prices` (mock `httpx.get`)
- [x] Write unit tests for `upload_to_s3` (mock `boto3.client`)

## Phase 4: Data Transformation
- [x] Design clean data schema (columns, types) — keep: `id`, `symbol`, `name`, `image`, `current_price`, `high_24h`, `low_24h`, `total_volume`, `market_cap`, `market_cap_rank`, `price_change_percentage_24h`, `circulating_supply`, `last_updated`; drop: `roi`, `ath`, `atl` and related
- [x] Write transformation logic (raw JSON -> clean tabular format)
- [x] Write tests for transformations

## Phase 5: Snowflake
- [ ] Create Snowflake account (free trial)
- [ ] Create database, schema, and tables
- [ ] Save Snowflake credentials in `.env`
- [ ] Write loader script (S3 -> Snowflake)
- [ ] Test full flow: API -> S3 -> Snowflake

## Phase 6: Airflow Orchestration
- [ ] Set up Airflow with Docker
- [ ] Write DAG connecting all pipeline steps
- [ ] Test scheduled runs locally

## Phase 7: Streamlit Dashboard
- [ ] Build dashboard reading from Snowflake
- [ ] Add key charts: price trends, volume, top movers
- [ ] Test locally

## Phase 8: Deployment
- [ ] Containerize all services (Docker)
- [ ] Deploy to Railway / Render
- [ ] Verify public access works
