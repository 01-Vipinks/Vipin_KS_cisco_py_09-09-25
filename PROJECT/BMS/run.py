"""
Run module for the Banking Management System.

Starts the Flask application server.
"""

from app.routes import application

if __name__ == "__main__":
    application.run(debug=True)
