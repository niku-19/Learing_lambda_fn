import json
from models.bad_request_error import BadRequestError
from utils.database import DatabaseConnectionManager
from models.custom_response import CustomResponse
from models.user_model import User
from utils.common.logger import configure_logger

#Configuring the Logger
get_module_logger = configure_logger()

def update_user_by_id_handler(event, context):
      """
      This function help to update a user by _id means user id.
      """

      logger = get_module_logger()

      body = json.loads(event["body"])
      user_id : str = event["pathParameters"]["_id"]


      if not user_id:
            logger.error("Missing user_id in the event")
            return BadRequestError("Missing userId ad _id.").response()


      #*checking validation 
      user : User = User(**body)

      #stabilizing connection with database
      with DatabaseConnectionManager() as db:    
            #* UPDATING USER
            db.users.update_one({"_id": user_id}, {"$set": user.model_dump()})
            logger.info(f"User updated : {user_id}")


      return CustomResponse(body={
            "message": "User updated Successfully",
      } , data = user_id).response()
            



