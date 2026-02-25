from enum import Enum


class AddLabelLabelType(str, Enum):
    DATE = "date"
    DECIMAL = "decimal"
    INTEGER = "integer"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
