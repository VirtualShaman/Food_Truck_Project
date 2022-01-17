from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app


class Menu:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.price = data['price']
        self.vote = data['vote']
        self.img_path = data['img_path']
        self.category = data['category']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def all_menu_items(cls):
        query = "SELECT * FROM menu_items;"
        results = connectToMySQL("food_truck").query_db(query)
        

        menu_items = []

        for oneitem in results :
            menu_items.append(cls(oneitem))

        return menu_items

    @classmethod
    def one_menu_item( cls, data ):
        query = "SELECT * FROM menu_items WHERE menu_items.id = %(menu_item_id)s;"

        results = connectToMySQL('food_truck').query_db(query, data)

        menu_item = cls(results[0])

        return menu_item

    @classmethod
    def submit_menu_item( cls, data ):
        query = "INSERT INTO menu_items (name, description, price, category, created_at, updated_at) VALUES (%(name)s, %(description)s, %(price)s, %(category)s, NOW(), NOW());"

        results = connectToMySQL('food_truck').query_db(query, data)

        return results

    @classmethod
    def update_menu_item( cls, data):
        query = "UPDATE menu_items SET name = %(name)s, description = %(description)s, price = %(price)s, category = %(category)s, updated_at = NOW() WHERE id= %(menu_item_id)s;"
        results = connectToMySQL('food_truck').query_db(query, data)
        return results

    @classmethod
    def delete_menu_item(cls,data):
        query = "DELETE FROM menu_items WHERE id = %(menu_item_id)s"
        results = connectToMySQL('food_truck').query_db(query, data)
        return results