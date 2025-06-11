# app/main.py

from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes.api import router as api_router

load_dotenv()

app = FastAPI(
    title= "Transit Access API",
    description= "Estimate public transit accessibility scores from addresses.",
    version= "0.1.0"
)

# Include routes from router
app.include_router(api_router)


