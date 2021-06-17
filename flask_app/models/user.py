# import the function that will return an instance of a connection
from ..config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        print(results)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT id, first_name, last_name, email, created_at, updated_at FROM users WHERE id=%(id)s;"
        print(query)
        results = connectToMySQL('users_schema').query_db(query, data)
        return results

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=now() WHERE id=%(id)s;"
        print(query)
        connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def delete_user(cls, data ):
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL('users_schema').query_db( query, data )