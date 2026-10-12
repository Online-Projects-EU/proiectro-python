from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReassignLeadList")


@_attrs_define
class ReassignLeadList:
    """Change the owner of a list (own-scope: change my list to someone else).

    Attributes:
        updated_at (datetime.datetime):
        owner (None | str | Unset):
        cascade_to_leads (bool | Unset):  Default: False.
    """

    updated_at: datetime.datetime
    owner: None | str | Unset = UNSET
    cascade_to_leads: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_at = self.updated_at.isoformat()

        owner: None | str | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        else:
            owner = self.owner

        cascade_to_leads = self.cascade_to_leads

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updated_at": updated_at,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner
        if cascade_to_leads is not UNSET:
            field_dict["cascade_to_leads"] = cascade_to_leads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        updated_at = isoparse(d.pop("updated_at"))

        def _parse_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner = _parse_owner(d.pop("owner", UNSET))

        cascade_to_leads = d.pop("cascade_to_leads", UNSET)

        reassign_lead_list = cls(
            updated_at=updated_at,
            owner=owner,
            cascade_to_leads=cascade_to_leads,
        )

        reassign_lead_list.additional_properties = d
        return reassign_lead_list

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
