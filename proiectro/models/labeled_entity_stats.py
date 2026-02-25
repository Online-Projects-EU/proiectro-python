from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LabeledEntityStats")


@_attrs_define
class LabeledEntityStats:
    """
    Attributes:
        entity_name (str):
        labeled_count (int):
        total_count (int):
        percentage (int):
    """

    entity_name: str
    labeled_count: int
    total_count: int
    percentage: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_name = self.entity_name

        labeled_count = self.labeled_count

        total_count = self.total_count

        percentage = self.percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity_name": entity_name,
                "labeled_count": labeled_count,
                "total_count": total_count,
                "percentage": percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_name = d.pop("entity_name")

        labeled_count = d.pop("labeled_count")

        total_count = d.pop("total_count")

        percentage = d.pop("percentage")

        labeled_entity_stats = cls(
            entity_name=entity_name,
            labeled_count=labeled_count,
            total_count=total_count,
            percentage=percentage,
        )

        labeled_entity_stats.additional_properties = d
        return labeled_entity_stats

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
