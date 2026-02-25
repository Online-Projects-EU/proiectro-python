from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_support_request_status_lifecycle import (
    EditSupportRequestStatusLifecycle,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditSupportRequestStatus")


@_attrs_define
class EditSupportRequestStatus:
    """Input schema for editing a support request status

    Attributes:
        name (str):
        lifecycle (EditSupportRequestStatusLifecycle):
        internal (bool | None | Unset):  Default: False.
        active (bool | None | Unset):  Default: False.
        sequence_no (int | None | Unset):  Default: 1.
    """

    name: str
    lifecycle: EditSupportRequestStatusLifecycle
    internal: bool | None | Unset = False
    active: bool | None | Unset = False
    sequence_no: int | None | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        lifecycle = self.lifecycle.value

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "lifecycle": lifecycle,
            }
        )
        if internal is not UNSET:
            field_dict["internal"] = internal
        if active is not UNSET:
            field_dict["active"] = active
        if sequence_no is not UNSET:
            field_dict["sequence_no"] = sequence_no

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        lifecycle = EditSupportRequestStatusLifecycle(d.pop("lifecycle"))

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

        edit_support_request_status = cls(
            name=name,
            lifecycle=lifecycle,
            internal=internal,
            active=active,
            sequence_no=sequence_no,
        )

        edit_support_request_status.additional_properties = d
        return edit_support_request_status

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
