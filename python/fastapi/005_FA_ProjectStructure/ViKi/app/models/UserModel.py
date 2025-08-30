
# create model for user
from pydantic import BaseModel, EmailStr   ,Field 
from typing import Optional
from models.userItem import UserItem  # Import UserItem model for request body validation
from models.ModelBase import ModelBase  # Importing ModelBase for common fields
from models.userItem import UserItems  # Import UserItems for list of users
from models.ItemBase import ItemBase  # Importing ItemBase for common fields


# Additional models for requests and responses
class UsersRequest(ItemBase):
    items: list[UserItem] = Field(default_factory=list)

# Response model for multiple users    
class UsersResponse(ItemBase):
    items: list[UserItem] = Field(default_factory=list)
    total: int = 0
    
# Response model for single user
class UserRequest(ItemBase):
    item: Optional[UserItem] = None
 
# Response model for single user   
class UserResponse(ItemBase):
    item: Optional[UserItem] = None

class UserModel(ModelBase):
    id:int = 0  # User ID field
    item: Optional[UserItem] = None # Use UserItem for request body validation
    items: list[UserItem] = Field(default_factory=list)
    userItems: Optional[UserItems] = None  # List to hold multiple UserItem instances
    response: Optional[UserResponse] = None
    multiResponse: Optional[UsersResponse] = None
