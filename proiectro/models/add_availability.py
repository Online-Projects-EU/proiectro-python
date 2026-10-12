from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddAvailability")


@_attrs_define
class AddAvailability:
    """
    Attributes:
        tenant (str):
        day_of_week (int):
        start_time (int):
        end_time (int):
    """

    tenant: str
    day_of_week: int
    start_time: int
    end_time: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tenant = self.tenant

        day_of_week = self.day_of_week

        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tenant": tenant,
                "day_of_week": day_of_week,
                "start_time": start_time,
                "end_time": end_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant = d.pop("tenant")

        day_of_week = d.pop("day_of_week")

        start_time = d.pop("start_time")

        end_time = d.pop("end_time")

        add_availability = cls(
            tenant=tenant,
            day_of_week=day_of_week,
            start_time=start_time,
            end_time=end_time,
        )

        add_availability.additional_properties = d
        return add_availability

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
