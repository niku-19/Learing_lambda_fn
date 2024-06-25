import json

from http import HTTPStatus
from utils.database import DatabaseConnectionManager
from bson import ObjectId
from models.user_model import User
from models.custom_response import CustomResponse


def create_user_handler(event , context): #FIXME : event or context should not be here
    """
    Creates a new user in the database based on the provided event data.

    Args:
    event (dict): The event data containing the user information.
    context (Any): The context of the function call (not used).

    Returns:
    dict: The inserted user document, or a BadRequestError if the user data is invalid.
    """

    
    # #* Extracting data from event
    #FIXME: REMOVE THIS LINE
    body = json.loads(event["body"])

    #* checking validation with pydantic
    user : User = User(**body)

    #* if validation is pass then we connect the db and save the user into the database  
    # FIXME: for now i am adding _id manually - need to be replace
    userId : str = str(ObjectId())


    # Updating user with _id 
    new_user_with_id = {**dict(user), "_id": userId}

    with DatabaseConnectionManager() as db :
        db.users.insert_one(new_user_with_id)
    
    return CustomResponse(body = {"message" : "User Created Successfully."} , data = new_user_with_id , statusCode = HTTPStatus.CREATED).response()
