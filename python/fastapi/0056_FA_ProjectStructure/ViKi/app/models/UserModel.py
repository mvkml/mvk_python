
# create model for user
from pydantic import BaseModel, EmailStr    
from typing import Optional
from models.userItem import UserItem  # Import UserItem model for request body validation
from models.ModelBase import ModelBase  # Importing ModelBase for common fields

class UserModel(ModelBase):
    item: Optional[UserItem] = None # Use UserItem for request body validation
    id:int = 0  # User ID field
    
    # You can add more fields as needed
    # Example: username, email, full_name, is_active, is_superuser, etc.