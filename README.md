# SIH Monorepo

## Frontend
```bash
cd frontend
npm install
npm run dev
```

## Backend
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload
```

## Docker Services
```bash
docker compose up -d
```

Services:
- Postgres: localhost:5432
- Redis: localhost:6379  
- MinIO: localhost:9000 (console: localhost:9001)
- Adminer: localhost:8080