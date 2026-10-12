from enum import Enum


class OutputProjectWorkItemDetailTimelineSource(str, Enum):
    CPM = "cpm"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
