from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddSupportRequestSeverity")


@_attrs_define
class AddSupportRequestSeverity:
    """Input schema for adding a support request severity

    Attributes:
        name (str):
        internal (bool | None | Unset):  Default: False.
        active (bool | None | Unset):  Default: False.
        sequence_no (int | None | Unset):  Default: 1.
        score (int | Unset):  Default: 1.
    """

    name: str
    internal: bool | None | Unset = False
    active: bool | None | Unset = False
    sequence_no: int | None | Unset = 1
    score: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        internal: bool | None | Unset
        if isinstance(self.internal, Unset):
            internal = UNSET
        else:
            internal = self.internal

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        sequence_no: int | None | Unset
        if isinstance(self.sequence_no, Unset):
            sequence_no = UNSET
        else:
            sequence_no = self.sequence_no

        score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if internal is not UNSET:
            field_dict["internal"] = internal
        if active is not UNSET:
            field_dict["active"] = active
        if sequence_no is not UNSET:
            field_dict["sequence_no"] = sequence_no
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_internal(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        internal = _parse_internal(d.pop("internal", UNSET))

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_sequence_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence_no = _parse_sequence_no(d.pop("sequence_no", UNSET))

        score = d.pop("score", UNSET)

        add_support_request_severity = cls(
            name=name,
            internal=internal,
            active=active,
            sequence_no=sequence_no,
            score=score,
        )

        add_support_request_severity.additional_properties = d
        return add_support_request_severity

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
