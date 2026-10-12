from enum import Enum


class OutputShareProposalState(str, Enum):
    ACCEPTED = "accepted"
    CURRENT = "current"
    GONE = "gone"
    LOST = "lost"
    REVISING = "revising"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
