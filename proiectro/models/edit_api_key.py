from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditApiKey")


@_attrs_define
class EditApiKey:
    """Input schema for editing an API key

    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        is_create (bool | None | Unset):  Default: False.
        is_read (bool | None | Unset):  Default: False.
        is_update (bool | None | Unset):  Default: False.
        is_delete (bool | None | Unset):  Default: False.
        expires_at (None | str | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    is_create: bool | None | Unset = False
    is_read: bool | None | Unset = False
    is_update: bool | None | Unset = False
    is_delete: bool | None | Unset = False
    expires_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_create: bool | None | Unset
        if isinstance(self.is_create, Unset):
            is_create = UNSET
        else:
            is_create = self.is_create

        is_read: bool | None | Unset
        if isinstance(self.is_read, Unset):
            is_read = UNSET
        else:
            is_read = self.is_read

        is_update: bool | None | Unset
        if isinstance(self.is_update, Unset):
            is_update = UNSET
        else:
            is_update = self.is_update

        is_delete: bool | None | Unset
        if isinstance(self.is_delete, Unset):
            is_delete = UNSET
        else:
            is_delete = self.is_delete

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_create is not UNSET:
            field_dict["is_create"] = is_create
        if is_read is not UNSET:
            field_dict["is_read"] = is_read
        if is_update is not UNSET:
            field_dict["is_update"] = is_update
        if is_delete is not UNSET:
            field_dict["is_delete"] = is_delete
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

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

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_create(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_create = _parse_is_create(d.pop("is_create", UNSET))

        def _parse_is_read(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_read = _parse_is_read(d.pop("is_read", UNSET))

        def _parse_is_update(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_update = _parse_is_update(d.pop("is_update", UNSET))

        def _parse_is_delete(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_delete = _parse_is_delete(d.pop("is_delete", UNSET))

        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        edit_api_key = cls(
            name=name,
            description=description,
            is_create=is_create,
            is_read=is_read,
            is_update=is_update,
            is_delete=is_delete,
            expires_at=expires_at,
        )

        edit_api_key.additional_properties = d
        return edit_api_key

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
