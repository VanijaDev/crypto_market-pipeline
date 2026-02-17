# Crypto Market Pipeline

End-to-end data pipeline: CryptoCompare API -> S3 -> Snowflake -> Streamlit dashboard. Orchestrated by Airflow, containerized with Docker.

## Interaction Mode

This is a **learning project**. The user is building everything themselves to gain hands-on experience.

- **Do not write code for the user.** Guide them step by step so they write it themselves.
- Explain concepts, patterns, and reasoning behind each decision.
- For external services (AWS, Snowflake, Airflow, etc.), provide detailed setup instructions with links, examples, and tutorials.
- Always ask for clarification when unsure about the question or the answer.
- Verify every claim before stating it. Do not assume — confirm by reading files, checking docs, or testing. If uncertain, say so explicitly.
- After each milestone, suggest what to learn or try next.

## Tech Stack

- Python 3.12+
- Apache Airflow (orchestration)
- AWS S3 (raw storage, partitioned by date)
- Snowflake (data warehouse)
- Streamlit (dashboard)
- Docker + docker-compose

## Project Structure

```
src/
  ingestion/       # API clients and data fetchers
  transformation/  # Data cleaning and transformation logic
  loading/         # S3 and Snowflake loaders
  utils/           # Shared helpers (logging, config, retry)
dags/              # Airflow DAG definitions
dashboard/         # Streamlit app
tests/             # Mirrors src/ structure
config/            # Settings, SQL schemas
docker/            # Dockerfiles and docker-compose
```

## Commands

```bash
# TODO: fill in as implementation progresses
# python -m pytest tests/               # Run tests
# docker-compose up                     # Start all services
# streamlit run dashboard/app.py        # Run dashboard locally
# airflow dags test <dag_id>            # Test a DAG
```

## Code Conventions

- Type hints on all function signatures
- snake_case for functions/variables, PascalCase for classes
- Use `pathlib.Path` over `os.path`
- Use `httpx` for HTTP calls (async-capable)
- Logging via `structlog` (structured JSON logs)
- Config from environment variables, loaded through a central config module
- Keep functions small and testable; no business logic in DAGs

## Environment Variables

- `CRYPTOCOMPARE_API_KEY` -- API key for CryptoCompare
- `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_S3_BUCKET` -- S3 access
- `SNOWFLAKE_ACCOUNT`, `SNOWFLAKE_USER`, `SNOWFLAKE_PASSWORD`, `SNOWFLAKE_DATABASE` -- Snowflake connection

Never commit `.env` files or credentials.
