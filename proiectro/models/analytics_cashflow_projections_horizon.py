from enum import Enum


class AnalyticsCashflowProjectionsHorizon(str, Enum):
    VALUE_0 = "3m"
    VALUE_1 = "6m"
    VALUE_2 = "12m"
    VALUE_3 = "24m"

    def __str__(self) -> str:
        return str(self.value)
