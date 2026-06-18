# example-repository

Prod-like FastAPI example with reusable internal modules.

## Run locally

```bash
python -m pip install -e ".[dev]"
uvicorn app.main:app --reload
```

## What is reusable

- `app/core` - config and structured logger with request context.
- `app/observability` - middleware for request/correlation IDs and metrics.
- `app/docs` - OpenAPI customization setup.
- `app/integrations` - placeholder for downstream clients (Kafka/Rabbit/HTTP).

## API endpoints

- `GET /health`
- `POST /api/v1/customers`
- `GET /api/v1/customers`
- `POST /api/v1/orders`
- `GET /api/v1/orders`
- `GET /metrics`

## CI/CD

- GitHub Actions: `.github/workflows/ci.yml`
- GitLab CI: `.gitlab-ci.yml`
- Helm chart: `helm/fastapi-app`

## Dashboards

- Grafana dashboard JSON is stored at `helm/fastapi-app/dashboards/fastapi-overview.json`.
- Helm template `helm/fastapi-app/templates/dashboards.yaml` renders dashboard ConfigMaps similar to `multi-biometric-matcher-service`.
- The dashboard uses current app metrics from `prometheus-fastapi-instrumentator`: `http_requests_total` and `http_request_duration_seconds_*`.
