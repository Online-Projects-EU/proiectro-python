from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputCsvImportCell")


@_attrs_define
class OutputCsvImportCell:
    """
    Attributes:
        column (str):
        message (str | Unset):  Default: ''.
        before (str | Unset):  Default: ''.
        after (str | Unset):  Default: ''.
    """

    column: str
    message: str | Unset = ""
    before: str | Unset = ""
    after: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        column = self.column

        message = self.message

        before = self.before

        after = self.after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "column": column,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column = d.pop("column")

        message = d.pop("message", UNSET)

        before = d.pop("before", UNSET)

        after = d.pop("after", UNSET)

        output_csv_import_cell = cls(
            column=column,
            message=message,
            before=before,
            after=after,
        )

        output_csv_import_cell.additional_properties = d
        return output_csv_import_cell

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
