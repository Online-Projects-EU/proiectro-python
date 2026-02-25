from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SupportRequestTimelineEvent")


@_attrs_define
class SupportRequestTimelineEvent:
    """Output schema for a single timeline event or comment

    Attributes:
        timestamp (str):
        author_name (str):
        author_id (str):
        event_type (str):
        event_type_display (str):
        reason (str):
        old_status_name (None | str | Unset):
        new_status_name (None | str | Unset):
        old_assignee_name (None | str | Unset):
        new_assignee_name (None | str | Unset):
        old_queue_name (None | str | Unset):
        new_queue_name (None | str | Unset):
        is_comment (bool | Unset):  Default: False.
        comment_content (None | str | Unset):
        comment_id (None | str | Unset):
        parent_comment_id (None | str | Unset):
        edited (bool | None | Unset):
        show_to_requester (bool | None | Unset):
    """

    timestamp: str
    author_name: str
    author_id: str
    event_type: str
    event_type_display: str
    reason: str
    old_status_name: None | str | Unset = UNSET
    new_status_name: None | str | Unset = UNSET
    old_assignee_name: None | str | Unset = UNSET
    new_assignee_name: None | str | Unset = UNSET
    old_queue_name: None | str | Unset = UNSET
    new_queue_name: None | str | Unset = UNSET
    is_comment: bool | Unset = False
    comment_content: None | str | Unset = UNSET
    comment_id: None | str | Unset = UNSET
    parent_comment_id: None | str | Unset = UNSET
    edited: bool | None | Unset = UNSET
    show_to_requester: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        author_name = self.author_name

        author_id = self.author_id

        event_type = self.event_type

        event_type_display = self.event_type_display

        reason = self.reason

        old_status_name: None | str | Unset
        if isinstance(self.old_status_name, Unset):
            old_status_name = UNSET
        else:
            old_status_name = self.old_status_name

        new_status_name: None | str | Unset
        if isinstance(self.new_status_name, Unset):
            new_status_name = UNSET
        else:
            new_status_name = self.new_status_name

        old_assignee_name: None | str | Unset
        if isinstance(self.old_assignee_name, Unset):
            old_assignee_name = UNSET
        else:
            old_assignee_name = self.old_assignee_name

        new_assignee_name: None | str | Unset
        if isinstance(self.new_assignee_name, Unset):
            new_assignee_name = UNSET
        else:
            new_assignee_name = self.new_assignee_name

        old_queue_name: None | str | Unset
        if isinstance(self.old_queue_name, Unset):
            old_queue_name = UNSET
        else:
            old_queue_name = self.old_queue_name

        new_queue_name: None | str | Unset
        if isinstance(self.new_queue_name, Unset):
            new_queue_name = UNSET
        else:
            new_queue_name = self.new_queue_name

        is_comment = self.is_comment

        comment_content: None | str | Unset
        if isinstance(self.comment_content, Unset):
            comment_content = UNSET
        else:
            comment_content = self.comment_content

        comment_id: None | str | Unset
        if isinstance(self.comment_id, Unset):
            comment_id = UNSET
        else:
            comment_id = self.comment_id

        parent_comment_id: None | str | Unset
        if isinstance(self.parent_comment_id, Unset):
            parent_comment_id = UNSET
        else:
            parent_comment_id = self.parent_comment_id

        edited: bool | None | Unset
        if isinstance(self.edited, Unset):
            edited = UNSET
        else:
            edited = self.edited

        show_to_requester: bool | None | Unset
        if isinstance(self.show_to_requester, Unset):
            show_to_requester = UNSET
        else:
            show_to_requester = self.show_to_requester

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "author_name": author_name,
                "author_id": author_id,
                "event_type": event_type,
                "event_type_display": event_type_display,
                "reason": reason,
            }
        )
        if old_status_name is not UNSET:
            field_dict["old_status_name"] = old_status_name
        if new_status_name is not UNSET:
            field_dict["new_status_name"] = new_status_name
        if old_assignee_name is not UNSET:
            field_dict["old_assignee_name"] = old_assignee_name
        if new_assignee_name is not UNSET:
            field_dict["new_assignee_name"] = new_assignee_name
        if old_queue_name is not UNSET:
            field_dict["old_queue_name"] = old_queue_name
        if new_queue_name is not UNSET:
            field_dict["new_queue_name"] = new_queue_name
        if is_comment is not UNSET:
            field_dict["is_comment"] = is_comment
        if comment_content is not UNSET:
            field_dict["comment_content"] = comment_content
        if comment_id is not UNSET:
            field_dict["comment_id"] = comment_id
        if parent_comment_id is not UNSET:
            field_dict["parent_comment_id"] = parent_comment_id
        if edited is not UNSET:
            field_dict["edited"] = edited
        if show_to_requester is not UNSET:
            field_dict["show_to_requester"] = show_to_requester

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp")

        author_name = d.pop("author_name")

        author_id = d.pop("author_id")

        event_type = d.pop("event_type")

        event_type_display = d.pop("event_type_display")

        reason = d.pop("reason")

        def _parse_old_status_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_status_name = _parse_old_status_name(d.pop("old_status_name", UNSET))

        def _parse_new_status_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_status_name = _parse_new_status_name(d.pop("new_status_name", UNSET))

        def _parse_old_assignee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_assignee_name = _parse_old_assignee_name(d.pop("old_assignee_name", UNSET))

        def _parse_new_assignee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_assignee_name = _parse_new_assignee_name(d.pop("new_assignee_name", UNSET))

        def _parse_old_queue_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        old_queue_name = _parse_old_queue_name(d.pop("old_queue_name", UNSET))

        def _parse_new_queue_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_queue_name = _parse_new_queue_name(d.pop("new_queue_name", UNSET))

        is_comment = d.pop("is_comment", UNSET)

        def _parse_comment_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment_content = _parse_comment_content(d.pop("comment_content", UNSET))

        def _parse_comment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment_id = _parse_comment_id(d.pop("comment_id", UNSET))

        def _parse_parent_comment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_comment_id = _parse_parent_comment_id(d.pop("parent_comment_id", UNSET))

        def _parse_edited(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        edited = _parse_edited(d.pop("edited", UNSET))

        def _parse_show_to_requester(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_to_requester = _parse_show_to_requester(d.pop("show_to_requester", UNSET))

        support_request_timeline_event = cls(
            timestamp=timestamp,
            author_name=author_name,
            author_id=author_id,
            event_type=event_type,
            event_type_display=event_type_display,
            reason=reason,
            old_status_name=old_status_name,
            new_status_name=new_status_name,
            old_assignee_name=old_assignee_name,
            new_assignee_name=new_assignee_name,
            old_queue_name=old_queue_name,
            new_queue_name=new_queue_name,
            is_comment=is_comment,
            comment_content=comment_content,
            comment_id=comment_id,
            parent_comment_id=parent_comment_id,
            edited=edited,
            show_to_requester=show_to_requester,
        )

        support_request_timeline_event.additional_properties = d
        return support_request_timeline_event

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
