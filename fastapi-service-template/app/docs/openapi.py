from fastapi import FastAPI


def setup_openapi(app: FastAPI) -> None:
    app.openapi_tags = [
        {"name": "service", "description": "Service-level endpoints"},
        {"name": "demo", "description": "Demo entities (customers and orders)"},
    ]
