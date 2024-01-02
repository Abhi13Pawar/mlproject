import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_directory = "logs"  # Name of the directory where logs will be stored

# Get the absolute path to the logs directory
logs_path = os.path.abspath(logs_directory)

try:
    # Create the logs directory if it doesn't exist
    os.makedirs(logs_path, exist_ok=True)
except OSError as e:
    print(f"Error creating logs directory: {e}")
    raise

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


