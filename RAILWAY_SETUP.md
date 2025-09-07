# Railway deployment configuration for SIH Backend

## Quick Start

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login and Initialize**
   ```bash
   railway login
   railway init
   ```

3. **Add Services in Railway Dashboard**
   - PostgreSQL Database
   - Redis Cache  
   - MinIO Object Storage
   - Backend API (connect GitHub repo)

4. **Deploy**
   ```bash
   railway up
   ```

## Service Configuration

### Backend API Service
- **Type**: Web Service
- **Build Command**: Uses Dockerfile in `backend/` directory
- **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- **Health Check**: `/api/health`

### PostgreSQL Database
- **Type**: Database
- **Template**: PostgreSQL
- **Auto-provides**: `DATABASE_URL`

### Redis Cache
- **Type**: Database
- **Template**: Redis  
- **Auto-provides**: `REDIS_URL`

### MinIO Object Storage
- **Type**: Private Service
- **Image**: `minio/minio:latest`
- **Command**: `server /data --console-address :9001`
- **Environment Variables**:
  - `MINIO_ROOT_USER`: your-access-key
  - `MINIO_ROOT_PASSWORD`: your-secret-key

## Environment Variables

Set these in Railway dashboard for your backend service:

```bash
SECRET_KEY=your-production-secret-key-here
MINIO_ENDPOINT=your-minio-service-url
MINIO_ACCESS_KEY=your-minio-access-key  
MINIO_SECRET_KEY=your-minio-secret-key
```

## Local Development

```bash
# Start all services
docker-compose up -d

# Run backend locally
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Files Created/Modified

- `railway.json` - Railway deployment configuration
- `backend/Dockerfile` - Docker configuration for backend
- `docker-compose.yml` - Updated with backend service and environment variables
- `env.example` - Environment variables template
- `backend/app/core/auth.py` - Updated to use environment variables
