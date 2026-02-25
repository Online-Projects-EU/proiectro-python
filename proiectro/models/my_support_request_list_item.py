from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MySupportRequestListItem")


@_attrs_define
class MySupportRequestListItem:
    """Output schema for a support request in My Support Requests list

    Attributes:
        id (str):
        title (str):
        public_reference (str):
        type_name (str):
        severity_name (str):
        status_name (str):
        status_lifecycle (str):
        created (datetime.datetime):
        updated (datetime.datetime):
        updated_formatted (str):
    """

    id: str
    title: str
    public_reference: str
    type_name: str
    severity_name: str
    status_name: str
    status_lifecycle: str
    created: datetime.datetime
    updated: datetime.datetime
    updated_formatted: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        public_reference = self.public_reference

        type_name = self.type_name

        severity_name = self.severity_name

        status_name = self.status_name

        status_lifecycle = self.status_lifecycle

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        updated_formatted = self.updated_formatted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "public_reference": public_reference,
                "type_name": type_name,
                "severity_name": severity_name,
                "status_name": status_name,
                "status_lifecycle": status_lifecycle,
                "created": created,
                "updated": updated,
                "updated_formatted": updated_formatted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        public_reference = d.pop("public_reference")

        type_name = d.pop("type_name")

        severity_name = d.pop("severity_name")

        status_name = d.pop("status_name")

        status_lifecycle = d.pop("status_lifecycle")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        updated_formatted = d.pop("updated_formatted")

        my_support_request_list_item = cls(
            id=id,
            title=title,
            public_reference=public_reference,
            type_name=type_name,
            severity_name=severity_name,
            status_name=status_name,
            status_lifecycle=status_lifecycle,
            created=created,
            updated=updated,
            updated_formatted=updated_formatted,
        )

        my_support_request_list_item.additional_properties = d
        return my_support_request_list_item

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
