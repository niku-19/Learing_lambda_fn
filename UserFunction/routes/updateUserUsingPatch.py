import json
from utils.common.logger import configure_logger
from models.bad_request_error import BadRequestError
from utils.database import DatabaseConnectionManager
from models.custom_response import CustomResponse

#Configuration of the logger
get_module_logger = configure_logger()


def update_user_by_id_using_patch_handler(event, context):
      """
      This function help us to update a user using patch method. such that user can patch only the required fields.
      """
      logger = get_module_logger()

      body = json.loads(event["body"])
      userId : str = event["pathParameters"]["_id"]

      #TODO : add input validator

      #* Checking that userId is not None
      if not userId.strip():
            logger.error("Missing userId in the event")
            return BadRequestError("Missing userId as _id.").response()
      
      with DatabaseConnectionManager() as db:
            db.users.update_one({"_id": userId}, {"$set": body})

      #Unsubscribing the logger
      return CustomResponse({
            "message" : "User Updated Successfully",
            } , data = userId).response()
            
            