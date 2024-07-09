from flask_restful import Resource
from flask import request
from models import User,db
from userService import userService

def responseMessage (message, data):
    return {"message": message, "data": data }


class UserController(Resource):
    def get(self):
        return responseMessage("Success", userService.getAll())
    
    def post(self):
        
        # Get the JSON data from the request.
        requestData = request.get_json()

        if not request:
            return {'message': "No data provided" }, 400

        newUser = User(
                firstname=requestData.get('firstname'),
                lastname=requestData.get('lastname'),
                gender=requestData.get('gender'),
                age=requestData.get('age')
            )
        
        serverResponse = userService.post(newUser)

        print(serverResponse)
        if serverResponse is None:
            return responseMessage("The user was not created", {}), 400
        
        return responseMessage("User successfully created", serverResponse)

class UserByIdController(Resource):   
    def delete(self, id):
        serverResponse = userService.delete(id)
        return responseMessage("User successfully deleted", serverResponse) if serverResponse else responseMessage("The user was not deleted", {}), 400
    
    def get(self, id):
        response = userService.getById(id)
        if response is None:
            return responseMessage("User not found", {}), 400

        return response

