from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddWebhook")


@_attrs_define
class AddWebhook:
    """
    Attributes:
        name (str):
        target_url (str):
        event_types (list[str] | Unset):
        is_active (bool | Unset):  Default: False.
        is_secure (bool | Unset):  Default: False.
    """

    name: str
    target_url: str
    event_types: list[str] | Unset = UNSET
    is_active: bool | Unset = False
    is_secure: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        target_url = self.target_url

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        is_active = self.is_active

        is_secure = self.is_secure

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "target_url": target_url,
            }
        )
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_secure is not UNSET:
            field_dict["is_secure"] = is_secure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        target_url = d.pop("target_url")

        event_types = cast(list[str], d.pop("event_types", UNSET))

        is_active = d.pop("is_active", UNSET)

        is_secure = d.pop("is_secure", UNSET)

        add_webhook = cls(
            name=name,
            target_url=target_url,
            event_types=event_types,
            is_active=is_active,
            is_secure=is_secure,
        )

        add_webhook.additional_properties = d
        return add_webhook

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
