from models.UserModel import UsersRequest, UsersResponse  # Import UserModel for input parameter and return type
from models.userItem import UserItem  # Import UserItem model for request body validation
from db.entities.userentity import UserEntity  # Import UserEntity for database operations
from datetime import datetime as ti

def map_user_item_to_entity(item: UserItem,entity:UserEntity=None)-> UserEntity:
    if entity is None:
        entity = UserEntity()
    entity.username = item.username
    entity.phone = item.phone
    entity.fullname = item.full_name
    entity.isactive = item.is_active
    entity.issuperuser = item.is_superuser
    entity.updateddate = ti.now()
    return entity
