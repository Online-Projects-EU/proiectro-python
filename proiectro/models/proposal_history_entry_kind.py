from enum import Enum


class ProposalHistoryEntryKind(str, Enum):
    LIFECYCLE = "lifecycle"
    STAGE = "stage"

    def __str__(self) -> str:
        return str(self.value)
