from pydantic import BaseModel


class HourlyStat(BaseModel):
    hourLabel: str
    vehiclesPerHour: int
    cycleDuration: int
