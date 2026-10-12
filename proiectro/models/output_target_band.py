from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OutputTargetBand")


@_attrs_define
class OutputTargetBand:
    """
    Attributes:
        id (str):
        name (str):
        threshold_percent (float | str):
        sequence_no (int):
    """

    id: str
    name: str
    threshold_percent: float | str
    sequence_no: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        threshold_percent: float | str
        threshold_percent = self.threshold_percent

        sequence_no = self.sequence_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "threshold_percent": threshold_percent,
                "sequence_no": sequence_no,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_threshold_percent(data: object) -> float | str:
            return cast(float | str, data)

        threshold_percent = _parse_threshold_percent(d.pop("threshold_percent"))

        sequence_no = d.pop("sequence_no")

        output_target_band = cls(
            id=id,
            name=name,
            threshold_percent=threshold_percent,
            sequence_no=sequence_no,
        )

        output_target_band.additional_properties = d
        return output_target_band

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
