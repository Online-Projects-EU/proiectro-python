from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditDocumentSeries")


@_attrs_define
class EditDocumentSeries:
    """
    Attributes:
        code (None | str | Unset):
        name (None | str | Unset):
        next_number (int | None | Unset):
        padding (int | None | Unset):
        lock_on_finalize (bool | None | Unset):
        is_active (bool | None | Unset):
    """

    code: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    next_number: int | None | Unset = UNSET
    padding: int | None | Unset = UNSET
    lock_on_finalize: bool | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        next_number: int | None | Unset
        if isinstance(self.next_number, Unset):
            next_number = UNSET
        else:
            next_number = self.next_number

        padding: int | None | Unset
        if isinstance(self.padding, Unset):
            padding = UNSET
        else:
            padding = self.padding

        lock_on_finalize: bool | None | Unset
        if isinstance(self.lock_on_finalize, Unset):
            lock_on_finalize = UNSET
        else:
            lock_on_finalize = self.lock_on_finalize

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name
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

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_next_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        next_number = _parse_next_number(d.pop("next_number", UNSET))

        def _parse_padding(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        padding = _parse_padding(d.pop("padding", UNSET))

        def _parse_lock_on_finalize(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        lock_on_finalize = _parse_lock_on_finalize(d.pop("lock_on_finalize", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        edit_document_series = cls(
            code=code,
            name=name,
            next_number=next_number,
            padding=padding,
            lock_on_finalize=lock_on_finalize,
            is_active=is_active,
        )

        edit_document_series.additional_properties = d
        return edit_document_series

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
