from fastapi import APIRouter
# Create router for admin endpoints
router = APIRouter()

# Default endpoint for the admin module
@router.get("")
def default():
    return {"message": "Admin Available"}

@router.get("/hello")
def hello_admin():
    """
    Simple test endpoint for Admin module.
    Will be available at: /api/v1/admin/hello
    """
    return {"message": "Hello from Admin API"}

@router.get("/status")
def admin_status():
    """
    Endpoint to check the status of the Admin module.
    Will be available at: /api/v1/admin/status
    """
    return {"status": "Admin module is operational"}      
