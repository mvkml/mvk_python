from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def hello_admin():
    """
    Simple test endpoint for Admin module.
    Available at: /api/v1/admin/hello
    """
    return {"message": "Hello from Admin API"}
