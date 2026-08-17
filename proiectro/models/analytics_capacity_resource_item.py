from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AnalyticsCapacityResourceItem")



@_attrs_define
class AnalyticsCapacityResourceItem:
    """ Capacity for a single resource. `category` is its parent in the resource hierarchy.

        Attributes:
            name (str):
            total_hours (float | str):
            allocated_hours (float | str):
            available_hours (float | str):
            category (None | str | Unset):
     """

    name: str
    total_hours: float | str
    allocated_hours: float | str
    available_hours: float | str
    category: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        total_hours: float | str
        total_hours = self.total_hours

        allocated_hours: float | str
        allocated_hours = self.allocated_hours

        available_hours: float | str
        available_hours = self.available_hours

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "total_hours": total_hours,
            "allocated_hours": allocated_hours,
            "available_hours": available_hours,
        })
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_total_hours(data: object) -> float | str:
            return cast(float | str, data)

        total_hours = _parse_total_hours(d.pop("total_hours"))


        def _parse_allocated_hours(data: object) -> float | str:
            return cast(float | str, data)

        allocated_hours = _parse_allocated_hours(d.pop("allocated_hours"))


        def _parse_available_hours(data: object) -> float | str:
            return cast(float | str, data)

        available_hours = _parse_available_hours(d.pop("available_hours"))


        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        analytics_capacity_resource_item = cls(
            name=name,
            total_hours=total_hours,
            allocated_hours=allocated_hours,
            available_hours=available_hours,
            category=category,
        )


        analytics_capacity_resource_item.additional_properties = d
        return analytics_capacity_resource_item

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
