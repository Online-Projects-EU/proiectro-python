from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="InboundMeetingSummary")


@_attrs_define
class InboundMeetingSummary:
    """
    Attributes:
        start_at (datetime.datetime):
        end_at (datetime.datetime):
        state (str):
        state_label (str):
    """

    start_at: datetime.datetime
    end_at: datetime.datetime
    state: str
    state_label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_at = self.start_at.isoformat()

        end_at = self.end_at.isoformat()

        state = self.state

        state_label = self.state_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_at": start_at,
                "end_at": end_at,
                "state": state,
                "state_label": state_label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_at = isoparse(d.pop("start_at"))

        end_at = isoparse(d.pop("end_at"))

        state = d.pop("state")

        state_label = d.pop("state_label")

        inbound_meeting_summary = cls(
            start_at=start_at,
            end_at=end_at,
            state=state,
            state_label=state_label,
        )

        inbound_meeting_summary.additional_properties = d
        return inbound_meeting_summary

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
