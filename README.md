# leet-info-graph-gpt-5.1-codex-mini-v3

> This project is being developed by an autonomous coding agent.

## Overview

# Research Infograph Assistant - Project Goals

## Overview

Build a full-stack web application that lets users sign in with Google, submit research prompts, 
and receive AI-generated infographics wit...

## Features

Backend DuckDB stores for users, sessions, sources, messages, and infographics with abstract interfaces and schema-aligned implementations.
## Getting Started

### Prerequisites

- Node 18+ and npm 10+ to run the frontend dev server.
- Install dependencies via `npm install` inside the `frontend` directory.
- Python 3.11+ with backend dependencies from `backend[all]`.
### Installation

```bash
# Installation instructions will be added
```

### Usage

```bash
# Start the backend service
cd backend
pip install -e .[test]
python -m infograph.svc.main --port 8000
```

```bash
# Start the frontend dev server
cd frontend
npm install
npm run dev
```

# Usage examples will be added
```

## Development

See .leet/.todos.json for the current development status.

## Testing

```bash
# Backend tests
docker run --rm -v "$(pwd)/backend:/app" -w /app python:3.11 bash -c "pip install -e .[test] && pytest tests/ -v"
```

# Test instructions will be added
```

## License

MIT
