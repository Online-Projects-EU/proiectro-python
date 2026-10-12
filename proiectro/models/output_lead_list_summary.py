from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputLeadListSummary")


@_attrs_define
class OutputLeadListSummary:
    """Compact representation used in the Lists tab.

    Attributes:
        id (str):
        name (str):
        is_pool (bool):
        is_active (bool):
        description (str | Unset):  Default: ''.
        owner_id (None | str | Unset):
        owner_name (None | str | Unset):
        owner_avatar_url (None | str | Unset):
        overdue_count (int | Unset):  Default: 0.
        today_count (int | Unset):  Default: 0.
        untriaged_count (int | Unset):  Default: 0.
        scheduled_count (int | Unset):  Default: 0.
        closed_count (int | Unset):  Default: 0.
        total_count (int | Unset):  Default: 0.
    """

    id: str
    name: str
    is_pool: bool
    is_active: bool
    description: str | Unset = ""
    owner_id: None | str | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    owner_avatar_url: None | str | Unset = UNSET
    overdue_count: int | Unset = 0
    today_count: int | Unset = 0
    untriaged_count: int | Unset = 0
    scheduled_count: int | Unset = 0
    closed_count: int | Unset = 0
    total_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_pool = self.is_pool

        is_active = self.is_active

        description = self.description

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        owner_avatar_url: None | str | Unset
        if isinstance(self.owner_avatar_url, Unset):
            owner_avatar_url = UNSET
        else:
            owner_avatar_url = self.owner_avatar_url

        overdue_count = self.overdue_count

        today_count = self.today_count

        untriaged_count = self.untriaged_count

        scheduled_count = self.scheduled_count

        closed_count = self.closed_count

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "is_pool": is_pool,
                "is_active": is_active,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if owner_avatar_url is not UNSET:
            field_dict["owner_avatar_url"] = owner_avatar_url
        if overdue_count is not UNSET:
            field_dict["overdue_count"] = overdue_count
        if today_count is not UNSET:
            field_dict["today_count"] = today_count
        if untriaged_count is not UNSET:
            field_dict["untriaged_count"] = untriaged_count
        if scheduled_count is not UNSET:
            field_dict["scheduled_count"] = scheduled_count
        if closed_count is not UNSET:
            field_dict["closed_count"] = closed_count
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_pool = d.pop("is_pool")

        is_active = d.pop("is_active")

        description = d.pop("description", UNSET)

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))

        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("owner_name", UNSET))

        def _parse_owner_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_avatar_url = _parse_owner_avatar_url(d.pop("owner_avatar_url", UNSET))

        overdue_count = d.pop("overdue_count", UNSET)

        today_count = d.pop("today_count", UNSET)

        untriaged_count = d.pop("untriaged_count", UNSET)

        scheduled_count = d.pop("scheduled_count", UNSET)

        closed_count = d.pop("closed_count", UNSET)

        total_count = d.pop("total_count", UNSET)

        output_lead_list_summary = cls(
            id=id,
            name=name,
            is_pool=is_pool,
            is_active=is_active,
            description=description,
            owner_id=owner_id,
            owner_name=owner_name,
            owner_avatar_url=owner_avatar_url,
            overdue_count=overdue_count,
            today_count=today_count,
            untriaged_count=untriaged_count,
            scheduled_count=scheduled_count,
            closed_count=closed_count,
            total_count=total_count,
        )

        output_lead_list_summary.additional_properties = d
        return output_lead_list_summary

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
