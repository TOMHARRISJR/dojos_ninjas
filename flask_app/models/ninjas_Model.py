from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['update_at']

    @classmethod
    def display_all_ninjas(cls):
        query = "SELECT * from ninja;"
        results = connectToMySQL('dojos_ninja_schema').query_db(query)
        # Create an empty list to append our instances of ninjas
        ninjas = []
        # Iterate over the db results and create instances of ninjas with cls.
        for item in results:
            ninjas.append(cls(item))
        return ninjas

    @classmethod
    def add_ninja(cls, data):
        query = "INSERT INTO ninja (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        results = connectToMySQL('dojos_ninja_schema').query_db(query, data)
        print(results)
        return results 

    @classmethod
    def get_one_ninja(cls, data):
        query = "SELECT * FROM ninja where id = %(id)s;"
        results = connectToMySQL('dojos_ninja_schema').query_db(query, data)
        if not results:
            return False
        return cls(results[0])
