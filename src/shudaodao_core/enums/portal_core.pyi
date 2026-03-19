from enum import Enum

class StringEnum(str, Enum): ...

class DataBaseEnum(StringEnum):
    Config = "Config"
    Auth = "Auth"
    Acm = "Portal"
    Meta = "Portal"

class StorageTypeEnum(Enum):
    Business = 10
    Personal = 20
