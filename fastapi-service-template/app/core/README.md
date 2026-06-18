# Core module

- `config.py` contains app settings through `pydantic-settings`.
- `logging.py` provides JSON logging with `request_id` and `correlation_id`.
- `request_context.py` stores per-request IDs via `contextvars`.
