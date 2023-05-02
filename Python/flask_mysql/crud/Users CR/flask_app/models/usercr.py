from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users(first_name,last_name,email,created_at,updated_at) VALUES (%(first_name)s, %(last_name)s,%(email)s,NOW(),NOW())"
        results = connectToMySQL('users_schema').query_db(query,data)
        return results

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        users_from_db =  connectToMySQL('users_schema').query_db(query)
        all_users_from_db =[]
        for user in users_from_db:
            all_users_from_db.append(cls(user))
        return all_users_from_db

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        user_from_db = connectToMySQL('users_schema').query_db(query,data)

        return cls(user_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)
