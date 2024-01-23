from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = "crud_db"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # the save method will be used when we need to save a new friend to our database
    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name,last_name,email)
    		VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users; "
        results = connectToMySQL(cls.DB).query_db(query)
        users= []
        for row in results:
            new_user = cls (row)
            users.append(new_user)
        return users



