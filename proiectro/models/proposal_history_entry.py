from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="ProposalHistoryEntry")


@_attrs_define
class ProposalHistoryEntry:
    """Single history entry for a proposal stage

    Attributes:
        stage_name (str):
        stage_type (str):
        entry_datetime (datetime.datetime):
        exit_datetime (datetime.datetime | None):
        duration_days (int | None):
        duration_hours (int | None):
        member_name (str):
        member_email (str):
        note (None | str):
        is_current (bool):
    """

    stage_name: str
    stage_type: str
    entry_datetime: datetime.datetime
    exit_datetime: datetime.datetime | None
    duration_days: int | None
    duration_hours: int | None
    member_name: str
    member_email: str
    note: None | str
    is_current: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_name = self.stage_name

        stage_type = self.stage_type

        entry_datetime = self.entry_datetime.isoformat()

        exit_datetime: None | str
        if isinstance(self.exit_datetime, datetime.datetime):
            exit_datetime = self.exit_datetime.isoformat()
        else:
            exit_datetime = self.exit_datetime

        duration_days: int | None
        duration_days = self.duration_days

        duration_hours: int | None
        duration_hours = self.duration_hours

        member_name = self.member_name

        member_email = self.member_email

        note: None | str
        note = self.note

        is_current = self.is_current

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_name": stage_name,
                "stage_type": stage_type,
                "entry_datetime": entry_datetime,
                "exit_datetime": exit_datetime,
                "duration_days": duration_days,
                "duration_hours": duration_hours,
                "member_name": member_name,
                "member_email": member_email,
                "note": note,
                "is_current": is_current,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage_name = d.pop("stage_name")

        stage_type = d.pop("stage_type")

        entry_datetime = isoparse(d.pop("entry_datetime"))

        def _parse_exit_datetime(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exit_datetime_type_0 = isoparse(data)

                return exit_datetime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        exit_datetime = _parse_exit_datetime(d.pop("exit_datetime"))

        def _parse_duration_days(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        duration_days = _parse_duration_days(d.pop("duration_days"))

        def _parse_duration_hours(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        duration_hours = _parse_duration_hours(d.pop("duration_hours"))

        member_name = d.pop("member_name")

        member_email = d.pop("member_email")

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        is_current = d.pop("is_current")

        proposal_history_entry = cls(
            stage_name=stage_name,
            stage_type=stage_type,
            entry_datetime=entry_datetime,
            exit_datetime=exit_datetime,
            duration_days=duration_days,
            duration_hours=duration_hours,
            member_name=member_name,
            member_email=member_email,
            note=note,
            is_current=is_current,
        )

        proposal_history_entry.additional_properties = d
        return proposal_history_entry

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
