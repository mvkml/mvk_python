from fastapi import APIRouter

# Create router for user endpoints
router = APIRouter()

@router.get("/hello")
def hello_user():
    """
    Simple test endpoint for User module.
    Will be available at: /api/v1/user/hello
    """
    return {"message": "Hello from User API"}
