from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_lead_import_error import OutputLeadImportError


T = TypeVar("T", bound="OutputLeadImportSummary")


@_attrs_define
class OutputLeadImportSummary:
    """Result-state of CSV import.

    Attributes:
        imported_count (int):
        skipped_count (int):
        error_count (int):
        lead_list_id (None | str | Unset):
        errors (list[OutputLeadImportError] | Unset):
    """

    imported_count: int
    skipped_count: int
    error_count: int
    lead_list_id: None | str | Unset = UNSET
    errors: list[OutputLeadImportError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        imported_count = self.imported_count

        skipped_count = self.skipped_count

        error_count = self.error_count

        lead_list_id: None | str | Unset
        if isinstance(self.lead_list_id, Unset):
            lead_list_id = UNSET
        else:
            lead_list_id = self.lead_list_id

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "imported_count": imported_count,
                "skipped_count": skipped_count,
                "error_count": error_count,
            }
        )
        if lead_list_id is not UNSET:
            field_dict["lead_list_id"] = lead_list_id
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_lead_import_error import OutputLeadImportError

        d = dict(src_dict)
        imported_count = d.pop("imported_count")

        skipped_count = d.pop("skipped_count")

        error_count = d.pop("error_count")

        def _parse_lead_list_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lead_list_id = _parse_lead_list_id(d.pop("lead_list_id", UNSET))

        _errors = d.pop("errors", UNSET)
        errors: list[OutputLeadImportError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = OutputLeadImportError.from_dict(errors_item_data)

                errors.append(errors_item)

        output_lead_import_summary = cls(
            imported_count=imported_count,
            skipped_count=skipped_count,
            error_count=error_count,
            lead_list_id=lead_list_id,
            errors=errors,
        )

        output_lead_import_summary.additional_properties = d
        return output_lead_import_summary

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
