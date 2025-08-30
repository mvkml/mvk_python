# create model for user
from pydantic import BaseModel, EmailStr , Field   
from typing import Optional

from models.ItemBase import ItemBase  # Importing ItemBase for common fields

class UserItem(ItemBase):
    id: int = 0
    username: str | None = None  # Optional field with default value None
    email: str | None = None #email: EmailStr | None = None  # Optional field with EmailStr type
    phone: str | None = None  # Optional field with default value None
    full_name: str | None = None  # Optional field with default value None
    is_active: bool = True  # Default value for active status
    is_superuser: bool = False  # Default value for superuser status
    message: str | None = None  # Optional field for additional messages
    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with ORMs like SQLAlchemy      
# This allows the model to work with ORM objects directly
# Example usage:
# user = User(id=1, username="johndoe", email="joh      
    
    

class UserItems(ItemBase):
    items: list[UserItem] = Field(default_factory=list)
    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with ORMs like SQLAlchemy
    