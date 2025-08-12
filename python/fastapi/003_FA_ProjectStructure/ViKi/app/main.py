from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import api_v1_router  # aggregated v1 routers

# Create FastAPI instance
app = FastAPI(title="My FastAPI App", version="1.0.0")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Example endpoint with parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {
        "item_id": item_id,
        "query": q
    }

app.include_router(api_v1_router, prefix="/api/v1")

# Optional: allow `python -m app.main`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=802, reload=True)
