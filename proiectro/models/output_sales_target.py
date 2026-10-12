from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputSalesTarget")


@_attrs_define
class OutputSalesTarget:
    """
    Attributes:
        id (str):
        member (str):
        member_name (str):
        scheme (str):
        scheme_name (str):
        metric (str):
        metric_label (str):
        amount (float | str):
        period_start (datetime.date):
        period_end (datetime.date):
        status (str):
        notes (str):
        currency (None | str | Unset):
        months (float | None | str | Unset):
        per_month (float | None | str | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    id: str
    member: str
    member_name: str
    scheme: str
    scheme_name: str
    metric: str
    metric_label: str
    amount: float | str
    period_start: datetime.date
    period_end: datetime.date
    status: str
    notes: str
    currency: None | str | Unset = UNSET
    months: float | None | str | Unset = UNSET
    per_month: float | None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member = self.member

        member_name = self.member_name

        scheme = self.scheme

        scheme_name = self.scheme_name

        metric = self.metric

        metric_label = self.metric_label

        amount: float | str
        amount = self.amount

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        status = self.status

        notes = self.notes

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        months: float | None | str | Unset
        if isinstance(self.months, Unset):
            months = UNSET
        else:
            months = self.months

        per_month: float | None | str | Unset
        if isinstance(self.per_month, Unset):
            per_month = UNSET
        else:
            per_month = self.per_month

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "member": member,
                "member_name": member_name,
                "scheme": scheme,
                "scheme_name": scheme_name,
                "metric": metric,
                "metric_label": metric_label,
                "amount": amount,
                "period_start": period_start,
                "period_end": period_end,
                "status": status,
                "notes": notes,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if months is not UNSET:
            field_dict["months"] = months
        if per_month is not UNSET:
            field_dict["per_month"] = per_month
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        member = d.pop("member")

        member_name = d.pop("member_name")

        scheme = d.pop("scheme")

        scheme_name = d.pop("scheme_name")

        metric = d.pop("metric")

        metric_label = d.pop("metric_label")

        def _parse_amount(data: object) -> float | str:
            return cast(float | str, data)

        amount = _parse_amount(d.pop("amount"))

        period_start = isoparse(d.pop("period_start")).date()

        period_end = isoparse(d.pop("period_end")).date()

        status = d.pop("status")

        notes = d.pop("notes")

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_months(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        months = _parse_months(d.pop("months", UNSET))

        def _parse_per_month(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        per_month = _parse_per_month(d.pop("per_month", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        output_sales_target = cls(
            id=id,
            member=member,
            member_name=member_name,
            scheme=scheme,
            scheme_name=scheme_name,
            metric=metric,
            metric_label=metric_label,
            amount=amount,
            period_start=period_start,
            period_end=period_end,
            status=status,
            notes=notes,
            currency=currency,
            months=months,
            per_month=per_month,
            updated_at=updated_at,
        )

        output_sales_target.additional_properties = d
        return output_sales_target

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
