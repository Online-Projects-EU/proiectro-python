from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.all_partners_project_item import AllPartnersProjectItem


T = TypeVar("T", bound="AllPartnersProjects")


@_attrs_define
class AllPartnersProjects:
    """Aggregated projects from all active partnerships

    Attributes:
        projects (list[AllPartnersProjectItem]):
        total (int):
    """

    projects: list[AllPartnersProjectItem]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projects": projects,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.all_partners_project_item import AllPartnersProjectItem

        d = dict(src_dict)
        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = AllPartnersProjectItem.from_dict(projects_item_data)

            projects.append(projects_item)

        total = d.pop("total")

        all_partners_projects = cls(
            projects=projects,
            total=total,
        )

        all_partners_projects.additional_properties = d
        return all_partners_projects

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
