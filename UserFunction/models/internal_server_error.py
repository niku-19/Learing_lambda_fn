
import datetime
import json


class InternalServerError():
      def __init__(self, error = "Server Error"):
            self.statusCode = 501
            self.body = json.dumps({
            "message": "Internal Server Error",
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