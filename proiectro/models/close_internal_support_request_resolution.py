from enum import Enum


class CloseInternalSupportRequestResolution(str, Enum):
    CANNOT_REPRODUCE = "CANNOT_REPRODUCE"
    DONE = "DONE"
    DUPLICATE = "DUPLICATE"
    EXPIRED = "EXPIRED"
    FIXED = "FIXED"
    MERGED = "MERGED"
    NOT_AN_ISSUE = "NOT_AN_ISSUE"
    NO_LONGER_REQUIRED = "NO_LONGER_REQUIRED"
    WONT_FIX = "WONT_FIX"

    def __str__(self) -> str:
        return str(self.value)
