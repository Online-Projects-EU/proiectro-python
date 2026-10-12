from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsCapacityForecastItem")


@_attrs_define
class AnalyticsCapacityForecastItem:
    """Booked demand against available capacity for one month of the horizon.

    Attributes:
        period (str):
        demand_hours (float | str):
        capacity_hours (float | str):
        gap_hours (float | str):
    """

    period: str
    demand_hours: float | str
    capacity_hours: float | str
    gap_hours: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period = self.period

        demand_hours: float | str
        demand_hours = self.demand_hours

        capacity_hours: float | str
        capacity_hours = self.capacity_hours

        gap_hours: float | str
        gap_hours = self.gap_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period": period,
                "demand_hours": demand_hours,
                "capacity_hours": capacity_hours,
                "gap_hours": gap_hours,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        period = d.pop("period")

        def _parse_demand_hours(data: object) -> float | str:
            return cast(float | str, data)

        demand_hours = _parse_demand_hours(d.pop("demand_hours"))

        def _parse_capacity_hours(data: object) -> float | str:
            return cast(float | str, data)

        capacity_hours = _parse_capacity_hours(d.pop("capacity_hours"))

        def _parse_gap_hours(data: object) -> float | str:
            return cast(float | str, data)

        gap_hours = _parse_gap_hours(d.pop("gap_hours"))

        analytics_capacity_forecast_item = cls(
            period=period,
            demand_hours=demand_hours,
            capacity_hours=capacity_hours,
            gap_hours=gap_hours,
        )

        analytics_capacity_forecast_item.additional_properties = d
        return analytics_capacity_forecast_item

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
