import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m-%d-%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
#logs_path is the path where the log file will be stored

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s %(levelname)s %(message)s',
    level=logging.INFO, # Set the logging level to INFO
    
)