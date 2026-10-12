from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsARCustomerItem")


@_attrs_define
class AnalyticsARCustomerItem:
    """AR aging by customer. Null wherever that band holds a receivable with no rate.

    Attributes:
        name (str):
        current (float | None | str | Unset):
        days_30 (float | None | str | Unset):
        days_60 (float | None | str | Unset):
        days_61_90 (float | None | str | Unset):
        days_90_plus (float | None | str | Unset):
        total (float | None | str | Unset):
    """

    name: str
    current: float | None | str | Unset = UNSET
    days_30: float | None | str | Unset = UNSET
    days_60: float | None | str | Unset = UNSET
    days_61_90: float | None | str | Unset = UNSET
    days_90_plus: float | None | str | Unset = UNSET
    total: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        current: float | None | str | Unset
        if isinstance(self.current, Unset):
            current = UNSET
        else:
            current = self.current

        days_30: float | None | str | Unset
        if isinstance(self.days_30, Unset):
            days_30 = UNSET
        else:
            days_30 = self.days_30

        days_60: float | None | str | Unset
        if isinstance(self.days_60, Unset):
            days_60 = UNSET
        else:
            days_60 = self.days_60

        days_61_90: float | None | str | Unset
        if isinstance(self.days_61_90, Unset):
            days_61_90 = UNSET
        else:
            days_61_90 = self.days_61_90

        days_90_plus: float | None | str | Unset
        if isinstance(self.days_90_plus, Unset):
            days_90_plus = UNSET
        else:
            days_90_plus = self.days_90_plus

        total: float | None | str | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if current is not UNSET:
            field_dict["current"] = current
        if days_30 is not UNSET:
            field_dict["days_30"] = days_30
        if days_60 is not UNSET:
            field_dict["days_60"] = days_60
        if days_61_90 is not UNSET:
            field_dict["days_61_90"] = days_61_90
        if days_90_plus is not UNSET:
            field_dict["days_90_plus"] = days_90_plus
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_current(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        current = _parse_current(d.pop("current", UNSET))

        def _parse_days_30(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        days_30 = _parse_days_30(d.pop("days_30", UNSET))

        def _parse_days_60(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        days_60 = _parse_days_60(d.pop("days_60", UNSET))

        def _parse_days_61_90(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        days_61_90 = _parse_days_61_90(d.pop("days_61_90", UNSET))

        def _parse_days_90_plus(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        days_90_plus = _parse_days_90_plus(d.pop("days_90_plus", UNSET))

        def _parse_total(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

        analytics_ar_customer_item = cls(
            name=name,
            current=current,
            days_30=days_30,
            days_60=days_60,
            days_61_90=days_61_90,
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
