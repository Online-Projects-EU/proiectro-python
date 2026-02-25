from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResourceUsageItem")


@_attrs_define
class ResourceUsageItem:
    """
    Attributes:
        external_id (str):
        resource_name (str):
        resource_id (str):
        booking_name (str):
        booking_id (str):
        member_full_name (str):
        member_id (str):
        usage (int):
        date (str):
        note (str):
    """

    external_id: str
    resource_name: str
    resource_id: str
    booking_name: str
    booking_id: str
    member_full_name: str
    member_id: str
    usage: int
    date: str
    note: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        resource_name = self.resource_name

        resource_id = self.resource_id

        booking_name = self.booking_name

        booking_id = self.booking_id

        member_full_name = self.member_full_name

        member_id = self.member_id

        usage = self.usage

        date = self.date

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "resource_name": resource_name,
                "resource_id": resource_id,
                "booking_name": booking_name,
                "booking_id": booking_id,
                "member_full_name": member_full_name,
                "member_id": member_id,
                "usage": usage,
                "date": date,
                "note": note,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_id = d.pop("external_id")

        resource_name = d.pop("resource_name")

        resource_id = d.pop("resource_id")

        booking_name = d.pop("booking_name")

        booking_id = d.pop("booking_id")

        member_full_name = d.pop("member_full_name")

        member_id = d.pop("member_id")

        usage = d.pop("usage")

        date = d.pop("date")

        note = d.pop("note")

        resource_usage_item = cls(
            external_id=external_id,
            resource_name=resource_name,
            resource_id=resource_id,
            booking_name=booking_name,
            booking_id=booking_id,
            member_full_name=member_full_name,
            member_id=member_id,
            usage=usage,
            date=date,
            note=note,
        )

        resource_usage_item.additional_properties = d
        return resource_usage_item

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
