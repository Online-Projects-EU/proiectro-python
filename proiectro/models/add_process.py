from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddProcess")


@_attrs_define
class AddProcess:
    """
    Attributes:
        name (str):
        description (str | Unset):  Default: ''.
        is_active (bool | None | Unset):  Default: False.
        allow_backward_move (bool | None | Unset):  Default: False.
        allow_skip_move (bool | None | Unset):  Default: False.
    """

    name: str
    description: str | Unset = ""
    is_active: bool | None | Unset = False
    allow_backward_move: bool | None | Unset = False
    allow_skip_move: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        allow_backward_move: bool | None | Unset
        if isinstance(self.allow_backward_move, Unset):
            allow_backward_move = UNSET
        else:
            allow_backward_move = self.allow_backward_move

        allow_skip_move: bool | None | Unset
        if isinstance(self.allow_skip_move, Unset):
            allow_skip_move = UNSET
        else:
            allow_skip_move = self.allow_skip_move

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if allow_backward_move is not UNSET:
            field_dict["allow_backward_move"] = allow_backward_move
        if allow_skip_move is not UNSET:
            field_dict["allow_skip_move"] = allow_skip_move

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_allow_backward_move(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_backward_move = _parse_allow_backward_move(
            d.pop("allow_backward_move", UNSET)
        )

        def _parse_allow_skip_move(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_skip_move = _parse_allow_skip_move(d.pop("allow_skip_move", UNSET))

        add_process = cls(
            name=name,
            description=description,
            is_active=is_active,
            allow_backward_move=allow_backward_move,
            allow_skip_move=allow_skip_move,
        )

        add_process.additional_properties = d
        return add_process

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
