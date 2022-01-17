from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app


class Info:
    def __init__(self, data):
        self.id = data['id']
        self.open_days = data['open_days']
        self.open_hours = data['open_hours']
        self.about = data['about']

    # @classmethod
    # def submit_info( cls, data ):
    #     query = "INSERT INTO info (open_days, open_hours, about, created_at, updated_at) VALUES (%(open_days)s, %(open_hours)s, %(about)s, NOW(), NOW());"

    #     results = connectToMySQL('food_truck').query_db(query, data)

    #     return results

    @classmethod
    def all_info(cls):
        query = "SELECT * FROM info;"
        results = connectToMySQL("food_truck").query_db(query)

        info = []

        for oneinfo in results :
            info.append(cls(oneinfo))

        return info

    @classmethod
    def one_info_item( cls, data ):
        query = "SELECT * FROM info WHERE info.id = %(info_id)s;"

        results = connectToMySQL("food_truck").query_db(query, data)

        info = cls(results[0])

        return info

    @classmethod
    def edit_info( cls, data ):
        query = "UPDATE info SET open_days = %(open_days)s, open_hours = %(open_hours)s, about = %(about)s, created_at = NOW(), updated_at = NOW() WHERE id = %(info_id)s;"

        results = connectToMySQL("food_truck").query_db(query, data)

        # request = cls(results[0])

        return results