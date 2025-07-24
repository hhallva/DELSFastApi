from fastapi import APIRouter, HTTPException
from datetime import datetime
from models.endpoint import EndpointCreate, Endpoint

router = APIRouter()

# Храним последнюю конечную точку
endpoint_db = None


@router.post("/", response_model=Endpoint, status_code=201)
async def update_endpoint(endpoint_data: EndpointCreate):
    global endpoint_db

    # Обработка null значения
    if endpoint_data.location is None:
        latitude = longitude = None
    else:
        try:
            lat_str, lon_str = endpoint_data.location.strip().split()
            latitude = round(float(lat_str), 6)
            longitude = round(float(lon_str), 6)
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid location format. Expected 'latitude longitude' or null"
            )

    # Обновляем конечную точку
    endpoint_db = Endpoint(
        latitude=latitude,
        longitude=longitude,
        timestamp=datetime.now().timestamp()
    )

    return endpoint_db


@router.get("/", response_model=Endpoint)
async def get_endpoint():
    if endpoint_db is None:
        raise HTTPException(
            status_code=404,
            detail="Endpoint not set yet"
        )
    return endpoint_db
