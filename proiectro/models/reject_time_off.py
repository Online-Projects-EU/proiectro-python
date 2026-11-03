from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RejectTimeOff")


@_attrs_define
class RejectTimeOff:
    """Input schema for turning down a time off request

    Attributes:
        decision_note (None | str | Unset):
    """

    decision_note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        decision_note: None | str | Unset
        if isinstance(self.decision_note, Unset):
            decision_note = UNSET
        else:
            decision_note = self.decision_note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if decision_note is not UNSET:
            field_dict["decision_note"] = decision_note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_decision_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decision_note = _parse_decision_note(d.pop("decision_note", UNSET))

        reject_time_off = cls(
            decision_note=decision_note,
        )

        reject_time_off.additional_properties = d
        return reject_time_off

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
