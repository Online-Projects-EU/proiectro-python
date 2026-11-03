from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_csv_import_row import OutputCsvImportRow


T = TypeVar("T", bound="OutputCsvImportPreview")


@_attrs_define
class OutputCsvImportPreview:
    """What a CSV import would do, row by row, before anything is written.

    Attributes:
        recognised_columns (list[str]):
        ignored_columns (list[str]):
        row_count (int):
        create_count (int):
        update_count (int):
        unchanged_count (int):
        error_count (int):
        new_item_names (list[str]):
        more_new_items (int):
        upload_token (str):
        rows (list[OutputCsvImportRow]):
        notes (list[str] | Unset):
    """

    recognised_columns: list[str]
    ignored_columns: list[str]
    row_count: int
    create_count: int
    update_count: int
    unchanged_count: int
    error_count: int
    new_item_names: list[str]
    more_new_items: int
    upload_token: str
    rows: list[OutputCsvImportRow]
    notes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recognised_columns = self.recognised_columns

        ignored_columns = self.ignored_columns

        row_count = self.row_count

        create_count = self.create_count

        update_count = self.update_count

        unchanged_count = self.unchanged_count

        error_count = self.error_count

        new_item_names = self.new_item_names

        more_new_items = self.more_new_items

        upload_token = self.upload_token

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        notes: list[str] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recognised_columns": recognised_columns,
                "ignored_columns": ignored_columns,
                "row_count": row_count,
                "create_count": create_count,
                "update_count": update_count,
                "unchanged_count": unchanged_count,
                "error_count": error_count,
                "new_item_names": new_item_names,
                "more_new_items": more_new_items,
                "upload_token": upload_token,
                "rows": rows,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_csv_import_row import OutputCsvImportRow

        d = dict(src_dict)
        recognised_columns = cast(list[str], d.pop("recognised_columns"))

        ignored_columns = cast(list[str], d.pop("ignored_columns"))

        row_count = d.pop("row_count")

        create_count = d.pop("create_count")

        update_count = d.pop("update_count")

        unchanged_count = d.pop("unchanged_count")

        error_count = d.pop("error_count")

        new_item_names = cast(list[str], d.pop("new_item_names"))

        more_new_items = d.pop("more_new_items")

        upload_token = d.pop("upload_token")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = OutputCsvImportRow.from_dict(rows_item_data)

            rows.append(rows_item)

        notes = cast(list[str], d.pop("notes", UNSET))

        output_csv_import_preview = cls(
            recognised_columns=recognised_columns,
            ignored_columns=ignored_columns,
            row_count=row_count,
            create_count=create_count,
            update_count=update_count,
            unchanged_count=unchanged_count,
            error_count=error_count,
            new_item_names=new_item_names,
            more_new_items=more_new_items,
            upload_token=upload_token,
            rows=rows,
            notes=notes,
        )

        output_csv_import_preview.additional_properties = d
        return output_csv_import_preview

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
