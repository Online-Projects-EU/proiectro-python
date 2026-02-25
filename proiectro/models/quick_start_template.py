from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.quick_start_conflict import QuickStartConflict


T = TypeVar("T", bound="QuickStartTemplate")


@_attrs_define
class QuickStartTemplate:
    """A quick start template with availability status.

    Attributes:
        key (str):
        name (str):
        description (str):
        available (bool):
        conflicts (list[QuickStartConflict]):
        feature_enabled (bool):
    """

    key: str
    name: str
    description: str
    available: bool
    conflicts: list[QuickStartConflict]
    feature_enabled: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        description = self.description

        available = self.available

        conflicts = []
        for conflicts_item_data in self.conflicts:
            conflicts_item = conflicts_item_data.to_dict()
            conflicts.append(conflicts_item)

        feature_enabled = self.feature_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "description": description,
                "available": available,
                "conflicts": conflicts,
                "feature_enabled": feature_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quick_start_conflict import QuickStartConflict

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        description = d.pop("description")

        available = d.pop("available")

        conflicts = []
        _conflicts = d.pop("conflicts")
        for conflicts_item_data in _conflicts:
            conflicts_item = QuickStartConflict.from_dict(conflicts_item_data)

            conflicts.append(conflicts_item)

        feature_enabled = d.pop("feature_enabled")

        quick_start_template = cls(
            key=key,
            name=name,
            description=description,
            available=available,
            conflicts=conflicts,
            feature_enabled=feature_enabled,
        )

        quick_start_template.additional_properties = d
        return quick_start_template

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
