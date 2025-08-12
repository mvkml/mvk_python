from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def hello_documents():
    """
    Simple test endpoint for Documents module.
    Available at: /api/v1/documents/hello
    """
    return {"message": "Hello from Documents API"}
