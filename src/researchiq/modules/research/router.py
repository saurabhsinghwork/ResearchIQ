from fastapi import APIRouter,status
from researchiq.modules.research.schemas import (ResearchCreateRequest, ResearchCreateresponse)
from researchiq.modules.research.service import create_research

router = APIRouter(prefix="/research",tags=["research"],)

@router.post("",status_code=status.HTTP_201_CREATED,response_model=ResearchCreateresponse)
def create_research_endpoint(request:ResearchCreateRequest):
    return create_research(request.question)