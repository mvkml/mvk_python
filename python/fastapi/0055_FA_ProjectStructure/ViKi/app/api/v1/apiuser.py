from fastapi import APIRouter
router = APIRouter()

from models.userItem import UserItem  # Import UserItem model for request body validation
from repositories.user_repo import repo_create_user  # Import UserRepo for database operations

@router.get("/cr")  
def create_user():
    return {"message": "User Avialable"}

@router.post("/create", response_model=UserItem)  
def create_user(item: UserItem):
    print("Creating user with data:", item)
    item.full_name = item.full_name or "No Name Provided"
    item.is_active = item.is_active if item.is_active is not None else True
    item.is_superuser = item.is_superuser if item.is_superuser is not None else False
    item.message = "User Created Successfully"
    item.message = "test"
    print("User data after processing:", item)
    print("\n")
    print("Calling repository to create user")
    item =  repo_create_user(item)  # Call the repository function to handle the creation logic
    print("\n")
    print("completed repository call to create user with data:", item)
    return item
    #return {"message": f"User Avialable {item.username}, {item.email}, {item.phone}, {item.full_name}, {item.is_active}, {item.is_superuser}, {item.message}"}


# Default endpoint for the User module
@router.get("/hi")
def default():
    return {"message": "User Avialable"}


@router.get("/hello")
def hello_user():
    """
    Simple test endpoint for User module.
    Will be available at: /api/v1/user/hello
    """
    return {"message": "Hello from User API"}
