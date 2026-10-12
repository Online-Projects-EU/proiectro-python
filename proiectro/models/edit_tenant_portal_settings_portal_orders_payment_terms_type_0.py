from enum import Enum


class EditTenantPortalSettingsPortalOrdersPaymentTermsType0(str, Enum):
    NONE = "none"
    ON_ACCEPT = "on_accept"
    ON_DELIVERY = "on_delivery"

    def __str__(self) -> str:
        return str(self.value)
