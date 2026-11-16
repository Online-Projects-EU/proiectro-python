from enum import Enum


class AnalyticsSalesLeadsSplitBy(str, Enum):
    LIST = "list"
    SOURCE = "source"

    def __str__(self) -> str:
        return str(self.value)
