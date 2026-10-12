from enum import Enum


class UpdateLeadStatusStatus(str, Enum):
    CONTACTED = "contacted"
    NEW = "new"
    NURTURING = "nurturing"
    QUALIFIED = "qualified"
    REPLIED = "replied"

    def __str__(self) -> str:
        return str(self.value)
