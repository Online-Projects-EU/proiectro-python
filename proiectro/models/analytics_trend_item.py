from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsTrendItem")


@_attrs_define
class AnalyticsTrendItem:
    """Single trend indicator.

    `unit` is the dimension the figure is in -- a currency code, `%`, `deals`, `tickets` -- so a
    consumer formats it without guessing. The template used to decide by matching words in the
    translated `name`.

        Attributes:
            name (str):
            trend (str):
            unit (str | Unset):  Default: ''.
            current_value (float | None | str | Unset):
            previous_value (float | None | str | Unset):
            change_percent (float | None | str | Unset):
    """

    name: str
    trend: str
    unit: str | Unset = ""
    current_value: float | None | str | Unset = UNSET
    previous_value: float | None | str | Unset = UNSET
    change_percent: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        trend = self.trend

        unit = self.unit

        current_value: float | None | str | Unset
        if isinstance(self.current_value, Unset):
            current_value = UNSET
        else:
            current_value = self.current_value

        previous_value: float | None | str | Unset
        if isinstance(self.previous_value, Unset):
            previous_value = UNSET
        else:
            previous_value = self.previous_value

        change_percent: float | None | str | Unset
        if isinstance(self.change_percent, Unset):
            change_percent = UNSET
        else:
            change_percent = self.change_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "trend": trend,
            }
        )
        if unit is not UNSET:
            field_dict["unit"] = unit
        if current_value is not UNSET:
            field_dict["current_value"] = current_value
        if previous_value is not UNSET:
            field_dict["previous_value"] = previous_value
        if change_percent is not UNSET:
            field_dict["change_percent"] = change_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        trend = d.pop("trend")

        unit = d.pop("unit", UNSET)

        def _parse_current_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        current_value = _parse_current_value(d.pop("current_value", UNSET))

        def _parse_previous_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        previous_value = _parse_previous_value(d.pop("previous_value", UNSET))

        def _parse_change_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        change_percent = _parse_change_percent(d.pop("change_percent", UNSET))

        analytics_trend_item = cls(
            name=name,
            trend=trend,
            unit=unit,
            current_value=current_value,
            previous_value=previous_value,
            change_percent=change_percent,
        )

        analytics_trend_item.additional_properties = d
        return analytics_trend_item

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
