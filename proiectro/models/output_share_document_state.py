from enum import Enum


class OutputShareDocumentState(str, Enum):
    CHANGED = "changed"
    CURRENT = "current"
    GONE = "gone"

    def __str__(self) -> str:
        return str(self.value)
