from enum import Enum


class AddFormFieldFieldType(str, Enum):
    BOOLEAN = "boolean"
    COORDINATES = "coordinates"
    COUNTRY = "country"
    DATE = "date"
    DATETIME = "datetime"
    DECIMAL = "decimal"
    EMAIL = "email"
    INTEGER = "integer"
    MULTISELECT = "multiselect"
    PHONE = "phone"
    RADIO = "radio"
    SCALE = "scale"
    SELECT = "select"
    TEXT = "text"
    TEXTAREA = "textarea"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
