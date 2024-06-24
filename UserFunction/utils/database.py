import os
import pymongo
from pymongo import MongoClient
from models.internal_server_error import InternalServerError
from pymongo.database import Database





DATABASE_NAME : str = os.environ.get('DATABASE_NAME' , "backed_rest_api")
MONGO_URL :str = os.environ.get('MONGO_URL', "mongodb://localhost:27017/")

class DatabaseConnectionManager:
      def __init__(self):
            self.db = None
            self.client = None

      def initialise_db(self):
            # Connect to MongoDB
            self.client = MongoClient(MONGO_URL , timeoutMS = 1000)
            
            # Check server connection
            self.client.server_info()
            
            # Access a specific database
            self.db = self.client[DATABASE_NAME]
            return self.db
            
      def __enter__(self):
            self.initialise_db()
            return self.db

      def __exit__(self , exc_type , exc_value , exc_tb):
            # Close the MongoDB client connection
            try:
                  if self.client:
                        self.client.close()
            except Exception as e :
                  logger.error(f"Exit Error {e}")            
                  logger.error(f"Exit Error {exc_type}")            
                  logger.error(f"Exit Error {exc_value}")            
                  logger.error(f"Exit Error {exc_tb}")            

                  




DatabaseConnectionManager().initialise_db()