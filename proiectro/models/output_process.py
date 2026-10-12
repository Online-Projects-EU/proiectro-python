from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputProcess")


@_attrs_define
class OutputProcess:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        is_active (bool):
        allow_backward_move (bool):
        allow_skip_move (bool):
        stage_count (int | Unset):  Default: 0.
        item_count (int | Unset):  Default: 0.
    """

    id: str
    name: str
    description: str
    is_active: bool
    allow_backward_move: bool
    allow_skip_move: bool
    stage_count: int | Unset = 0
    item_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        is_active = self.is_active

        allow_backward_move = self.allow_backward_move

        allow_skip_move = self.allow_skip_move

        stage_count = self.stage_count

        item_count = self.item_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "is_active": is_active,
                "allow_backward_move": allow_backward_move,
                "allow_skip_move": allow_skip_move,
            }
        )
        if stage_count is not UNSET:
            field_dict["stage_count"] = stage_count
        if item_count is not UNSET:
            field_dict["item_count"] = item_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        is_active = d.pop("is_active")

        allow_backward_move = d.pop("allow_backward_move")

        allow_skip_move = d.pop("allow_skip_move")

        stage_count = d.pop("stage_count", UNSET)

        item_count = d.pop("item_count", UNSET)

        output_process = cls(
            id=id,
            name=name,
            description=description,
            is_active=is_active,
            allow_backward_move=allow_backward_move,
            allow_skip_move=allow_skip_move,
            stage_count=stage_count,
            item_count=item_count,
        )

        output_process.additional_properties = d
        return output_process

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
