from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkLogItem")


@_attrs_define
class WorkLogItem:
    """
    Attributes:
        external_id (str):
        member_full_name (str):
        member_id (str):
        hours (int):
        date (str):
        note (str):
        is_deletable (bool):
        is_editable (bool):
        booking_name (None | str | Unset):
        booking_id (None | str | Unset):
    """

    external_id: str
    member_full_name: str
    member_id: str
    hours: int
    date: str
    note: str
    is_deletable: bool
    is_editable: bool
    booking_name: None | str | Unset = UNSET
    booking_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        member_full_name = self.member_full_name

        member_id = self.member_id

        hours = self.hours

        date = self.date

        note = self.note

        is_deletable = self.is_deletable

        is_editable = self.is_editable

        booking_name: None | str | Unset
        if isinstance(self.booking_name, Unset):
            booking_name = UNSET
        else:
            booking_name = self.booking_name

        booking_id: None | str | Unset
        if isinstance(self.booking_id, Unset):
            booking_id = UNSET
        else:
            booking_id = self.booking_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "member_full_name": member_full_name,
                "member_id": member_id,
                "hours": hours,
                "date": date,
                "note": note,
                "is_deletable": is_deletable,
                "is_editable": is_editable,
            }
        )
        if booking_name is not UNSET:
            field_dict["booking_name"] = booking_name
        if booking_id is not UNSET:
            field_dict["booking_id"] = booking_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_id = d.pop("external_id")

        member_full_name = d.pop("member_full_name")

        member_id = d.pop("member_id")

        hours = d.pop("hours")

        date = d.pop("date")

        note = d.pop("note")

        is_deletable = d.pop("is_deletable")

        is_editable = d.pop("is_editable")

        def _parse_booking_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_name = _parse_booking_name(d.pop("booking_name", UNSET))

        def _parse_booking_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_id = _parse_booking_id(d.pop("booking_id", UNSET))

        work_log_item = cls(
            external_id=external_id,
            member_full_name=member_full_name,
            member_id=member_id,
            hours=hours,
            date=date,
            note=note,
            is_deletable=is_deletable,
            is_editable=is_editable,
            booking_name=booking_name,
            booking_id=booking_id,
        )

        work_log_item.additional_properties = d
        return work_log_item

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
