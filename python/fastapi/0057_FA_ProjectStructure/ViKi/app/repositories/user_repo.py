from models.userItem import UserItem  # Import UserItem model for request body validation
from models.userItem import UserItems  # Import UserItem model for request body validation
from db.entities.userentity import UserEntity  # Import UserEntity for database operations
from models.UserModel import UserModel  # Import UserModel for input parameter and return type
from db.DBSession import get_db_session  # Import the session management function
from datetime import datetime as ti
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

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
        if model is None:
            model = UserModel()
            model.item = UserItem(
                id=0,
                username="",
                email="",
                phone="",
                full_name="",
                is_active=False,
                is_superuser=False,
                message="Invalid user model",
                IsInvalid=True
            )
            return model
        if model.id is None or model.id <= 0:
            model.item = UserItem(
                id=0,
                username="",
                email="",
                phone="",
                full_name="",
                is_active=False,
                is_superuser=False,
                message="Invalid user ID",
                IsInvalid=True
            )
            return model
        item =  repo_get_user_by_id(model.id)
        print("/n")
        print("repo_get_user_by_id",item.message)
        model.item = item
        print("item message after repo_get_user_by_id:", model.item.message)
    except Exception as e:
        if model is None:
            model = UserModel()
        if model.item is None:
            model.item = UserItem()
        model.item.message = f"Error retrieving user: {str(e)}"
        model.item.IsInvalid = True  
    return model

#can you mention response model in function defination  
def repo_update_user_by_userId(model: UserModel):
    try:
        if model is None:
            model = UserModel()
            model.item = UserItem(
                id=0,
                username="",
                email="",
                phone="",
                full_name="",
                is_active=False,
                is_superuser=False,
                message="Invalid user model",
                IsInvalid=True
            )
            return model
        if model.id is None or model.id <= 0:
            model.item = UserItem(
                id=0,
                username="",
                email="",
                phone="",
                full_name="",
                is_active=False,
                is_superuser=False,
                message="Invalid user ID",
                IsInvalid=True
            )
            return model
        item =  repo_get_user_by_id(model.id)
        print("/n")
        print("repo_get_user_by_id",item.message)
        model.item = item
        print("item message after repo_get_user_by_id:", model.item.message)
    except Exception as e:
        if model is None:
            model = UserModel()
        if model.item is None:
            model.item = UserItem()
        model.item.message = f"Error retrieving user: {str(e)}"
        model.item.IsInvalid = True  
    return model



def repo_get_all_users(model: UserModel):
    ds = None
    try:
        #DATABASE_URL = "postgresql+psycopg://postgres:Postgres%40007@localhost:5432/vikihospitalbot"
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

def repo_get_user_by_id(user_id: int):
    print("/n")
    print("repo get user by id ")
    ds = None
    try:
        #DATABASE_URL = "postgresql+psycopg://postgres:Postgres%40007@localhost:5432/vikihospitalbot"
        DATABASE_URL = "postgresql+psycopg://postgres:Postgres%40007@localhost:5432/VikiHospitalBot"
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
        ds = SessionLocal()  # Create a new session
        user = ds.query(UserEntity).filter(UserEntity.id == user_id).first()
        if user:
            print("\n User found:", user.username)
            return UserItem(
                id=user.id,
                username=user.username,
                phone=user.phone,
                full_name=user.fullname,
                is_active=user.isactive,
                is_superuser=user.issuperuser,
                message="User found",
                IsInvalid=False
            )
        else:
            print("\n User not found with ID:", user_id)
            return UserItem(
                id=0,
                username="",
                email="",
                phone="",
                full_name="",
                is_active=False,
                is_superuser=False,
                message="User not found",
                IsInvalid=True
            )
    except Exception as e:
        return UserItem(
            id=0,
            username="",
            email="",
            phone="",
            full_name="",
            is_active=False,
            is_superuser=False,
            message=f"Error retrieving user: {str(e)}",
            IsInvalid=True
        )
    finally:
        if ds is not None:
            ds.close()

def repo_create_user(item: UserItem):
    ds = None
    try:
        item.Message = "User created successfully"
        item.message = "SQL Created Successfully"
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
        # item.id = entity.id  # Set the ID from the created entity
        item.message = "User created successfully"
        item.IsInvalid = False
        return item
    except Exception as e:
        item.Message = "failed"
        item.message = f"Error creating user: {str(e)}"
        item.IsInvalid = True 
        return item
    finally:
        if ds is not None:
            ds.close()
        if item.IsInvalid:
            item.message = "invalid user data"