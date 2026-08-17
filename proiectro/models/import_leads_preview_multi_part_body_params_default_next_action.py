from enum import Enum

class ImportLeadsPreviewMultiPartBodyParamsDefaultNextAction(str, Enum):
    PLUS_30D = "plus_30d"
    PLUS_3D = "plus_3d"
    PLUS_7D = "plus_7d"
    PLUS_90D = "plus_90d"
    TODAY = "today"
    TOMORROW = "tomorrow"
    TRIAGE_LATER = "triage_later"

    def __str__(self) -> str:
        return str(self.value)
