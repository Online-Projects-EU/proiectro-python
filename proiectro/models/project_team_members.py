from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_team_member import ProjectTeamMember


T = TypeVar("T", bound="ProjectTeamMembers")


@_attrs_define
class ProjectTeamMembers:
    """List of team members for a project

    Attributes:
        team_members (list[ProjectTeamMember]):
        project_id (str):
        project_name (str):
    """

    team_members: list[ProjectTeamMember]
    project_id: str
    project_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_members = []
        for team_members_item_data in self.team_members:
            team_members_item = team_members_item_data.to_dict()
            team_members.append(team_members_item)

        project_id = self.project_id

        project_name = self.project_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_members": team_members,
                "project_id": project_id,
                "project_name": project_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_team_member import ProjectTeamMember

        d = dict(src_dict)
        team_members = []
        _team_members = d.pop("team_members")
        for team_members_item_data in _team_members:
            team_members_item = ProjectTeamMember.from_dict(team_members_item_data)

            team_members.append(team_members_item)

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        project_team_members = cls(
            team_members=team_members,
            project_id=project_id,
            project_name=project_name,
        )

        project_team_members.additional_properties = d
        return project_team_members

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
