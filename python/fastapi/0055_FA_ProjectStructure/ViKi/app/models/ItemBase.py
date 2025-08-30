from pydantic import BaseModel, EmailStr    
from typing import Optional

class ItemBase(BaseModel):
    __abstract__ = True
    # This class can be extended to include common fields or methods for all models in the application.
    # For example, you might want to add fields like created_at, updated_at, etc. in the future.
    Message: str | None = None  # Optional field for additional messages
    IsInvalid: bool = False  # Default value for invalid status