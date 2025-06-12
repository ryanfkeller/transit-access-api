# app/core/logging.py

import logging
from app.core.config import get_required_env

level = get_required_env("LOG_LEVEL").upper()

logging.basicConfig(
    level=getattr(logging, level),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("transit-api")
