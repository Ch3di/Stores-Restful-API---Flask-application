from models.user import UserModel
from werkzeug.security import safe_str_cmp # compare strings safely


def authenticate(username, password):
    user = UserModel.findUserByUsername(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identify(payload):
    user_id = payload['identity']
    return UserModel.findUserById(user_id)
