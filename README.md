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
