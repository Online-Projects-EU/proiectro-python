from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputOperationalItemActions")


@_attrs_define
class OutputOperationalItemActions:
    """What the caller's participation in the process allows on this item.

    Attributes:
        can_annotate (bool | Unset):  Default: False.
        can_edit (bool | Unset):  Default: False.
        can_delete (bool | Unset):  Default: False.
        can_move (bool | Unset):  Default: False.
        can_approve (bool | Unset):  Default: False.
        can_reject (bool | Unset):  Default: False.
        can_reassign (bool | Unset):  Default: False.
    """

    can_annotate: bool | Unset = False
    can_edit: bool | Unset = False
    can_delete: bool | Unset = False
    can_move: bool | Unset = False
    can_approve: bool | Unset = False
    can_reject: bool | Unset = False
    can_reassign: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_annotate = self.can_annotate

        can_edit = self.can_edit

        can_delete = self.can_delete

        can_move = self.can_move

        can_approve = self.can_approve

        can_reject = self.can_reject

        can_reassign = self.can_reassign

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_annotate is not UNSET:
            field_dict["can_annotate"] = can_annotate
        if can_edit is not UNSET:
            field_dict["can_edit"] = can_edit
        if can_delete is not UNSET:
            field_dict["can_delete"] = can_delete
        if can_move is not UNSET:
            field_dict["can_move"] = can_move
        if can_approve is not UNSET:
            field_dict["can_approve"] = can_approve
        if can_reject is not UNSET:
            field_dict["can_reject"] = can_reject
        if can_reassign is not UNSET:
            field_dict["can_reassign"] = can_reassign

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_annotate = d.pop("can_annotate", UNSET)

        can_edit = d.pop("can_edit", UNSET)

        can_delete = d.pop("can_delete", UNSET)

        can_move = d.pop("can_move", UNSET)

        can_approve = d.pop("can_approve", UNSET)

        can_reject = d.pop("can_reject", UNSET)

        can_reassign = d.pop("can_reassign", UNSET)

        output_operational_item_actions = cls(
            can_annotate=can_annotate,
            can_edit=can_edit,
            can_delete=can_delete,
            can_move=can_move,
            can_approve=can_approve,
            can_reject=can_reject,
            can_reassign=can_reassign,
        )

        output_operational_item_actions.additional_properties = d
        return output_operational_item_actions

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
