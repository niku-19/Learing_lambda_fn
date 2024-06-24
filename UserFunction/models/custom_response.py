import datetime
import json
from bson import ObjectId
import os
from http import HTTPStatus
DATE_TIME_FORMAT = os.environ.get("DATE_TIME_FORMAT" , "%Y-%m-%d %H:%M:%S")

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime(DATE_TIME_FORMAT)
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

class CustomResponse: #FIXME : CHANGE NAME
    """
    This class is used to create a custom response for the API calls.
    """
    
    def __init__(self,body = {}, data = [] , success = True , headers={"Content-Type": "application/json"} , statusCode = HTTPStatus.OK):
        self.statusCode = statusCode
        self.body = body 
        self.headers = headers
        self.data = data
        self.success = success


    def response(self):
        return {
            "success" : self.success,
            "statusCode": self.statusCode,
            "body": self.body,
            "data" : self.data,
            "headers": {
            "Content-Type": "application/json"
            },
            "meta": {
            "timestamp": str(datetime.datetime.now()),
            "request_id": "abcd-1234"
            }
        }
