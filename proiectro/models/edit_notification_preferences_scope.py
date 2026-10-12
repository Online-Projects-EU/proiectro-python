from enum import Enum


class EditNotificationPreferencesScope(str, Enum):
    TENANT = "tenant"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
