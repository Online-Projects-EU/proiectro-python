from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsARCustomerItem")


@_attrs_define
class AnalyticsARCustomerItem:
    """AR aging by customer

    Attributes:
        name (str):
        current (float | str):
        days_30 (float | str):
        days_60 (float | str):
        days_90_plus (float | str):
        total (float | str):
    """

    name: str
    current: float | str
    days_30: float | str
    days_60: float | str
    days_90_plus: float | str
    total: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        current: float | str
        current = self.current

        days_30: float | str
        days_30 = self.days_30

        days_60: float | str
        days_60 = self.days_60

        days_90_plus: float | str
        days_90_plus = self.days_90_plus

        total: float | str
        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "current": current,
                "days_30": days_30,
                "days_60": days_60,
                "days_90_plus": days_90_plus,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_current(data: object) -> float | str:
            return cast(float | str, data)

        current = _parse_current(d.pop("current"))

        def _parse_days_30(data: object) -> float | str:
            return cast(float | str, data)

        days_30 = _parse_days_30(d.pop("days_30"))

        def _parse_days_60(data: object) -> float | str:
            return cast(float | str, data)

        days_60 = _parse_days_60(d.pop("days_60"))

        def _parse_days_90_plus(data: object) -> float | str:
            return cast(float | str, data)

        days_90_plus = _parse_days_90_plus(d.pop("days_90_plus"))

        def _parse_total(data: object) -> float | str:
            return cast(float | str, data)

        total = _parse_total(d.pop("total"))

        analytics_ar_customer_item = cls(
            name=name,
            current=current,
            days_30=days_30,
            days_60=days_60,
            days_90_plus=days_90_plus,
            total=total,
        )

        analytics_ar_customer_item.additional_properties = d
        return analytics_ar_customer_item

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
