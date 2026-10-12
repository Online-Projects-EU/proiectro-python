from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputLeadTeamRollupRow")


@_attrs_define
class OutputLeadTeamRollupRow:
    """One row of the per-rep manager dashboard.

    Attributes:
        member_id (str):
        member_name (str):
        member_avatar_url (str):
        overdue_count (int | Unset):  Default: 0.
        today_count (int | Unset):  Default: 0.
        untriaged_count (int | Unset):  Default: 0.
        scheduled_count (int | Unset):  Default: 0.
        converted_30d_count (int | Unset):  Default: 0.
    """

    member_id: str
    member_name: str
    member_avatar_url: str
    overdue_count: int | Unset = 0
    today_count: int | Unset = 0
    untriaged_count: int | Unset = 0
    scheduled_count: int | Unset = 0
    converted_30d_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_id = self.member_id

        member_name = self.member_name

        member_avatar_url = self.member_avatar_url

        overdue_count = self.overdue_count

        today_count = self.today_count

        untriaged_count = self.untriaged_count

        scheduled_count = self.scheduled_count

        converted_30d_count = self.converted_30d_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "member_id": member_id,
                "member_name": member_name,
                "member_avatar_url": member_avatar_url,
            }
        )
        if overdue_count is not UNSET:
            field_dict["overdue_count"] = overdue_count
        if today_count is not UNSET:
            field_dict["today_count"] = today_count
        if untriaged_count is not UNSET:
            field_dict["untriaged_count"] = untriaged_count
        if scheduled_count is not UNSET:
            field_dict["scheduled_count"] = scheduled_count
        if converted_30d_count is not UNSET:
            field_dict["converted_30d_count"] = converted_30d_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        member_id = d.pop("member_id")

        member_name = d.pop("member_name")

        member_avatar_url = d.pop("member_avatar_url")

        overdue_count = d.pop("overdue_count", UNSET)

        today_count = d.pop("today_count", UNSET)

        untriaged_count = d.pop("untriaged_count", UNSET)

        scheduled_count = d.pop("scheduled_count", UNSET)

        converted_30d_count = d.pop("converted_30d_count", UNSET)

        output_lead_team_rollup_row = cls(
            member_id=member_id,
            member_name=member_name,
            member_avatar_url=member_avatar_url,
            overdue_count=overdue_count,
            today_count=today_count,
            untriaged_count=untriaged_count,
            scheduled_count=scheduled_count,
            converted_30d_count=converted_30d_count,
        )

        output_lead_team_rollup_row.additional_properties = d
        return output_lead_team_rollup_row

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
