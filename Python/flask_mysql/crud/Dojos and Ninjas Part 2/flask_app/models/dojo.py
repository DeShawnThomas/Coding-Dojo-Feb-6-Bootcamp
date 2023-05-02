from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name,created_at,updated_at) VALUES (%(name)s,now(),now())"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results
    
    @classmethod
    def get_dojo_with_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                'id': row_from_db['ninjas.id'],
                'first_name': row_from_db['first_name'],
                'last_name': row_from_db['last_name'],
                'age': row_from_db['age'],
                'created_at': row_from_db['ninjas.created_at'],
                'updated_at': row_from_db['ninjas.updated_at']
            }
            dojo.ninjas.append( ninja.Ninja(ninja_data) )
        return dojo
    
    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)

        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db =  connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        all_dojos_from_db =[]
        for dojo in dojos_from_db:
            all_dojos_from_db.append(cls(dojo))
        return all_dojos_from_db

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        dojo_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(dojo_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)


