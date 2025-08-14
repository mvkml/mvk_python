from fastapi import APIRouter
"""
This module defines the main API router for version 1 (v1) of the application.
It imports and includes individual routers for different API domains (user, admin, chat, documents, report)
under the `/user`, `/admin`, `/chat`, `/documents`, and `/report` prefixes, respectively.
Currently, only the user router is active; others are commented out for future implementation.
Usage:
    - Import this router in your main FastAPI application and include it under the desired prefix (e.g., `/api/v1`).
Example:
    app.include_router(api_v1_router, prefix="/api/v1")
# Note: Uncomment and implement additional routers as needed.
"""

# Import individual module routers for v1
# (create these files as you go: app/api/v1/user.py, admin.py, chat.py, documents.py, report.py)
#from api.v1.user import router as user_router
from api.v1.user import router as user_router  # User management router
from api.v1.report import router as report_router  # Report management router
from api.v1.admin import router as admin_router  # Admin management router
# from api.v1.chat import router as chat_router  # Chat management router



'''
from api.v1.admin import router as admin_router
from api.v1.chat import router as chat_router
from api.v1.documents import router as documents_router
from api.v1.report import router as report_router
from app.api.router import api_v1_router
'''

api_v1_router = APIRouter()
api_v1_router.include_router(user_router, prefix="/user", tags=["User"])
api_v1_router.include_router(report_router, prefix="/report", tags=["Report"])
api_v1_router.include_router(admin_router, prefix="/admin", tags=["Admin"]) 

'''
api_v1_router.include_router(admin_router, prefix="/admin", tags=["Admin"])
api_v1_router.include_router(chat_router, prefix="/chat", tags=["Chat"])
api_v1_router.include_router(documents_router, prefix="/documents", tags=["Documents"])
api_v1_router.include_router(report_router, prefix="/report", tags=["Report"])
'''
