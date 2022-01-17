from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app


class Request:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.phone = data['phone']
        self.company = data['company']
        self.type = data['type']
        self.guestnum = data['guestnum']
        self.description = data['description']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.zip = data['zip']
        self.start = data['start']
        self.end = data['end']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def submit_request( cls, data ):
        query = "INSERT INTO requests (first_name, last_name, email, phone, company, type, guestnum, description, address, city, state, zip, start, end, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(phone)s, %(company)s, %(type)s, %(guestnum)s, %(description)s, %(address)s, %(city)s, %(state)s, %(zip)s, %(start)s, %(end)s, NOW(), NOW());"

        results = connectToMySQL('food_truck').query_db(query, data)

        return results

    @classmethod
    def all_requests(cls):
        query = "SELECT * FROM requests;"
        results = connectToMySQL("food_truck").query_db(query)

        requests = []

        for onerequest in results :
            requests.append(cls(onerequest))

        return requests

    @classmethod
    def one_request( cls, data ):
        query = "SELECT * FROM requests WHERE requests.id = %(request_id)s;"

        results = connectToMySQL("food_truck").query_db(query, data)

        request = cls(results[0])

        return request

    @classmethod
    def edit_request( cls, data ):
        query = "UPDATE requests SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, phone = %(phone)s, company = %(company)s, type = %(type)s, guestnum = %(guestnum)s, description = %(description)s, address = %(address)s, city = %(city)s, state = %(state)s, zip = %(zip)s, start = %(start)s, end = %(end)s, created_at = NOW(), updated_at = NOW() WHERE id = %(request_id)s;"

        results = connectToMySQL("food_truck").query_db(query, data)

        # request = cls(results[0])

        return results

    @classmethod
    def update_request_status( cls, data ):
        query = "UPDATE requests SET type = %(type)s, created_at = NOW(), updated_at = NOW() WHERE id = %(request_id)s;"

        results = connectToMySQL("food_truck").query_db(query, data)

        # request = cls(results[0])

        return results

    @classmethod
    def delete_request(cls,data):
        query = "DELETE FROM requests WHERE id = %(request_id)s"
        results = connectToMySQL('food_truck').query_db(query, data)
        return results

    @classmethod
    def delete_completed_catering_requests(cls):
        query = "DELETE FROM requests WHERE type = 'Catering - Complete'"
        results = connectToMySQL('food_truck').query_db(query)
        return results

    @classmethod
    def delete_spam_catering_requests(cls):
        query = "DELETE FROM requests WHERE type = 'Catering - Spam'"
        results = connectToMySQL('food_truck').query_db(query)
        return results

    @classmethod
    def delete_completed_contact_requests(cls):
        query = "DELETE FROM requests WHERE type = 'Contact - Complete'"
        results = connectToMySQL('food_truck').query_db(query)
        return results

    @classmethod
    def delete_spam_contact_requests(cls):
        query = "DELETE FROM requests WHERE type = 'Contact - Spam'"
        results = connectToMySQL('food_truck').query_db(query)
        return results