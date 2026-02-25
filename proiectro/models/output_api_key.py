from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputApiKey")


@_attrs_define
class OutputApiKey:
    """API Key information

    Attributes:
        external_id_str (str):
        name (str):
        key_prefix (str):
        is_active (bool):
        is_create (bool):
        is_read (bool):
        is_update (bool):
        is_delete (bool):
        created_at (datetime.datetime):
        description (None | str | Unset):
        expires_at (datetime.datetime | None | Unset):
        last_used_at (datetime.datetime | None | Unset):
        last_used_ip (None | str | Unset):
    """

    external_id_str: str
    name: str
    key_prefix: str
    is_active: bool
    is_create: bool
    is_read: bool
    is_update: bool
    is_delete: bool
    created_at: datetime.datetime
    description: None | str | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    last_used_at: datetime.datetime | None | Unset = UNSET
    last_used_ip: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id_str = self.external_id_str

        name = self.name

        key_prefix = self.key_prefix

        is_active = self.is_active

        is_create = self.is_create

        is_read = self.is_read

        is_update = self.is_update

        is_delete = self.is_delete

        created_at = self.created_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        last_used_at: None | str | Unset
        if isinstance(self.last_used_at, Unset):
            last_used_at = UNSET
        elif isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        last_used_ip: None | str | Unset
        if isinstance(self.last_used_ip, Unset):
            last_used_ip = UNSET
        else:
            last_used_ip = self.last_used_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id_str": external_id_str,
                "name": name,
                "key_prefix": key_prefix,
                "is_active": is_active,
                "is_create": is_create,
                "is_read": is_read,
                "is_update": is_update,
                "is_delete": is_delete,
                "created_at": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if last_used_ip is not UNSET:
            field_dict["last_used_ip"] = last_used_ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_id_str = d.pop("external_id_str")

        name = d.pop("name")

        key_prefix = d.pop("key_prefix")

        is_active = d.pop("is_active")

        is_create = d.pop("is_create")

        is_read = d.pop("is_read")

        is_update = d.pop("is_update")

        is_delete = d.pop("is_delete")

        created_at = isoparse(d.pop("created_at"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_last_used_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = isoparse(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at", UNSET))

        def _parse_last_used_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_used_ip = _parse_last_used_ip(d.pop("last_used_ip", UNSET))

        output_api_key = cls(
            external_id_str=external_id_str,
            name=name,
            key_prefix=key_prefix,
            is_active=is_active,
            is_create=is_create,
            is_read=is_read,
            is_update=is_update,
            is_delete=is_delete,
            created_at=created_at,
            description=description,
            expires_at=expires_at,
            last_used_at=last_used_at,
            last_used_ip=last_used_ip,
        )

        output_api_key.additional_properties = d
        return output_api_key

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
