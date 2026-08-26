# ResearchIQ

ResearchIQ is an AI-powered research automation platform. This repository is intentionally starting as a **professional FastAPI skeleton only**.

At this stage it contains:

- FastAPI application startup
- Environment-based configuration
- A `/health` endpoint
- A health endpoint test
- Basic packaging and Docker setup

It does **not** yet contain ResearchIQ product features such as research jobs, authentication, crawling, databases, RAG, reports, schedules, or webhooks. Those will be added gradually while learning the codebase.

## Requirements

- Python 3.11+

## Local setup

### 1. Create a virtual environment

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
py -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install the project

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

### 3. Create the environment file

Copy `.env.example` to `.env`.

Windows:

```cmd
copy .env.example .env
```

macOS/Linux:

```bash
cp .env.example .env
```

### 4. Run the API

```bash
uvicorn researchiq.main:app --reload
```

Open:

- API root: http://127.0.0.1:8000
- Health: http://127.0.0.1:8000/health
- Swagger UI: http://127.0.0.1:8000/docs

### 5. Run tests

```bash
pytest
```

## Current API

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Confirms that the service is running |

## Learning rule

Do not add ResearchIQ features until the current repository structure and startup flow are understood. The codebase will grow one small feature at a time.
