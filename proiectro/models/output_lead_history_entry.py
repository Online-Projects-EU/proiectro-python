from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.output_lead_history_entry_kind import OutputLeadHistoryEntryKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputLeadHistoryEntry")


@_attrs_define
class OutputLeadHistoryEntry:
    """Single entry in a lead's unified timeline: a status it was in, or a sales activity logged on it.

    Attributes:
        kind (OutputLeadHistoryEntryKind):
        name (str):
        type_ (str):
        entry_datetime (datetime.datetime):
        activity_icon (None | str | Unset):
        exit_datetime (datetime.datetime | None | Unset):
        duration_days (int | None | Unset):
        duration_hours (int | None | Unset):
        member_name (None | str | Unset):
        member_email (str | Unset):  Default: ''.
        note (None | str | Unset):
        is_current (bool | Unset):  Default: False.
        is_autonomous (bool | Unset):  Default: False.
    """

    kind: OutputLeadHistoryEntryKind
    name: str
    type_: str
    entry_datetime: datetime.datetime
    activity_icon: None | str | Unset = UNSET
    exit_datetime: datetime.datetime | None | Unset = UNSET
    duration_days: int | None | Unset = UNSET
    duration_hours: int | None | Unset = UNSET
    member_name: None | str | Unset = UNSET
    member_email: str | Unset = ""
    note: None | str | Unset = UNSET
    is_current: bool | Unset = False
    is_autonomous: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        name = self.name

        type_ = self.type_

        entry_datetime = self.entry_datetime.isoformat()

        activity_icon: None | str | Unset
        if isinstance(self.activity_icon, Unset):
            activity_icon = UNSET
        else:
            activity_icon = self.activity_icon

        exit_datetime: None | str | Unset
        if isinstance(self.exit_datetime, Unset):
            exit_datetime = UNSET
        elif isinstance(self.exit_datetime, datetime.datetime):
            exit_datetime = self.exit_datetime.isoformat()
        else:
            exit_datetime = self.exit_datetime

        duration_days: int | None | Unset
        if isinstance(self.duration_days, Unset):
            duration_days = UNSET
        else:
            duration_days = self.duration_days

        duration_hours: int | None | Unset
        if isinstance(self.duration_hours, Unset):
            duration_hours = UNSET
        else:
            duration_hours = self.duration_hours

        member_name: None | str | Unset
        if isinstance(self.member_name, Unset):
            member_name = UNSET
        else:
            member_name = self.member_name

        member_email = self.member_email

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        is_current = self.is_current

        is_autonomous = self.is_autonomous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "name": name,
                "type": type_,
                "entry_datetime": entry_datetime,
            }
        )
        if activity_icon is not UNSET:
            field_dict["activity_icon"] = activity_icon
        if exit_datetime is not UNSET:
            field_dict["exit_datetime"] = exit_datetime
        if duration_days is not UNSET:
            field_dict["duration_days"] = duration_days
        if duration_hours is not UNSET:
            field_dict["duration_hours"] = duration_hours
        if member_name is not UNSET:
            field_dict["member_name"] = member_name
        if member_email is not UNSET:
            field_dict["member_email"] = member_email
        if note is not UNSET:
            field_dict["note"] = note
        if is_current is not UNSET:
            field_dict["is_current"] = is_current
        if is_autonomous is not UNSET:
            field_dict["is_autonomous"] = is_autonomous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = OutputLeadHistoryEntryKind(d.pop("kind"))

        name = d.pop("name")

        type_ = d.pop("type")

        entry_datetime = isoparse(d.pop("entry_datetime"))

        def _parse_activity_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        activity_icon = _parse_activity_icon(d.pop("activity_icon", UNSET))

        def _parse_exit_datetime(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exit_datetime_type_0 = isoparse(data)

                return exit_datetime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        exit_datetime = _parse_exit_datetime(d.pop("exit_datetime", UNSET))

        def _parse_duration_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_days = _parse_duration_days(d.pop("duration_days", UNSET))

        def _parse_duration_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_hours = _parse_duration_hours(d.pop("duration_hours", UNSET))

        def _parse_member_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_name = _parse_member_name(d.pop("member_name", UNSET))

        member_email = d.pop("member_email", UNSET)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        is_current = d.pop("is_current", UNSET)

        is_autonomous = d.pop("is_autonomous", UNSET)

        output_lead_history_entry = cls(
            kind=kind,
            name=name,
            type_=type_,
            entry_datetime=entry_datetime,
            activity_icon=activity_icon,
            exit_datetime=exit_datetime,
            duration_days=duration_days,
            duration_hours=duration_hours,
            member_name=member_name,
            member_email=member_email,
            note=note,
            is_current=is_current,
            is_autonomous=is_autonomous,
        )

        output_lead_history_entry.additional_properties = d
        return output_lead_history_entry

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
