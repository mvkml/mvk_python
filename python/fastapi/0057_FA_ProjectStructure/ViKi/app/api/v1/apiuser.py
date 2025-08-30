from fastapi import APIRouter
router = APIRouter()

from models.userItem import UserItem  # Import UserItem model for request body validation
from models.UserModel import UserModel  # Import UserModel for input parameter and return type  
from models.userItem import UserItems  # Import UserItem model for request body validation
from repositories.user_repo import repo_create_user,repo_get_user_by_userId,repo_get_all_users  # Import UserRepo for database operations

@router.get("/cr")  
def create_user():
    return {"message": "User Avialable"}


# /getuserbyid?id=1
# http://127.0.0.1:802/api/v1/user/getuser/byid/1
@router.get("/getuser/byid/{id}", response_model=UserItem)  
def get_user_by_id(id: int):
    response = UserItem()
    try:
        model = UserModel()
        model.id = id
        print("\n")
        print("Fetching user with ID:", id)
        model = repo_get_user_by_userId(model)
        response =  model.item
    except Exception as e:
        print("Error fetching user:", e)
        response.message = f"Error fetching user: {e}"   
    return response


#http://127.0.0.1:802/api/v1/user/getusers
@router.get("/getusers", response_model=UserItems)  
def get_users():
    response = UserItems()
    try:
        model = UserModel()
        print("\n")
        print("Fetching all users")
        model = repo_get_all_users(model)
        print("\n")
        print("Number of users fetched:", len(model.userItems.items))
        response =  model.userItems
    except Exception as e:
        print("Error fetching users:", e)
        response.Message = f"Error fetching users: {e}"
    return response




@router.get("/getuser")  
def get_user():
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
