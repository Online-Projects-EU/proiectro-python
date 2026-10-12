from enum import Enum


class OutputProjectWorkItemDetailSchedulingBehaviour(str, Enum):
    EVENT = "event"
    EXECUTION = "execution"
    SUMMARY = "summary"

    def __str__(self) -> str:
        return str(self.value)
