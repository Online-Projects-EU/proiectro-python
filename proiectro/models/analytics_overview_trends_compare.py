from enum import Enum


class AnalyticsOverviewTrendsCompare(str, Enum):
    MOM = "mom"
    NONE = "none"
    POP = "pop"
    YOY = "yoy"

    def __str__(self) -> str:
        return str(self.value)
