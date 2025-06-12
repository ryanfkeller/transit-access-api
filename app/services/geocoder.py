# app/services/geocoder.py

import os
import httpx
from typing import Optional
from app import __version__
from app.core.config import get_required_env
from app.core.logging import logger

def geocode_address(address: str) -> Optional[tuple[float, float]]:
    base_url = get_required_env("OSM_API_BASE")
    contact_email = get_required_env("CONTACT_EMAIL")
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }

    headers = {"User-Agent": f"transit-access-api/{__version__} ({contact_email})"}

    try:
        response = httpx.get(f"{base_url}/search", params=params, headers=headers)
        response.raise_for_status()
    except httpx.HTTPError as e:
        logger.error(f"Geocoding HTTP error: {e}")
        return None
    
    if response.status_code != 200:
        return None
    
    results = response.json()
    if not results:
        return None
    
    lat = float(results[0]["lat"])
    lon = float(results[0]["lon"])
    return lat, lon