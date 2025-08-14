from fastapi import APIRouter

router = APIRouter()

# Default endpoint for the Report module
@router.get("")
def default():
    return {"message": "Report Available"}

@router.get("/hello")
def hello_report(): 
    """
    Simple test endpoint for Report module.
    Will be available at: /api/v1/report/hello
    """
    return {"message": "Hello from Report API"} 

@router.get("/status")
def report_status():
    """
    Endpoint to check the status of the Report module.
    Will be available at: /api/v1/report/status
    """
    return {"status": "Report module is operational"}       
