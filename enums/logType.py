from enum import Enum


class LogType(str, Enum):
    alert = "внимание"
    notification = "уведомление"