# common/model_utility.py
# Utility functions for model validation and manipulation
# This module provides common functions to validate and manipulate data models used across the application.
# It helps ensure data integrity and consistency before processing or storing in the database.
# Functions include validation checks, default value assignments, and data transformations.
# This will check model is valid or not
# It will return model with IsInvalid=True and Message with reason if invalid

from models.UserModel import UserModel, UserRequest, UserResponse,UsersResponse
from models.userItem import UserItem, UserItems
  
def validate_model(model:UserModel):
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
            Message="Invalid user model",
            IsInvalid=True
        )
        return model
    # Add more validation rules as needed
    model.IsInvalid = False
    model.Message = "Valid user model"
    return model

def validate_item_Id(model:UserModel) -> UserModel:
    print("Validating user ID in model...")
    model = validate_model(model)
    if model.IsInvalid:
        return model
    if model.item.IsInvalid:
        return model
    if model.item.id is None or model.item.id <= 0:
        model.item.IsInvalid = True
        model.item.Message = "Invalid user ID"
        model.IsInvalid = True
        model.Message = "Invalid user ID"
        return model
    model.item.IsInvalid = False
    model.IsInvalid = False
    model.Message = "Valid user ID"
    return model

def validate_item(model:UserModel) -> UserModel:
    model = validate_model(model)
    if model.IsInvalid:
        return model
    if model.item is None:
        model.item = UserItem(
            id=0,
            username="",
            email="",
            phone="",
            full_name="",
            is_active=False,
            is_superuser=False,
            Message="Invalid user item",
            IsInvalid=True
        )
        return model
    # Add more validation rules as needed
    model.item.IsInvalid = False
    model.item.Message = "Valid user item"
    model.item.IsInvalid = False
    return model

def validate_delete_items(model:UserModel) -> UserModel:
    model = validate_model(model)
    if model.IsInvalid:
        model.items = UserItems(items=[])
        model.Message = "users are required in model"
        model.IsInvalid = True
        return model
    elif model.items is None or len(model.items) == 0:
        model.items = UserItems(items=[])
        model.Message = "users are required in model"
        model.IsInvalid = True
        return model
    else:
        for item in model.items:
            if item.id is not None and item.id > 0  :
                item.Message = "User ID should not be provided for delete operation"
                item.IsInvalid = True
                return model
    
    # Add more validation rules as needed
    model.Message = "Valid users"
    model.IsInvalid = False
    return model


def validate_create_items(model:UserModel) -> UserModel:
    model = validate_model(model)
    if model.IsInvalid:
        model.items = UserItems(items=[])
        model.Message = "users are required in model"
        model.IsInvalid = True
        return model
    elif model.items is None or len(model.items) == 0:
        model.items = UserItems(items=[])
        model.Message = "users are required in model"
        model.IsInvalid = True
        return model
    else:
        for item in model.items:
            if not item.username or item.username.strip() == "":
                model.Message = "Username is required"
                model.IsInvalid = True
                return model
    
    # Add more validation rules as needed
    model.Message = "Valid users"
    model.IsInvalid = False
    return model


def get_UserResponse(source:UserItem) ->UserResponse:
    destination = UserResponse()
    destination.item = source
    destination.Message = source.Message
    destination.IsInvalid = source.IsInvalid
    return destination


def get_UsersResponse(source:UserModel) ->UserResponse:
    destination = UsersResponse()
    if source.items is None:
        source.items = []
    if destination.items is None:
        destination.items = []
    destination.items = source.items
    destination.Message = source.Message
    destination.IsInvalid = source.IsInvalid
    return destination