# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import queries, health
from app.core.config import settings

app = FastAPI(
    title="TravelBuddy Q&A API",
    description="A Q&A API for travel questions powered by DeepSeek LLM",
    version="1.0.0"
)

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(health.router, prefix="/api/v1")
app.include_router(queries.router, prefix="/api/v1")

@app.get("/", summary="Root endpoint")
async def root():
    """Returns a welcome message for the API."""
    return {"message": "TravelBuddy Q&A API is running"}