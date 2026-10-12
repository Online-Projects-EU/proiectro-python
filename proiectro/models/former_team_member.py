from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormerTeamMember")


@_attrs_define
class FormerTeamMember:
    """A former team member, excluded from the workspace: the name they had, and when and by whom
    they were excluded.

        Attributes:
            id (str):
            name (str):
            avatar_url (str):
            excluded_at (datetime.datetime):
            excluded_by (None | str | Unset):
    """

    id: str
    name: str
    avatar_url: str
    excluded_at: datetime.datetime
    excluded_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        avatar_url = self.avatar_url

        excluded_at = self.excluded_at.isoformat()

        excluded_by: None | str | Unset
        if isinstance(self.excluded_by, Unset):
            excluded_by = UNSET
        else:
            excluded_by = self.excluded_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "avatar_url": avatar_url,
                "excluded_at": excluded_at,
            }
        )
        if excluded_by is not UNSET:
            field_dict["excluded_by"] = excluded_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        avatar_url = d.pop("avatar_url")

        excluded_at = isoparse(d.pop("excluded_at"))

        def _parse_excluded_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        excluded_by = _parse_excluded_by(d.pop("excluded_by", UNSET))

        former_team_member = cls(
            id=id,
            name=name,
            avatar_url=avatar_url,
            excluded_at=excluded_at,
            excluded_by=excluded_by,
        )

        former_team_member.additional_properties = d
        return former_team_member

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
