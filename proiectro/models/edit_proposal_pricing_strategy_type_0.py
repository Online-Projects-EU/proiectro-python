from enum import Enum


class EditProposalPricingStrategyType0(str, Enum):
    FIXED_AMOUNT = "fixed_amount"
    MARGIN_TARGET = "margin_target"
    PERCENTAGE = "percentage"
    PRODUCT_PRICES = "product_prices"

    def __str__(self) -> str:
        return str(self.value)
