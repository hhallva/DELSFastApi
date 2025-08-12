from enum import Enum


class EventType(str, Enum):
    no_connection = "нет связи"
    connection_restored = "связь восстановлена"
