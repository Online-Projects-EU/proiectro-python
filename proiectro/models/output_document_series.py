from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputDocumentSeries")


@_attrs_define
class OutputDocumentSeries:
    """
    Attributes:
        id (str):
        code (str):
        name (str):
        next_number (int):
        next_full_number (str):
        padding (int):
        is_active (bool):
        document_count (int | Unset):  Default: 0.
    """

    id: str
    code: str
    name: str
    next_number: int
    next_full_number: str
    padding: int
    is_active: bool
    document_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        code = self.code

        name = self.name

        next_number = self.next_number

        next_full_number = self.next_full_number

        padding = self.padding

        is_active = self.is_active

        document_count = self.document_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "code": code,
                "name": name,
                "next_number": next_number,
                "next_full_number": next_full_number,
                "padding": padding,
                "is_active": is_active,
            }
        )
        if document_count is not UNSET:
            field_dict["document_count"] = document_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        code = d.pop("code")

        name = d.pop("name")

        next_number = d.pop("next_number")

        next_full_number = d.pop("next_full_number")

        padding = d.pop("padding")

        is_active = d.pop("is_active")

        document_count = d.pop("document_count", UNSET)

        output_document_series = cls(
            id=id,
            code=code,
            name=name,
            next_number=next_number,
            next_full_number=next_full_number,
            padding=padding,
            is_active=is_active,
            document_count=document_count,
        )

        output_document_series.additional_properties = d
        return output_document_series

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
