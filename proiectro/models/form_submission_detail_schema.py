from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.form_submission_detail_schema_all_fields_item import FormSubmissionDetailSchemaAllFieldsItem
  from ..models.form_submission_detail_schema_status_options_item import FormSubmissionDetailSchemaStatusOptionsItem
  from ..models.form_submission_detail_schema_values import FormSubmissionDetailSchemaValues





T = TypeVar("T", bound="FormSubmissionDetailSchema")



@_attrs_define
class FormSubmissionDetailSchema:
    """ One submission rendered against its OWN version's fields (historical accuracy).

        Attributes:
            submission_id (str):
            form_name (str):
            submitted_at (datetime.datetime):
            status (str):
            all_fields (list[FormSubmissionDetailSchemaAllFieldsItem]):
            values (FormSubmissionDetailSchemaValues):
            submitter_name (None | str | Unset):
            submitter_email (None | str | Unset):
            status_options (list[FormSubmissionDetailSchemaStatusOptionsItem] | Unset):
     """

    submission_id: str
    form_name: str
    submitted_at: datetime.datetime
    status: str
    all_fields: list[FormSubmissionDetailSchemaAllFieldsItem]
    values: FormSubmissionDetailSchemaValues
    submitter_name: None | str | Unset = UNSET
    submitter_email: None | str | Unset = UNSET
    status_options: list[FormSubmissionDetailSchemaStatusOptionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.form_submission_detail_schema_values import FormSubmissionDetailSchemaValues
        from ..models.form_submission_detail_schema_status_options_item import FormSubmissionDetailSchemaStatusOptionsItem
        from ..models.form_submission_detail_schema_all_fields_item import FormSubmissionDetailSchemaAllFieldsItem
        submission_id = self.submission_id

        form_name = self.form_name

        submitted_at = self.submitted_at.isoformat()

        status = self.status

        all_fields = []
        for all_fields_item_data in self.all_fields:
            all_fields_item = all_fields_item_data.to_dict()
            all_fields.append(all_fields_item)



        values = self.values.to_dict()

        submitter_name: None | str | Unset
        if isinstance(self.submitter_name, Unset):
            submitter_name = UNSET
        else:
            submitter_name = self.submitter_name

        submitter_email: None | str | Unset
        if isinstance(self.submitter_email, Unset):
            submitter_email = UNSET
        else:
            submitter_email = self.submitter_email

        status_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.status_options, Unset):
            status_options = []
            for status_options_item_data in self.status_options:
                status_options_item = status_options_item_data.to_dict()
                status_options.append(status_options_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "submission_id": submission_id,
            "form_name": form_name,
            "submitted_at": submitted_at,
            "status": status,
            "all_fields": all_fields,
            "values": values,
        })
        if submitter_name is not UNSET:
            field_dict["submitter_name"] = submitter_name
        if submitter_email is not UNSET:
            field_dict["submitter_email"] = submitter_email
        if status_options is not UNSET:
            field_dict["status_options"] = status_options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_submission_detail_schema_all_fields_item import FormSubmissionDetailSchemaAllFieldsItem
        from ..models.form_submission_detail_schema_status_options_item import FormSubmissionDetailSchemaStatusOptionsItem
        from ..models.form_submission_detail_schema_values import FormSubmissionDetailSchemaValues
        d = dict(src_dict)
        submission_id = d.pop("submission_id")

        form_name = d.pop("form_name")

        submitted_at = isoparse(d.pop("submitted_at"))




        status = d.pop("status")

        all_fields = []
        _all_fields = d.pop("all_fields")
        for all_fields_item_data in (_all_fields):
            all_fields_item = FormSubmissionDetailSchemaAllFieldsItem.from_dict(all_fields_item_data)



            all_fields.append(all_fields_item)


        values = FormSubmissionDetailSchemaValues.from_dict(d.pop("values"))




        def _parse_submitter_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        submitter_name = _parse_submitter_name(d.pop("submitter_name", UNSET))


        def _parse_submitter_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        submitter_email = _parse_submitter_email(d.pop("submitter_email", UNSET))


        _status_options = d.pop("status_options", UNSET)
        status_options: list[FormSubmissionDetailSchemaStatusOptionsItem] | Unset = UNSET
        if _status_options is not UNSET:
            status_options = []
            for status_options_item_data in _status_options:
                status_options_item = FormSubmissionDetailSchemaStatusOptionsItem.from_dict(status_options_item_data)



                status_options.append(status_options_item)


        form_submission_detail_schema = cls(
            submission_id=submission_id,
            form_name=form_name,
            submitted_at=submitted_at,
            status=status,
            all_fields=all_fields,
            values=values,
            submitter_name=submitter_name,
            submitter_email=submitter_email,
            status_options=status_options,
        )


        form_submission_detail_schema.additional_properties = d
        return form_submission_detail_schema

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
