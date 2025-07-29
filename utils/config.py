import os 
import sys 
from pathlib import Path 
import logging 
from logging.handlers import RotatingFileHandler

#create a root directory for app_logs to store the logs history 
LOG_DIR = Path(__file__).resolve().parent.parent/ "Logs"

directory = LOG_DIR.mkdir(parents=True,exist_ok=True)
 
LOG_FILE = LOG_DIR/ "app_logs"


project_Root = sys.path.append(str(Path().resolve().parent.parent))
# from dotenv import load_dotenv 

PARENT_DIR = Path(__file__).resolve().parent.parent 
DATA_DIR = PARENT_DIR/ "data"
RAW_DATA_DIR = DATA_DIR/ "raw"
PROCESSED_DATA_DIR = DATA_DIR/ "processed"
TRANSFORMED_DATA_DIR = DATA_DIR/ "transformed"
MODELS_DIR = PARENT_DIR/ "models"


for d in [DATA_DIR,RAW_DATA_DIR,PROCESSED_DATA_DIR,TRANSFORMED_DATA_DIR,MODELS_DIR]:
    d.mkdir(exist_ok=True)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s", "%Y-%m-%d %H-%M-%S")


file_handler = RotatingFileHandler( 
    filename = LOG_FILE, 
    maxBytes = 5*1024*1024, 
    backupCount = 3, 
    encoding = "utf-8"
)
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger = logging.getLogger() 
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


logger.propagate = False