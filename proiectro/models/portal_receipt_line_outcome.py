from enum import Enum


class PortalReceiptLineOutcome(str, Enum):
    DAMAGED = "damaged"
    NOT_RECEIVED = "not_received"
    RECEIVED = "received"

    def __str__(self) -> str:
        return str(self.value)
