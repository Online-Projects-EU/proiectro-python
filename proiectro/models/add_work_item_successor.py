from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddWorkItemSuccessor")


@_attrs_define
class AddWorkItemSuccessor:
    """Schema for adding a successor dependency to a work item

    Attributes:
        work_item_id (str):
        successor_id (str):
        dependency_type (str):
        lag_duration (int | Unset):  Default: 0.
    """

    work_item_id: str
    successor_id: str
    dependency_type: str
    lag_duration: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_item_id = self.work_item_id

        successor_id = self.successor_id

        dependency_type = self.dependency_type

        lag_duration = self.lag_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "work_item_id": work_item_id,
                "successor_id": successor_id,
                "dependency_type": dependency_type,
            }
        )
        if lag_duration is not UNSET:
            field_dict["lag_duration"] = lag_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        work_item_id = d.pop("work_item_id")

        successor_id = d.pop("successor_id")

        dependency_type = d.pop("dependency_type")

        lag_duration = d.pop("lag_duration", UNSET)

        add_work_item_successor = cls(
            work_item_id=work_item_id,
            successor_id=successor_id,
            dependency_type=dependency_type,
            lag_duration=lag_duration,
        )

        add_work_item_successor.additional_properties = d
        return add_work_item_successor

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
