from flask import Flask, jsonify, request
from flask_restful import Api
from models import db
import config
from userController import UserController, UserByIdController

# create an instance of flask
app = Flask(__name__)
# create database
app.config.from_object(config)

# Initialize the Flask-SQLAlchemy object.
db.init_app(app)

# Create the Flask-RESTful API manager, for url routing
api = Api(app)


#Create the endpoins
api.add_resource(UserController, '/users')  # For creating a user
api.add_resource(UserByIdController, '/users/<int:id>')  # For getting/deleting a user by ID

# main function
if __name__ == "__main__":
    # Create the database tables.
    with app.app_context():
        db.create_all()
    # Start the Flask development web server.
    app.run(debug=True)
    
