from enum import Enum


class OutputLeadHistoryEntryKind(str, Enum):
    ACTIVITY = "activity"
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
