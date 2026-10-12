from enum import Enum


class AddProcessStageStageType(str, Enum):
    FINAL = "final"
    INPUT = "input"
    INTERNAL = "internal"
    OUTPUT = "output"

    def __str__(self) -> str:
        return str(self.value)
