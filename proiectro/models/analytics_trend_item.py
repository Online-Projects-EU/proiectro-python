from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsTrendItem")


@_attrs_define
class AnalyticsTrendItem:
    """Single trend indicator

    Attributes:
        name (str):
        current_value (float | str):
        previous_value (float | str):
        trend (str):
        change_percent (float | None | str | Unset):
    """

    name: str
    current_value: float | str
    previous_value: float | str
    trend: str
    change_percent: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        current_value: float | str
        current_value = self.current_value

        previous_value: float | str
        previous_value = self.previous_value

        trend = self.trend

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
                "current_value": current_value,
                "previous_value": previous_value,
                "trend": trend,
            }
        )
        if change_percent is not UNSET:
            field_dict["change_percent"] = change_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_current_value(data: object) -> float | str:
            return cast(float | str, data)

        current_value = _parse_current_value(d.pop("current_value"))

        def _parse_previous_value(data: object) -> float | str:
            return cast(float | str, data)

        previous_value = _parse_previous_value(d.pop("previous_value"))

        trend = d.pop("trend")

        def _parse_change_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        change_percent = _parse_change_percent(d.pop("change_percent", UNSET))

        analytics_trend_item = cls(
            name=name,
            current_value=current_value,
            previous_value=previous_value,
            trend=trend,
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
