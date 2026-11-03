from enum import Enum


class EditDocumentTemplateKindType0(str, Enum):
    CHAT_MESSAGE = "chat_message"
    DOCUMENT = "document"
    EMAIL = "email"

    def __str__(self) -> str:
        return str(self.value)
