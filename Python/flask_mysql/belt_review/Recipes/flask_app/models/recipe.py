from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

class Recipe:
    db="users_with_recipes_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            all_recipe = cls(row)
            user_data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": "",
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            all_recipe.creator = user.User(user_data)
            recipes.append(all_recipe)
        return recipes
    
    @classmethod
    def get_one_by_id(cls,data):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        if not result:
            return False

        result = result[0]
        single_recipe = cls(result)
        user_data = {
                "id": result['users.id'],
                "first_name": result['first_name'],
                "last_name": result['last_name'],
                "email": result['email'],
                "password": "",
                "created_at": result['users.created_at'],
                "updated_at": result['users.updated_at']
        }
        single_recipe.creator = user.User(user_data)
        return single_recipe

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name,description,instructions,date_cooked,under_thirty,user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(date_cooked)s,%(under_thirty)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s , date_cooked = %(date_cooked)s, under_thirty = %(under_thirty)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if len(data['name']) < 3:
            flash("Name must be at least 3 characters long.")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 3 characters long.")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Instructions must be at least 3 characters long.")
            is_valid = False
        if data['date_cooked'] == '':
                flash("A date cooked is needed.")
                is_valid = False
        if 'under_thirty' not in data:
            flash("Under thirty minute cook time is required.")
            is_valid = False

        return is_valid