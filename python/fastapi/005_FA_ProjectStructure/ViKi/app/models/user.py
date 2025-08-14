# create model for user
from pydantic import BaseModel, EmailStr    

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str | None = None  # Optional field with default value None
    is_active: bool = True  # Default value for active status
    is_superuser: bool = False  # Default value for superuser status

    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with ORMs like SQLAlchemy      
# This allows the model to work with ORM objects directly
# Example usage:
# user = User(id=1, username="johndoe", email="joh      
    