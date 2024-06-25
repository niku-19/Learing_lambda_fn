import json
from routes.createUser import create_user_handler
from http import HTTPStatus
from routes.getUser import get_user_by_id_handler
from routes.updateUser import update_user_by_id_handler
from routes.updateUserUsingPatch import update_user_by_id_using_patch_handler
from routes.deleteUser import delete_user_by_id_handler

def test_create_user_handler():
    event = {
    "body": "{\"firstName\":\"OM\",\"lastName\":\"Gaikwad\", \"age\": 22, \"email\":\"om.gaikwad@braincells.in\" , \"phoneNumber\":\"+916205666646\" , \"password\":\"Nikhil$1999@05@19$;?;\" ,\"isEnabled\": true,\"birthday\":\"1999-05-19 05:30:00\"}",
    "routeKey": "POST /user",
    }
    context = {}

    create_new_user_response = create_user_handler(event , context)

    # Here We are Checking for the create_new_user_response to be a success
    assert create_new_user_response['success'] == True

    # Here we are Checking for the create_new_user_response state to be CREATED
    assert create_new_user_response['statusCode'] == HTTPStatus.CREATED

    # Now if a new user is create then definitely we have _id that represent uniqueId for each use
    # So lets take out the _id from the create_new_user_response
    create_new_user_id = create_new_user_response["data"]["_id"]

    get_user_event = {
        "body": "",
        "routeKey": "GET /user/{userId}",
        "pathParameters": {
        "_id" : f"{create_new_user_id}"
        }
        }
    
    get_user_response = get_user_by_id_handler(get_user_event , context)

    # Here We are Checking for the get_user_response to be a success
    assert get_user_response['success'] == True

    # Here we are Checking for the get_user_response state to be OK
    assert get_user_response['statusCode'] == HTTPStatus.OK

    # Now what can we do is we can check the data that u want to create is same or something wrongs happens
    # So lets take out the data from get_ser_response 

    get_user_response_data = get_user_response["data"]

    #so as of now check for the _id further we can also check for the accurate data

    assert get_user_response_data["_id"] == create_new_user_id



def test_update_user_handler():
    #* SO HERE WE HAVE TO DO THREE TASK
    #* 1. CREATE A NEW USER
    #* 2. UPDATE THE USER
    #* 3. GET THE USER AND VALIDATE THE DATA IS THE UPDATED ONE OR NOT 

    event = {
    "body": "{\"firstName\":\"OM\",\"lastName\":\"Gaikwad\", \"age\": 22, \"email\":\"om.gaikwad@braincells.in\" , \"phoneNumber\":\"+916205666646\" , \"password\":\"Nikhil$1999@05@19$;?;\" ,\"isEnabled\": true,\"birthday\":\"1999-05-19 05:30:00\"}",
    "routeKey": "POST /user",
    }

    context = {}

    create_new_user_response = create_user_handler(event , context)

    # Here We are Checking for the create_new_user_response to be a success
    assert create_new_user_response['success'] == True

    # Here we are Checking for the create_new_user_response state to be CREATED
    assert create_new_user_response['statusCode'] == HTTPStatus.CREATED

    # Now if a new user is create then definitely we have _id that represent uniqueId for each use
    # So lets take out the _id from the create_new_user_response
    create_new_user_id = create_new_user_response["data"]["_id"]

    # Now we have to update the user
    update_user_event = {
    "body": "{\"firstName\":\"Niku\",\"lastName\":\"Kumar\", \"age\": 24, \"email\":\"nikhilranjankumar1999@gmail.com.com\" , \"phoneNumber\":\"+916203601617\" , \"password\":\"Nikhil$1999@05@19$;?;\" ,\"isEnabled\": true,\"birthday\":\"1999-05-19 05:30:00\"}",
    "routeKey": "PUT /user/{userId}",
    "pathParameters" : {
        "_id" : f"{create_new_user_id}"
        }
    }

    update_user_response = update_user_by_id_handler(update_user_event , context)

    # Here We are Checking for the update_user_response to be a success
    assert update_user_response['success'] == True

    # Here we are Checking for the update_user_response state to be OK
    assert update_user_response['statusCode'] == HTTPStatus.OK

    # Now Lets get the updated user. While updating the user we can not changes its unique id so lets try to catch with same id.

    get_user_event = {
        "body": "",
        "routeKey": "GET /user/{userId}",
        "pathParameters": {
        "_id" : f"{create_new_user_id}"
        }
        }
    

    get_user_response = get_user_by_id_handler(get_user_event , context)

    # Here We are Checking for the get_user_response to be a success
    assert get_user_response['success'] == True

    # Here we are Checking for the get_user_response state to be OK
    assert get_user_response['statusCode'] == HTTPStatus.OK

    # Now what can we do is we can check the data that is updated or not
    # So lets take out the data from get_ser_response

    get_user_response_data = get_user_response["data"]

    #HACK Now lets check the content that is updated
    assert get_user_response_data["firstName"] == "Niku"
    assert get_user_response_data["lastName"] == "Kumar"
    assert get_user_response_data["age"] == 24
    assert get_user_response_data["email"] == "nikhilranjankumar1999@gmail.com.com"
    assert get_user_response_data["phoneNumber"] == "+916203601617"
    assert get_user_response_data["isEnabled"] == True
    assert get_user_response_data["_id"] == create_new_user_id



def test_update_user_handler_with_patch_request():
    #* SO HERE WE HAVE TO DO 4 TASK
    #* 1. CREATE A NEW USER
    #* 2. UPDATE THE USER
    #* 3. GET THE USER AND VALIDATE THE DATA IS THE UPDATED ONE OR NOT
    #* 4. CHECK IF THE DATA IS UPDATED OR NOT WITH PATCH REQUEST


    event = {
    "body": "{\"firstName\":\"OM\",\"lastName\":\"Gaikwad\", \"age\": 22, \"email\":\"om.gaikwad@braincells.in\" , \"phoneNumber\":\"+916205666646\" , \"password\":\"Nikhil$1999@05@19$;?;\" ,\"isEnabled\": true,\"birthday\":\"1999-05-19 05:30:00\"}",
    "routeKey": "POST /user",
    }
    context = {}

    create_new_user_response = create_user_handler(event , context)

    # Here We are Checking for the create_new_user_response to be a success
    assert create_new_user_response['success'] == True

    # Here we are Checking for the create_new_user_response state to be CREATED
    assert create_new_user_response['statusCode'] == HTTPStatus.CREATED

    # Now if a new user is create then definitely we have _id that represent uniqueId for each use
    # So lets take out the _id from the create_new_user_response
    create_new_user_id = create_new_user_response["data"]["_id"]

    get_user_event = {
        "body": "",
        "routeKey": "GET /user/{userId}",
        "pathParameters": {
        "_id" : f"{create_new_user_id}"
        }
        }
    
    get_user_response = get_user_by_id_handler(get_user_event , context)

    # Here We are Checking for the get_user_response to be a success
    assert get_user_response['success'] == True

    # Here we are Checking for the get_user_response state to be OK
    assert get_user_response['statusCode'] == HTTPStatus.OK

    # Now what can we do is we can check the data that u want to create is same or something wrongs happens
    # So lets take out the data from get_ser_response 

    get_user_response_data = get_user_response["data"]

    #so as of now check for the _id further we can also check for the accurate data

    assert get_user_response_data["_id"] == create_new_user_id



def test_update_user_handler():
    #* SO HERE WE HAVE TO DO THREE TASK
    #* 1. CREATE A NEW USER
    #* 2. UPDATE THE USER
    #* 3. GET THE USER AND VALIDATE THE DATA IS THE UPDATED ONE OR NOT 

    event = {
    "body": "{\"firstName\":\"OM\",\"lastName\":\"Gaikwad\", \"age\": 22, \"email\":\"om.gaikwad@braincells.in\" , \"phoneNumber\":\"+916205666646\" , \"password\":\"Nikhil$1999@05@19$;?;\" ,\"isEnabled\": true,\"birthday\":\"1999-05-19 05:30:00\"}",
    "routeKey": "POST /user",
    }

    context = {}

    create_new_user_response = create_user_handler(event , context)

    # Here We are Checking for the create_new_user_response to be a success
    assert create_new_user_response['success'] == True

    # Here we are Checking for the create_new_user_response state to be CREATED
    assert create_new_user_response['statusCode'] == HTTPStatus.CREATED

    # Now if a new user is create then definitely we have _id that represent uniqueId for each use
    # So lets take out the _id from the create_new_user_response
    create_new_user_id = create_new_user_response["data"]["_id"]

    # Now we have to update the user
    update_user_event = {
    "body": "{\"firstName\":\"Niku Ranjan\",\"age\": 30}",
    "routeKey": "PATCH /user/{userId}",
    "pathParameters" : {
        "_id" : f"{create_new_user_id}"
    }
    }

    update_user_response = update_user_by_id_using_patch_handler(update_user_event , context)

    # Here We are Checking for the update_user_response to be a success
    assert update_user_response['success'] == True

    # Here we are Checking for the update_user_response state to be OK
    assert update_user_response['statusCode'] == HTTPStatus.OK

    # Now Lets get the updated user. While updating the user we can not changes its unique id so lets try to catch with same id.

    get_user_event = {
        "body": "",
        "routeKey": "GET /user/{userId}",
        "pathParameters": {
        "_id" : f"{create_new_user_id}"
        }
        }
    

    get_user_response = get_user_by_id_handler(get_user_event , context)

    # Here We are Checking for the get_user_response to be a success
    assert get_user_response['success'] == True

    # Here we are Checking for the get_user_response state to be OK
    assert get_user_response['statusCode'] == HTTPStatus.OK

    # Now what can we do is we can check the data that is updated or not
    # So lets take out the data from get_ser_response

    get_user_response_data = get_user_response["data"]

    #HACK Now lets check the content that is updated
    assert get_user_response_data["firstName"] == "Niku Ranjan"
    assert get_user_response_data["age"] == 30


def test_delete_user_handler():
    #* SO HERE WE HAVE TO DO THREE TASK
    #* 1. CREATE A NEW USER
    #* 2. DELETE THE USER
    #* 3. GET THE USER AND VALIDATE THE DATA IS THE DELETED ONE OR NOT

    event = {
    "body": "{\"firstName\":\"OM\",\"lastName\":\"Gaikwad\", \"age\": 22, \"email\":\"om.gaikwad@braincells.in\" , \"phoneNumber\":\"+916205666646\" , \"password\":\"Nikhil$1999@05@19$;?;\" ,\"isEnabled\": true,\"birthday\":\"1999-05-19 05:30:00\"}",
    "routeKey": "POST /user",
    }
    context = {}

    create_new_user_response = create_user_handler(event , context)

    # Here We are Checking for the create_new_user_response to be a success
    assert create_new_user_response['success'] == True

    # Here we are Checking for the create_new_user_response state to be CREATED
    assert create_new_user_response['statusCode'] == HTTPStatus.CREATED

    # Now if a new user is create then definitely we have _id that represent uniqueId for each use
    # So lets take out the _id from the create_new_user_response
    create_new_user_id = create_new_user_response["data"]["_id"]

    # Now we have to delete the user

    delete_user_event = {
    "body" : "",
    "routeKey" : "DELETE /user/{userId}",
    "pathParameters" : {
        "_id" : f"{create_new_user_id}"
    }
    }

    #Now lets make an api call

    delete_user_response = delete_user_by_id_handler(delete_user_event , context)

    # Here We are Checking for the delete_user_response to be a success
    assert delete_user_response['success'] == True

    # Here we are Checking for the delete_user_response state to be OK
    assert delete_user_response['statusCode'] == HTTPStatus.OK

    # Now lets check that user is deleted or while getting through _id.

    get_user_event = {
        "body": "",
        "routeKey": "GET /user/{userId}",
        "pathParameters": {
        "_id" : f"{create_new_user_id}"
        }
        }
    
    #Now lets make an api call

    get_user_response = get_user_by_id_handler(get_user_event , context)

    # Here We are Checking for the get_user_response to be a fail
    assert get_user_response['success'] == False

    # Here we are Checking for the get_user_response state to be NOT_FOUND
    assert get_user_response['statusCode'] == HTTPStatus.NOT_FOUND
