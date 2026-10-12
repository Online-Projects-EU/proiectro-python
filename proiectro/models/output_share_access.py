from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputShareAccess")


@_attrs_define
class OutputShareAccess:
    """
    Attributes:
        kind (str):
        channel (str):
        created_at (datetime.datetime):
        item_type (str | Unset):  Default: ''.
        item_label (str | Unset):  Default: ''.
        who (None | str | Unset):
    """

    kind: str
    channel: str
    created_at: datetime.datetime
    item_type: str | Unset = ""
    item_label: str | Unset = ""
    who: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        channel = self.channel

        created_at = self.created_at.isoformat()

        item_type = self.item_type

        item_label = self.item_label

        who: None | str | Unset
        if isinstance(self.who, Unset):
            who = UNSET
        else:
            who = self.who

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "channel": channel,
                "created_at": created_at,
            }
        )
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if item_label is not UNSET:
            field_dict["item_label"] = item_label
        if who is not UNSET:
            field_dict["who"] = who

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind")

        channel = d.pop("channel")

        created_at = isoparse(d.pop("created_at"))

        item_type = d.pop("item_type", UNSET)

        item_label = d.pop("item_label", UNSET)

        def _parse_who(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        who = _parse_who(d.pop("who", UNSET))

        output_share_access = cls(
            kind=kind,
            channel=channel,
            created_at=created_at,
            item_type=item_type,
            item_label=item_label,
            who=who,
        )

        output_share_access.additional_properties = d
        return output_share_access

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
