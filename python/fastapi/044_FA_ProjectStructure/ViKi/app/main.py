from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router import api_v1_router  # aggregated v1 routers

# ViKi API - FastAPI Application
# This is the main entry point for the ViKi API application.
app = FastAPI(
    title="ViKi API",
    description="Large-project skeleton with versioned routers",
    version="1.0.0",
)

# CORS (tweak as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # replace with your allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}

# Default root endpoint
#@app.get("")  # Handles requests to the root URL
#def default():
    # Returns a simple JSON response indicating the API is alive
    #return {"status": "Alive", "message": "Welcome to the ViKi API!"}

# Mount all v1 endpoints under /api/v1
app.include_router(api_v1_router, prefix="/api/v1")

# Optional: allow `python -m app.main`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=801, reload=True)
