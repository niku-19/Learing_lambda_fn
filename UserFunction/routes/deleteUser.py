from models.bad_request_error import BadRequestError
from utils.database import DatabaseConnectionManager
from models.custom_response import CustomResponse
from http import HTTPStatus
from utils.common.logger import configure_logger
from pymongo.database import Database
from models.user_model import User
import logging

#* Configuring the logger 
get_module_logger = configure_logger()

def delete_user_by_id_handler(event , context):
      """
            This function help to delete a user by _id means user id.
      """
      logger = get_module_logger()

      #* Extracting the userId from path Parameters.
      user_id : str = event["pathParameters"]["_id"]

      #* If userId is not preset | userId is empty then ->
      if not user_id: #HACK
            logger.error("Missing user_id in the event")
            return BadRequestError("Missing userId as _id").response()

      #* connection with database
      with DatabaseConnectionManager() as db:      
            #* deleting user
            db.users.delete_one({"_id": user_id})

      #* Unsubscribing the logger 
      return CustomResponse(body={"message": "User deleted successfully"}, data = user_id ).response()


