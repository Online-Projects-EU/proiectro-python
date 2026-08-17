from enum import Enum

class EditCustomFormDataClassification(str, Enum):
    CONFIDENTIAL = "confidential"
    INTERNAL = "internal"
    PERSONAL_DATA = "personal_data"

    def __str__(self) -> str:
        return str(self.value)
