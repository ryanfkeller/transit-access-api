# app/main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from pathlib import Path

from app.core.settings import settings
from app.core.log_utils import get_logger
from app.routes import router as api_router
from app.services.gtfs_loader import load_gtfs_feeds

logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up app and loading GTFS feeds...")

    try: 
        gtfs_feeds = load_gtfs_feeds(settings.feeds_config_path)
        app.state.gtfs_feeds = gtfs_feeds
        logger.info(f"Loaded {len(gtfs_feeds)} GTFS feeds.")
    except Exception as e:
        logger.exception("Failed to load GTFS feeds during startup.")
        raise e
    
    yield

    logger.info("Shutting down app...")


app = FastAPI(
    title= "Transit Access API",
    description= "Estimate public transit accessibility scores from addresses.",
    version= "0.1.0",
    lifespan=lifespan
)

# Include routes from router
app.include_router(api_router)


