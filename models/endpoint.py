from typing import Optional

from pydantic import BaseModel


class EndpointCreate(BaseModel):
    location: Optional[str] = None


class Endpoint(BaseModel):
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    timestamp: float
