from app.models.user import UserItem  # Import UserItem model for request body validation
from datetime import datetime
from app.db.entities.user_entity import UserEntity  # Import UserEntity for database operations

def map_user(source:UserItem)-> UserEntity:
    destination = UserEntity()
    if(source.id is None):
        destination.Id = 0
        return destination
    destination.Id = source.id
    destination.username = source.username
    destination.phone = source.phone
    destination.fullName = source.full_name
    destination.isActive = source.is_active
    destination.isSuperUser = source.is_superuser
    destination.CreatedDate = source.created_date
    destination.UpdatedDate = datetime.now()  # Assuming you want to set the current time as the updated date
    destination.message = source.message    
    return destination
    