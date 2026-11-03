from enum import Enum


class OutputCsvImportRowAction(str, Enum):
    CREATE = "create"
    ERROR = "error"
    UNCHANGED = "unchanged"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
