from enum import Enum


class EditBeliefSplitByType0(str, Enum):
    FUNNEL = "funnel"
    LIST = "list"
    OWNER = "owner"
    SOURCE = "source"

    def __str__(self) -> str:
        return str(self.value)
