from flask import Flask, Response, json
from flask_restful import Api, Resource, reqparse
import pymongo 
from bson.objectid import ObjectId

####################################################################################

app = Flask(__name__)
api = Api(app)

####################################################################################
try: 
    mongo = pymongo.MongoClient(
        host="localhost", 
        port=27017,
        serverSelectionTimeoutMS = 1000)
    db = mongo.test2
    collection = db['users']

    mongo.server_info()  #trigger exception if cannot connect to db

except:
    print("ERROR -  Cannot connect to db")

####################################################################################
# Building a class to define the users details and handle the HTTP requests with the endpoints.

class UsersDetails(Resource):
    # Defining users with unique IDs.
    def get(self):
        try:
            users = list(collection.find())
            for user in users:
                user['_id'] = str(user['_id'])  # Converting ObjectId to string for each created IDs.
            return users, 200                   # Status code 200 represents successful.
        except Exception as ex:
            print(ex)
            return users, 500                   # Status code 500 represents server error.
            

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name is required to register')
        parser.add_argument('email', type=str, required=True, help='Email is required to register')
        parser.add_argument('password', type=str, required=True, help='Password is required for each users')
        args = parser.parse_args()
        
        try:
            user = {
                'name': args['name'],
                'email': args['email'],
                'password': args['password']
            }
            result = collection.insert_one(user)
            return {'message': 'New User is created', 'id': str(result.inserted_id)}, 201  # Indicates that the request has succeeded and has led to the creation of a resource.
        
        except Exception as ex:
            print(ex)
            return Response(response=json.dumps({"messsage":"Sorry cannot find a user"}), status=500, mimetype="application/json")
            
####################################################################################

class UserEntryDetails(Resource):
    # Getting the user details with its unique user_id.
    def get(self, user_id):
        user = collection.find_one({'_id': ObjectId(user_id)})
        try: 
            if user:
                user['_id'] = str(user['_id'])  # Converting ObjectId to string
                return user, 200
            else:
                # A 404 indicates requested API service cannot be found, or that a requested entity cannot be found.
                return Response(response=json.dumps({"messsage":"Sorry user is not found"}), status=404, mimetype="application/json")
                
        except Exception as ex:
            print(ex)
            return Response(response=json.dumps({"messsage":"Sorry given user ID does not exit"}), status=500, mimetype="application/json")

    # This block of code will help to edit the already entered user's details with the new one.
    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Please enter the name')
        parser.add_argument('email', type=str, required=True, help='Please enter an email')
        parser.add_argument('password', type=str, required=True, help='Give the password to access')
        args = parser.parse_args()
        
        user = collection.find_one({'_id': ObjectId(user_id)})
        try:
            if user:                      # Initiating the user details of the updated users.
                updated_user = {
                    'name': args['name'],
                    'email': args['email'],
                    'password': args['password']
                }
                collection.update_one({'_id': ObjectId(user_id)}, {'$set': updated_user})
                return Response(response=json.dumps({"messsage":"User details are updated"}), status=200, mimetype="application/json")
                
            else:
                # A 404 indicates requested API service cannot be found, or that a requested entity cannot be found.
                return Response(response=json.dumps({"messsage":"Sorry a user is not found"}), status=404, mimetype="application/json")
               
            
        except Exception as ex:
            print(ex)
            return Response(response=json.dumps({"messsage":"Sorry cannot update a user"}), status=500, mimetype="application/json")

    # Here defining the delete funtion to initiate deleting the unwanted users.
    def delete(self, user_id):
        user = collection.find_one({'_id': ObjectId(user_id)})
        try:
            if user:
                collection.delete_one({'_id': ObjectId(user_id)})
                return Response(response=json.dumps({"messsage":"Given User is deleted"}), status=200, mimetype="application/json")
            
            else:
                # A 404 indicates requested API service cannot be found, or that a requested entity cannot be found.
                return Response(response=json.dumps({"messsage":"User is not found"}), status=404, mimetype="application/json")
                
            
        except Exception as ex:
            print(ex)
            # Status code 500 represents Internal Server Error.
            return Response(response=json.dumps({"messsage":"Sorry cannot delete a user"}), status=500, mimetype="application/json")


####################################################################################

# This function is used to associate the resource classes with their corresponding URL endpoints.

api.add_resource(UsersDetails, '/users')
api.add_resource(UserEntryDetails, '/users/<string:user_id>')


####################################################################################

# Finally running the Flask Application with port 80.

if __name__ == "__main__":
    app.run(port=80, debug=True)