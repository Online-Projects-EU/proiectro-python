from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_resource_items_items_item import ProjectResourceItemsItemsItem


T = TypeVar("T", bound="ProjectResourceItems")


@_attrs_define
class ProjectResourceItems:
    """List of unique resources working on a project

    The item structure depends on the mode:
    - booking_mode=True: items contain ProjectResourceItemBooking fields
    - usage_mode=True: items contain ProjectResourceItemUsage fields

        Attributes:
            items (list[ProjectResourceItemsItemsItem]):
            project_id (str):
            project_name (str):
            total_resources (int):
            booking_mode (bool):
            usage_mode (bool):
    """

    items: list[ProjectResourceItemsItemsItem]
    project_id: str
    project_name: str
    total_resources: int
    booking_mode: bool
    usage_mode: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        project_id = self.project_id

        project_name = self.project_name

        total_resources = self.total_resources

        booking_mode = self.booking_mode

        usage_mode = self.usage_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "project_id": project_id,
                "project_name": project_name,
                "total_resources": total_resources,
                "booking_mode": booking_mode,
                "usage_mode": usage_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_resource_items_items_item import (
            ProjectResourceItemsItemsItem,
        )

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = ProjectResourceItemsItemsItem.from_dict(items_item_data)

            items.append(items_item)

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        total_resources = d.pop("total_resources")

        booking_mode = d.pop("booking_mode")

        usage_mode = d.pop("usage_mode")

        project_resource_items = cls(
            items=items,
            project_id=project_id,
            project_name=project_name,
            total_resources=total_resources,
            booking_mode=booking_mode,
            usage_mode=usage_mode,
        )

        project_resource_items.additional_properties = d
        return project_resource_items

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
