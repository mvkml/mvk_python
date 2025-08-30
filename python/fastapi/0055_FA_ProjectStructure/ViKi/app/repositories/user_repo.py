from models.userItem import UserItem  # Import UserItem model for request body validation
from db.entities.userentity import UserEntity  # Import UserEntity for database operations
from db.DBSession import get_db_session  # Import the session management function
from datetime import datetime as ti
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine


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