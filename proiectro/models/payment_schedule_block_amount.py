from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PaymentScheduleBlockAmount")


@_attrs_define
class PaymentScheduleBlockAmount:
    """One currency's share of a block. A payment keeps the currency it was created in, so a block whose
    proposal changed currency can hold two, and they are never added together.

        Attributes:
            currency (str):
            symbol (str):
            total (float | str):
            paid (float | str):
    """

    currency: str
    symbol: str
    total: float | str
    paid: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        symbol = self.symbol

        total: float | str
        total = self.total

        paid: float | str
        paid = self.paid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "symbol": symbol,
                "total": total,
                "paid": paid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency")

        symbol = d.pop("symbol")

        def _parse_total(data: object) -> float | str:
            return cast(float | str, data)

        total = _parse_total(d.pop("total"))

        def _parse_paid(data: object) -> float | str:
            return cast(float | str, data)

        paid = _parse_paid(d.pop("paid"))

        payment_schedule_block_amount = cls(
            currency=currency,
            symbol=symbol,
            total=total,
            paid=paid,
        )

        payment_schedule_block_amount.additional_properties = d
        return payment_schedule_block_amount

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
