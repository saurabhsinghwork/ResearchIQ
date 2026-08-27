from fastapi import APIRouter,status,HTTPException
from researchiq.modules.research.schemas import (ResearchCreateRequest, ResearchResponse, ResearchUpdateRequest)
from researchiq.modules.research.service import (create_research,get_research_jobs,get_research_by_id,update_research,delete_research)

router = APIRouter(prefix="/research",tags=["research"],)

@router.post("",status_code=status.HTTP_201_CREATED,response_model=ResearchResponse)
def create_research_endpoint(request:ResearchCreateRequest):
    return create_research(request.question)

@router.get("",response_model=list[ResearchResponse])
def list_research_jobs():
    return get_research_jobs()

@router.get("/{research_id}",response_model=ResearchResponse)
def get_research_endpoint(research_id:int):
    research_job = get_research_by_id(research_id)
    if research_job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Research Job not found")
    return research_job

@router.put("/{research_id}",response_model=ResearchResponse)
def update_research_endpoint(research_id:int,request:ResearchUpdateRequest):
    research_job = update_research(research_id,request.question)
    if research_job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Research Job not found")
    return research_job

@router.delete("/{research_id}",response_model=ResearchResponse)
def delete_research_endpoint(research_id:int):
    research_job = delete_research(research_id)
    if research_job is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Research Job not found")
    return research_job