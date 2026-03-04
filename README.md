# Crypto Market Analytics Data Pipeline

A production-like data engineering pipeline that automatically collects cryptocurrency market data from a public API, stores it in the cloud, transforms it, and makes it available for analytics and visualization.

## Goal

A portfolio project to get hands-on experience building an end-to-end data engineering pipeline.

## How It Works

1. **Ingest** -- A Python script fetches daily crypto data from the [CoinGecko API](https://www.coingecko.com/en/api)
2. **Store** -- Raw data lands in AWS S3 in a partitioned format
3. **Orchestrate** -- Apache Airflow runs the workflow automatically every day
4. **Transform & Load** -- Processed data is loaded into a Snowflake data warehouse
5. **Visualize** -- A public Streamlit dashboard displays key metrics and trends

## Tech Stack

| Layer            | Tool             | Role                               |
| ---------------- | ---------------- | ---------------------------------- |
| Data extraction  | Python           | API calls, response parsing        |
| Orchestration    | Apache Airflow   | Daily scheduled jobs               |
| Cloud storage    | AWS S3           | Raw and partitioned data           |
| Data warehouse   | Snowflake        | Clean data for analytics           |
| Dashboard        | Streamlit        | Interactive visualization          |
| Containerization | Docker           | Reproducible environments          |
| Deployment       | Railway / Render | Hosts Airflow + dashboard publicly |

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
make airflow-build   # Build the custom Docker image
make airflow-init    # Initialize the database (run once)
make airflow-start   # Start all services in the background
make airflow-stop    # Stop all services
make airflow-logs    # Tail logs from all services
```

Airflow UI is available at **http://localhost:8080** (default credentials: `airflow` / `airflow`).

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
dashboard/       # Streamlit app (coming soon)
tests/           # Mirrors src/ structure
config/          # SQL schemas
```

## Running Tests

```bash
make test
```
