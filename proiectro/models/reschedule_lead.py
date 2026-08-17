from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="RescheduleLead")



@_attrs_define
class RescheduleLead:
    """ 
        Attributes:
            updated_at (datetime.datetime):
            next_action_at (None | str | Unset):
            next_action_channel (None | str | Unset):  Default: ''.
            next_action_note (None | str | Unset):  Default: ''.
     """

    updated_at: datetime.datetime
    next_action_at: None | str | Unset = UNSET
    next_action_channel: None | str | Unset = ''
    next_action_note: None | str | Unset = ''
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        updated_at = self.updated_at.isoformat()

        next_action_at: None | str | Unset
        if isinstance(self.next_action_at, Unset):
            next_action_at = UNSET
        else:
            next_action_at = self.next_action_at

        next_action_channel: None | str | Unset
        if isinstance(self.next_action_channel, Unset):
            next_action_channel = UNSET
        else:
            next_action_channel = self.next_action_channel

        next_action_note: None | str | Unset
        if isinstance(self.next_action_note, Unset):
            next_action_note = UNSET
        else:
            next_action_note = self.next_action_note


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "updated_at": updated_at,
        })
        if next_action_at is not UNSET:
            field_dict["next_action_at"] = next_action_at
        if next_action_channel is not UNSET:
            field_dict["next_action_channel"] = next_action_channel
        if next_action_note is not UNSET:
            field_dict["next_action_note"] = next_action_note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        updated_at = isoparse(d.pop("updated_at"))




        def _parse_next_action_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_action_at = _parse_next_action_at(d.pop("next_action_at", UNSET))


        def _parse_next_action_channel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_action_channel = _parse_next_action_channel(d.pop("next_action_channel", UNSET))


        def _parse_next_action_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_action_note = _parse_next_action_note(d.pop("next_action_note", UNSET))


        reschedule_lead = cls(
            updated_at=updated_at,
            next_action_at=next_action_at,
            next_action_channel=next_action_channel,
            next_action_note=next_action_note,
        )


        reschedule_lead.additional_properties = d
        return reschedule_lead

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
