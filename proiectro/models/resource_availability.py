from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resource_availability_days import ResourceAvailabilityDays


T = TypeVar("T", bound="ResourceAvailability")


@_attrs_define
class ResourceAvailability:
    """
    Attributes:
        resource (str):
        resource_timezone (str):
        days (ResourceAvailabilityDays):
    """

    resource: str
    resource_timezone: str
    days: ResourceAvailabilityDays
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource

        resource_timezone = self.resource_timezone

        days = self.days.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "resource_timezone": resource_timezone,
                "days": days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_availability_days import ResourceAvailabilityDays

        d = dict(src_dict)
        resource = d.pop("resource")

        resource_timezone = d.pop("resource_timezone")

        days = ResourceAvailabilityDays.from_dict(d.pop("days"))

        resource_availability = cls(
            resource=resource,
            resource_timezone=resource_timezone,
            days=days,
        )

        resource_availability.additional_properties = d
        return resource_availability

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
