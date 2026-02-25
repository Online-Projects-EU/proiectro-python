from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputWebhookDelivery")


@_attrs_define
class OutputWebhookDelivery:
    """
    Attributes:
        id (str):
        event_id (str):
        event_type (str):
        created_at (str):
        http_status (int | None | Unset):
        error_message (str | Unset):  Default: ''.
        attempt (int | Unset):  Default: 1.
        duration_ms (int | None | Unset):
    """

    id: str
    event_id: str
    event_type: str
    created_at: str
    http_status: int | None | Unset = UNSET
    error_message: str | Unset = ""
    attempt: int | Unset = 1
    duration_ms: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event_id = self.event_id

        event_type = self.event_type

        created_at = self.created_at

        http_status: int | None | Unset
        if isinstance(self.http_status, Unset):
            http_status = UNSET
        else:
            http_status = self.http_status

        error_message = self.error_message

        attempt = self.attempt

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "event_id": event_id,
                "event_type": event_type,
                "created_at": created_at,
            }
        )
        if http_status is not UNSET:
            field_dict["http_status"] = http_status
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if attempt is not UNSET:
            field_dict["attempt"] = attempt
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        event_id = d.pop("event_id")

        event_type = d.pop("event_type")

        created_at = d.pop("created_at")

        def _parse_http_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        http_status = _parse_http_status(d.pop("http_status", UNSET))

        error_message = d.pop("error_message", UNSET)

        attempt = d.pop("attempt", UNSET)

        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        output_webhook_delivery = cls(
            id=id,
            event_id=event_id,
            event_type=event_type,
            created_at=created_at,
            http_status=http_status,
            error_message=error_message,
            attempt=attempt,
            duration_ms=duration_ms,
        )

        output_webhook_delivery.additional_properties = d
        return output_webhook_delivery

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
