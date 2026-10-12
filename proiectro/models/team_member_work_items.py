from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.team_member_work_item import TeamMemberWorkItem


T = TypeVar("T", bound="TeamMemberWorkItems")


@_attrs_define
class TeamMemberWorkItems:
    """List of work items owned by a team member in a project

    Attributes:
        team_member_id (str):
        team_member_name (str):
        project_id (str):
        project_name (str):
        work_items (list[TeamMemberWorkItem]):
        total (int):
    """

    team_member_id: str
    team_member_name: str
    project_id: str
    project_name: str
    work_items: list[TeamMemberWorkItem]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_member_id = self.team_member_id

        team_member_name = self.team_member_name

        project_id = self.project_id

        project_name = self.project_name

        work_items = []
        for work_items_item_data in self.work_items:
            work_items_item = work_items_item_data.to_dict()
            work_items.append(work_items_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_member_id": team_member_id,
                "team_member_name": team_member_name,
                "project_id": project_id,
                "project_name": project_name,
                "work_items": work_items,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_member_work_item import TeamMemberWorkItem

        d = dict(src_dict)
        team_member_id = d.pop("team_member_id")

        team_member_name = d.pop("team_member_name")

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        work_items = []
        _work_items = d.pop("work_items")
        for work_items_item_data in _work_items:
            work_items_item = TeamMemberWorkItem.from_dict(work_items_item_data)

            work_items.append(work_items_item)

        total = d.pop("total")

        team_member_work_items = cls(
            team_member_id=team_member_id,
            team_member_name=team_member_name,
            project_id=project_id,
            project_name=project_name,
            work_items=work_items,
            total=total,
        )

        team_member_work_items.additional_properties = d
        return team_member_work_items

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
