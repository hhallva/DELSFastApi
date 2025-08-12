from datetime import date, time

from fastapi import APIRouter, HTTPException
from typing import List

from enums.eventType import EventType
from enums.logType import LogType
from models.device import Device
from enums.deviceType import DeviceType
from models.hourlyStat import HourlyStat
from models.log import Log
from models.phase import Phase
from models.streetStat import StreetStat

router = APIRouter()

devices_db = [
    Device(id="d1", name="ул. Тверская", type=DeviceType.rtc, latitude=55.751244, longitude=37.618423),
    Device(id="d2", name="ул. Охотный Ряд", type=DeviceType.rts, latitude=55.756989, longitude=37.615724),
]

phases_db = {
    "d1": [{"id": i, "active": i % 2 == 0, "duration": i * 10} for i in range(1, 6)],
    "d2": [{"id": i, "active": i % 3 == 0, "duration": i * 15} for i in range(1, 6)]
}

hourly_stats_db = {
    "d1": [
        {"hourLabel": f"{h}:00", "vehiclesPerHour": (h + 1) * 50, "cycleDuration": (h + 3 + 1) * 10}
        for h in range(12)
    ],
    "d2": [
        {"hourLabel": f"{h}:00", "vehiclesPerHour": (h + 2) * 40, "cycleDuration": (h + 4 + 1) * 10}
        for h in range(12)
    ]
}

streets_db = {
    "d1": [
        {"streetName": "ул. Тверская", "cars": 120, "trucks": 15, "buses": 8, "averageSpeed": 55},
        {"streetName": "ул. Моховая", "cars": 95, "trucks": 8, "buses": 12, "averageSpeed": 60},
        {"streetName": "ул. Охотный Ряд", "cars": 95, "trucks": 8, "buses": 12, "averageSpeed": 60}
    ],
    "d2": [
        {"streetName": "ул. Тверская", "cars": 120, "trucks": 15, "buses": 8, "averageSpeed": 55},
        {"streetName": "ул. Моховая", "cars": 95, "trucks": 8, "buses": 12, "averageSpeed": 60},
        {"streetName": "ул. Охотный Ряд", "cars": 95, "trucks": 8, "buses": 12, "averageSpeed": 60}
    ]
}

logs_db = {
    "d1": [
        {
            "date": date(2023, 5, 10),
            "time": time(14, 30),
            "type": LogType.alert,
            "eventType": EventType.no_connection},
        {
            "date": date(2023, 5, 10),
            "time": time(14, 45),
            "type": LogType.notification,
            "eventType": EventType.connection_restored
        }
    ],
    "d2": [
        {
            "date": date(2023, 5, 11),
            "time": time(9, 15),
            "type": LogType.alert,
            "eventType": EventType.no_connection}
    ]
}


@router.get("/", response_model=List[Device], status_code=200)
async def get_devices():
    if devices_db is None:
        raise HTTPException(
            status_code=404,
            detail="Devices not found"
        )
    return devices_db


@router.get("/{device_id}/currentstate", response_model=List[Phase])
async def get_current_state(device_id: str):
    return phases_db.get(device_id, [])


@router.get("/{device_id}/statistic/hourly", response_model=List[HourlyStat])
async def get_hourly_stats(device_id: str):
    return hourly_stats_db.get(device_id, [])


@router.get("/{device_id}/statistic/streets", response_model=List[StreetStat])
async def get_street_stats(device_id: str):
    stats = streets_db.get(device_id, [])
    return [StreetStat.calculate_amount(StreetStat(**s)) for s in stats]


@router.get("/{device_id}/log", response_model=List[Log])
async def get_device_logs(device_id: str):
    return logs_db.get(device_id, [])
