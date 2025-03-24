import logging
from dotenv import load_dotenv
import os

load_dotenv()

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))

    return logger
