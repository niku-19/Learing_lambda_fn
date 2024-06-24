import datetime
import json
from http import HTTPStatus

class BadRequestError():
    def __init__(self, error = "Server cannot understand this request" , status_code = HTTPStatus.BAD_REQUEST):
        self.statusCode = status_code
        self.body = json.dumps({
            "message": "Bad Request",
            "error": str(error)
        })
    
    def response(self):
        return {
            "success" : False,
            "statusCode": self.statusCode,
            "body": self.body,
            "data" : [],
            "headers": {
            "Content-Type": "application/json"
            },
            "meta": {
            "timestamp": str(datetime.datetime.now()),
            "request_id": "abcd-1234"
            }
        }