# This script serves as the main entry point to run the Flask application.
from app import app  # Import the Flask app instance

if __name__ == '__main__':
    # Run the Flask development server
    # debug=True enables auto-reloading and the Flask debugger
    app.run(debug=True)
