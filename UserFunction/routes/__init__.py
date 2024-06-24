from routes.createUser import create_user_handler
from routes.getUser import get_user_by_id_handler
from routes.deleteUser import delete_user_by_id_handler
from routes.updateUser import update_user_by_id_handler
from routes.updateUserUsingPatch import update_user_by_id_using_patch_handler


switcher  = {
    'POST /user': create_user_handler, # createUser 
    'GET /user/{userId}': get_user_by_id_handler,
    'DELETE /user/{userId}': delete_user_by_id_handler,
    'PUT /user/{userId}': update_user_by_id_handler,
    'PATCH /user/{userId}': update_user_by_id_using_patch_handler
}
