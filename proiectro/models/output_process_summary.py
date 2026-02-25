from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputProcessSummary")


@_attrs_define
class OutputProcessSummary:
    """
    Attributes:
        id (str):
        name (str):
        total_items (int | Unset):  Default: 0.
        input_items (int | Unset):  Default: 0.
        pending_approval (int | Unset):  Default: 0.
    """

    id: str
    name: str
    total_items: int | Unset = 0
    input_items: int | Unset = 0
    pending_approval: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        total_items = self.total_items

        input_items = self.input_items

        pending_approval = self.pending_approval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if total_items is not UNSET:
            field_dict["total_items"] = total_items
        if input_items is not UNSET:
            field_dict["input_items"] = input_items
        if pending_approval is not UNSET:
            field_dict["pending_approval"] = pending_approval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        total_items = d.pop("total_items", UNSET)

        input_items = d.pop("input_items", UNSET)

        pending_approval = d.pop("pending_approval", UNSET)

        output_process_summary = cls(
            id=id,
            name=name,
            total_items=total_items,
            input_items=input_items,
            pending_approval=pending_approval,
        )

        output_process_summary.additional_properties = d
        return output_process_summary

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
