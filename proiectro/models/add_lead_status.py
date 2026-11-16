from enum import Enum


class AddLeadStatus(str, Enum):
    CONTACTED = "contacted"
    DISQUALIFIED = "disqualified"
    DO_NOT_CONTACT = "do_not_contact"
    NEW = "new"
    NURTURING = "nurturing"
    QUALIFIED = "qualified"
    REPLIED = "replied"

    def __str__(self) -> str:
        return str(self.value)
