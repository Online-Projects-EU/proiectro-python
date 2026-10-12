from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resource_activity_item import ResourceActivityItem


T = TypeVar("T", bound="ProjectResourceActivityOutput")


@_attrs_define
class ProjectResourceActivityOutput:
    """
    Attributes:
        usage_items (list[ResourceActivityItem]):
        total_usage (int):
        usage_count (int):
        resource_id (str):
        resource_name (str):
        project_id (str):
    """

    usage_items: list[ResourceActivityItem]
    total_usage: int
    usage_count: int
    resource_id: str
    resource_name: str
    project_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usage_items = []
        for usage_items_item_data in self.usage_items:
            usage_items_item = usage_items_item_data.to_dict()
            usage_items.append(usage_items_item)

        total_usage = self.total_usage

        usage_count = self.usage_count

        resource_id = self.resource_id

        resource_name = self.resource_name

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "usage_items": usage_items,
                "total_usage": total_usage,
                "usage_count": usage_count,
                "resource_id": resource_id,
                "resource_name": resource_name,
                "project_id": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_activity_item import ResourceActivityItem

        d = dict(src_dict)
        usage_items = []
        _usage_items = d.pop("usage_items")
        for usage_items_item_data in _usage_items:
            usage_items_item = ResourceActivityItem.from_dict(usage_items_item_data)

            usage_items.append(usage_items_item)

        total_usage = d.pop("total_usage")

        usage_count = d.pop("usage_count")

        resource_id = d.pop("resource_id")

        resource_name = d.pop("resource_name")

        project_id = d.pop("project_id")

        project_resource_activity_output = cls(
            usage_items=usage_items,
            total_usage=total_usage,
            usage_count=usage_count,
            resource_id=resource_id,
            resource_name=resource_name,
            project_id=project_id,
        )

        project_resource_activity_output.additional_properties = d
        return project_resource_activity_output

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
