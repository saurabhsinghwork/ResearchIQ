from fastapi import FastAPI

from researchiq.api.v1.router import router as v1_router
from researchiq.api.health import router as health_router
from researchiq.core.config import get_settings


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(health_router)
app.include_router(v1_router,prefix="/api/v1")
