from lambda_function import lambda_handler



context = {}

#* TESTING API

#* CREATE USER EXAMPLE EVENT 

# event = {
#     "body": "{\"firstName\":\"N\",\"lastName\":\"Gaikwad\", \"age\": 22, \"email\":\"om.gaikwad@braincells.in\" , \"phoneNumber\":\"+916205666646\" , \"password\":\"Nikhil$1999@05@19$;?;\" ,\"isEnabled\": true,\"birthday\":\"1999-05-19 05:30:00\"}",
#     "routeKey": "POST /user",
# }

#* GET USER EXAMPLE EVENT
# event = {
#     "body": "",
#     "routeKey": "GET /user/{userId}",
#     "pathParameters": {
#         "_id" : "6678305e2bbaf46945ef33fa"
#     }
#}


#* DELETE USER EXAMPLE EVENT

# event = {
#     "body" : "",
#     "routeKey" : "DELETE /user/{userId}",
#     "pathParameters" : {
#         "_id" : "66726ccb6c78aa85232361b6"
#     }
# }


#* UPDATE USER EXAMPLE EVENT

# event = {
#     "body": "{\"firstName\":\"Niku\",\"lastName\":\"Kumar\", \"age\": 24, \"email\":\"nikhilranjankumar1999@gmail.com.com\" , \"phoneNumber\":\"+916203601617\" , \"password\":\"Nikhil$1999@05@19$;?;\" ,\"isEnabled\": true,\"birthday\":\"1999-05-19 05:30:00\"}",
#     "routeKey": "PUT /user/{userId}",
#     "pathParameters" : {
#         "_id" : "667275b2bd7538ba8d70e00a"
#     }
# }


#* UPDATE USER USING PATCH EXAMPLE EVENT
# event = {
#     "body": "{\"firstName\":\"Niku Ranjan\",\"password\":\"$1999@05@19$;?;\"}",
#     "routeKey": "PATCH /user/{userId}",
#     "pathParameters" : {
#         "_id" : "6678305e2bbaf46945ef33fa"
#     }
# }


print(lambda_handler(event, context))