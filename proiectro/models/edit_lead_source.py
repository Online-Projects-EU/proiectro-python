from enum import Enum

class EditLeadSource(str, Enum):
    COLD_EMAIL = "cold_email"
    EVENT = "event"
    IMPORT = "import"
    LINKEDIN = "linkedin"
    OTHER = "other"
    REFERRAL = "referral"
    WEB_FORM = "web_form"

    def __str__(self) -> str:
        return str(self.value)
