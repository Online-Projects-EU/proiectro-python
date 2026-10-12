from enum import Enum


class OutputShareFileEntityType(str, Enum):
    ORG = "org"
    PROPOSAL = "proposal"

    def __str__(self) -> str:
        return str(self.value)
