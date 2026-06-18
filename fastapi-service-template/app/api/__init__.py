from fastapi import APIRouter

from app.api.routes import router as demo_router

router = APIRouter()
router.include_router(demo_router, prefix="/v1", tags=["demo"])
