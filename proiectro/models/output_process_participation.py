from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputProcessParticipation")


@_attrs_define
class OutputProcessParticipation:
    """
    Attributes:
        id (str):
        role_id (str):
        role_name (str):
        participation_type (str):
        participation_type_key (str | Unset):  Default: ''.
    """

    id: str
    role_id: str
    role_name: str
    participation_type: str
    participation_type_key: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        role_id = self.role_id

        role_name = self.role_name

        participation_type = self.participation_type

        participation_type_key = self.participation_type_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "role_id": role_id,
                "role_name": role_name,
                "participation_type": participation_type,
            }
        )
        if participation_type_key is not UNSET:
            field_dict["participation_type_key"] = participation_type_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        role_id = d.pop("role_id")

        role_name = d.pop("role_name")

        participation_type = d.pop("participation_type")

        participation_type_key = d.pop("participation_type_key", UNSET)

        output_process_participation = cls(
            id=id,
            role_id=role_id,
            role_name=role_name,
            participation_type=participation_type,
            participation_type_key=participation_type_key,
        )

        output_process_participation.additional_properties = d
        return output_process_participation

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
