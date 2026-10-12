from enum import Enum


class EditLeadStatus(str, Enum):
    CONTACTED = "contacted"
    CONVERTED = "converted"
    DISQUALIFIED = "disqualified"
    DO_NOT_CONTACT = "do_not_contact"
    NEW = "new"
    NURTURING = "nurturing"
    QUALIFIED = "qualified"
    REPLIED = "replied"

    def __str__(self) -> str:
        return str(self.value)
