from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsRevenueMonthItem")


@_attrs_define
class AnalyticsRevenueMonthItem:
    """Revenue for a single month

    Attributes:
        month (str):
        recurring (float | str):
        one_time (float | str):
        total (float | str):
    """

    month: str
    recurring: float | str
    one_time: float | str
    total: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        recurring: float | str
        recurring = self.recurring

        one_time: float | str
        one_time = self.one_time

        total: float | str
        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "recurring": recurring,
                "one_time": one_time,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = d.pop("month")

        def _parse_recurring(data: object) -> float | str:
            return cast(float | str, data)

        recurring = _parse_recurring(d.pop("recurring"))

        def _parse_one_time(data: object) -> float | str:
            return cast(float | str, data)

        one_time = _parse_one_time(d.pop("one_time"))

        def _parse_total(data: object) -> float | str:
            return cast(float | str, data)

        total = _parse_total(d.pop("total"))

        analytics_revenue_month_item = cls(
            month=month,
            recurring=recurring,
            one_time=one_time,
            total=total,
        )

        analytics_revenue_month_item.additional_properties = d
        return analytics_revenue_month_item

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
