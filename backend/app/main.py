from fastapi import FastAPI
from .api.routes import router as api_router

app = FastAPI(title="SIH Backend")

app.include_router(api_router, prefix="/api")
