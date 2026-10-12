from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_process_assignee import OutputProcessAssignee


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
        assignable_members (list[OutputProcessAssignee] | Unset):
    """

    id: str
    name: str
    total_items: int | Unset = 0
    input_items: int | Unset = 0
    pending_approval: int | Unset = 0
    assignable_members: list[OutputProcessAssignee] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        total_items = self.total_items

        input_items = self.input_items

        pending_approval = self.pending_approval

        assignable_members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.assignable_members, Unset):
            assignable_members = []
            for assignable_members_item_data in self.assignable_members:
                assignable_members_item = assignable_members_item_data.to_dict()
                assignable_members.append(assignable_members_item)

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
        if assignable_members is not UNSET:
            field_dict["assignable_members"] = assignable_members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_process_assignee import OutputProcessAssignee

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        total_items = d.pop("total_items", UNSET)

        input_items = d.pop("input_items", UNSET)

        pending_approval = d.pop("pending_approval", UNSET)

        _assignable_members = d.pop("assignable_members", UNSET)
        assignable_members: list[OutputProcessAssignee] | Unset = UNSET
        if _assignable_members is not UNSET:
            assignable_members = []
            for assignable_members_item_data in _assignable_members:
                assignable_members_item = OutputProcessAssignee.from_dict(
                    assignable_members_item_data
                )

                assignable_members.append(assignable_members_item)

        output_process_summary = cls(
            id=id,
            name=name,
            total_items=total_items,
            input_items=input_items,
            pending_approval=pending_approval,
            assignable_members=assignable_members,
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
