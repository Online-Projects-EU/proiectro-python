from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_process_participation import OutputProcessParticipation


T = TypeVar("T", bound="OutputProcessParticipations")


@_attrs_define
class OutputProcessParticipations:
    """
    Attributes:
        process_id (str):
        process_name (str):
        participations (list[OutputProcessParticipation]):
    """

    process_id: str
    process_name: str
    participations: list[OutputProcessParticipation]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_id = self.process_id

        process_name = self.process_name

        participations = []
        for participations_item_data in self.participations:
            participations_item = participations_item_data.to_dict()
            participations.append(participations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process_id": process_id,
                "process_name": process_name,
                "participations": participations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_process_participation import OutputProcessParticipation

        d = dict(src_dict)
        process_id = d.pop("process_id")

        process_name = d.pop("process_name")

        participations = []
        _participations = d.pop("participations")
        for participations_item_data in _participations:
            participations_item = OutputProcessParticipation.from_dict(
                participations_item_data
            )

            participations.append(participations_item)

        output_process_participations = cls(
            process_id=process_id,
            process_name=process_name,
            participations=participations,
        )

        output_process_participations.additional_properties = d
        return output_process_participations

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
