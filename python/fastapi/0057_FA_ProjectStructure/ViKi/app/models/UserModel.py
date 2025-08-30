
# create model for user
from pydantic import BaseModel, EmailStr    
from typing import Optional
from models.userItem import UserItem  # Import UserItem model for request body validation
from models.ModelBase import ModelBase  # Importing ModelBase for common fields
from models.userItem import UserItems  # Import UserItems for list of users

class UserModel(ModelBase):
    id:int = 0  # User ID field
    item: Optional[UserItem] = None # Use UserItem for request body validation
    userItems: Optional[UserItems] = None  # List to hold multiple UserItem instances
    # You can add more fields as needed
    # Example: username, email, full_name, is_active, is_superuser, etc.