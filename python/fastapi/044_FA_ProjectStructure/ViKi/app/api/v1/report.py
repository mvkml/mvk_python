from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def hello_report():
    """
    Simple test endpoint for Report module.
    Available at: /api/v1/report/hello
    """
    return {"message": "Hello from Report API"}
