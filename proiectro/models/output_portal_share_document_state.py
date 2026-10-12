from enum import Enum


class OutputPortalShareDocumentState(str, Enum):
    CHANGED = "changed"
    CURRENT = "current"

    def __str__(self) -> str:
        return str(self.value)
