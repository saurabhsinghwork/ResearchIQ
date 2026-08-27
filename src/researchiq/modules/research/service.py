
research_jobs = []

def create_research(question:str) -> dict:
    research_job = {
        "id": len(research_jobs)+1,
        "question": question,
        "status":"pending"
    }
    research_jobs.append(research_job)
    return research_job

def get_research_jobs() -> list[dict]:
    return research_jobs

def get_research_by_id(research_id:int) -> dict|None:
    for research_job in research_jobs:
        if research_job["id"]==research_id:
            return research_job
    return None

def update_research(research_id:int,question:str) -> dict | None :
    research_job = get_research_by_id(research_id)
    if research_job:
        research_job["question"] = question
        return research_job
    return None

def delete_research(research_id:int) -> dict | None :
    research_job = get_research_by_id(research_id)
    if research_job:
        research_jobs.remove(research_job)
        return research_job
    return None

