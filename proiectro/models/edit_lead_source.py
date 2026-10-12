from enum import Enum


class EditLeadSource(str, Enum):
    COLD_CALL = "cold_call"
    COLD_EMAIL = "cold_email"
    EMAIL_CAMPAIGN = "email_campaign"
    EVENT = "event"
    EXISTING_CUSTOMER = "existing_customer"
    IMPORT = "import"
    INBOUND_CALL = "inbound_call"
    INBOUND_EMAIL = "inbound_email"
    LINKEDIN = "linkedin"
    ORGANIC_SEARCH = "organic_search"
    OTHER = "other"
    PAID_ADS = "paid_ads"
    PARTNER = "partner"
    REFERRAL = "referral"
    SOCIAL_MEDIA = "social_media"
    WEB_FORM = "web_form"

    def __str__(self) -> str:
        return str(self.value)
