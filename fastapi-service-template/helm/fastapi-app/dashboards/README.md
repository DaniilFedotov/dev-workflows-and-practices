# Grafana dashboards

This directory stores Grafana dashboard JSON files.

Helm template `templates/dashboards.yaml` packages every `*.json` from this directory into a ConfigMap with labels required by dashboard sidecars.

Current dashboard:
- `fastapi-overview.json` for default metrics produced by `prometheus-fastapi-instrumentator`.
