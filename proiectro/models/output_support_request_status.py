from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputSupportRequestStatus")


@_attrs_define
class OutputSupportRequestStatus:
    """Output schema for a single support request status

    Attributes:
        id (str):
        name (str):
        internal (bool):
        active (bool):
        sequence_no (int):
        lifecycle (None | str | Unset):
        lifecycle_display (None | str | Unset):
    """

    id: str
    name: str
    internal: bool
    active: bool
    sequence_no: int
    lifecycle: None | str | Unset = UNSET
    lifecycle_display: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        internal = self.internal

        active = self.active

        sequence_no = self.sequence_no

        lifecycle: None | str | Unset
        if isinstance(self.lifecycle, Unset):
            lifecycle = UNSET
        else:
            lifecycle = self.lifecycle

        lifecycle_display: None | str | Unset
        if isinstance(self.lifecycle_display, Unset):
            lifecycle_display = UNSET
        else:
            lifecycle_display = self.lifecycle_display

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "internal": internal,
                "active": active,
                "sequence_no": sequence_no,
            }
        )
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if lifecycle_display is not UNSET:
            field_dict["lifecycle_display"] = lifecycle_display

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        internal = d.pop("internal")

        active = d.pop("active")

        sequence_no = d.pop("sequence_no")

        def _parse_lifecycle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lifecycle = _parse_lifecycle(d.pop("lifecycle", UNSET))

        def _parse_lifecycle_display(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lifecycle_display = _parse_lifecycle_display(d.pop("lifecycle_display", UNSET))

        output_support_request_status = cls(
            id=id,
            name=name,
            internal=internal,
            active=active,
            sequence_no=sequence_no,
            lifecycle=lifecycle,
            lifecycle_display=lifecycle_display,
        )

        output_support_request_status.additional_properties = d
        return output_support_request_status

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
