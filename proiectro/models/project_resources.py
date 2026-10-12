from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_resource import ProjectResource


T = TypeVar("T", bound="ProjectResources")


@_attrs_define
class ProjectResources:
    """List of resources for a project

    Attributes:
        resources (list[ProjectResource]):
        project_id (str):
        project_name (str):
    """

    resources: list[ProjectResource]
    project_id: str
    project_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        project_id = self.project_id

        project_name = self.project_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resources": resources,
                "project_id": project_id,
                "project_name": project_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_resource import ProjectResource

        d = dict(src_dict)
        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = ProjectResource.from_dict(resources_item_data)

            resources.append(resources_item)

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        project_resources = cls(
            resources=resources,
            project_id=project_id,
            project_name=project_name,
        )

        project_resources.additional_properties = d
        return project_resources

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
