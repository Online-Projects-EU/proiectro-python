from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateCalendarToken")


@_attrs_define
class CreateCalendarToken:
    """Input schema for creating a calendar subscription token

    Attributes:
        feed_type (str):
        entity_id (str):
    """

    feed_type: str
    entity_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feed_type = self.feed_type

        entity_id = self.entity_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feed_type": feed_type,
                "entity_id": entity_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feed_type = d.pop("feed_type")

        entity_id = d.pop("entity_id")

        create_calendar_token = cls(
            feed_type=feed_type,
            entity_id=entity_id,
        )

        create_calendar_token.additional_properties = d
        return create_calendar_token

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
