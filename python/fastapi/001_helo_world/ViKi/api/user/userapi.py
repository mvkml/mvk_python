from fastapi import APIRouter

# Create a router for user-related endpoints
router = APIRouter()

@router.get("/hello")
def hello_user():
    """
    Simple endpoint to return a hello message for the user API.
    Accessible at: GET /user/hello
    """
    return {"message": "Hello, User API!"}
