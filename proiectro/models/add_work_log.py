from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddWorkLog")


@_attrs_define
class AddWorkLog:
    """
    Attributes:
        work_item (str):
        project (str):
        member (str):
        hours (int):
        date (str):
        booking (None | str | Unset):
        note (None | str | Unset):
    """

    work_item: str
    project: str
    member: str
    hours: int
    date: str
    booking: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_item = self.work_item

        project = self.project

        member = self.member

        hours = self.hours

        date = self.date

        booking: None | str | Unset
        if isinstance(self.booking, Unset):
            booking = UNSET
        else:
            booking = self.booking

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "work_item": work_item,
                "project": project,
                "member": member,
                "hours": hours,
                "date": date,
            }
        )
        if booking is not UNSET:
            field_dict["booking"] = booking
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        work_item = d.pop("work_item")

        project = d.pop("project")

        member = d.pop("member")

        hours = d.pop("hours")

        date = d.pop("date")

        def _parse_booking(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking = _parse_booking(d.pop("booking", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        add_work_log = cls(
            work_item=work_item,
            project=project,
            member=member,
            hours=hours,
            date=date,
            booking=booking,
            note=note,
        )

        add_work_log.additional_properties = d
        return add_work_log

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
