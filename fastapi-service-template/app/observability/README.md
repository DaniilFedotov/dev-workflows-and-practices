# Observability module

- `middleware.py` sets `X-Request-Id` / `X-Correlation-Id` and propagates them.
- `metrics.py` enables Prometheus endpoint at `/metrics`.
- This module is FastAPI-specific and intended for copy-paste reuse.
