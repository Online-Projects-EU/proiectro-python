from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_sales_target_metric import AddSalesTargetMetric
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddSalesTarget")


@_attrs_define
class AddSalesTarget:
    """
    Attributes:
        member (str):
        scheme (str):
        amount (float | str):
        period_start (str):
        period_end (str):
        metric (AddSalesTargetMetric | Unset):  Default: AddSalesTargetMetric.REVENUE.
        currency (None | str | Unset):
        notes (None | str | Unset):  Default: ''.
    """

    member: str
    scheme: str
    amount: float | str
    period_start: str
    period_end: str
    metric: AddSalesTargetMetric | Unset = AddSalesTargetMetric.REVENUE
    currency: None | str | Unset = UNSET
    notes: None | str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member = self.member

        scheme = self.scheme

        amount: float | str
        amount = self.amount

        period_start = self.period_start

        period_end = self.period_end

        metric: str | Unset = UNSET
        if not isinstance(self.metric, Unset):
            metric = self.metric.value

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "member": member,
                "scheme": scheme,
                "amount": amount,
                "period_start": period_start,
                "period_end": period_end,
            }
        )
        if metric is not UNSET:
            field_dict["metric"] = metric
        if currency is not UNSET:
            field_dict["currency"] = currency
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        member = d.pop("member")

        scheme = d.pop("scheme")

        def _parse_amount(data: object) -> float | str:
            return cast(float | str, data)

        amount = _parse_amount(d.pop("amount"))

        period_start = d.pop("period_start")

        period_end = d.pop("period_end")

        _metric = d.pop("metric", UNSET)
        metric: AddSalesTargetMetric | Unset
        if isinstance(_metric, Unset):
            metric = UNSET
        else:
            metric = AddSalesTargetMetric(_metric)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        add_sales_target = cls(
            member=member,
            scheme=scheme,
            amount=amount,
            period_start=period_start,
            period_end=period_end,
            metric=metric,
            currency=currency,
            notes=notes,
        )

        add_sales_target.additional_properties = d
        return add_sales_target

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
