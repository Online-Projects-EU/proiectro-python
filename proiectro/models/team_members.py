from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.former_team_member import FormerTeamMember
    from ..models.invitation_output import InvitationOutput
    from ..models.team_member import TeamMember


T = TypeVar("T", bound="TeamMembers")


@_attrs_define
class TeamMembers:
    """
    Attributes:
        members (list[TeamMember]):
        invitations (list[InvitationOutput]):
        former_members (list[FormerTeamMember] | Unset):
    """

    members: list[TeamMember]
    invitations: list[InvitationOutput]
    former_members: list[FormerTeamMember] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        invitations = []
        for invitations_item_data in self.invitations:
            invitations_item = invitations_item_data.to_dict()
            invitations.append(invitations_item)

        former_members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.former_members, Unset):
            former_members = []
            for former_members_item_data in self.former_members:
                former_members_item = former_members_item_data.to_dict()
                former_members.append(former_members_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "members": members,
                "invitations": invitations,
            }
        )
        if former_members is not UNSET:
            field_dict["former_members"] = former_members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.former_team_member import FormerTeamMember
        from ..models.invitation_output import InvitationOutput
        from ..models.team_member import TeamMember

        d = dict(src_dict)
        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = TeamMember.from_dict(members_item_data)

            members.append(members_item)

        invitations = []
        _invitations = d.pop("invitations")
        for invitations_item_data in _invitations:
            invitations_item = InvitationOutput.from_dict(invitations_item_data)

            invitations.append(invitations_item)

        _former_members = d.pop("former_members", UNSET)
        former_members: list[FormerTeamMember] | Unset = UNSET
        if _former_members is not UNSET:
            former_members = []
            for former_members_item_data in _former_members:
                former_members_item = FormerTeamMember.from_dict(
                    former_members_item_data
                )

                former_members.append(former_members_item)

        team_members = cls(
            members=members,
            invitations=invitations,
            former_members=former_members,
        )

        team_members.additional_properties = d
        return team_members

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
