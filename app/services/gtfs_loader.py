# app/services/gtfs_loader.py

import json
from pathlib import Path
from typing import Any

from gtfs_kit import read_feed
from app.core.settings import settings
from app.core.log_utils import get_logger

logger = get_logger(__name__)

def load_gtfs_feeds(zip_path: Path) -> dict[str, dict[str, Any]]:
    """
    Loads GTFS feeds based on a feeds.json config file

    Returns a nested dict of {agency: {service: feed}}
    """

    feed_config_path = Path(settings.feeds_config_path)
    if not feed_config_path.exists():
        raise FileNotFoundError(f"Feeds config file not found: {settings.feeds_config_path}")
    
    with feed_config_path.open() as f:
        feeds_config = json.load(f)

    all_feeds: dict[str, dict[str, Any]] = {}

    for agency, services in feeds_config.items():
        logger.info(f"Loading feeds for agency: {agency}")
        all_feeds[agency] = {}

        for service_type, zip_path_str in services.items():
            zip_path = Path(zip_path_str)
            if not zip_path.exists():
                logger.warning(f"Missing GTFS ZIP for {agency} {service_type}: {zip_path}")
                continue

            try: 
                feed = read_feed(str(zip_path), dist_units="km")
                all_feeds[agency][service_type] = feed
                logger.info(f"Loaded {agency} {service_type} from feed {zip_path}")
            except Exception as e:
                logger.exception(f"Error loading {agency} {service_type} from {zip_path}")
    
    return all_feeds
