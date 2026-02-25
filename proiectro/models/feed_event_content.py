from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedEventContent")


@_attrs_define
class FeedEventContent:
    """
    Attributes:
        source (str):
        author_id (str):
        author_name (str):
        timestamp (datetime.datetime):
        title (str):
        description (str):
        author_avatar_url (None | str | Unset):
        author_email (None | str | Unset):
        author_phone (None | str | Unset):
        is_system (bool | Unset):  Default: False.
        tenant_logo_url (None | str | Unset):
    """

    source: str
    author_id: str
    author_name: str
    timestamp: datetime.datetime
    title: str
    description: str
    author_avatar_url: None | str | Unset = UNSET
    author_email: None | str | Unset = UNSET
    author_phone: None | str | Unset = UNSET
    is_system: bool | Unset = False
    tenant_logo_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        author_id = self.author_id

        author_name = self.author_name

        timestamp = self.timestamp.isoformat()

        title = self.title

        description = self.description

        author_avatar_url: None | str | Unset
        if isinstance(self.author_avatar_url, Unset):
            author_avatar_url = UNSET
        else:
            author_avatar_url = self.author_avatar_url

        author_email: None | str | Unset
        if isinstance(self.author_email, Unset):
            author_email = UNSET
        else:
            author_email = self.author_email

        author_phone: None | str | Unset
        if isinstance(self.author_phone, Unset):
            author_phone = UNSET
        else:
            author_phone = self.author_phone

        is_system = self.is_system

        tenant_logo_url: None | str | Unset
        if isinstance(self.tenant_logo_url, Unset):
            tenant_logo_url = UNSET
        else:
            tenant_logo_url = self.tenant_logo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "author_id": author_id,
                "author_name": author_name,
                "timestamp": timestamp,
                "title": title,
                "description": description,
            }
        )
        if author_avatar_url is not UNSET:
            field_dict["author_avatar_url"] = author_avatar_url
        if author_email is not UNSET:
            field_dict["author_email"] = author_email
        if author_phone is not UNSET:
            field_dict["author_phone"] = author_phone
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
        if tenant_logo_url is not UNSET:
            field_dict["tenant_logo_url"] = tenant_logo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        author_id = d.pop("author_id")

        author_name = d.pop("author_name")

        timestamp = isoparse(d.pop("timestamp"))

        title = d.pop("title")

        description = d.pop("description")

        def _parse_author_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_avatar_url = _parse_author_avatar_url(d.pop("author_avatar_url", UNSET))

        def _parse_author_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_email = _parse_author_email(d.pop("author_email", UNSET))

        def _parse_author_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_phone = _parse_author_phone(d.pop("author_phone", UNSET))

        is_system = d.pop("is_system", UNSET)

        def _parse_tenant_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_logo_url = _parse_tenant_logo_url(d.pop("tenant_logo_url", UNSET))

        feed_event_content = cls(
            source=source,
            author_id=author_id,
            author_name=author_name,
            timestamp=timestamp,
            title=title,
            description=description,
            author_avatar_url=author_avatar_url,
            author_email=author_email,
            author_phone=author_phone,
            is_system=is_system,
            tenant_logo_url=tenant_logo_url,
        )

        feed_event_content.additional_properties = d
        return feed_event_content

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
