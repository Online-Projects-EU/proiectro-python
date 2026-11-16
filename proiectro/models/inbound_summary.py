from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inbound_item_summary import InboundItemSummary
    from ..models.inbound_meeting_summary import InboundMeetingSummary


T = TypeVar("T", bound="InboundSummary")


@_attrs_define
class InboundSummary:
    """What a public surface added to an activity (PUBLIC_INBOUND.md 4.6): where it came from, the
    catalog items picked, the form answers and the meeting asked for. The text itself is the note.

        Attributes:
            channel (str):
            channel_label (str):
            form_title (None | str | Unset):
            items (list[InboundItemSummary] | Unset):
            form_submission_id (None | str | Unset):
            meeting (InboundMeetingSummary | None | Unset):
    """

    channel: str
    channel_label: str
    form_title: None | str | Unset = UNSET
    items: list[InboundItemSummary] | Unset = UNSET
    form_submission_id: None | str | Unset = UNSET
    meeting: InboundMeetingSummary | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.inbound_meeting_summary import InboundMeetingSummary

        channel = self.channel

        channel_label = self.channel_label

        form_title: None | str | Unset
        if isinstance(self.form_title, Unset):
            form_title = UNSET
        else:
            form_title = self.form_title

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        form_submission_id: None | str | Unset
        if isinstance(self.form_submission_id, Unset):
            form_submission_id = UNSET
        else:
            form_submission_id = self.form_submission_id

        meeting: dict[str, Any] | None | Unset
        if isinstance(self.meeting, Unset):
            meeting = UNSET
        elif isinstance(self.meeting, InboundMeetingSummary):
            meeting = self.meeting.to_dict()
        else:
            meeting = self.meeting

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel": channel,
                "channel_label": channel_label,
            }
        )
        if form_title is not UNSET:
            field_dict["form_title"] = form_title
        if items is not UNSET:
            field_dict["items"] = items
        if form_submission_id is not UNSET:
            field_dict["form_submission_id"] = form_submission_id
        if meeting is not UNSET:
            field_dict["meeting"] = meeting

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inbound_item_summary import InboundItemSummary
        from ..models.inbound_meeting_summary import InboundMeetingSummary

        d = dict(src_dict)
        channel = d.pop("channel")

        channel_label = d.pop("channel_label")

        def _parse_form_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form_title = _parse_form_title(d.pop("form_title", UNSET))

        _items = d.pop("items", UNSET)
        items: list[InboundItemSummary] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = InboundItemSummary.from_dict(items_item_data)

                items.append(items_item)

        def _parse_form_submission_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form_submission_id = _parse_form_submission_id(
            d.pop("form_submission_id", UNSET)
        )

        def _parse_meeting(data: object) -> InboundMeetingSummary | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meeting_type_0 = InboundMeetingSummary.from_dict(data)

                return meeting_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InboundMeetingSummary | None | Unset, data)

        meeting = _parse_meeting(d.pop("meeting", UNSET))

        inbound_summary = cls(
            channel=channel,
            channel_label=channel_label,
            form_title=form_title,
            items=items,
            form_submission_id=form_submission_id,
            meeting=meeting,
        )

        inbound_summary.additional_properties = d
        return inbound_summary

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
