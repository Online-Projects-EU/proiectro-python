from enum import Enum


class EditSalesTargetStatusType0(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    VOID = "void"

    def __str__(self) -> str:
        return str(self.value)
