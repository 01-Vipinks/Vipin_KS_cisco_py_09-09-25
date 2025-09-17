"""
Logger setup module for Banking Management System.

Configures a structured JSON logger with console and file output handlers.
"""

import logging
import sys
from pythonjsonlogger import jsonlogger

# Create logger
logger = logging.getLogger("banking_system_logger")
logger.setLevel(logging.WARNING)  # Raised level to WARNING to suppress INFO logs

# Setup console handler
console_handler = logging.StreamHandler(sys.stdout)
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Setup file handler
file_handler = logging.FileHandler('banking_system_logs.json')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Test run
if __name__ == "__main__":
    logger.warning("Logger initialized with level WARNING")
    logger.info("This info log will not appear on console")
