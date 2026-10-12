from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_internal_support_request_timeline_replies_map import (
        OutputInternalSupportRequestTimelineRepliesMap,
    )
    from ..models.support_request_timeline_event import SupportRequestTimelineEvent


T = TypeVar("T", bound="OutputInternalSupportRequestTimeline")


@_attrs_define
class OutputInternalSupportRequestTimeline:
    """Output schema for internal support request timeline

    Attributes:
        events (list[SupportRequestTimelineEvent]):
        event_count (int):
        support_request_id (str):
        replies_map (OutputInternalSupportRequestTimelineRepliesMap | Unset):
        status_lifecycle (str | Unset):  Default: ''.
    """

    events: list[SupportRequestTimelineEvent]
    event_count: int
    support_request_id: str
    replies_map: OutputInternalSupportRequestTimelineRepliesMap | Unset = UNSET
    status_lifecycle: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        event_count = self.event_count

        support_request_id = self.support_request_id

        replies_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.replies_map, Unset):
            replies_map = self.replies_map.to_dict()

        status_lifecycle = self.status_lifecycle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "event_count": event_count,
                "support_request_id": support_request_id,
            }
        )
        if replies_map is not UNSET:
            field_dict["replies_map"] = replies_map
        if status_lifecycle is not UNSET:
            field_dict["status_lifecycle"] = status_lifecycle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_internal_support_request_timeline_replies_map import (
            OutputInternalSupportRequestTimelineRepliesMap,
        )
        from ..models.support_request_timeline_event import SupportRequestTimelineEvent

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = SupportRequestTimelineEvent.from_dict(events_item_data)

            events.append(events_item)

        event_count = d.pop("event_count")

        support_request_id = d.pop("support_request_id")

        _replies_map = d.pop("replies_map", UNSET)
        replies_map: OutputInternalSupportRequestTimelineRepliesMap | Unset
        if isinstance(_replies_map, Unset):
            replies_map = UNSET
        else:
            replies_map = OutputInternalSupportRequestTimelineRepliesMap.from_dict(
                _replies_map
            )

        status_lifecycle = d.pop("status_lifecycle", UNSET)

        output_internal_support_request_timeline = cls(
            events=events,
            event_count=event_count,
            support_request_id=support_request_id,
            replies_map=replies_map,
            status_lifecycle=status_lifecycle,
        )

        output_internal_support_request_timeline.additional_properties = d
        return output_internal_support_request_timeline

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
