"""
Configuration settings for the Banking Management System project.

Contains constants like database URL, SMTP server info,
default batch sizes, and JSON logging flag.
"""

# Removed unused `import os`

config = {
    'DB_URL': 'sqlite:///Banking_app_db.db',
    'SMTP_SERVER': 'smtp.gmail.com',
    'SMTP_PORT': 587,
    'DEFAULT_BATCH_SIZE': 10,
    'LOG_JSON': True
}
