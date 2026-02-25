from enum import Enum


class EditProductPricingType(str, Enum):
    FIXED_PRICE = "fixed_price"
    HOURLY_RATE = "hourly_rate"
    PER_UNIT = "per_unit"
    SUBSCRIPTION_PER_MONTH = "subscription_per_month"
    SUBSCRIPTION_PER_YEAR = "subscription_per_year"
    TIME_AND_MATERIALS = "time_and_materials"

    def __str__(self) -> str:
        return str(self.value)
