# Crypto Market Analytics Data Pipeline

A production-like data engineering pipeline that automatically collects cryptocurrency market data from a public API, stores it in the cloud, transforms it, and makes it available for analytics and visualization.

**Live dashboard:** [cryptomarket-pipelinegit-9usngr4pkyfu6x9ulfrnwq.streamlit.app](https://cryptomarket-pipelinegit-9usngr4pkyfu6x9ulfrnwq.streamlit.app)

## Goal

A portfolio project to get hands-on experience building an end-to-end data engineering pipeline.

## Architecture

```
CoinGecko API
      │
      ▼
  fetch_prices.py          # Extract: daily market snapshot
      │
      ▼
  AWS S3 (raw layer)       # raw/prices/YYYY/MM/DD/prices.json
      │
      ▼
  transform_prices.py      # Clean, enrich, compute derived metrics
      │
      ├──► AWS S3 (clean layer)   # clean/prices/YYYY/MM/DD/prices.csv
      │
      └──► Snowflake (Prices table)
                │
                ▼
        Streamlit Dashboard  (hosted on Streamlit Community Cloud)
```

Orchestrated by **Apache Airflow** (DAG: `crypto_market_pipeline`, runs daily).

## Tech Stack

| Layer            | Tool                    | Role                                        |
| ---------------- | ----------------------- | ------------------------------------------- |
| Data extraction  | Python + httpx          | API calls, response parsing                 |
| Orchestration    | Apache Airflow          | Daily scheduled DAG                         |
| Cloud storage    | AWS S3                  | Raw JSON and clean CSV, partitioned by date |
| Data warehouse   | Snowflake               | Clean data for analytics                    |
| Dashboard        | Streamlit               | Interactive visualization                   |
| Containerization | Docker + docker-compose | Reproducible local Airflow environment      |

## Data Flow

Each daily run:

1. Fetches market data for tracked coins from the CoinGecko `/coins/markets` endpoint
2. Uploads raw JSON to S3 (`raw/prices/YYYY/MM/DD/prices.json`)
3. Transforms the data — drops unused fields, computes `volume_to_market_cap_ratio`, `price_position_in_range`, `price_distance_from_high_pct`
4. Uploads clean CSV to S3 (`clean/prices/YYYY/MM/DD/prices.csv`)
5. Loads into Snowflake `Prices` table (append — full history retained)

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (with containerd image store enabled)
- Python 3.12+
- Accounts: [CoinGecko API](https://www.coingecko.com/en/api) (free Demo plan), AWS S3, Snowflake

## Setup

**1. Clone the repo and create your environment file:**

```bash
cp .env.example .env
# Fill in your credentials in .env
```

**2. Create and activate a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**3. Set your Airflow user ID (Linux/Mac):**

```bash
echo "AIRFLOW_UID=$(id -u)" >> .env
```

## Running Airflow

```bash
make airflow-build    # Build the custom Docker image (first time only)
make airflow-init     # Initialize the database (first time only)
make airflow-start    # Start all services in the background
make airflow-stop     # Stop all services
make airflow-logs     # Tail logs from all services
make airflow-healthy  # Check container status
```

Airflow UI is available at **http://localhost:8080** (default credentials: `airflow` / `airflow`).

To trigger the pipeline manually: open the UI, find `crypto_market_pipeline`, and click **Trigger DAG**.

## Running the Dashboard Locally

```bash
make dashboard-run
```

Opens at **http://localhost:8501**.

## Running Tests

```bash
make test
```

## Project Structure

```
src/
  extract/       # CoinGecko API client
  transform/     # Data cleaning and transformation
  load/          # S3 and Snowflake loaders
  utils/         # Shared helpers (logging, config, retry)
airflow/
  dags/          # Airflow DAG definitions
  config/        # Airflow configuration
docker/
  Dockerfile           # Custom Airflow image with project dependencies
  docker-compose.yaml  # Full Airflow stack (scheduler, worker, webserver)
dashboard/       # Streamlit app
tests/           # Mirrors src/ structure
config/          # SQL schemas
```
