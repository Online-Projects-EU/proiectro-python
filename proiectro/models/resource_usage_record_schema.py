from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceUsageRecordSchema")


@_attrs_define
class ResourceUsageRecordSchema:
    """Individual resource usage record for datatable

    Attributes:
        usage_id (str):
        date (datetime.date):
        date_formatted (str):
        usage_quantity (int):
        project_id (str):
        project_name (str):
        member_id (str):
        member_name (str):
        project_link (None | str | Unset):
        member_link (None | str | Unset):
        note (None | str | Unset):
    """

    usage_id: str
    date: datetime.date
    date_formatted: str
    usage_quantity: int
    project_id: str
    project_name: str
    member_id: str
    member_name: str
    project_link: None | str | Unset = UNSET
    member_link: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usage_id = self.usage_id

        date = self.date.isoformat()

        date_formatted = self.date_formatted

        usage_quantity = self.usage_quantity

        project_id = self.project_id

        project_name = self.project_name

        member_id = self.member_id

        member_name = self.member_name

        project_link: None | str | Unset
        if isinstance(self.project_link, Unset):
            project_link = UNSET
        else:
            project_link = self.project_link

        member_link: None | str | Unset
        if isinstance(self.member_link, Unset):
            member_link = UNSET
        else:
            member_link = self.member_link

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "usage_id": usage_id,
                "date": date,
                "date_formatted": date_formatted,
                "usage_quantity": usage_quantity,
                "project_id": project_id,
                "project_name": project_name,
                "member_id": member_id,
                "member_name": member_name,
            }
        )
        if project_link is not UNSET:
            field_dict["project_link"] = project_link
        if member_link is not UNSET:
            field_dict["member_link"] = member_link
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        usage_id = d.pop("usage_id")

        date = isoparse(d.pop("date")).date()

        date_formatted = d.pop("date_formatted")

        usage_quantity = d.pop("usage_quantity")

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        member_id = d.pop("member_id")

        member_name = d.pop("member_name")

        def _parse_project_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_link = _parse_project_link(d.pop("project_link", UNSET))

        def _parse_member_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_link = _parse_member_link(d.pop("member_link", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        resource_usage_record_schema = cls(
            usage_id=usage_id,
            date=date,
            date_formatted=date_formatted,
            usage_quantity=usage_quantity,
            project_id=project_id,
            project_name=project_name,
            member_id=member_id,
            member_name=member_name,
            project_link=project_link,
            member_link=member_link,
            note=note,
        )

        resource_usage_record_schema.additional_properties = d
        return resource_usage_record_schema

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
