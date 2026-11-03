from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_csv_import_row import OutputCsvImportRow


T = TypeVar("T", bound="OutputCsvImportSummary")


@_attrs_define
class OutputCsvImportSummary:
    """
    Attributes:
        created_count (int):
        updated_count (int):
        unchanged_count (int):
        error_count (int):
        rows (list[OutputCsvImportRow]):
    """

    created_count: int
    updated_count: int
    unchanged_count: int
    error_count: int
    rows: list[OutputCsvImportRow]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_count = self.created_count

        updated_count = self.updated_count

        unchanged_count = self.unchanged_count

        error_count = self.error_count

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_count": created_count,
                "updated_count": updated_count,
                "unchanged_count": unchanged_count,
                "error_count": error_count,
                "rows": rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_csv_import_row import OutputCsvImportRow

        d = dict(src_dict)
        created_count = d.pop("created_count")

        updated_count = d.pop("updated_count")

        unchanged_count = d.pop("unchanged_count")

        error_count = d.pop("error_count")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = OutputCsvImportRow.from_dict(rows_item_data)

            rows.append(rows_item)

        output_csv_import_summary = cls(
            created_count=created_count,
            updated_count=updated_count,
            unchanged_count=unchanged_count,
            error_count=error_count,
            rows=rows,
        )

        output_csv_import_summary.additional_properties = d
        return output_csv_import_summary

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
