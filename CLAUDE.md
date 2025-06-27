# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Development Commands

### Running the Application
```bash
# Run frontend only (Streamlit)
make run-frontend

# Run backend API (FastAPI)
make run-backend

# Run both frontend and backend
make run-app

# Run with local models (Ollama)
make run-ollama  # Start Ollama server
make download-ollama-model MODEL_NAME=llama3.2  # Download a model
```

### Testing and Quality Checks
```bash
# Run all tests
make test

# Run LLM inference tests specifically
make test-inference-llm

# Run pre-commit checks (linting, formatting, secrets detection)
make pre-commit

# Install pre-commit hooks
make pre-commit-install
```

### Docker Development
```bash
# Build and run with docker-compose (includes Ollama)
make docker-compose

# Run development container
make docker-dev

# Run production container
make docker-prod
```

## High-Level Architecture

### Application Structure
This is a Generative AI application template with three main deployment modes:
1. **Streamlit-only**: Simple UI for chat and embeddings (`src/main_frontend.py`)
2. **Streamlit + FastAPI**: Full stack with API backend (`src/main_backend.py` + `src/api/`)
3. **Docker**: Containerized deployment with optional Ollama support

### Key Components

**LLM Integration** (`src/ml/llm.py`):
- Uses LiteLLM for multi-provider support (OpenAI, Azure, Anthropic, etc.)
- Instructor for structured outputs with Pydantic models
- Supports both cloud and local models via Ollama
- Configurable via environment variables in `.env`

**Settings System** (`src/settings_env.py`):
- Pydantic-based configuration with validation
- Separate settings classes for different features (inference, embeddings, evaluation, Azure)
- Automatically loads from `.env` file
- Validates required fields based on enabled features

**Evaluation Framework** (`src/evaluation/`):
- Multiple evaluation approaches: baseline, JSON extraction, prompt comparison
- Metrics include RAGAS, information extraction, custom validators
- Configured via YAML files in `src/evaluation/configs/`
- Red team testing capabilities for security evaluation

**RAG System** (`src/pages/2_azure_rag.py`):
- Integration with Azure AI Search for vector search
- Azure Blob Storage for document storage
- Configurable chunking and retrieval strategies
- Optional feature - only loads if Azure settings are configured

### Development Workflow

1. **Environment Setup**: Copy `.env.example` to `.env` and configure required variables
2. **Dependency Management**: Uses UV package manager (`uv pip install` commands)
3. **Code Quality**: Pre-commit hooks enforce Ruff formatting, conventional commits, and security checks
4. **Testing**: pytest with async support, tests located in `tests/`
5. **Documentation**: Auto-generated with MkDocs from docstrings (Google style required)

### Important Configuration Files
- `pyproject.toml`: Package dependencies, tool configurations (Ruff, pytest)
- `.pre-commit-config.yaml`: Pre-commit hooks configuration
- `Makefile`: All development commands and workflows
- `.env`: Environment variables (create from `.env.example`)
- `mkdocs.yml`: Documentation configuration

### CI/CD Pipeline
GitHub Actions workflow (`.github/workflows/test-deploy.yaml`):
1. Runs pre-commit checks on all pushes
2. Executes test suite with Ollama integration
3. Tests docker-compose setup on PRs
4. Deploys documentation to GitHub Pages on main branch merges