from http import HTTPStatus
from models.bad_request_error import BadRequestError
from models.custom_response import CustomResponse
from utils.common.logger import configure_logger
from pymongo.database import Database
from models.user_model import User
from utils.database import DatabaseConnectionManager
import logging

get_module_logger = configure_logger()

def get_user_by_id_handler(event , context):
      """
      This function help to get user by it _id from the database.
      """
      # Getting the logger form the configure logger function
      logger = get_module_logger()

      #* Extracting the userId from path Parameters.
      userId : str = event['pathParameters']['_id']

      #* KEPT TEMP : NEED TO CHECK.
      if not userId:
            logger.error("Missing userId in the request")
            return BadRequestError("Missing userId as _id").response()

      #* connection with database
      with DatabaseConnectionManager() as db:
            user : User  = db.users.find_one({"_id": userId})

      #* if User is not found then ->
      if user is None :
            logger.error(f"User not found : {userId}")
            return BadRequestError(f"User not found with _id : {userId}" , status_code = HTTPStatus.NOT_FOUND).response()

      return CustomResponse(body={"message": "User found"} , data = user).response()


