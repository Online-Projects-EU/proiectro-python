from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputTimeOff")


@_attrs_define
class OutputTimeOff:
    """Output schema for one stretch of time off

    Attributes:
        id (str):
        member_id (str):
        member_name (str):
        exception_type (str):
        exception_type_name (str):
        start_date (datetime.date):
        end_date (datetime.date):
        days (int):
        approval_state (str):
        approval_state_name (str):
        note (None | str | Unset):
        decided_by_name (None | str | Unset):
        decided_at (datetime.datetime | None | Unset):
        decision_note (None | str | Unset):
    """

    id: str
    member_id: str
    member_name: str
    exception_type: str
    exception_type_name: str
    start_date: datetime.date
    end_date: datetime.date
    days: int
    approval_state: str
    approval_state_name: str
    note: None | str | Unset = UNSET
    decided_by_name: None | str | Unset = UNSET
    decided_at: datetime.datetime | None | Unset = UNSET
    decision_note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member_id = self.member_id

        member_name = self.member_name

        exception_type = self.exception_type

        exception_type_name = self.exception_type_name

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        days = self.days

        approval_state = self.approval_state

        approval_state_name = self.approval_state_name

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        decided_by_name: None | str | Unset
        if isinstance(self.decided_by_name, Unset):
            decided_by_name = UNSET
        else:
            decided_by_name = self.decided_by_name

        decided_at: None | str | Unset
        if isinstance(self.decided_at, Unset):
            decided_at = UNSET
        elif isinstance(self.decided_at, datetime.datetime):
            decided_at = self.decided_at.isoformat()
        else:
            decided_at = self.decided_at

        decision_note: None | str | Unset
        if isinstance(self.decision_note, Unset):
            decision_note = UNSET
        else:
            decision_note = self.decision_note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "member_id": member_id,
                "member_name": member_name,
                "exception_type": exception_type,
                "exception_type_name": exception_type_name,
                "start_date": start_date,
                "end_date": end_date,
                "days": days,
                "approval_state": approval_state,
                "approval_state_name": approval_state_name,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if decided_by_name is not UNSET:
            field_dict["decided_by_name"] = decided_by_name
        if decided_at is not UNSET:
            field_dict["decided_at"] = decided_at
        if decision_note is not UNSET:
            field_dict["decision_note"] = decision_note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        member_id = d.pop("member_id")

        member_name = d.pop("member_name")

        exception_type = d.pop("exception_type")

        exception_type_name = d.pop("exception_type_name")

        start_date = isoparse(d.pop("start_date")).date()

        end_date = isoparse(d.pop("end_date")).date()

        days = d.pop("days")

        approval_state = d.pop("approval_state")

        approval_state_name = d.pop("approval_state_name")

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_decided_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decided_by_name = _parse_decided_by_name(d.pop("decided_by_name", UNSET))

        def _parse_decided_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                decided_at_type_0 = isoparse(data)

                return decided_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        decided_at = _parse_decided_at(d.pop("decided_at", UNSET))

        def _parse_decision_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decision_note = _parse_decision_note(d.pop("decision_note", UNSET))

        output_time_off = cls(
            id=id,
            member_id=member_id,
            member_name=member_name,
            exception_type=exception_type,
            exception_type_name=exception_type_name,
            start_date=start_date,
            end_date=end_date,
            days=days,
            approval_state=approval_state,
            approval_state_name=approval_state_name,
            note=note,
            decided_by_name=decided_by_name,
            decided_at=decided_at,
            decision_note=decision_note,
        )

        output_time_off.additional_properties = d
        return output_time_off

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
