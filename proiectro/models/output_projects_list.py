from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_list_item import ProjectListItem


T = TypeVar("T", bound="OutputProjectsList")


@_attrs_define
class OutputProjectsList:
    """List of active projects (closed_won stage)

    Attributes:
        projects (list[ProjectListItem]):
        total_count (int):
    """

    projects: list[ProjectListItem]
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projects": projects,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_list_item import ProjectListItem

        d = dict(src_dict)
        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = ProjectListItem.from_dict(projects_item_data)

            projects.append(projects_item)

        total_count = d.pop("total_count")

        output_projects_list = cls(
            projects=projects,
            total_count=total_count,
        )

        output_projects_list.additional_properties = d
        return output_projects_list

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
