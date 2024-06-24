from pydantic import ValidationError
import pymongo
from models.internal_server_error import InternalServerError
from routes import switcher
from typing import Any, Dict
from utils.common.logger import configure_logger
from models.bad_request_error import BadRequestError
import logging

get_module_logger = configure_logger()


# This is the main function | This is the main handler which executes first when user hits an API call.
def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    # Getting the logger from the get_module_logger function
    logger = get_module_logger()

    try:
        route_key : str = event.get('routeKey')
        return switcher[route_key](event, context)
    except pymongo.errors.ServerSelectionTimeoutError as e:
        logger.error(f"MongoDB Error: {e}")
        internal_server_error = InternalServerError(str(e))
        return internal_server_error.response()
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        return BadRequestError(str(e)).response()
    except Exception as e:
        logger.error(f"Error: {e}")
        internal_server_error = InternalServerError(str(e))
        return internal_server_error.response()


    