import uuid

from fastapi import FastAPI, Request

from app.core.request_context import correlation_id_ctx, request_id_ctx


def setup_middlewares(app: FastAPI) -> None:
    @app.middleware("http")
    async def context_middleware(request: Request, call_next):
        request_id = request.headers.get("X-Request-Id") or str(uuid.uuid4())
        correlation_id = request.headers.get("X-Correlation-Id") or request_id

        request_id_token = request_id_ctx.set(request_id)
        correlation_id_token = correlation_id_ctx.set(correlation_id)

        try:
            response = await call_next(request)
        finally:
            request_id_ctx.reset(request_id_token)
            correlation_id_ctx.reset(correlation_id_token)

        response.headers["X-Request-Id"] = request_id
        response.headers["X-Correlation-Id"] = correlation_id
        return response
