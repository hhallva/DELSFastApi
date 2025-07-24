from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EndpointCreate(BaseModel):
    location: Optional[str] = None


class Endpoint(BaseModel):
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    timestamp: float
