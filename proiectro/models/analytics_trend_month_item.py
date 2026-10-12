from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsTrendMonthItem")


@_attrs_define
class AnalyticsTrendMonthItem:
    """Trend for a single month - created vs closed

    Attributes:
        month (str):
        created (int):
        closed (int):
    """

    month: str
    created: int
    closed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        created = self.created

        closed = self.closed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "created": created,
                "closed": closed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = d.pop("month")

        created = d.pop("created")

        closed = d.pop("closed")

        analytics_trend_month_item = cls(
            month=month,
            created=created,
            closed=closed,
        )

        analytics_trend_month_item.additional_properties = d
        return analytics_trend_month_item

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
