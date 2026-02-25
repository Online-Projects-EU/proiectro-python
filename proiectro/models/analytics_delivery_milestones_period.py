from enum import Enum


class AnalyticsDeliveryMilestonesPeriod(str, Enum):
    MTD = "MTD"
    Q1 = "Q1"
    Q2 = "Q2"
    Q3 = "Q3"
    Q4 = "Q4"
    QTD = "QTD"
    R12 = "R12"
    YTD = "YTD"

    def __str__(self) -> str:
        return str(self.value)
