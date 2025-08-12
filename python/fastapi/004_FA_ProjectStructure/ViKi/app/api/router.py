from fastapi import APIRouter

# Import individual module routers for v1
# (create these files as you go: app/api/v1/user.py, admin.py, chat.py, documents.py, report.py)
from api.v1.user import router as user_router
from api.v1.admin import router as admin_router
from api.v1.chat import router as chat_router
from api.v1.documents import router as documents_router
from api.v1.report import router as report_router

api_v1_router = APIRouter()
api_v1_router.include_router(user_router, prefix="/user", tags=["User"])
api_v1_router.include_router(admin_router, prefix="/admin", tags=["Admin"])
api_v1_router.include_router(chat_router, prefix="/chat", tags=["Chat"])
api_v1_router.include_router(documents_router, prefix="/documents", tags=["Documents"])
api_v1_router.include_router(report_router, prefix="/report", tags=["Report"])
