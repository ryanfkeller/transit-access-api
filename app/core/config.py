# app/core/config.py

import os

def get_required_env(var_name: str) -> str:
    value = os.getenv(var_name)
    if value is None :
        raise RuntimeError(f"Missing required environment variable: {var_name}")
    return value