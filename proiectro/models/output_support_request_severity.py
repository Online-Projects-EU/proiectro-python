from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OutputSupportRequestSeverity")


@_attrs_define
class OutputSupportRequestSeverity:
    """Output schema for a single support request severity

    Attributes:
        id (str):
        name (str):
        internal (bool):
        active (bool):
        sequence_no (int):
        score (int):
    """

    id: str
    name: str
    internal: bool
    active: bool
    sequence_no: int
    score: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        internal = self.internal

        active = self.active

        sequence_no = self.sequence_no

        score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "internal": internal,
                "active": active,
                "sequence_no": sequence_no,
                "score": score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        internal = d.pop("internal")

        active = d.pop("active")

        sequence_no = d.pop("sequence_no")

        score = d.pop("score")

        output_support_request_severity = cls(
            id=id,
            name=name,
            internal=internal,
            active=active,
            sequence_no=sequence_no,
            score=score,
        )

        output_support_request_severity.additional_properties = d
        return output_support_request_severity

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
