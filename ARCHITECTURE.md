# ResearchIQ Starter Architecture

This repository intentionally contains only the minimum infrastructure needed to start a professional FastAPI service.

## Current structure

```text
researchiq-starter/
├── README.md
├── ARCHITECTURE.md
├── pyproject.toml
├── .env.example
├── .gitignore
├── .dockerignore
├── Dockerfile
├── src/
│   └── researchiq/
│       ├── __init__.py
│       ├── main.py
│       ├── api/
│       │   ├── __init__.py
│       │   └── health.py
│       └── core/
│           ├── __init__.py
│           └── config.py
└── tests/
    └── test_health.py
```

## Current request flow

```text
Client
  ↓
FastAPI application (`main.py`)
  ↓
Health router (`api/health.py`)
  ↓
JSON response
```

## File responsibilities

### `src/researchiq/main.py`
Creates the FastAPI application and connects application-level routers.

### `src/researchiq/api/health.py`
Contains the health-check endpoint only.

### `src/researchiq/core/config.py`
Loads basic application configuration from environment variables.

### `tests/test_health.py`
Checks that the application starts and `/health` returns a successful response.

## Architectural rule

New folders and layers should be added only when a real ResearchIQ feature requires them. The repository should remain professional without creating unnecessary abstractions.
