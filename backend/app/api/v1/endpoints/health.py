# backend/app/api/v1/endpoints/health.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/health", summary="Health check")
async def health_check():
    """Returns the health status of the API."""
    return {"status": "healthy"}