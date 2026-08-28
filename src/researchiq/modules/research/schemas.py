from pydantic import BaseModel, Field

class ResearchCreateRequest(BaseModel):
    question:str = Field(min_length=5,max_length=1000)

class ResearchResponse(BaseModel):
    id: int
    question: str
    status: str

class ResearchUpdateRequest(BaseModel):
    question:str = Field(min_length=5,max_length=1000)    