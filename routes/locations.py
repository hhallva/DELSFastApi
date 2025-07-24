from fastapi import APIRouter, HTTPException
from datetime import datetime
from models.location import LocationCreate, Location

router = APIRouter()

# Храним последнее местоположение
location_db = None


@router.post("/", response_model=Location, status_code=201)
async def update_location(location_data: LocationCreate):
    global location_db

    # Проверка и парсинг данных
    try:
        lat_str, lon_str = location_data.location.strip().split()
        latitude = round(float(lat_str), 6)
        longitude = round(float(lon_str), 6)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid location format. Expected 'latitude longitude'"
        )

    # Обновляем текущее местоположение
    location_db = Location(
        latitude=latitude,
        longitude=longitude,
        timestamp=datetime.now().timestamp()
    )

    return location_db


@router.get("/", response_model=Location)
async def get_location():
    if location_db is None:
        raise HTTPException(
            status_code=404,
            detail="Location not set yet"
        )
    return location_db
