from fastapi import APIRouter

from researchiq.core.config import get_settings


router = APIRouter(tags=["Health"])


@router.get("/health")
def health_check() -> dict[str, str]:
    settings = get_settings()

    return {
        "status": "ok",
        "service": settings.app_name,
        "environment": settings.app_env,
        "version": settings.app_version,
    }
