from enum import Enum


class AddProcessParticipationParticipationType(str, Enum):
    OBSERVER = "observer"
    REVIEWER = "reviewer"
    SUBMITTER = "submitter"
    SUPERVISOR = "supervisor"
    WORKER = "worker"

    def __str__(self) -> str:
        return str(self.value)
