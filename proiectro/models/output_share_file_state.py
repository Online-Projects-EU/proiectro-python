from enum import Enum


class OutputShareFileState(str, Enum):
    CURRENT = "current"
    GONE = "gone"
    REPLACED = "replaced"

    def __str__(self) -> str:
        return str(self.value)
