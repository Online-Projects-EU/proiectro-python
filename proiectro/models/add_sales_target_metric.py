from enum import Enum


class AddSalesTargetMetric(str, Enum):
    DEALS_WON = "deals_won"
    REVENUE = "revenue"

    def __str__(self) -> str:
        return str(self.value)
