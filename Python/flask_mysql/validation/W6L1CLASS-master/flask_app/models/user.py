from flask_app.config.mysqlconnection import connectToMySQL
import re

from flask_app.models import post
from flask import flash,request

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:

    db="facegram"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.posts=[]



    #CREATE
    @classmethod
    def save(cls,data):
        
        query="""
        INSERT INTO users(first_name,last_name,email,password) 
        VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    #READ
    @classmethod
    def get_all(cls):
        query="""
        SELECT * FROM users
        LEFT JOIN posts
        ON users.id = posts.user_id;
        
        """
        results = connectToMySQL(cls.db).query_db(query)
        # print(results)
        for key,value in results[0].items():
            print(key,":\t",value)
        users =[]
        this_user = None
        for row in results:
            if len(users) == 0 or not this_user.id == row['id']:
                this_user = cls(row)
                users.append(this_user)
            if row["posts.id"] == None:
                continue
            else:
                data={
                    'id':row["posts.id"],
                    'img_url':row['img_url'],
                    'comment':row['comment'],
                    'created_at':row['posts.created_at'],
                    'updated_at':row['posts.updated_at'],
                    'user_id':row['user_id']
                }
                this_user.posts.append(post.Post(data))

        return users
    
    @classmethod
    def get_one_by_email(cls,email):
        data={
            "email":email
        }
        query="""
        SELECT * FROM users WHERE email=%(email)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        if not results:
            return []
        return cls(results[0])
    
    @classmethod
    def get_one(cls,id):
        data={
            "id":id
        }
        query="""
        SELECT * FROM users WHERE id=%(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    #UPDATE
    @classmethod
    def update(cls, data):
        query = """
        UPDATE users 
        SET first_name = %(first_name)s,
        last_name = %(last_name)s,
        email = %(email)s,
        password = %(password)s 
        WHERE id = %(id)s;"""

        results = connectToMySQL(cls.db).query_db(query, data)
        return results


    #DELETE
    @classmethod
    def delete(cls,id):
        data={
            'id':id
        }
        query="""
        DELETE FROM users
        WHERE id=%(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
        
    @staticmethod
    def validate_user(user):
        is_valid=True
        if len(user['f_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(user['l_name']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if len(user['email']) < 1:
            flash("Email must be entered.")
            is_valid = False
        #W6L1
        elif User.get_one_by_email(user['email']):
            flash("Email is already taken")
        elif not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        return is_valid
    
    #w6l1
    @staticmethod
    def validate_login(user):
        is_valid=True
        if len(user['email']) < 1:
            flash("Email must be entered.")
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False