
# create model for user
from pydantic import BaseModel, EmailStr    
from typing import Optional
from app.models.userItem import UserItem  # Import UserItem model for request body validation
from app.models.ModelBase import ModelBase  # Importing ModelBase for common fields

class UserModel(ModelBase):
    item: UserItem  # Use UserItem for request body validation
    
     