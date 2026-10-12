from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputSupportRequestQueue")


@_attrs_define
class OutputSupportRequestQueue:
    """Output schema for a single support request queue

    Attributes:
        id (str):
        name (str):
        internal (bool):
        active (bool):
        sequence_no (int):
        automatically_assign (bool):
        owner_role_id (None | str | Unset):
        owner_role_name (None | str | Unset):
        open_count (int | Unset):  Default: 0.
        unassigned_count (int | Unset):  Default: 0.
    """

    id: str
    name: str
    internal: bool
    active: bool
    sequence_no: int
    automatically_assign: bool
    owner_role_id: None | str | Unset = UNSET
    owner_role_name: None | str | Unset = UNSET
    open_count: int | Unset = 0
    unassigned_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        internal = self.internal

        active = self.active

        sequence_no = self.sequence_no

        automatically_assign = self.automatically_assign

        owner_role_id: None | str | Unset
        if isinstance(self.owner_role_id, Unset):
            owner_role_id = UNSET
        else:
            owner_role_id = self.owner_role_id

        owner_role_name: None | str | Unset
        if isinstance(self.owner_role_name, Unset):
            owner_role_name = UNSET
        else:
            owner_role_name = self.owner_role_name

        open_count = self.open_count

        unassigned_count = self.unassigned_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "internal": internal,
                "active": active,
                "sequence_no": sequence_no,
                "automatically_assign": automatically_assign,
            }
        )
        if owner_role_id is not UNSET:
            field_dict["owner_role_id"] = owner_role_id
        if owner_role_name is not UNSET:
            field_dict["owner_role_name"] = owner_role_name
        if open_count is not UNSET:
            field_dict["open_count"] = open_count
        if unassigned_count is not UNSET:
            field_dict["unassigned_count"] = unassigned_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        internal = d.pop("internal")

        active = d.pop("active")

        sequence_no = d.pop("sequence_no")

        automatically_assign = d.pop("automatically_assign")

        def _parse_owner_role_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_role_id = _parse_owner_role_id(d.pop("owner_role_id", UNSET))

        def _parse_owner_role_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_role_name = _parse_owner_role_name(d.pop("owner_role_name", UNSET))

        open_count = d.pop("open_count", UNSET)

        unassigned_count = d.pop("unassigned_count", UNSET)

        output_support_request_queue = cls(
            id=id,
            name=name,
            internal=internal,
            active=active,
            sequence_no=sequence_no,
            automatically_assign=automatically_assign,
            owner_role_id=owner_role_id,
            owner_role_name=owner_role_name,
            open_count=open_count,
            unassigned_count=unassigned_count,
        )

        output_support_request_queue.additional_properties = d
        return output_support_request_queue

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
