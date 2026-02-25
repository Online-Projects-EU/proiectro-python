from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlockPaymentsSummary")


@_attrs_define
class BlockPaymentsSummary:
    """
    Attributes:
        total_amount (float | str):
        paid_amount (float | str):
        unpaid_amount (float | str):
        currency_symbol (str):
        payment_count (int):
        paid_count (int):
        unpaid_count (int):
        next_due_date (None | str | Unset):
    """

    total_amount: float | str
    paid_amount: float | str
    unpaid_amount: float | str
    currency_symbol: str
    payment_count: int
    paid_count: int
    unpaid_count: int
    next_due_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_amount: float | str
        total_amount = self.total_amount

        paid_amount: float | str
        paid_amount = self.paid_amount

        unpaid_amount: float | str
        unpaid_amount = self.unpaid_amount

        currency_symbol = self.currency_symbol

        payment_count = self.payment_count

        paid_count = self.paid_count

        unpaid_count = self.unpaid_count

        next_due_date: None | str | Unset
        if isinstance(self.next_due_date, Unset):
            next_due_date = UNSET
        else:
            next_due_date = self.next_due_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_amount": total_amount,
                "paid_amount": paid_amount,
                "unpaid_amount": unpaid_amount,
                "currency_symbol": currency_symbol,
                "payment_count": payment_count,
                "paid_count": paid_count,
                "unpaid_count": unpaid_count,
            }
        )
        if next_due_date is not UNSET:
            field_dict["next_due_date"] = next_due_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_total_amount(data: object) -> float | str:
            return cast(float | str, data)

        total_amount = _parse_total_amount(d.pop("total_amount"))

        def _parse_paid_amount(data: object) -> float | str:
            return cast(float | str, data)

        paid_amount = _parse_paid_amount(d.pop("paid_amount"))

        def _parse_unpaid_amount(data: object) -> float | str:
            return cast(float | str, data)

        unpaid_amount = _parse_unpaid_amount(d.pop("unpaid_amount"))

        currency_symbol = d.pop("currency_symbol")

        payment_count = d.pop("payment_count")

        paid_count = d.pop("paid_count")

        unpaid_count = d.pop("unpaid_count")

        def _parse_next_due_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_due_date = _parse_next_due_date(d.pop("next_due_date", UNSET))

        block_payments_summary = cls(
            total_amount=total_amount,
            paid_amount=paid_amount,
            unpaid_amount=unpaid_amount,
            currency_symbol=currency_symbol,
            payment_count=payment_count,
            paid_count=paid_count,
            unpaid_count=unpaid_count,
            next_due_date=next_due_date,
        )

        block_payments_summary.additional_properties = d
        return block_payments_summary

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
