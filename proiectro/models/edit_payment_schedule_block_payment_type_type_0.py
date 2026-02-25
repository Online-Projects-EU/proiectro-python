from enum import Enum


class EditPaymentScheduleBlockPaymentTypeType0(str, Enum):
    MILESTONE_PAYMENT = "milestone_payment"
    PROGRESS_PAYMENT = "progress_payment"
    UPFRONT_PAYMENT = "upfront_payment"
    UPON_COMPLETION = "upon_completion"

    def __str__(self) -> str:
        return str(self.value)
