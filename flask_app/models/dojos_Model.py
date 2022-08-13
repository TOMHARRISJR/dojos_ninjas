from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas_Model import Ninja

class Dojo():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def display_dojos(cls):
        query = "SELECT * from dojos;"
        results = connectToMySQL('dojos_ninja_schema').query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for item in results:
            dojos.append(cls(item))
        return dojos

    @classmethod
    def add_Dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        results = connectToMySQL('dojos_ninja_schema').query_db(query, data)
        print(results)
        return results 

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos where id = %(id)s;"
        results = connectToMySQL('dojos_ninja_schema').query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def get_all_ninjas(cls,data):
        query = "SELECT * FROM ninja WHERE dojo_id = %(id)s;"
        results = connectToMySQL('dojos_ninja_schema').query_db(query, data)
        if not results:
            return False
        ninjas = []
        # Iterate over the db results and create instances of dojos with cls.
        for item in results:
            ninjas.append(Ninja(item))
        return ninjas



        
        