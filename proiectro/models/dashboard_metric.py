from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardMetric")


@_attrs_define
class DashboardMetric:
    """Individual metric for display with comparison data

    Attributes:
        label (str):
        value (float | str):
        trend (str):
        currency (str):
        change_percent (float | None | str | Unset):
        current_period (None | str | Unset):
        comparison_period (None | str | Unset):
    """

    label: str
    value: float | str
    trend: str
    currency: str
    change_percent: float | None | str | Unset = UNSET
    current_period: None | str | Unset = UNSET
    comparison_period: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        value: float | str
        value = self.value

        trend = self.trend

        currency = self.currency

        change_percent: float | None | str | Unset
        if isinstance(self.change_percent, Unset):
            change_percent = UNSET
        else:
            change_percent = self.change_percent

        current_period: None | str | Unset
        if isinstance(self.current_period, Unset):
            current_period = UNSET
        else:
            current_period = self.current_period

        comparison_period: None | str | Unset
        if isinstance(self.comparison_period, Unset):
            comparison_period = UNSET
        else:
            comparison_period = self.comparison_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "value": value,
                "trend": trend,
                "currency": currency,
            }
        )
        if change_percent is not UNSET:
            field_dict["change_percent"] = change_percent
        if current_period is not UNSET:
            field_dict["current_period"] = current_period
        if comparison_period is not UNSET:
            field_dict["comparison_period"] = comparison_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        def _parse_value(data: object) -> float | str:
            return cast(float | str, data)

        value = _parse_value(d.pop("value"))

        trend = d.pop("trend")

        currency = d.pop("currency")

        def _parse_change_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        change_percent = _parse_change_percent(d.pop("change_percent", UNSET))

        def _parse_current_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_period = _parse_current_period(d.pop("current_period", UNSET))

        def _parse_comparison_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comparison_period = _parse_comparison_period(d.pop("comparison_period", UNSET))

        dashboard_metric = cls(
            label=label,
            value=value,
            trend=trend,
            currency=currency,
            change_percent=change_percent,
            current_period=current_period,
            comparison_period=comparison_period,
        )

        dashboard_metric.additional_properties = d
        return dashboard_metric

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
