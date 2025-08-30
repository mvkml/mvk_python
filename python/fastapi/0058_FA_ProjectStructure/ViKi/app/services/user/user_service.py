from models.userItem import UserItem  # Import UserItem model for request body validation
from models.UserModel import UserModel  # Import UserModel for input parameter and return type
from models.userItem import UserItems  # Import UserItem model for request body validation
from repositories import user_repo
from common import model_utility as mu


def delete_users(model:UserModel)-> UserModel:
    model = mu.validate_delete_items(model)
    if model.IsInvalid:
        return model
    model =  user_repo.upsert_users(model)
    model.multiResponse = mu.get_UsersResponse(model)
    return model

def upsert_users(model:UserModel)-> UserModel:
    model = mu.validate_create_items(model)
    if model.IsInvalid:
        return model
    model =  user_repo.upsert_users(model)
    model.multiResponse = mu.get_UsersResponse(model)
    return model

def update_user(model:UserModel)-> UserModel:
    model =  user_repo.update_user(model)
    model.response = mu.get_UserResponse(model.item)
    return model

def upsert_user(model:UserModel)-> UserModel:
    model =  user_repo.upsert_user(model)
    model.response = mu.get_UserResponse(model.item)
    return model

def delete_user(model:UserModel)-> UserModel:
    model =  user_repo.delete_user(model)
    model.response = mu.get_UserResponse(model.item)
    return model
    