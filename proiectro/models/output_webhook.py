from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputWebhook")


@_attrs_define
class OutputWebhook:
    """
    Attributes:
        id (str):
        name (str):
        target_url (str):
        event_types (list[str]):
        is_active (bool):
        is_secure (bool):
        created_at (str):
        created_by (None | str | Unset):
        last_delivery_status (int | None | Unset):
        failure_count (int | Unset):  Default: 0.
    """

    id: str
    name: str
    target_url: str
    event_types: list[str]
    is_active: bool
    is_secure: bool
    created_at: str
    created_by: None | str | Unset = UNSET
    last_delivery_status: int | None | Unset = UNSET
    failure_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        target_url = self.target_url

        event_types = self.event_types

        is_active = self.is_active

        is_secure = self.is_secure

        created_at = self.created_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        last_delivery_status: int | None | Unset
        if isinstance(self.last_delivery_status, Unset):
            last_delivery_status = UNSET
        else:
            last_delivery_status = self.last_delivery_status

        failure_count = self.failure_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "target_url": target_url,
                "event_types": event_types,
                "is_active": is_active,
                "is_secure": is_secure,
                "created_at": created_at,
            }
        )
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if last_delivery_status is not UNSET:
            field_dict["last_delivery_status"] = last_delivery_status
        if failure_count is not UNSET:
            field_dict["failure_count"] = failure_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        target_url = d.pop("target_url")

        event_types = cast(list[str], d.pop("event_types"))

        is_active = d.pop("is_active")

        is_secure = d.pop("is_secure")

        created_at = d.pop("created_at")

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_last_delivery_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_delivery_status = _parse_last_delivery_status(
            d.pop("last_delivery_status", UNSET)
        )

        failure_count = d.pop("failure_count", UNSET)

        output_webhook = cls(
            id=id,
            name=name,
            target_url=target_url,
            event_types=event_types,
            is_active=is_active,
            is_secure=is_secure,
            created_at=created_at,
            created_by=created_by,
            last_delivery_status=last_delivery_status,
            failure_count=failure_count,
        )

        output_webhook.additional_properties = d
        return output_webhook

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
