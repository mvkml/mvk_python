from fastapi import FastAPI
from api.user.userapi import router as user_router

# Create FastAPI app instance
app = FastAPI(
    title="ViKi API",
    description="Sample FastAPI project",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Rest API is up and  available!"}

# Include the user API router
app.include_router(user_router, prefix="/user", tags=["User API"])

# Optional: allow running with `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=802, reload=True)
