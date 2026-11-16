from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputSentMessageAttachment")


@_attrs_define
class OutputSentMessageAttachment:
    """A file an email carried, kept as it went out. `purged_at` is when its content was removed, after the
    days a sent file is kept; its name and size stay.

        Attributes:
            id (str):
            name (str):
            size (int):
            purged_at (datetime.datetime | None | Unset):
    """

    id: str
    name: str
    size: int
    purged_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        size = self.size

        purged_at: None | str | Unset
        if isinstance(self.purged_at, Unset):
            purged_at = UNSET
        elif isinstance(self.purged_at, datetime.datetime):
            purged_at = self.purged_at.isoformat()
        else:
            purged_at = self.purged_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "size": size,
            }
        )
        if purged_at is not UNSET:
            field_dict["purged_at"] = purged_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        size = d.pop("size")

        def _parse_purged_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                purged_at_type_0 = isoparse(data)

                return purged_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        purged_at = _parse_purged_at(d.pop("purged_at", UNSET))

        output_sent_message_attachment = cls(
            id=id,
            name=name,
            size=size,
            purged_at=purged_at,
        )

        output_sent_message_attachment.additional_properties = d
        return output_sent_message_attachment

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
