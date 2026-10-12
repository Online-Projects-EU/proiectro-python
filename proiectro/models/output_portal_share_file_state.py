from enum import Enum


class OutputPortalShareFileState(str, Enum):
    CURRENT = "current"
    REPLACED = "replaced"

    def __str__(self) -> str:
        return str(self.value)
