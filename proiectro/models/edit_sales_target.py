from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_sales_target_metric_type_0 import EditSalesTargetMetricType0
from ..models.edit_sales_target_status_type_0 import EditSalesTargetStatusType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditSalesTarget")


@_attrs_define
class EditSalesTarget:
    """
    Attributes:
        member (None | str | Unset):
        scheme (None | str | Unset):
        metric (EditSalesTargetMetricType0 | None | Unset):
        amount (float | None | str | Unset):
        currency (None | str | Unset):
        period_start (None | str | Unset):
        period_end (None | str | Unset):
        status (EditSalesTargetStatusType0 | None | Unset):
        notes (None | str | Unset):
    """

    member: None | str | Unset = UNSET
    scheme: None | str | Unset = UNSET
    metric: EditSalesTargetMetricType0 | None | Unset = UNSET
    amount: float | None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    period_start: None | str | Unset = UNSET
    period_end: None | str | Unset = UNSET
    status: EditSalesTargetStatusType0 | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member: None | str | Unset
        if isinstance(self.member, Unset):
            member = UNSET
        else:
            member = self.member

        scheme: None | str | Unset
        if isinstance(self.scheme, Unset):
            scheme = UNSET
        else:
            scheme = self.scheme

        metric: None | str | Unset
        if isinstance(self.metric, Unset):
            metric = UNSET
        elif isinstance(self.metric, EditSalesTargetMetricType0):
            metric = self.metric.value
        else:
            metric = self.metric

        amount: float | None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        period_start: None | str | Unset
        if isinstance(self.period_start, Unset):
            period_start = UNSET
        else:
            period_start = self.period_start

        period_end: None | str | Unset
        if isinstance(self.period_end, Unset):
            period_end = UNSET
        else:
            period_end = self.period_end

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, EditSalesTargetStatusType0):
            status = self.status.value
        else:
            status = self.status

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if member is not UNSET:
            field_dict["member"] = member
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if metric is not UNSET:
            field_dict["metric"] = metric
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if period_start is not UNSET:
            field_dict["period_start"] = period_start
        if period_end is not UNSET:
            field_dict["period_end"] = period_end
        if status is not UNSET:
            field_dict["status"] = status
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_member(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member = _parse_member(d.pop("member", UNSET))

        def _parse_scheme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheme = _parse_scheme(d.pop("scheme", UNSET))

        def _parse_metric(data: object) -> EditSalesTargetMetricType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metric_type_0 = EditSalesTargetMetricType0(data)

                return metric_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditSalesTargetMetricType0 | None | Unset, data)

        metric = _parse_metric(d.pop("metric", UNSET))

        def _parse_amount(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))

        def _parse_period_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period_start = _parse_period_start(d.pop("period_start", UNSET))

        def _parse_period_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period_end = _parse_period_end(d.pop("period_end", UNSET))

        def _parse_status(data: object) -> EditSalesTargetStatusType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = EditSalesTargetStatusType0(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditSalesTargetStatusType0 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        edit_sales_target = cls(
            member=member,
            scheme=scheme,
            metric=metric,
            amount=amount,
            currency=currency,
            period_start=period_start,
            period_end=period_end,
            status=status,
            notes=notes,
        )

        edit_sales_target.additional_properties = d
        return edit_sales_target

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
