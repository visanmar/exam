from werkzeug.security import generate_password_hash, check_password_hash


class UsersModel():

    @classmethod
    def user_exists(cls, mongo, email):
        try:
            cursor = mongo.db.usuarios.find_one({'email':email})
            if cursor:
                return True
            else:
                return False
        except Exception as exc:
            raise exc
        
    @classmethod
    def register_user(cls, mongo, email, password):
        try:
            hashed_password = generate_password_hash(password)
            user_id = mongo.db.usuarios.insert_one({'email':email, 'password':hashed_password}).inserted_id
            if not user_id:
                return False
            print(user_id)
            return user_id
        except Exception as exc:
            print(exc)
            raise exc