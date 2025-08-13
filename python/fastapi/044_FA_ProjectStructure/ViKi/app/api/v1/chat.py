from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def hello_chat():
    """
    Simple test endpoint for Chat module.
    Available at: /api/v1/chat/hello
    """
    return {"message": "Hello from Chat API"}
