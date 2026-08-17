from enum import Enum

class EditTenantLeadVisibilityType0(str, Enum):
    OPEN = "open"
    OWN_AND_LISTS = "own_and_lists"
    OWN_AND_POOL = "own_and_pool"

    def __str__(self) -> str:
        return str(self.value)
