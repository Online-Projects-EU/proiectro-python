from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddMyTimeOff")


@_attrs_define
class AddMyTimeOff:
    """Input schema for asking for time off

    Attributes:
        exception_type (str):
        start_date (str):
        end_date (str):
        note (None | str | Unset):
    """

    exception_type: str
    start_date: str
    end_date: str
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exception_type = self.exception_type

        start_date = self.start_date

        end_date = self.end_date

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exception_type": exception_type,
                "start_date": start_date,
                "end_date": end_date,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exception_type = d.pop("exception_type")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        add_my_time_off = cls(
            exception_type=exception_type,
            start_date=start_date,
            end_date=end_date,
            note=note,
        )

        add_my_time_off.additional_properties = d
        return add_my_time_off

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
