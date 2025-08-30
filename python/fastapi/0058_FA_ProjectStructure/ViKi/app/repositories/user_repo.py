from models.userItem import UserItem  # Import UserItem model for request body validation
from models.userItem import UserItems  # Import UserItem model for request body validation
from db.entities.userentity import UserEntity  # Import UserEntity for database operations
from models.UserModel import UserModel  # Import UserModel for input parameter and return type
from db.DBSession import get_db_session  # Import the session management function
from datetime import datetime as ti

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

from repositories.utilities.connectoin_utility import get_connection  # Import database connection utility
from repositories.utilities import map_utility

# from common.model_utility import validate_user_model,validate_user_model_item  # Import model validation utilities
from common import model_utility as mu

# I would like to use user model as input parameter and return type
# and user model having user item as property
# so that I can use user item for request body validation
# as user item having all user related properties
# I will use user model for input parameter and return type
# so that I can use user item for request body validation
# user id is part of user model
# so that I can use user id for get user by id
#can you mention response model in function defination 
 
def repo_get_user_by_userId(model: UserModel):
    print("/n")
    print("repo get user by user id called ")
    try:
        if mu.validate_item(model).item.IsInvalid:
            return model
        if mu.validate_model_item_id(model).IsInvalid:
            return model
        item =  update_user(model.id)
        print("/n")
        print("repo_get_user_by_id",item.Message)
        model.item = item
        print("item message after repo_get_user_by_id:", model.item.Message)
    except Exception as e:
        model.item.Message = f"Error retrieving user: {str(e)}"
        model.item.IsInvalid = True
        model.IsInvalid = True
        model.Message = f"Error retrieving user: {str(e)}"  
    return model


def delete_users(model: UserModel) -> UserModel:
    ds = None
    try:
        ds = get_connection() # Create a new session
        for item in model.items:
            if item.id is None or item.id <=0:
                item.Message = "Invalid user id"
                item.IsInvalid = True
                continue
            try:
                entity = ds.query(UserEntity).filter(UserEntity.id == item.id).first()
                if entity:
                    ds.delete(entity)
                    ds.commit() # Commit the transaction    
                    item.Message = f"Deleted User {item.id} successfully"
                    item.IsInvalid = False
                    ds.commit() # Commit the transaction    
                    continue
                else:
                    item.Message = f"User {item.id} not found to delete"
                    item.IsInvalid = True
            except Exception as e:
                item.Message = f"Error creating user: {str(e)}"
                item.IsInvalid = True
    except Exception as e:
        model.item.IsInvalid = True
        model.IsInvalid = True
        model.Message = f"Error retrieving user: {str(e)}"
    finally:
        if ds is not None:
            ds.close()
    return model


def upsert_users(model: UserModel) -> UserModel:
    ds = None
    try:
        ds = get_connection() # Create a new session
        for item in model.items:
            try:
                entity = ds.query(UserEntity).filter(UserEntity.id == item.id).first()
                if entity:
                    entity = map_utility.map_user_item_to_entity(item, entity)
                     # Update existing entity
                    item.Message = f"Updated User {item.id} successfully"
                    item.IsInvalid = False
                    ds.commit() # Commit the transaction    
                    continue
                else:
                    entity = map_utility.map_user_item_to_entity(item)
                    entity.createddate = ti.now()  # Set the creation date
                    ds.add(entity)
                    ds.commit()  # Commit the transaction
                    ds.refresh(entity)  # Refresh the entity to get the ID and other fields
                    item.id = entity.id  # Set the ID from the created entity
                    item.Message = "User created successfully"
                    item.IsInvalid = False
            except Exception as e:
                item.Message = f"Error creating user: {str(e)}"
                item.IsInvalid = True
    except Exception as e:
        model.item.IsInvalid = True
        model.IsInvalid = True
        model.Message = f"Error retrieving user: {str(e)}"
    finally:
        if ds is not None:
            ds.close()
    return model

#can you mention response model in function defination  
# write porper comment for below function   
def update_user(model: UserModel) -> UserModel:
    try:
        model = mu.validate_item_Id(model)
        if model.item.IsInvalid:
            return model
        model.item =  update_user_entity(model.item)
        print("item message after repo_get_user_by_id:", model.item.Message)
    except Exception as e:
        if model.item is None:
            model.item = UserItem()
        model.item.Message = f"Error retrieving user: {str(e)}"
        model.item.IsInvalid = True
        model.IsInvalid = True
        model.Message = f"Error retrieving user: {str(e)}"  
    return model

#can you mention response model in function defination
def repo_get_all_users(model: UserModel):
    ds = None
    try:
        DATABASE_URL = "postgresql+psycopg://postgres:Postgres%40007@localhost:5432/VikiHospitalBot"
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
        ds = SessionLocal()  # Create a new session
        model.userItems = UserItems()
        model.userItems.items = []
        users = ds.query(UserEntity).all()
        user_items = []
        print("\n")
        print("Total users fetched from DB:", len(users))
        for user in users:
            user_items.append(UserItem(
                id=user.id,
                username=user.username,
                phone=user.phone,
                full_name=user.fullname,
                is_active=user.isactive,
                is_superuser=user.issuperuser,
                message="User found",
                IsInvalid=False
            ))
        model.Message = "Users retrieved successfully"
        model.IsInvalid = False
        model.userItems.items = user_items
        model.userItems.Message = "Users retrieved successfully"
        model.userItems.IsInvalid = False
        print("\n Total users fetched:", len(model.userItems.items))
        return model
    except Exception as e:
        model.userItems = UserItems()
        model.Message = f"Error retrieving users: {str(e)}"
        model.IsInvalid = True
        print("Error retrieving users:", e)
        return model
    finally:
        if ds is not None:
            ds.close()

#can you mention response model in function defination
def get_users(model: UserModel):
    ds = None
    try:
        ds = get_connection()  # Create a new session
        model.userItems = UserItems()
        model.userItems.items = []
        users = ds.query(UserEntity).all()
        users = ds.query(UserEntity).filter(UserEntity.id == model.item.id).to_list()
        user_items = []
        print("\n")
        print("Total users fetched from DB:", len(users))
        for user in users:
            user_items.append(UserItem(
                id=user.id,
                username=user.username,
                phone=user.phone,
                full_name=user.fullname,
                is_active=user.isactive,
                is_superuser=user.issuperuser,
                message="User found",
                IsInvalid=False
            ))
        model.Message = "Users retrieved successfully"
        model.IsInvalid = False
        model.userItems.items = user_items
        model.userItems.Message = "Users retrieved successfully"
        model.userItems.IsInvalid = False
        print("\n Total users fetched:", len(model.userItems.items))
        return model
    except Exception as e:
        model.userItems = UserItems()
        model.Message = f"Error retrieving users: {str(e)}"
        model.IsInvalid = True
        print("Error retrieving users:", e)
        return model
    finally:
        if ds is not None:
            ds.close()

def update_user_entity(item: UserItem)-> UserItem:
    ds = None
    try:
        ds = get_connection()  # Create a new session
        user = ds.query(UserEntity).filter(UserEntity.id == item.id).first()
        print("Fetched user for update:", user)
        if user:
            user.username = item.username
            user.phone = item.phone
            user.fullname = item.full_name
            user.isactive = item.is_active
            user.issuperuser = item.is_superuser
            user.updateddate = ti.now()  # Update the update date
            ds.commit() # Commit the transaction
        else:
            item.Message = "User not found"
            item.IsInvalid = True
            return item
    except Exception as e:
        item.Message = f"Error updating user: {str(e)}"
        item.IsInvalid = True
        return item
    finally:
        if ds is not None:
            ds.close()
    item.Message = "User updated successfully"
    item.IsInvalid = False
    return item

def delete_user(model: UserModel) -> UserModel:
    try:
        model = mu.validate_item_Id(model)
        if model.item.IsInvalid:
            return model
        model.item =  delete_user_entity(model.item)
    except Exception as e:
        if model.item is None:
            model.item = UserItem()
        model.item.Message = f"Error retrieving user: {str(e)}"
        model.item.IsInvalid = True
        model.IsInvalid = True
        model.Message = f"Error retrieving user: {str(e)}"  
    return model

def delete_user_entity(item: UserItem)-> UserItem:
    ds = None
    try:
        ds = get_connection()  # Create a new session
        user = ds.query(UserEntity).filter(UserEntity.id == item.id).first()
        if user:
            ds.delete(user)
            ds.commit() # Commit the transaction
            item.Message = f"User {item.id} deleted successfully"
            item.IsInvalid = False
            return item
        else:
            item.Message = f"User {item.id} not found"
            item.IsInvalid = True
            return item
    except Exception as e:
        item.Message = f"Error updating user: {str(e)}"
        item.IsInvalid = True
        return item
    finally:
        if ds is not None:
            ds.close()

def upsert_user(model: UserModel) -> UserModel:
    try:
        model = mu.validate_item_Id(model)
        if model.item.IsInvalid:
            return model
        model.item =  upsert_user_entity(model.item)
        print("item message after repo_get_user_by_id:", model.item.Message)
    except Exception as e:
        if model.item is None:
            model.item = UserItem()
        model.item.Message = f"Error retrieving user: {str(e)}"
        model.item.IsInvalid = True
        model.IsInvalid = True
        model.Message = f"Error retrieving user: {str(e)}"  
    return model

def upsert_user_entity(item: UserItem)-> UserItem:
    ds = None
    try:
        ds = get_connection()  # Create a new session
        user = ds.query(UserEntity).filter(UserEntity.id == item.id).first()
        if user:
            user.username = item.username
            user.phone = item.phone
            user.fullname = item.full_name
            user.isactive = item.is_active
            user.issuperuser = item.is_superuser
            user.updateddate = ti.now()  # Update the update date
            ds.commit() # Commit the transaction
            item.id = user.id
            item.Message = "User updated successfully"
            item.IsInvalid = False
            return item
        else:
            user = UserEntity(
            username=item.username,
            phone=item.phone,
            fullname  =item.full_name,
            isactive=item.is_active,
            issuperuser=item.is_superuser
            )
            user.createddate = ti.now()  # Set the creation date
            user.updateddate = ti.now()  # Set the update date
            ds.add(user)
            ds.commit()  # Commit the transaction
            ds.refresh(user)  # Refresh the entity to get the ID and other fields
            # item.id = entity.id  # Set the ID from the created entity
            item.id = user.id
            item.Message = "User created successfully"
            item.IsInvalid = False
            return item
    except Exception as e:
        item.Message = f"Error updating user: {str(e)}"
        item.IsInvalid = True
        return item
    finally:
        if ds is not None:
            ds.close()
    return item


def repo_create_user(item: UserItem):
    ds = None
    try:
        item.Message = "User created successfully"
        entity = UserEntity(
            username=item.username,
            phone=item.phone,
            fullname  =item.full_name,
            isactive=item.is_active,
            issuperuser=item.is_superuser
        )
        entity.createddate = ti.now()  # Set the creation date
        entity.updateddate = ti.now()  # Set the update date
        #DATABASE_URL = "postgresql+psycopg://postgres:Postgres%40007@localhost:5432/vikihospitalbot"
        DATABASE_URL = "postgresql+psycopg://postgres:Postgres%40007@localhost:5432/VikiHospitalBot"
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
        ds = SessionLocal()  # Create a new session
        ds.add(entity)
        ds.commit()  # Commit the transaction
        ds.refresh(entity)  # Refresh the entity to get the ID and other fields
        item.id = entity.id
        item.Message = "User created successfully"
        item.IsInvalid = False
        return item
    except Exception as e:
        item.Message = f"Error creating user: {str(e)}"
        item.IsInvalid = True 
        return item
    finally:
        if ds is not None:
            ds.close()
        if item.IsInvalid:
            item.Message = "invalid user data"
            
            
