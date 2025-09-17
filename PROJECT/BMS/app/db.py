"""
Database setup module for the Banking Management System.

Creates the shared SQLAlchemy database instance for ORM mapping
and session management that is used throughout the application.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
