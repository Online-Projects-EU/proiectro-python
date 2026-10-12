from enum import Enum


class OutputShareState(str, Enum):
    DRAFT = "draft"
    EXPIRED = "expired"
    PUBLISHED = "published"
    UNPUBLISHED = "unpublished"

    def __str__(self) -> str:
        return str(self.value)
