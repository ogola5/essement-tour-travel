# backend/app/api/v1/endpoints/queries.py
from fastapi import APIRouter, HTTPException
from app.api.v1.schemas import QueryRequest, QueryResponse
from app.services.query_service import QueryService

router = APIRouter()

@router.post("/query", response_model=QueryResponse, summary="Handle user query")
async def handle_query(request: QueryRequest):
    """
    Processes a user query and returns an LLM-generated response.
    
    Args:
        request: QueryRequest containing the user's question.
    
    Returns:
        QueryResponse with the question, response, and status.
    
    Raises:
        HTTPException: If the query is empty or processing fails.
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    try:
        response = await QueryService.process_query(request.text)
        return QueryResponse(
            question=request.text,
            response=response,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process query: {str(e)}")