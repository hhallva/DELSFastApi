from pydantic import BaseModel


class LocationCreate(BaseModel):
    location: str


class Location(BaseModel):
    latitude: float
    longitude: float
    timestamp: float
