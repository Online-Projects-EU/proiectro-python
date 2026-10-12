from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AllowedChildType")


@_attrs_define
class AllowedChildType:
    """Work item type that can be added as a child based on WBS rules

    Attributes:
        work_item_type_id (str):
        name (str):
        scheduling_behaviour (str):
    """

    work_item_type_id: str
    name: str
    scheduling_behaviour: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_item_type_id = self.work_item_type_id

        name = self.name

        scheduling_behaviour = self.scheduling_behaviour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "work_item_type_id": work_item_type_id,
                "name": name,
                "scheduling_behaviour": scheduling_behaviour,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        work_item_type_id = d.pop("work_item_type_id")

        name = d.pop("name")

        scheduling_behaviour = d.pop("scheduling_behaviour")

        allowed_child_type = cls(
            work_item_type_id=work_item_type_id,
            name=name,
            scheduling_behaviour=scheduling_behaviour,
        )

        allowed_child_type.additional_properties = d
        return allowed_child_type

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
