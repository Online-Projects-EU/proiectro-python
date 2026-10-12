from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditWorkResourceUsage")


@_attrs_define
class EditWorkResourceUsage:
    """
    Attributes:
        member (str):
        usage (int):
        date (str):
        booking (None | str | Unset):
        note (None | str | Unset):
    """

    member: str
    usage: int
    date: str
    booking: None | str | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member = self.member

        usage = self.usage

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
                "member": member,
                "usage": usage,
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
        member = d.pop("member")

        usage = d.pop("usage")

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

        edit_work_resource_usage = cls(
            member=member,
            usage=usage,
            date=date,
            booking=booking,
            note=note,
        )

        edit_work_resource_usage.additional_properties = d
        return edit_work_resource_usage

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
