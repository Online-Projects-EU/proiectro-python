from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputLeadImportPreview")


@_attrs_define
class OutputLeadImportPreview:
    """Preview-state of CSV import, shown before the rep clicks Confirm.

    Attributes:
        mapped_columns (list[str]):
        unmapped_columns (list[str]):
        row_count (int):
        has_header (bool):
        upload_token (str):
        estimated_duplicates (int | Unset):  Default: 0.
        company_matches (int | Unset):  Default: 0.
        assigned_list_name (str | Unset):  Default: ''.
        default_next_action (str | Unset):  Default: 'triage_later'.
    """

    mapped_columns: list[str]
    unmapped_columns: list[str]
    row_count: int
    has_header: bool
    upload_token: str
    estimated_duplicates: int | Unset = 0
    company_matches: int | Unset = 0
    assigned_list_name: str | Unset = ""
    default_next_action: str | Unset = "triage_later"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mapped_columns = self.mapped_columns

        unmapped_columns = self.unmapped_columns

        row_count = self.row_count

        has_header = self.has_header

        upload_token = self.upload_token

        estimated_duplicates = self.estimated_duplicates

        company_matches = self.company_matches

        assigned_list_name = self.assigned_list_name

        default_next_action = self.default_next_action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mapped_columns": mapped_columns,
                "unmapped_columns": unmapped_columns,
                "row_count": row_count,
                "has_header": has_header,
                "upload_token": upload_token,
            }
        )
        if estimated_duplicates is not UNSET:
            field_dict["estimated_duplicates"] = estimated_duplicates
        if company_matches is not UNSET:
            field_dict["company_matches"] = company_matches
        if assigned_list_name is not UNSET:
            field_dict["assigned_list_name"] = assigned_list_name
        if default_next_action is not UNSET:
            field_dict["default_next_action"] = default_next_action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mapped_columns = cast(list[str], d.pop("mapped_columns"))

        unmapped_columns = cast(list[str], d.pop("unmapped_columns"))

        row_count = d.pop("row_count")

        has_header = d.pop("has_header")

        upload_token = d.pop("upload_token")

        estimated_duplicates = d.pop("estimated_duplicates", UNSET)

        company_matches = d.pop("company_matches", UNSET)

        assigned_list_name = d.pop("assigned_list_name", UNSET)

        default_next_action = d.pop("default_next_action", UNSET)

        output_lead_import_preview = cls(
            mapped_columns=mapped_columns,
            unmapped_columns=unmapped_columns,
            row_count=row_count,
            has_header=has_header,
            upload_token=upload_token,
            estimated_duplicates=estimated_duplicates,
            company_matches=company_matches,
            assigned_list_name=assigned_list_name,
            default_next_action=default_next_action,
        )

        output_lead_import_preview.additional_properties = d
        return output_lead_import_preview

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
