from fastapi import APIRouter
from researchiq.modules.research.router import router as research_router

router = APIRouter()
router.include_router(research_router)