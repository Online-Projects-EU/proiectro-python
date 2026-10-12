from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resource_usage_item import ResourceUsageItem


T = TypeVar("T", bound="WorkItemResourceUsageOutput")


@_attrs_define
class WorkItemResourceUsageOutput:
    """
    Attributes:
        resource_usage (list[ResourceUsageItem]):
        total_usage (int):
        usage_count (int):
        work_item_id (str):
        work_item_name (str):
        project_id (str):
    """

    resource_usage: list[ResourceUsageItem]
    total_usage: int
    usage_count: int
    work_item_id: str
    work_item_name: str
    project_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_usage = []
        for resource_usage_item_data in self.resource_usage:
            resource_usage_item = resource_usage_item_data.to_dict()
            resource_usage.append(resource_usage_item)

        total_usage = self.total_usage

        usage_count = self.usage_count

        work_item_id = self.work_item_id

        work_item_name = self.work_item_name

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_usage": resource_usage,
                "total_usage": total_usage,
                "usage_count": usage_count,
                "work_item_id": work_item_id,
                "work_item_name": work_item_name,
                "project_id": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_usage_item import ResourceUsageItem

        d = dict(src_dict)
        resource_usage = []
        _resource_usage = d.pop("resource_usage")
        for resource_usage_item_data in _resource_usage:
            resource_usage_item = ResourceUsageItem.from_dict(resource_usage_item_data)

            resource_usage.append(resource_usage_item)

        total_usage = d.pop("total_usage")

        usage_count = d.pop("usage_count")

        work_item_id = d.pop("work_item_id")

        work_item_name = d.pop("work_item_name")

        project_id = d.pop("project_id")

        work_item_resource_usage_output = cls(
            resource_usage=resource_usage,
            total_usage=total_usage,
            usage_count=usage_count,
            work_item_id=work_item_id,
            work_item_name=work_item_name,
            project_id=project_id,
        )

        work_item_resource_usage_output.additional_properties = d
        return work_item_resource_usage_output

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
