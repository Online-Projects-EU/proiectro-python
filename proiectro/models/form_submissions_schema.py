from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.form_submissions_schema_columns_item import FormSubmissionsSchemaColumnsItem
  from ..models.form_submissions_schema_dynamic_columns_item import FormSubmissionsSchemaDynamicColumnsItem
  from ..models.form_submissions_schema_submissions_item import FormSubmissionsSchemaSubmissionsItem





T = TypeVar("T", bound="FormSubmissionsSchema")



@_attrs_define
class FormSubmissionsSchema:
    """ Full-result-set payload for the client-side submissions datatable (Part 5, Option A).
    `columns` are fixed + dynamic-summary headers; each row carries a pivoted `values` map.
    `export_url`, when set by the list worker, surfaces the surface's CSV-download link (M-1).

        Attributes:
            columns (list[FormSubmissionsSchemaColumnsItem]):
            dynamic_columns (list[FormSubmissionsSchemaDynamicColumnsItem]):
            submissions (list[FormSubmissionsSchemaSubmissionsItem]):
            total_count (int | Unset):  Default: 0.
            export_url (None | str | Unset):
     """

    columns: list[FormSubmissionsSchemaColumnsItem]
    dynamic_columns: list[FormSubmissionsSchemaDynamicColumnsItem]
    submissions: list[FormSubmissionsSchemaSubmissionsItem]
    total_count: int | Unset = 0
    export_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.form_submissions_schema_dynamic_columns_item import FormSubmissionsSchemaDynamicColumnsItem
        from ..models.form_submissions_schema_submissions_item import FormSubmissionsSchemaSubmissionsItem
        from ..models.form_submissions_schema_columns_item import FormSubmissionsSchemaColumnsItem
        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)



        dynamic_columns = []
        for dynamic_columns_item_data in self.dynamic_columns:
            dynamic_columns_item = dynamic_columns_item_data.to_dict()
            dynamic_columns.append(dynamic_columns_item)



        submissions = []
        for submissions_item_data in self.submissions:
            submissions_item = submissions_item_data.to_dict()
            submissions.append(submissions_item)



        total_count = self.total_count

        export_url: None | str | Unset
        if isinstance(self.export_url, Unset):
            export_url = UNSET
        else:
            export_url = self.export_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "columns": columns,
            "dynamic_columns": dynamic_columns,
            "submissions": submissions,
        })
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if export_url is not UNSET:
            field_dict["export_url"] = export_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_submissions_schema_columns_item import FormSubmissionsSchemaColumnsItem
        from ..models.form_submissions_schema_dynamic_columns_item import FormSubmissionsSchemaDynamicColumnsItem
        from ..models.form_submissions_schema_submissions_item import FormSubmissionsSchemaSubmissionsItem
        d = dict(src_dict)
        columns = []
        _columns = d.pop("columns")
        for columns_item_data in (_columns):
            columns_item = FormSubmissionsSchemaColumnsItem.from_dict(columns_item_data)



            columns.append(columns_item)


        dynamic_columns = []
        _dynamic_columns = d.pop("dynamic_columns")
        for dynamic_columns_item_data in (_dynamic_columns):
            dynamic_columns_item = FormSubmissionsSchemaDynamicColumnsItem.from_dict(dynamic_columns_item_data)



            dynamic_columns.append(dynamic_columns_item)


        submissions = []
        _submissions = d.pop("submissions")
        for submissions_item_data in (_submissions):
            submissions_item = FormSubmissionsSchemaSubmissionsItem.from_dict(submissions_item_data)



            submissions.append(submissions_item)


        total_count = d.pop("total_count", UNSET)

        def _parse_export_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        export_url = _parse_export_url(d.pop("export_url", UNSET))


        form_submissions_schema = cls(
            columns=columns,
            dynamic_columns=dynamic_columns,
            submissions=submissions,
            total_count=total_count,
            export_url=export_url,
        )


        form_submissions_schema.additional_properties = d
        return form_submissions_schema

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
