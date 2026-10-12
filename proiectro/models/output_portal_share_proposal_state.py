from enum import Enum


class OutputPortalShareProposalState(str, Enum):
    ACCEPTED = "accepted"
    CURRENT = "current"
    LOST = "lost"
    REVISING = "revising"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
