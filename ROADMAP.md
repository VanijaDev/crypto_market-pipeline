# Development Roadmap

## Phase 1: Project Setup
- [ ] Create Python virtual environment (3.12+)
- [ ] Install initial dependencies (httpx, python-dotenv)
- [ ] Create project folder structure
- [ ] Create `.env` file (from template)
- [ ] Git initial commit

## Phase 2: CryptoCompare API
- [ ] Register at CryptoCompare
- [ ] Get free API key
- [ ] Save API key in `.env`
- [ ] Write Python script to fetch daily OHLCV data
- [ ] Test locally, inspect and understand the response

## Phase 3: AWS S3 Storage
- [ ] Create AWS account (free tier)
- [ ] Create IAM user with S3 permissions
- [ ] Create S3 bucket
- [ ] Save AWS credentials in `.env`
- [ ] Write upload script (raw JSON, partitioned by date)
- [ ] Test: fetch from API -> upload to S3

## Phase 4: Data Transformation
- [ ] Design clean data schema (columns, types)
- [ ] Write transformation logic (raw JSON -> clean tabular format)
- [ ] Write tests for transformations

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
