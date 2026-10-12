from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookCreated")


@_attrs_define
class WebhookCreated:
    """`add_webhook` answer: the new endpoint's id, and — for a secure endpoint — its
    signing secret, returned once, here only. The browser also gets it via the session
    for one-time display; an API client has no session, so this is its only chance.

        Attributes:
            response_id (str):
            success (bool):
            message (str):
            webhook_id (str):
            url (None | str | Unset):
            secret_key (None | str | Unset):
    """

    response_id: str
    success: bool
    message: str
    webhook_id: str
    url: None | str | Unset = UNSET
    secret_key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response_id = self.response_id

        success = self.success

        message = self.message

        webhook_id = self.webhook_id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        secret_key: None | str | Unset
        if isinstance(self.secret_key, Unset):
            secret_key = UNSET
        else:
            secret_key = self.secret_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response_id": response_id,
                "success": success,
                "message": message,
                "webhook_id": webhook_id,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if secret_key is not UNSET:
            field_dict["secret_key"] = secret_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        response_id = d.pop("response_id")

        success = d.pop("success")

        message = d.pop("message")

        webhook_id = d.pop("webhook_id")

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_secret_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret_key = _parse_secret_key(d.pop("secret_key", UNSET))

        webhook_created = cls(
            response_id=response_id,
            success=success,
            message=message,
            webhook_id=webhook_id,
            url=url,
            secret_key=secret_key,
        )

        webhook_created.additional_properties = d
        return webhook_created

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
