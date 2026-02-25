from enum import Enum


class EditProductProductType(str, Enum):
    BUNDLE = "bundle"
    GOOD = "good"
    SERVICE = "service"

    def __str__(self) -> str:
        return str(self.value)
