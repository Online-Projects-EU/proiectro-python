from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.feed_event_content import FeedEventContent
    from ..models.feed_event_possible_reactions import FeedEventPossibleReactions


T = TypeVar("T", bound="FeedEvent")


@_attrs_define
class FeedEvent:
    """
    Attributes:
        id (str):
        is_audit (bool):
        timestamp (datetime.datetime):
        content (FeedEventContent):
        possible_reactions (FeedEventPossibleReactions):
    """

    id: str
    is_audit: bool
    timestamp: datetime.datetime
    content: FeedEventContent
    possible_reactions: FeedEventPossibleReactions
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_audit = self.is_audit

        timestamp = self.timestamp.isoformat()

        content = self.content.to_dict()

        possible_reactions = self.possible_reactions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "is_audit": is_audit,
                "timestamp": timestamp,
                "content": content,
                "possible_reactions": possible_reactions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feed_event_content import FeedEventContent
        from ..models.feed_event_possible_reactions import FeedEventPossibleReactions

        d = dict(src_dict)
        id = d.pop("id")

        is_audit = d.pop("is_audit")

        timestamp = isoparse(d.pop("timestamp"))

        content = FeedEventContent.from_dict(d.pop("content"))

        possible_reactions = FeedEventPossibleReactions.from_dict(
            d.pop("possible_reactions")
        )

        feed_event = cls(
            id=id,
            is_audit=is_audit,
            timestamp=timestamp,
            content=content,
            possible_reactions=possible_reactions,
        )

        feed_event.additional_properties = d
        return feed_event

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
