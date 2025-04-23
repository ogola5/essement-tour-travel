from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Travel Assistant API is running"}

@app.post("/api/query")
async def handle_query(query: str):
    # This is a mock response - replace with actual LLM integration
    return {
        "response": f"Mock response to: {query}\n\nRequired documents:\n1. Valid passport\n2. Visa (if applicable)\n3. Travel insurance",
        "status": "success"
    }