
research_jobs = []

def create_research(question:str)->dict:
    research_job = {
        "id": len(research_jobs)+1
        "question": question
        "status":"pending"
    }
    research_jobs.append(research_job)
    return research_job