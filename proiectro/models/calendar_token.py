from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CalendarToken")


@_attrs_define
class CalendarToken:
    """Calendar subscription token data

    Attributes:
        id (str):
        feed_type (str):
        entity_id (str):
        entity_name (str):
        feed_url (str):
        last_accessed (datetime.datetime | None):
    """

    id: str
    feed_type: str
    entity_id: str
    entity_name: str
    feed_url: str
    last_accessed: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        feed_type = self.feed_type

        entity_id = self.entity_id

        entity_name = self.entity_name

        feed_url = self.feed_url

        last_accessed: None | str
        if isinstance(self.last_accessed, datetime.datetime):
            last_accessed = self.last_accessed.isoformat()
        else:
            last_accessed = self.last_accessed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "feed_type": feed_type,
                "entity_id": entity_id,
                "entity_name": entity_name,
                "feed_url": feed_url,
                "last_accessed": last_accessed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        feed_type = d.pop("feed_type")

        entity_id = d.pop("entity_id")

        entity_name = d.pop("entity_name")

        feed_url = d.pop("feed_url")

        def _parse_last_accessed(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_accessed_type_0 = isoparse(data)

                return last_accessed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_accessed = _parse_last_accessed(d.pop("last_accessed"))

        calendar_token = cls(
            id=id,
            feed_type=feed_type,
            entity_id=entity_id,
            entity_name=entity_name,
            feed_url=feed_url,
            last_accessed=last_accessed,
        )

        calendar_token.additional_properties = d
        return calendar_token

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
