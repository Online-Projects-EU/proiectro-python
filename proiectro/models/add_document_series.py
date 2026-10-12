from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddDocumentSeries")


@_attrs_define
class AddDocumentSeries:
    """
    Attributes:
        code (str):
        name (str):
        next_number (int | Unset):  Default: 1.
        padding (int | Unset):  Default: 0.
        lock_on_finalize (bool | Unset):  Default: False.
        is_active (bool | Unset):  Default: True.
    """

    code: str
    name: str
    next_number: int | Unset = 1
    padding: int | Unset = 0
    lock_on_finalize: bool | Unset = False
    is_active: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        next_number = self.next_number

        padding = self.padding

        lock_on_finalize = self.lock_on_finalize

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
            }
        )
        if next_number is not UNSET:
            field_dict["next_number"] = next_number
        if padding is not UNSET:
            field_dict["padding"] = padding
        if lock_on_finalize is not UNSET:
            field_dict["lock_on_finalize"] = lock_on_finalize
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name")

        next_number = d.pop("next_number", UNSET)

        padding = d.pop("padding", UNSET)

        lock_on_finalize = d.pop("lock_on_finalize", UNSET)

        is_active = d.pop("is_active", UNSET)

        add_document_series = cls(
            code=code,
            name=name,
            next_number=next_number,
            padding=padding,
            lock_on_finalize=lock_on_finalize,
            is_active=is_active,
        )

        add_document_series.additional_properties = d
        return add_document_series

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
