# Import the Flask class from the Flask module
from flask import Flask

# Import the 'api' object from the 'extensions' module
from .extensions import api

# Import the 'ns' object from the 'resources' module
from .resources import ns

# Define a function called 'create_app' to create the Flask application
def create_app():
    # Create an instance of the Flask class and assign it to the 'app' variable
    app = Flask(__name__)

    # Initialize the 'api' object with the Flask application
    api.init_app(app)

    # Add the 'ns' namespace to the 'api' object
    api.add_namespace(ns)

    # Return the configured Flask application
    return app
