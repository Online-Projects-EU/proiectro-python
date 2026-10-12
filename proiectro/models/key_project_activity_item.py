from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KeyProjectActivityItem")


@_attrs_define
class KeyProjectActivityItem:
    """Single activity item in key project activities list

    Attributes:
        id (str):
        name (str):
        hierarchy_id (str):
        is_finished (bool):
        percent_complete (int):
    """

    id: str
    name: str
    hierarchy_id: str
    is_finished: bool
    percent_complete: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        hierarchy_id = self.hierarchy_id

        is_finished = self.is_finished

        percent_complete = self.percent_complete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "hierarchy_id": hierarchy_id,
                "is_finished": is_finished,
                "percent_complete": percent_complete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        hierarchy_id = d.pop("hierarchy_id")

        is_finished = d.pop("is_finished")

        percent_complete = d.pop("percent_complete")

        key_project_activity_item = cls(
            id=id,
            name=name,
            hierarchy_id=hierarchy_id,
            is_finished=is_finished,
            percent_complete=percent_complete,
        )

        key_project_activity_item.additional_properties = d
        return key_project_activity_item

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
