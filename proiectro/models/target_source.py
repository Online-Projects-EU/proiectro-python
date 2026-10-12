from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetSource")


@_attrs_define
class TargetSource:
    """One target row behind an attainment entry, as the admin typed it, with its monthly rate.

    Attributes:
        amount (float | str):
        period_start (datetime.date):
        period_end (datetime.date):
        per_month (float | str):
        currency (None | str | Unset):
    """

    amount: float | str
    period_start: datetime.date
    period_end: datetime.date
    per_month: float | str
    currency: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount: float | str
        amount = self.amount

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        per_month: float | str
        per_month = self.per_month

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "period_start": period_start,
                "period_end": period_end,
                "per_month": per_month,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_amount(data: object) -> float | str:
            return cast(float | str, data)

        amount = _parse_amount(d.pop("amount"))

        period_start = isoparse(d.pop("period_start")).date()

        period_end = isoparse(d.pop("period_end")).date()

        def _parse_per_month(data: object) -> float | str:
            return cast(float | str, data)

        per_month = _parse_per_month(d.pop("per_month"))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        target_source = cls(
            amount=amount,
            period_start=period_start,
            period_end=period_end,
            per_month=per_month,
            currency=currency,
        )

        target_source.additional_properties = d
        return target_source

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
