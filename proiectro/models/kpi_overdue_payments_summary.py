from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KPIOverduePaymentsSummary")


@_attrs_define
class KPIOverduePaymentsSummary:
    """
    Attributes:
        currency (str):
        amounts_available (bool):
        uncovered_currencies (str):
        description (str | Unset):  Default: ''.
        count (str | Unset):  Default: '0'.
        total_amount (str | Unset):  Default: '0'.
        oldest_days_overdue (str | Unset):  Default: '0'.
    """

    currency: str
    amounts_available: bool
    uncovered_currencies: str
    description: str | Unset = ""
    count: str | Unset = "0"
    total_amount: str | Unset = "0"
    oldest_days_overdue: str | Unset = "0"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        amounts_available = self.amounts_available

        uncovered_currencies = self.uncovered_currencies

        description = self.description

        count = self.count

        total_amount = self.total_amount

        oldest_days_overdue = self.oldest_days_overdue

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "amountsAvailable": amounts_available,
                "uncoveredCurrencies": uncovered_currencies,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if count is not UNSET:
            field_dict["count"] = count
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if oldest_days_overdue is not UNSET:
            field_dict["oldestDaysOverdue"] = oldest_days_overdue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency")

        amounts_available = d.pop("amountsAvailable")

        uncovered_currencies = d.pop("uncoveredCurrencies")

        description = d.pop("description", UNSET)

        count = d.pop("count", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        oldest_days_overdue = d.pop("oldestDaysOverdue", UNSET)

        kpi_overdue_payments_summary = cls(
            currency=currency,
            amounts_available=amounts_available,
            uncovered_currencies=uncovered_currencies,
            description=description,
            count=count,
            total_amount=total_amount,
            oldest_days_overdue=oldest_days_overdue,
        )

        kpi_overdue_payments_summary.additional_properties = d
        return kpi_overdue_payments_summary

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
