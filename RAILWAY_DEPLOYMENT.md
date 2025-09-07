# Railway deployment guide

## Prerequisites
1. Install Railway CLI: `npm install -g @railway/cli`
2. Login to Railway: `railway login`
3. Create a new project: `railway init`

## Services to Add
You'll need to add these services in Railway dashboard:

### 1. PostgreSQL Database
- Service Type: Database
- Template: PostgreSQL
- Railway will automatically provide `DATABASE_URL`

### 2. Redis Cache
- Service Type: Database  
- Template: Redis
- Railway will automatically provide `REDIS_URL`

### 3. MinIO Object Storage
- Service Type: Private Service
- Use the MinIO Docker image: `minio/minio:latest`
- Command: `server /data --console-address :9001`
- Environment variables:
  - `MINIO_ROOT_USER`: your-access-key
  - `MINIO_ROOT_PASSWORD`: your-secret-key

### 4. Backend API
- Service Type: Web Service
- Connect your GitHub repository
- Railway will use the `railway.json` configuration

## Environment Variables
Set these in Railway dashboard for your backend service:

```
SECRET_KEY=your-production-secret-key
MINIO_ENDPOINT=your-minio-service-url
MINIO_ACCESS_KEY=your-minio-access-key
MINIO_SECRET_KEY=your-minio-secret-key
```

## Deployment Commands
```bash
# Deploy to Railway
railway up

# View logs
railway logs

# Connect to database
railway connect postgres
```

## Local Development
```bash
# Start all services locally
docker-compose up -d

# Run backend locally
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
