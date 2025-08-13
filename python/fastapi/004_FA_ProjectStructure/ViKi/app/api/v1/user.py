from fastapi import APIRouter

# Create router for user endpoints
router = APIRouter()

# Default endpoint for the User module
@router.get("")
def default():
    return {"message": "User Avialable"}


@router.get("/hello")
def hello_user():
    """
    Simple test endpoint for User module.
    Will be available at: /api/v1/user/hello
    """
    return {"message": "Hello from User API"}
