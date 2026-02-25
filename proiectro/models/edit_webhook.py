from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditWebhook")


@_attrs_define
class EditWebhook:
    """
    Attributes:
        name (None | str | Unset):
        target_url (None | str | Unset):
        event_types (list[str] | None | Unset):
        is_active (bool | None | Unset):  Default: False.
        is_secure (bool | None | Unset):  Default: False.
    """

    name: None | str | Unset = UNSET
    target_url: None | str | Unset = UNSET
    event_types: list[str] | None | Unset = UNSET
    is_active: bool | None | Unset = False
    is_secure: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        target_url: None | str | Unset
        if isinstance(self.target_url, Unset):
            target_url = UNSET
        else:
            target_url = self.target_url

        event_types: list[str] | None | Unset
        if isinstance(self.event_types, Unset):
            event_types = UNSET
        elif isinstance(self.event_types, list):
            event_types = self.event_types

        else:
            event_types = self.event_types

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        is_secure: bool | None | Unset
        if isinstance(self.is_secure, Unset):
            is_secure = UNSET
        else:
            is_secure = self.is_secure

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if target_url is not UNSET:
            field_dict["target_url"] = target_url
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_target_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_url = _parse_target_url(d.pop("target_url", UNSET))

        def _parse_event_types(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_types_type_0 = cast(list[str], data)

                return event_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        event_types = _parse_event_types(d.pop("event_types", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_is_secure(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_secure = _parse_is_secure(d.pop("is_secure", UNSET))

        edit_webhook = cls(
            name=name,
            target_url=target_url,
            event_types=event_types,
            is_active=is_active,
            is_secure=is_secure,
        )

        edit_webhook.additional_properties = d
        return edit_webhook

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
