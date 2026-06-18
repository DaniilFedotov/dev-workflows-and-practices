from fastapi import FastAPI

from app.api import router as api_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.docs.openapi import setup_openapi
from app.observability.metrics import setup_metrics
from app.observability.middleware import setup_middlewares
from app.schemas.common import HealthResponse


def create_app() -> FastAPI:
    setup_logging(settings.log_level)
    app = FastAPI(title=settings.app_name, version=settings.app_version)

    setup_openapi(app)
    setup_middlewares(app)
    setup_metrics(app)

    @app.get("/health", response_model=HealthResponse, tags=["service"])
    def health() -> HealthResponse:
        return HealthResponse(status="ok")

    app.include_router(api_router, prefix="/api")
    return app


app = create_app()
