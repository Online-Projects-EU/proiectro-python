from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DependencyItem")


@_attrs_define
class DependencyItem:
    """A single work item dependency

    Attributes:
        external_id (str):
        predecessor_id (str):
        predecessor_name (str):
        predecessor_hierarchy_id (str):
        successor_id (str):
        successor_name (str):
        successor_hierarchy_id (str):
        dependency_type (str):
        dependency_type_label (str):
        lag_duration (int):
        description (str):
    """

    external_id: str
    predecessor_id: str
    predecessor_name: str
    predecessor_hierarchy_id: str
    successor_id: str
    successor_name: str
    successor_hierarchy_id: str
    dependency_type: str
    dependency_type_label: str
    lag_duration: int
    description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        predecessor_id = self.predecessor_id

        predecessor_name = self.predecessor_name

        predecessor_hierarchy_id = self.predecessor_hierarchy_id

        successor_id = self.successor_id

        successor_name = self.successor_name

        successor_hierarchy_id = self.successor_hierarchy_id

        dependency_type = self.dependency_type

        dependency_type_label = self.dependency_type_label

        lag_duration = self.lag_duration

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "predecessor_id": predecessor_id,
                "predecessor_name": predecessor_name,
                "predecessor_hierarchy_id": predecessor_hierarchy_id,
                "successor_id": successor_id,
                "successor_name": successor_name,
                "successor_hierarchy_id": successor_hierarchy_id,
                "dependency_type": dependency_type,
                "dependency_type_label": dependency_type_label,
                "lag_duration": lag_duration,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_id = d.pop("external_id")

        predecessor_id = d.pop("predecessor_id")

        predecessor_name = d.pop("predecessor_name")

        predecessor_hierarchy_id = d.pop("predecessor_hierarchy_id")

        successor_id = d.pop("successor_id")

        successor_name = d.pop("successor_name")

        successor_hierarchy_id = d.pop("successor_hierarchy_id")

        dependency_type = d.pop("dependency_type")

        dependency_type_label = d.pop("dependency_type_label")

        lag_duration = d.pop("lag_duration")

        description = d.pop("description")

        dependency_item = cls(
            external_id=external_id,
            predecessor_id=predecessor_id,
            predecessor_name=predecessor_name,
            predecessor_hierarchy_id=predecessor_hierarchy_id,
            successor_id=successor_id,
            successor_name=successor_name,
            successor_hierarchy_id=successor_hierarchy_id,
            dependency_type=dependency_type,
            dependency_type_label=dependency_type_label,
            lag_duration=lag_duration,
            description=description,
        )

        dependency_item.additional_properties = d
        return dependency_item

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
