from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputStageHistoryEntry")


@_attrs_define
class OutputStageHistoryEntry:
    """
    Attributes:
        process_name (str):
        stage_name (str):
        stage_type (str):
        entered_at (datetime.datetime):
        exited_at (datetime.datetime | None | Unset):
        duration_days (int | None | Unset):
        duration_hours (int | None | Unset):
        moved_by_name (None | str | Unset):
        notes (None | str | Unset):
        approval_action (None | str | Unset):
        approval_reason (None | str | Unset):
        is_current (bool | Unset):  Default: False.
    """

    process_name: str
    stage_name: str
    stage_type: str
    entered_at: datetime.datetime
    exited_at: datetime.datetime | None | Unset = UNSET
    duration_days: int | None | Unset = UNSET
    duration_hours: int | None | Unset = UNSET
    moved_by_name: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    approval_action: None | str | Unset = UNSET
    approval_reason: None | str | Unset = UNSET
    is_current: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_name = self.process_name

        stage_name = self.stage_name

        stage_type = self.stage_type

        entered_at = self.entered_at.isoformat()

        exited_at: None | str | Unset
        if isinstance(self.exited_at, Unset):
            exited_at = UNSET
        elif isinstance(self.exited_at, datetime.datetime):
            exited_at = self.exited_at.isoformat()
        else:
            exited_at = self.exited_at

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

        moved_by_name: None | str | Unset
        if isinstance(self.moved_by_name, Unset):
            moved_by_name = UNSET
        else:
            moved_by_name = self.moved_by_name

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        approval_action: None | str | Unset
        if isinstance(self.approval_action, Unset):
            approval_action = UNSET
        else:
            approval_action = self.approval_action

        approval_reason: None | str | Unset
        if isinstance(self.approval_reason, Unset):
            approval_reason = UNSET
        else:
            approval_reason = self.approval_reason

        is_current = self.is_current

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process_name": process_name,
                "stage_name": stage_name,
                "stage_type": stage_type,
                "entered_at": entered_at,
            }
        )
        if exited_at is not UNSET:
            field_dict["exited_at"] = exited_at
        if duration_days is not UNSET:
            field_dict["duration_days"] = duration_days
        if duration_hours is not UNSET:
            field_dict["duration_hours"] = duration_hours
        if moved_by_name is not UNSET:
            field_dict["moved_by_name"] = moved_by_name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if approval_action is not UNSET:
            field_dict["approval_action"] = approval_action
        if approval_reason is not UNSET:
            field_dict["approval_reason"] = approval_reason
        if is_current is not UNSET:
            field_dict["is_current"] = is_current

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        process_name = d.pop("process_name")

        stage_name = d.pop("stage_name")

        stage_type = d.pop("stage_type")

        entered_at = isoparse(d.pop("entered_at"))

        def _parse_exited_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                exited_at_type_0 = isoparse(data)

                return exited_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        exited_at = _parse_exited_at(d.pop("exited_at", UNSET))

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

        def _parse_moved_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        moved_by_name = _parse_moved_by_name(d.pop("moved_by_name", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_approval_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approval_action = _parse_approval_action(d.pop("approval_action", UNSET))

        def _parse_approval_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approval_reason = _parse_approval_reason(d.pop("approval_reason", UNSET))

        is_current = d.pop("is_current", UNSET)

        output_stage_history_entry = cls(
            process_name=process_name,
            stage_name=stage_name,
            stage_type=stage_type,
            entered_at=entered_at,
            exited_at=exited_at,
            duration_days=duration_days,
            duration_hours=duration_hours,
            moved_by_name=moved_by_name,
            notes=notes,
            approval_action=approval_action,
            approval_reason=approval_reason,
            is_current=is_current,
        )

        output_stage_history_entry.additional_properties = d
        return output_stage_history_entry

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
