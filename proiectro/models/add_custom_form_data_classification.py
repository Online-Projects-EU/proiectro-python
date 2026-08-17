from enum import Enum

class AddCustomFormDataClassification(str, Enum):
    CONFIDENTIAL = "confidential"
    INTERNAL = "internal"
    PERSONAL_DATA = "personal_data"

    def __str__(self) -> str:
        return str(self.value)
