# backend/app/api/v1/schemas.py
from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    """Request model for user queries."""
    text: str = Field(..., min_length=1, description="The user's question")

class QueryResponse(BaseModel):
    """Response model for query results."""
    question: str = Field(..., description="The user's original question")
    response: str = Field(..., description="The LLM-generated response in markdown")
    status: str = Field(..., description="Status of the query (e.g., 'success')")