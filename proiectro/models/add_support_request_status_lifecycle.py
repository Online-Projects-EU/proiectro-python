from enum import Enum


class AddSupportRequestStatusLifecycle(str, Enum):
    CLOSED = "CLOSED"
    IN_PROGRESS = "IN_PROGRESS"
    NEW = "NEW"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    PENDING_REQUESTER = "PENDING_REQUESTER"

    def __str__(self) -> str:
        return str(self.value)
