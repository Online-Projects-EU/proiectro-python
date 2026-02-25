from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditSupportRequestQueue")


@_attrs_define
class EditSupportRequestQueue:
    """Input schema for editing a support request queue

    Attributes:
        name (str):
        internal (bool | None | Unset):  Default: False.
        active (bool | None | Unset):  Default: False.
        sequence_no (int | None | Unset):  Default: 1.
        owner_role_id (None | str | Unset):
        automatically_assign (bool | None | Unset):  Default: False.
    """

    name: str
    internal: bool | None | Unset = False
    active: bool | None | Unset = False
    sequence_no: int | None | Unset = 1
    owner_role_id: None | str | Unset = UNSET
    automatically_assign: bool | None | Unset = False
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

        owner_role_id: None | str | Unset
        if isinstance(self.owner_role_id, Unset):
            owner_role_id = UNSET
        else:
            owner_role_id = self.owner_role_id

        automatically_assign: bool | None | Unset
        if isinstance(self.automatically_assign, Unset):
            automatically_assign = UNSET
        else:
            automatically_assign = self.automatically_assign

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
        if owner_role_id is not UNSET:
            field_dict["owner_role_id"] = owner_role_id
        if automatically_assign is not UNSET:
            field_dict["automatically_assign"] = automatically_assign

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

        def _parse_owner_role_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_role_id = _parse_owner_role_id(d.pop("owner_role_id", UNSET))

        def _parse_automatically_assign(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        automatically_assign = _parse_automatically_assign(
            d.pop("automatically_assign", UNSET)
        )

        edit_support_request_queue = cls(
            name=name,
            internal=internal,
            active=active,
            sequence_no=sequence_no,
            owner_role_id=owner_role_id,
            automatically_assign=automatically_assign,
        )

        edit_support_request_queue.additional_properties = d
        return edit_support_request_queue

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
