# app/core/logger.py

import logging
from app.core.settings import settings

logging.basicConfig(
    level=getattr(logging, settings.log_level),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

def get_logger(name: str) -> logging.Logger :
    return logging.getLogger(f"transit-api:{name}")