from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Post:

    db="facegram"

    def __init__(self,data):
        self.id = data['id']
        self.img_url = data['img_url']
        self.comment=data['comment']
        self.user_id = data['user_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.owner=None
        self.likes=[]



    #CREATE
    @classmethod
    def save(cls,data):
        
        query="""
        INSERT INTO posts(img_url,comment,user_id) 
        VALUES(%(img_url)s,%(comment)s,%(user_id)s);
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    #READ
    @classmethod
    def get_all(cls):
        query="""
        SELECT * FROM posts
        LEFT JOIN users
        ON posts.user_id = users.id
        LEFT JOIN likes
        ON posts.id = likes.post_id
        LEFT JOIN users AS liked_by
        ON likes.user_id = liked_by.id
        """
        results = connectToMySQL(cls.db).query_db(query)
        if not results:
            return []
        print("**********************")
        for key in results[0].keys():
            print(key)
        posts =[]
        this_post = None
        for row in results:
            if this_post == None or not this_post.id == row['id']:
                this_post = cls(row)
                data={
                    'id':row["users.id"],
                    'first_name':row['first_name'],
                    'last_name':row['last_name'],
                    'email':row['email'],
                    'password':row['password'],
                    'created_at':row['users.created_at'],
                    'updated_at':row['users.updated_at']
                }
                this_post.owner = user.User(data)
                posts.append(this_post)
            
            if not row['likes.user_id'] == None:
                data={
                    'id':row["liked_by.id"],
                    'first_name':row['liked_by.first_name'],
                    'last_name':row['liked_by.last_name'],
                    'email':row['liked_by.email'],
                    'password':row['liked_by.password'],
                    'created_at':row['liked_by.created_at'],
                    'updated_at':row['liked_by.updated_at']
                }

                this_post.likes.append(user.User(data))

            
        return posts
    
    
    
    @classmethod
    def get_one(cls,id):
        data={
            "id":id
        }
        query="""
        SELECT * FROM posts 
        LEFT JOIN users
        ON posts.user_id = users.id
        WHERE posts.id=%(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        print("WE ARE HERE")
        for key,value in results[0].items():
            print(key,"\t\t",value) 
        # print(results)
        return cls(results[0])

    #UPDATE
    @classmethod
    def update(cls, data):
        query = """
        UPDATE posts 
        SET img_url = %(img_url)s,
        comment = %(comment)s
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
        DELETE FROM posts
        WHERE id=%(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
        
    #w6l2
    @classmethod
    def like(cls,id,user_id):
        data={

            'post_id':id,
            'user_id':user_id
        }
        query = """
        INSERT INTO likes(post_id,user_id) 
        VALUES(%(post_id)s,%(user_id)s);
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    #TODO complete unlike functionality
    def unlike(cls,id,user_id):
        data={

            'id':id,
            'user_id':user_id
        }

        query = """
        DELETE FROM likes
        WHERE post_id = %(post_id)s
        AND user_id=%(user_id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return results