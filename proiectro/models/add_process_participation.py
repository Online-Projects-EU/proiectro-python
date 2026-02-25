from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_process_participation_participation_type import (
    AddProcessParticipationParticipationType,
)

T = TypeVar("T", bound="AddProcessParticipation")


@_attrs_define
class AddProcessParticipation:
    """
    Attributes:
        process (str):
        role (str):
        participation_type (AddProcessParticipationParticipationType):
    """

    process: str
    role: str
    participation_type: AddProcessParticipationParticipationType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process = self.process

        role = self.role

        participation_type = self.participation_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process": process,
                "role": role,
                "participation_type": participation_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        process = d.pop("process")

        role = d.pop("role")

        participation_type = AddProcessParticipationParticipationType(
            d.pop("participation_type")
        )

        add_process_participation = cls(
            process=process,
            role=role,
            participation_type=participation_type,
        )

        add_process_participation.additional_properties = d
        return add_process_participation

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
