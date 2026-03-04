# Usage: in root: make <command-name>

# General
test:
	python -m pytest tests/

# Airflow
airflow-init:
	docker compose --project-directory . -f docker/docker-compose.yaml up airflow-init
airflow-healthy:
	docker compose --project-directory . -f docker/docker-compose.yaml ps
airflow-start:
	docker compose --project-directory . -f docker/docker-compose.yaml up -d
airflow-stop:
	docker compose --project-directory . -f docker/docker-compose.yaml down
airflow-logs:
	docker compose --project-directory . -f docker/docker-compose.yaml logs -f
airflow-build:
	docker compose --project-directory . -f docker/docker-compose.yaml build
