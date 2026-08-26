from pydantic import BaseModel, Field

class ResearchCreateRequest(BaseModel):
    question:str = Field(min_length=5,max_length=1000)

class ResearchCreateresponse(BaseModel):
    message: str
    question: str