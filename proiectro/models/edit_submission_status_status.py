from enum import Enum


class EditSubmissionStatusStatus(str, Enum):
    ARCHIVED = "archived"
    NEW = "new"
    REVIEWED = "reviewed"

    def __str__(self) -> str:
        return str(self.value)
