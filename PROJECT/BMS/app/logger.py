import logging
import sys
from pythonjsonlogger import jsonlogger

# Create logger
logger = logging.getLogger("banking_system_logger")
logger.setLevel(logging.INFO)

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
    logger.info("Logger initialized successfully")
    logger.info("Test log entry", extra={"module": "test", "status": "success"})
