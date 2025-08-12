from pydantic import BaseModel

from datetime import date, time

from enums.eventType import EventType
from enums.logType import LogType


class Log(BaseModel):
    date: date
    time: time
    type: LogType
    eventType: EventType
