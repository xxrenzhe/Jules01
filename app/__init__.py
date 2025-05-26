# This script initializes the Flask application.
# It creates the Flask app instance and imports the routes.

from flask import Flask

# Create the Flask app instance
app = Flask(__name__)

# Import routes after the app instance is created to avoid circular imports
from app import routes
