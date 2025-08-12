from pydantic import BaseModel

from enums.deviceType import DeviceType


class Device(BaseModel):
    id: str
    name: str
    type: DeviceType
    latitude: float
    longitude: float

