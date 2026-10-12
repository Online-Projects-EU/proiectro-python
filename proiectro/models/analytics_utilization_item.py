from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsUtilizationItem")


@_attrs_define
class AnalyticsUtilizationItem:
    """Booked against available hours, for one resource or one category.

    `utilization_rate` is None when the entity has no weekly schedule on file — capacity is
    unknown, not zero, and a rate of 0% would read as "idle".

        Attributes:
            name (str):
            booked_hours (float | str):
            available_hours (float | str):
            utilization_rate (float | None | str | Unset):
    """

    name: str
    booked_hours: float | str
    available_hours: float | str
    utilization_rate: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        booked_hours: float | str
        booked_hours = self.booked_hours

        available_hours: float | str
        available_hours = self.available_hours

        utilization_rate: float | None | str | Unset
        if isinstance(self.utilization_rate, Unset):
            utilization_rate = UNSET
        else:
            utilization_rate = self.utilization_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "booked_hours": booked_hours,
                "available_hours": available_hours,
            }
        )
        if utilization_rate is not UNSET:
            field_dict["utilization_rate"] = utilization_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_booked_hours(data: object) -> float | str:
            return cast(float | str, data)

        booked_hours = _parse_booked_hours(d.pop("booked_hours"))

        def _parse_available_hours(data: object) -> float | str:
            return cast(float | str, data)

        available_hours = _parse_available_hours(d.pop("available_hours"))

        def _parse_utilization_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        utilization_rate = _parse_utilization_rate(d.pop("utilization_rate", UNSET))

        analytics_utilization_item = cls(
            name=name,
            booked_hours=booked_hours,
            available_hours=available_hours,
            utilization_rate=utilization_rate,
        )

        analytics_utilization_item.additional_properties = d
        return analytics_utilization_item

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
