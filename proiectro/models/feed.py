from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feed_event import FeedEvent
    from ..models.feed_reactions import FeedReactions


T = TypeVar("T", bound="Feed")


@_attrs_define
class Feed:
    """
    Attributes:
        events (list[FeedEvent]):
        reactions (FeedReactions):
        per_page (int):
        next_page (int):
        can_post (bool | Unset):  Default: False.
    """

    events: list[FeedEvent]
    reactions: FeedReactions
    per_page: int
    next_page: int
    can_post: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        reactions = self.reactions.to_dict()

        per_page = self.per_page

        next_page = self.next_page

        can_post = self.can_post

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "reactions": reactions,
                "per_page": per_page,
                "next_page": next_page,
            }
        )
        if can_post is not UNSET:
            field_dict["can_post"] = can_post

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feed_event import FeedEvent
        from ..models.feed_reactions import FeedReactions

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = FeedEvent.from_dict(events_item_data)

            events.append(events_item)

        reactions = FeedReactions.from_dict(d.pop("reactions"))

        per_page = d.pop("per_page")

        next_page = d.pop("next_page")

        can_post = d.pop("can_post", UNSET)

        feed = cls(
            events=events,
            reactions=reactions,
            per_page=per_page,
            next_page=next_page,
            can_post=can_post,
        )

        feed.additional_properties = d
        return feed

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
