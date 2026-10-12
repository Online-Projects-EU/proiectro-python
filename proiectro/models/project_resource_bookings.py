from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_resource_booking import ProjectResourceBooking


T = TypeVar("T", bound="ProjectResourceBookings")


@_attrs_define
class ProjectResourceBookings:
    """List of resource bookings for a project

    Attributes:
        resource_bookings (list[ProjectResourceBooking]):
        project_id (str):
        project_name (str):
    """

    resource_bookings: list[ProjectResourceBooking]
    project_id: str
    project_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_bookings = []
        for resource_bookings_item_data in self.resource_bookings:
            resource_bookings_item = resource_bookings_item_data.to_dict()
            resource_bookings.append(resource_bookings_item)

        project_id = self.project_id

        project_name = self.project_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_bookings": resource_bookings,
                "project_id": project_id,
                "project_name": project_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_resource_booking import ProjectResourceBooking

        d = dict(src_dict)
        resource_bookings = []
        _resource_bookings = d.pop("resource_bookings")
        for resource_bookings_item_data in _resource_bookings:
            resource_bookings_item = ProjectResourceBooking.from_dict(
                resource_bookings_item_data
            )

            resource_bookings.append(resource_bookings_item)

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        project_resource_bookings = cls(
            resource_bookings=resource_bookings,
            project_id=project_id,
            project_name=project_name,
        )

        project_resource_bookings.additional_properties = d
        return project_resource_bookings

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
