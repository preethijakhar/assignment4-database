# PROG8850 – Assignment 4 (Preethi Jakhar)

Simple Flyway migrations with MySQL, GitHub Actions CI, and small Ansible helpers.

## Project layout
- `docker-compose.yml` – MySQL (port 3307) + Adminer (8081)
- `migrations/initial/` – first-time schema for `subscribersdb`
- `migrations/incremental/` – later changes
- `.github/workflows/ci.yml` – runs initial + incremental migrations and tests
- `tests/test_subscribers.py` – CRUD unit test (self-contained)
- `ansible/up.yml`, `ansible/down.yml` – local bring-up/tear-down

## Run locally
```bash
docker compose up -d                  # start DB on 3307
docker ps                             # check containers
# Initial & incremental migrations
docker run --rm --network host -v "$PWD/migrations/initial:/flyway/sql" flyway/flyway:10-alpine -url="jdbc:mysql://127.0.0.1:3307/subscribersdb" -user="subuser" -password="subpass" migrate
docker run --rm --network host -v "$PWD/migrations/incremental:/flyway/sql" flyway/flyway:10-alpine -url="jdbc:mysql://127.0.0.1:3307/subscribersdb" -user="subuser" -password="subpass" migrate
# Tests
pip install -r requirements.txt
python -m unittest -v tests/test_subscribers.py
# Tear down
docker compose down -v
